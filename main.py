import json
import logging
import multiprocessing
import struct
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pprint import pprint
from typing import Union

import cx_Oracle
import pika
from pydantic import BaseModel
from sqlalchemy import or_
from sqlalchemy.orm import session

from config import db, db_oracle
from database.models import Action, Actionproperty, Actiontype, Actionpropertytype, ActionpropertyString, \
    ActionpropertyInteger, ActionpropertyDouble, ActionpropertyDate, Znoinfo, t_sprav_onk_n, t_sprav_onk_m, \
    t_sprav_onk_t, ActionpropertyReference, t_sprav_onk_reasons, Rbvisitonkogoal, Event, Diagnostic, Diagnosis, \
    t_znoinfo_clinical_group, Netricapatientconditiononadmission, t_sprav_onk_stad, ZNO_Table_G, ZNO_Table_R, \
    Rbcarnotianindex


class CMergeActions:
    with db.session_scope() as session:
        session = session

    def format_row(self, action):
        """
        Форматируем SQLAlchemy Row в JSON для клонирования Row
        """
        return {k: v for k, v in action.__dict__.items() if not k.startswith("_") and k != 'id'}

    def prepare_insert_action_property(self, action_id, model: BaseModel, type_id: int):
        """
        Создаем базу для ActionProperty
        """
        action = self.session.query(Action).filter(Action.id == action_id).first()
        model.createDatetime = action.createDatetime
        model.createPerson_id = action.createPerson_id
        model.modifyDatetime = action.modifyDatetime
        model.modifyPerson_id = action.modifyPerson_id
        model.action_id = action.id
        model.deleted = 0
        model.norm = ''
        model.isAssigned = 0
        model.isAutoFillCancelled = 0
        model.type_id = type_id
        return model

    def fill_property_row(self, model: BaseModel, action_property_id, value):
        """
        Заполнение полей ActionProperty_...
        """
        model.id = action_property_id
        model.index = 0
        model.value = value
        return model

    def insert_action_property(self,
                               action_id: int,
                               type_id: int,
                               property_value: Union[str, int, float],
                               model: Union[
                                   ActionpropertyString,
                                   ActionpropertyInteger,
                                   ActionpropertyDouble,
                                   ActionpropertyDate
                               ]
                               ):
        """
        Создаем запись в ActionProperty и в ActionProperty_...
        """
        if type_id:
            if property_value:
                property_row = self.session.query(Actionproperty).filter(Actionproperty.action_id == action_id,
                                                                         Actionproperty.type_id == type_id).first()
                if not property_row:
                    action_property_insert_model = self.prepare_insert_action_property(action_id, Actionproperty(),
                                                                                       type_id)
                    self.session.add(action_property_insert_model)
                    self.session.flush()
                    model = self.fill_property_row(model, action_property_insert_model.id, property_value)
                    self.session.add(model)
                    self.session.flush()
                else:
                    prop = self.session.query(ActionpropertyString).filter(
                        ActionpropertyString.id == property_row.id).first()
                    if prop:
                        prop.value = prop.value + property_value
                        self.session.flush()

    def create_new_action(self, old_action_id, actiontype_id):
        old_action = self.session.query(Action).filter(Action.id == old_action_id).first()
        new_action = Action(**(self.format_row(old_action)))
        old_action.deleted = 1
        new_action.plannedEndDate = False
        new_action.actionType_id = actiontype_id
        if new_action.createPerson_id is None:
            new_action.createPerson_id = 1
        if new_action.modifyPerson_id is None:
            new_action.createPerson_id = 1
        if new_action.createDatetime is None:
            new_action.createDatetime = False
        if new_action.modifyDatetime is None:
            new_action.modifyDatetime = False
        new_action.note = f"Перенесено из БАРСА id = {old_action.id}"
        self.session.add(new_action)
        self.session.flush()
        return new_action

    # Маппинг для полей из барса Индекс Карновского
    bars_vista_map = {
        "Повод обращения": {
            "vista_type_id": {67979: 21773},  # Маппинг формата ActionType.id: ActionPropertyType.id
            "vista_model": lambda: ActionpropertyReference(),  # модель пропы
            "insert_to": "Action",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "vista_table": Rbvisitonkogoal,  # таблица, в которой искать значение из барса по полю vista_table_col
            "vista_table_col": 'name'  # поле, в котором искать значение из барса в таблице vista_table
        },
        "Клин. группа": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": t_znoinfo_clinical_group,  # таблица в висте, где искать значение
            "ZNO_vista_col": "name",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "id",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "clinical_group",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": False,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": True,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "шкала EСOG": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": t_znoinfo_clinical_group,  # таблица в висте, где искать значение
            "ZNO_vista_col": "name",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "id",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "clinical_group",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": False,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": True,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "Индекс Карновского": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": t_znoinfo_clinical_group,  # таблица в висте, где искать значение
            "ZNO_vista_col": "name",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "id",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "clinical_group",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": False,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": True,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "Дата проведения консилиума": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": t_znoinfo_clinical_group,  # таблица в висте, где искать значение
            "ZNO_vista_col": "name",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "id",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "clinical_group",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": False,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": True,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "Стадия": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": t_sprav_onk_stad,  # таблица в висте, где искать значение
            "ZNO_vista_col": "NAME",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "ID_ST",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "stady",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": True,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": True,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "G": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": ZNO_Table_G,  # таблица в висте, где искать значение
            "ZNO_vista_col": "name",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "id",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "parameter_g",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": False,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": False,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "R": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": ZNO_Table_R,  # таблица в висте, где искать значение
            "ZNO_vista_col": "name",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "id",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "parameter_r",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": False,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": False,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "SUSPICIO": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "ZNO_vista_table": ZNO_Table_R,  # таблица в висте, где искать значение
            "ZNO_vista_col": "name",  # поле, по которому искать в ZNO_vista_table
            "ZNO_field_id_name": "id",  # значение, которое инсертить в ZnoInfo
            "ZNO_table_coll": "parameter_r",  # поле, в которое инсертить в ZnoInfo
            "check_MKB": False,  # проверять ли МКБ при получении значения из ZNO_vista_table
            "alchemy_table": False,  # тут флаг, что ZNO_vista_table является таблиеей, а не классом из models.py
            "ZNO_vista_table_mkb_col_name": "DS_CODE"  # поле, в таблице ZNO_vista_table где ищем диагноз
        },
        "M": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",
            "ZNO_vista_table": t_sprav_onk_m,
            "ZNO_vista_col": "NAME",
            "ZNO_field_id_name": "ID_M",
            "ZNO_table_coll": "stady_m",
            "check_MKB": True,
            "alchemy_table": True,
            "ZNO_vista_table_mkb_col_name": "DS_CODE"
        },
        "T": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",
            "ZNO_vista_table": t_sprav_onk_t,
            "ZNO_vista_col": "NAME",
            "ZNO_field_id_name": "ID_T",
            "ZNO_table_coll": "stady_t",
            "check_MKB": True,
            "alchemy_table": True,
            "ZNO_vista_table_mkb_col_name": "DS_CODE"
        },
        "N": {
            "vista_type_id": None,
            "vista_model": None,
            "insert_to": "ZNO",
            "ZNO_vista_table": t_sprav_onk_n,
            "ZNO_vista_col": "NAME",
            "ZNO_field_id_name": "ID_N",
            "ZNO_table_coll": "stady_n",
            "check_MKB": True,
            "alchemy_table": True,
            "ZNO_vista_table_mkb_col_name": "DS_CODE"
        },
        "Состояние": {
            "vista_type_id": {67979: 21752,
                              69156: 23326,
                              69157: 23354,
                              69168: 23636,
                              69159: 23418,
                              69164: 23534,
                              419294591: 23699,
                              69155: 23279,
                              419294589: 23680,
                              },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "ЧДД": {
            "vista_type_id": {67979: 21754,
                              69156: 23320,
                              69157: 23348,
                              69168: 23630,
                              69159: 23412,
                              419294591: 23698,
                              69164: 23528,
                              419294589: 23683,
                              },
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Status localis": {
            "vista_type_id": {67979: 21750,
                              69156: 23327,
                              69157: 23355,
                              69168: 23637,
                              69159: 23419,
                              69164: 23535,
                              419294588: 23678,
                              69155: 23280,
                              419294589: 23681
                              },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Анамнез заболевания": {
            "vista_type_id": {67979: 21752,
                              69156: 23297,
                              69168: 23607,
                              419294591: 23691,
                              69159: 23389,
                              69162: 23455,
                              69164: 23505,
                              419294590: 23711,
                              419294588: 23673,
                              69155: 23277,
                              69165: 23549
                              },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Анамнез гемотрансфузий": {
            "vista_type_id": {
                419294588: 23675,

            },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Пл. пов тела": {
            "vista_type_id": {
                419294591: 23700,

            },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Аллергологический анамнез": {
            "vista_type_id": {67979: 21751,
                              69156: 23299,
                              69159: 23391,
                              419294591: 23694,
                              419294590: 23710,
                              69164: 23507,
                              69165: 23551
                              },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рекомендации по лечению": {
            "vista_type_id": {67979: 23661},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результаты обследований в КОД": {
            "vista_type_id": {67979: 21779},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "В ходе приема была проведена манипуляция": {
            "vista_type_id": {67979: 21776},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Проведенное лечение": {
            "vista_type_id": {67979: 21769,
                              69168: 23639,
                              419294588: 23679,
                              419294589: 23684,
                              },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Пульс": {
            "vista_type_id": {67979: 21755,
                              69156: 23319,
                              69157: 23347,
                              69168: 23629,
                              69159: 23411,
                              419294591: 23701,
                              69164: 23527
                              },
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Анамнез жизни": {
            "vista_type_id": {67979: 21750,
                              69156: 23298,
                              69168: 23608,
                              419294591: 23692,
                              419294590: 23712,
                              69159: 23390,
                              69164: 23506,
                              69155: 23278,
                              69165: 23550,
                              419294588: 23674,
                              419294589: 23685
                              },
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Давление": {
            "vista_type_id": {67979: 21757,
                              69156: 23321,
                              69157: 23349,
                              69168: 23631,
                              69159: 23413,
                              69164: 23529,
                              419294591: 23697,
                              419294589: 23682
                              },
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Обследования и консультации": {
            "vista_type_id": {67979: 21778,
                              419294589: 23687},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "При проведении манипуляции использована аппаратура": {
            "vista_type_id": {67979: 21777},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Состояние тяжести": {
            "vista_type_id": {69157: 23333,
                              69167: 23595,
                              69168: 23599,
                              69159: 23381,
                              419294591: 23690,
                              69163: 23468,
                              69164: 23497,
                              69165: 23541,
                              69156: 23289},  # Маппинг формата ActionType.id: ActionPropertyType.id
            "vista_model": lambda: ActionpropertyReference(),  # модель пропы
            "insert_to": "Action",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
            "vista_table": Netricapatientconditiononadmission,
            # таблица, в которой искать значение из барса по полю vista_table_col
            "vista_table_col": 'name'  # поле, в котором искать значение из барса в таблице vista_table
        },
        "№ продлеваемого/предыдущего ЛН": {
            "vista_type_id": {69153: 23258},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "№ ЛН по совместительству": {
            "vista_type_id": {69153: 23261},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Этапы проведенного ранее лечения": {
            "vista_type_id": {69168: 23602,
                              69159: 23384,
                              69164: 23500,
                              69165: 23544,
                              69156: 23292},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Цель госпитализации, эффективность лечения": {
            "vista_type_id": {69161: 23452},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Факторы риска ВТЭО": {
            "vista_type_id": {69168: 23646,
                              69159: 23428},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Трансфузионный анамнез": {
            "vista_type_id": {69163: 23470},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Трансфузии по индивидуальному подбору в прошлом": {
            "vista_type_id": {69163: 23472},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Индекс массы тела": {
            "vista_type_id": {419294591: 23703},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результаты обследования": {
            "vista_type_id": {419294591: 23704},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Дополнение к плану обследования": {
            "vista_type_id": {419294591: 23705},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Дополнение к плану лечения": {
            "vista_type_id": {419294591: 23706},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Трансфузии (переливания) донорской крови и (или) ее компонентов": {
            "vista_type_id": {69165: 23565,
                              69156: 23313,
                              69164: 23521},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Температура": {
            "vista_type_id": {69156: 23318,
                              69157: 23346,
                              69168: 23628,
                              69159: 23410,
                              419294589: 23686,
                              419294591: 23702,
                              69164: 23526},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Страховой анамнез": {
            "vista_type_id": {69165: 23557,
                              69156: 23305,
                              69168: 23615,
                              69159: 23397,
                              69164: 23513},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Степени утраты профессиональной трудоспособности (в процентах), установленные по повторным несчастным случаям на производстве и профессиональным заболеваниям, и даты, до которых они установлены": {
            "vista_type_id": {69155: 23287},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Статус работы": {
            "vista_type_id": {69165: 23556,
                              69156: 23304,
                              69168: 23614,
                              419294591: 23693,
                              69159: 23396,
                              69164: 23512},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Сроки лечения": {
            "vista_type_id": {69161: 23451},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Срок, на который установлена степень утраты профессиональной трудоспособности в процентах": {
            "vista_type_id": {69155: 23285},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Состав подкомиссии": {
            "vista_type_id": {69166: 23587},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Сопутствующие": {
            "vista_type_id": {69165: 23585},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Содержание дневника": {
            "vista_type_id": {69157: 23335},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "СОД": {
            "vista_type_id": {69157: 23334},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Сатурация": {
            "vista_type_id": {69168: 23647,
                              69159: 23429},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "С какого года наблюдается в мед организации": {
            "vista_type_id": {69155: 23276},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рост": {
            "vista_type_id": {69156: 23324,
                              69157: 23352,
                              69168: 23634,
                              69159: 23416,
                              69164: 23532},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Решение врачебного консилиума": {
            "vista_type_id": {69165: 23579,
                              69168: 23645,
                              419294591: 23689,
                              69159: 23427},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рекомендуемые мероприятия по реконструктивной хирургии": {
            "vista_type_id": {69155: 23273},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рекомендуемые мероприятия по протезированию и ортезированию": {
            "vista_type_id": {69155: 23274},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рекомендуемые мероприятия по медицинской реабилитации": {
            "vista_type_id": {69155: 23272},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рекомендации заведующего отделением": {
            "vista_type_id": {69168: 23649,
                              69159: 23431},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рекомендации": {
            "vista_type_id": {69156: 23329,
                              69164: 23537},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результаты операции": {
            "vista_type_id": {69162: 23461},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Лечащий врач": {
            "vista_type_id": {419294590: 23714},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Члены вк": {
            "vista_type_id": {419294590: 23715},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результаты консилиума": {
            "vista_type_id": {419294590: 23716},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Цели проведения врачебной комиссии": {
            "vista_type_id": {419294590: 23717},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Форма проведения": {
            "vista_type_id": {419294590: 23718},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Консилиум проведен с применением телемедицинских технологий": {
            "vista_type_id": {419294590: 23719},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Присутствие пациента на консилиуме": {
            "vista_type_id": {419294590: 23720},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результаты обследований с другого ЛПУ": {
            "vista_type_id": {69168: 23604,
                              69159: 23386,
                              69164: 23502,
                              69165: 23546,
                              419294588: 23707,
                              69156: 23294},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результаты обследований": {
            "vista_type_id": {69168: 23603,
                              69159: 23385,
                              69162: 23458,
                              69164: 23501,
                              419294588: 23708,
                              419294590: 23713,
                              69165: 23545,
                              69156: 23293},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результаты медицинского обследования": {
            "vista_type_id": {69165: 23559,
                              69156: 23307,
                              69164: 23515},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Результат (мл/мин/1.73м2) (СКФ (CKD-EPI))": {
            "vista_type_id": {69159: 23439},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Результат (мл/мин) (СКФ(Cockcroft-Gault Equation))": {
            "vista_type_id": {69159: 23437},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Реабилитационный прогноз": {
            "vista_type_id": {69155: 23271},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Реабилитационный потенциал": {
            "vista_type_id": {69155: 23269},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Рассмотренные вопросы": {
            "vista_type_id": {69166: 23591},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Протокол": {
            "vista_type_id": {69167: 23597},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Производитель": {
            "vista_type_id": {69163: 23488},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Произведена биологическая проба": {
            "vista_type_id": {69163: 23490},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Проведенные операции": {
            "vista_type_id": {69168: 23660,
                              69162: 23460},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Проведенные консультации": {
            "vista_type_id": {69155: 23282},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Проведенные исследования": {
            "vista_type_id": {69157: 23343,
                              69162: 23457,
                              69155: 23281},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Причина смерти": {
            "vista_type_id": {69165: 23582},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Принадлежность к негроидной рассе": {
            "vista_type_id": {69159: 23440},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Примечание": {
            "vista_type_id": {69156: 23331,
                              69164: 23539},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Применение лекарственных препаратов (включая химиотерапию, вакцинацию), медицинских изделий, лечебного питания": {
            "vista_type_id": {69165: 23564,
                              69156: 23312,
                              69164: 23520},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "ПРЕЕМСТВЕННОСТЬ ЭТАПОВ": {
            "vista_type_id": {69161: 23453},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Предоставленные документы": {
            "vista_type_id": {69166: 23588},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Посттрансфузионные реакции и осложнения": {
            "vista_type_id": {69163: 23474},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Показания к трансфузии": {
            "vista_type_id": {69163: 23478},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Подписи": {
            "vista_type_id": {69166: 23592},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "План обследования": {
            "vista_type_id": {69168: 23641,
                              69159: 23423},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "План лечения": {
            "vista_type_id": {69159: 23421},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "План дальнейшего лечения": {
            "vista_type_id": {69168: 23648,
                              69159: 23430},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "ОФОРМЛЕНИЕ ДОКУМЕНТАЦИИ": {
            "vista_type_id": {69161: 23454},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Особенности течения": {
            "vista_type_id": {69163: 23476},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Осмотры врачей-специалистов, консилиумы врачей, врачебные комиссии": {
            "vista_type_id": {69165: 23560,
                              69156: 23308,
                              69164: 23516},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Осмотр совместно с заведующим отделением": {
            "vista_type_id": {69168: 23642,
                              69159: 23424},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Осложнения": {
            "vista_type_id": {69165: 23584},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Осложнение во время трансфузии": {
            "vista_type_id": {69163: 23492},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Оперативные вмешательства (операции), включая сведения об анестезиологическом пособии": {
            "vista_type_id": {69165: 23566,
                              69156: 23314,
                              69164: 23522},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Объем лабораторных обследований в соответствии со стандартами": {
            "vista_type_id": {69161: 23444},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Объем инструментальных обследований в соответствии со стандартами": {
            "vista_type_id": {69161: 23445},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Объем и качество обслуживания": {
            "vista_type_id": {69161: 23443},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Обоснование диагноза": {
            "vista_type_id": {69161: 23448},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Обоснование": {
            "vista_type_id": {69162: 23463},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Наименование компонента": {
            "vista_type_id": {69163: 23480},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Наименование вида ВМП": {
            "vista_type_id": {69166: 23590},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Наблюдение за состоянием больного": {
            "vista_type_id": {69163: 23493},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Метод определения резуса": {
            "vista_type_id": {69163: 23471},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Метод лечения": {
            "vista_type_id": {69165: 23563,
                              69156: 23311,
                              69164: 23519},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Метод и скорость трансфузии в/в капельно, медленно": {
            "vista_type_id": {69163: 23491},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Медицинские вмешательства": {
            "vista_type_id": {69165: 23567,
                              69156: 23315,
                              69164: 23523},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },

        "Масса": {
            "vista_type_id": {69159: 23434},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "ЛН №": {
            "vista_type_id": {69154: 23263},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Лечебный эффект": {
            "vista_type_id": {69165: 23586},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Круглосуточное наблюдение": {
            "vista_type_id": {69168: 23643,
                              69159: 23425},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Креатинин (СКФ(Cockcroft-Gault Equation))": {
            "vista_type_id": {69159: 23436},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Креатинин (СКФ (CKD-EPI))": {
            "vista_type_id": {69159: 23438},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Коэффициент": {
            "vista_type_id": {69159: 23435},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Контроль показателей крови через 12-24 часа": {
            "vista_type_id": {69163: 23495},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Контактный телефон": {
            "vista_type_id": {69166: 23593},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Количество и макроскопическая оценка первой порции": {
            "vista_type_id": {69163: 23494},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Кол-во дней": {
            "vista_type_id": {69154: 23266},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Код вида ВМП": {
            "vista_type_id": {69166: 23589},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Клинический прогноз": {
            "vista_type_id": {69155: 23270},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Исход заболевания": {
            "vista_type_id": {69165: 23583},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Исследование Антител": {
            "vista_type_id": {69163: 23473},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Осмотр совместно с завееееедующим отделения": {
            "vista_type_id": {419294591: 23696},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Жалобы": {
            "vista_type_id": {69156: 23296,
                              69157: 23341,
                              69168: 23606,
                              69159: 23388,
                              69164: 23504,
                              419294588: 23676,
                              419294591: 23695,
                              419294589: 23688,
                              69165: 23548},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Дополнительные сведения": {
            "vista_type_id": {69165: 23568,
                              69156: 23316,
                              69164: 23524},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Дополнительно": {
            "vista_type_id": {69157: 23344},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Диурез": {
            "vista_type_id": {69157: 23337},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Динамика": {
            "vista_type_id": {69165: 23581},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Диагноз поставлен в соответствии с правилами классификации": {
            "vista_type_id": {69161: 23447},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Дата, до которой установлена степень утраты профессиональной трудоспособности в процентах": {
            "vista_type_id": {69155: 23286},
            "vista_model": lambda: ActionpropertyDate(),
            "insert_to": "Action"
        },
        "Дата с:": {
            "vista_type_id": {69154: 23264},
            "vista_model": lambda: ActionpropertyDate(),
            "insert_to": "Action"
        },
        "Дата по:": {
            "vista_type_id": {69153: 23260,
                              69154: 23265},
            "vista_model": lambda: ActionpropertyDate(),
            "insert_to": "Action"
        },
        "Дата выдачи": {
            "vista_type_id": {69155: 23268},
            "vista_model": lambda: ActionpropertyDate(),
            "insert_to": "Action"
        },
        "Гинекологический анамнез": {
            "vista_type_id": {69165: 23552,
                              69156: 23300,
                              419294588: 23677,
                              69168: 23610,
                              69159: 23392,
                              69164: 23508},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Выдан с:": {
            "vista_type_id": {69153: 23259},
            "vista_model": lambda: ActionpropertyDate(),
            "insert_to": "Action"
        },
        "Время и способ размораживания (для сзп)": {
            "vista_type_id": {69163: 23481},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Врачебный консилиум считает целесообразным назначение препарата": {
            "vista_type_id": {69162: 23464},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Врачебный консилиум": {
            "vista_type_id": {69156: 23330,
                              69164: 23538},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Возраст": {
            "vista_type_id": {69159: 23433},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Вид лечения": {
            "vista_type_id": {69165: 23562,
                              69156: 23310,
                              69164: 23518},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Вес": {
            "vista_type_id": {69156: 23325,
                              69157: 23353,
                              69168: 23635,
                              69159: 23417,
                              69164: 23533},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Больничный лист с (если требуется)": {
            "vista_type_id": {69165: 23555,
                              69156: 23303,
                              69168: 23613,
                              69159: 23395,
                              69164: 23511},
            "vista_model": lambda: ActionpropertyDate(),
            "insert_to": "Action"
        },
        "Больничный лист": {
            "vista_type_id": {69165: 23554,
                              69156: 23302,
                              69168: 23612,
                              69159: 23394,
                              69164: 23510},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "анти – Д: серия": {
            "vista_type_id": {69163: 23486},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "анти – А: серия": {
            "vista_type_id": {69163: 23482},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "анти – B: серия": {
            "vista_type_id": {69163: 23484},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Анамнез гемотранфузии": {
            "vista_type_id": {69165: 23553,
                              69156: 23301,
                              69168: 23611,
                              69159: 23393,
                              69164: 23509},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Акушерский анамнез": {
            "vista_type_id": {69163: 23475},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Адекватность лечения по диагнозу": {
            "vista_type_id": {69161: 23450},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "SpO2": {
            "vista_type_id": {69157: 23336},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Cтепень утраты профессиональной трудоспособности в процентах на момент направления гражданина на МСЭ": {
            "vista_type_id": {69155: 23284},
            "vista_model": lambda: ActionpropertyInteger(),
            "insert_to": "Action"
        },
        "Cостав консилиума врачей": {
            "vista_type_id": {69162: 23466},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Обоснование выбора оперативного вмешательства": {
            "vista_type_id": {419294590: 23709},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "(и.о) З/О": {
            "vista_type_id": {69157: 23339,
                              69168: 23600,
                              69159: 23382,
                              69164: 23498,
                              69165: 23542,
                              69156: 23290},
            "vista_model": lambda: ActionpropertyString(),
            "insert_to": "Action"
        },
        "Метод подтверждения": {
            "insert_to": "Diagnostic",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "LYM": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "OSS": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "HEP": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "PUL": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "PLE": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "BRA": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "SKI": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "PER": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "MAR": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "OTH": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "UMB": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "ADR": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },
        "OVA": {
            "insert_to": "ZNO",  # куда инсертить значение Action - в пропы, ZNO - в ZnoInfo
        },

    }

    def check_event_ZNO(self, action_id):
        action_row = self.session.query(Action).filter(Action.id == action_id).first()
        zno_row = self.session.query(Znoinfo).filter(Znoinfo.event_id == action_row.event_id).first()
        if not zno_row:
            event_row = self.session.query(Event).filter(Event.deleted == 0, Event.id == action_row.event_id).first()
            diagnostic_row = self.session.query(Diagnostic).filter(Diagnostic.event_id == event_row.id,
                                                                   Diagnostic.deleted == 0,
                                                                   Diagnostic.diagnosisType_id == 2).first()
            diagnosis_row = self.session.query(Diagnosis).filter(Diagnosis.id == diagnostic_row.diagnosis_id,
                                                                 Diagnosis.deleted == 0,
                                                                 Diagnosis.diagnosisType_id == 2).first()

            if diagnosis_row:
                zno_row = Znoinfo(createDatetime=datetime.now(),
                                  createPerson_id=action_row.person_id,
                                  event_id=event_row.id,
                                  MKB=diagnosis_row.MKB)
                self.session.add(zno_row)
                self.session.flush()
                return zno_row
            return None
        return zno_row

    def process_action(self, old_action: int, actiontype_id: int):
        new_action = self.create_new_action(old_action, actiontype_id)
        bars_values = self.get_bars_values(old_action)
        for bars_row in bars_values:
            field_props = self.bars_vista_map.get(bars_row['bars_field'], None)

            if field_props:
                if field_props.get('insert_to') == 'Action':
                    if bars_row.get('bars_table_name', None):
                        bars_code = next(filter(lambda x: x is not None, [bars_row.get('bars_num_value', None),
                                                                          bars_row.get('bars_str_value', None)]), None)
                        if bars_code:
                            bars_value_str = self.get_bast_rb_value(bars_row.get('bars_table_name'), bars_code)
                            insert_value = self.get_vista_rb_id(field_props.get('vista_table'),
                                                                field_props.get('vista_table_col'),
                                                                bars_value_str)
                        else:
                            insert_value = None
                    else:
                        insert_value = bars_row.get('bars_str_value')

                    if insert_value:
                        self.insert_action_property(
                            new_action.id,
                            field_props.get("vista_type_id").get(actiontype_id),
                            insert_value,
                            field_props.get("vista_model")()
                        )
                elif field_props.get('insert_to') == 'ZNO':
                    if bars_row.get('bars_table_name', None):
                        zno_row = self.check_event_ZNO(new_action.id)
                        bars_code = next(filter(lambda x: x is not None, [bars_row.get('bars_num_value', None),
                                                                          bars_row.get('bars_str_value', None)]), None)
                        if bars_code:
                            bars_value_str = self.get_bast_rb_value(bars_row.get('bars_table_name'), bars_code)
                            if zno_row:
                                insert_value = self.get_vista_ZNO_id(tablename=field_props.get('ZNO_vista_table'),
                                                                     table_col_name=field_props.get('ZNO_vista_col'),
                                                                     table_id_name=field_props.get('ZNO_field_id_name'),
                                                                     field_value=bars_value_str,
                                                                     mkb=zno_row.MKB,
                                                                     mkb_field_name=field_props.get(
                                                                         'ZNO_vista_table_mkb_col_name'),
                                                                     chek_mkb=field_props.get('check_MKB', False),
                                                                     alchemy_table=field_props.get('alchemy_table',
                                                                                                   False))
                                if insert_value:
                                    setattr(zno_row, field_props.get('ZNO_table_coll'), insert_value)
                                    self.session.flush()
                                continue
                        else:
                            bars_value_str = '0'

                    else:
                        bars_value_str = next(filter(lambda x: x is not None, [bars_row.get('bars_num_value', None),
                                                                               bars_row.get('bars_str_value', None)]),
                                              None)
                    if str(bars_value_str) != '0':
                        zno_row = self.check_event_ZNO(new_action.id)
                        if zno_row:
                            if bars_row['bars_field'] in (
                            'LYM', 'OSS', 'HEP', 'PUL', 'PLE', 'BRA', 'SKI', 'PER', 'MAR', 'OTH', 'UMB', 'ADR',
                            'OVA') and bars_value_str:
                                bars_vista_map = {
                                    'LYM': 1,
                                    'OSS': 2,
                                    'HEP': 3,
                                    'PUL': 4,
                                    'PLE': 16,
                                    'BRA': 5,
                                    'SKI': 6,
                                    'PER': 9,
                                    'MAR': 10,
                                    'OTH': 11,
                                    'UMB': 13,
                                    'ADR': 14,
                                    'OVA': 15,
                                }
                                bars_field_value = bars_vista_map.get(bars_row['bars_field'])
                                if zno_row.Metastases:
                                    if str(bars_field_value) and str(bars_field_value) not in str(
                                            zno_row.Metastases).split(';'):
                                        zno_row.Metastases = ';'.join(
                                            str(zno_row.Metastases).split(';')) + f';{bars_field_value}'
                                        zno_row.Suspicio = None
                                else:
                                    if bars_field_value:
                                        zno_row.Metastases = bars_field_value
                                        zno_row.Suspicio = None
                            elif bars_row['bars_field'] == 'SUSPICIO':
                                zno_row.Suspicio = 1
                            elif bars_row['bars_field'] == 'Дата проведения консилиума':
                                zno_row.consiliumDate = bars_row['bars_date_value'] if bars_row[
                                    'bars_date_value'] else None
                            elif bars_row['bars_field'] == 'Индекс Карновского':
                                smth = self.session.query(Rbcarnotianindex).filter(
                                    Rbcarnotianindex.code == bars_row['bars_num_value']).first()
                                zno_row.carnotian = smth.id if smth else None
                            elif bars_row['bars_field'] == 'шкала EСOG':
                                zno_row.ecog = bars_row['bars_num_value'] if bars_row['bars_num_value'] else None
                            else:
                                insert_value = self.get_vista_ZNO_id(tablename=field_props.get('ZNO_vista_table'),
                                                                     table_col_name=field_props.get('ZNO_vista_col'),
                                                                     table_id_name=field_props.get('ZNO_field_id_name'),
                                                                     field_value=bars_value_str,
                                                                     mkb=zno_row.MKB,
                                                                     mkb_field_name=field_props.get(
                                                                         'ZNO_vista_table_mkb_col_name'),
                                                                     chek_mkb=field_props.get('check_MKB', False),
                                                                     alchemy_table=field_props.get('alchemy_table',
                                                                                                   False))
                                setattr(zno_row, field_props.get('ZNO_table_coll'), insert_value)
                            self.session.flush()
                elif field_props.get('insert_to') == 'Diagnostic':
                    action_info = self.session.query(Action).filter(Action.id == old_action).first()
                    smth_event = self.session.query(Event).filter(Event.id == action_info.event_id).first()
                    smth_diagnostic = self.session.query(Diagnostic).filter(
                        Diagnostic.event_id == smth_event.id).first()
                    diagnostic_map = {
                        'гистологический': 1,
                        'клинико-рентгенологический': 2,
                        'цитологический': 3,
                        'клинический': 4,
                        'рентгенологический': 5,
                    }
                    smth_diagnostic.diagnostic_confirmation_method_id = diagnostic_map.get(
                        str(bars_row.get('bars_str_value')).lower())
                    self.session.flush()

        self.session.commit()

    def get_vista_rb_id(self, tablename, field_name, field_value: str):
        row = self.session.query(tablename).filter(getattr(tablename, field_name) == field_value).first()
        return row.id

    def get_vista_ZNO_id(self,
                         tablename,
                         table_col_name,
                         table_id_name,
                         field_value: str,
                         mkb: str,
                         mkb_field_name: str,
                         chek_mkb: bool,
                         alchemy_table=True):
        if alchemy_table:
            if chek_mkb:
                row = self.session.query(tablename).filter(getattr(tablename.c, table_col_name) == field_value,
                                                           getattr(tablename.c, mkb_field_name) == mkb).first()
                if not row:
                    row = self.session.query(tablename).filter(getattr(tablename.c, table_col_name) == field_value,
                                                               or_(getattr(tablename.c, mkb_field_name) == '',
                                                                   getattr(tablename.c,
                                                                           mkb_field_name) == None)).first()
            else:
                row = self.session.query(tablename).filter(getattr(tablename.c, table_col_name) == field_value).first()
        else:
            if chek_mkb:
                row = self.session.query(tablename).filter(getattr(tablename, table_col_name) == field_value).first()
                if not row:
                    row = self.session.query(tablename).filter(getattr(tablename, table_col_name) == field_value,
                                                               getattr(tablename, mkb_field_name) == '').first()
            else:
                row = self.session.query(tablename).filter(getattr(tablename, table_col_name) == field_value).first()
        return getattr(row, table_id_name) if row else None

    def insert_into_ZNO(self, zno_row, bars_map, bars_value, vista_table, vista_table_id_name, zno_field_name):

        new_value = bars_map.get(int(bars_value))

        vista_value = self.session.query(vista_table).filter(vista_table.c.NAME == new_value,
                                                             vista_table.c.DS_CODE == zno_row.MKB).first()
        if not vista_value:
            vista_value = self.session.query(vista_table).filter(vista_table.c.NAME == new_value,
                                                                 vista_table.c.DS_CODE == "").first()

        setattr(zno_row, str(zno_field_name), getattr(vista_value, str(vista_table_id_name)))
        self.session.flush()

    def get_bars_values(self, old_action: int):
        with db_oracle.session_scope() as session1:
            result = session1.execute(f"""
        select D_VISIT_TAB_FIELDS.F_NAME as "bars_field",
       D_VISIT_TAB_FIELDS.id,
       D_VISIT_FIELDS.STR_VALUE as "bars_str_value",
       D_VISIT_FIELDS.DAT_VALUE as "bars_date_value",
       D_EXTRA_DICT_VALUES.NOTE as "bars_extra_value",
       D_VISIT_FIELDS.NUM_VALUE as "bars_num_value",
       D_VISIT_FIELDS.DAT_VALUE as "bars_date_value",
       D_UNITLIST.TABLENAME as "bars_table_name",
       D_VISIT_TAB_FIELDS.EDIT_METHOD as "bars_edit_method",
       D_ADD_DIR_VALUES.STR_VALUE as "bars_add_dir_value",
                      CASE
                   WHEN D_VISIT_TAB_FIELDS.EDIT_METHOD = 5 AND (D_VISIT_FIELDS.STR_VALUE = 0 OR D_VISIT_FIELDS.NUM_VALUE = 0)
                       THEN 'нет'
                   WHEN D_VISIT_TAB_FIELDS.EDIT_METHOD = 5
                       THEN 'да'
                   ELSE NULL
               END AS "bars_edit_method_result"
        from D_VISIT_FIELDS
                 join D_VISIT_TAB_FIELDS on D_VISIT_FIELDS.TEMPLATE_FIELD = D_VISIT_TAB_FIELDS.ID
                 LEFT JOIN D_EXTRA_DICT_VALUES on D_EXTRA_DICT_VALUES.PID = D_VISIT_TAB_FIELDS.EXTRA_DICT and
                                                  D_EXTRA_DICT_VALUES.NUM_VALUE = D_VISIT_FIELDS.NUM_VALUE
                 LEFT JOIN D_UNITLIST on D_UNITLIST.UNITCODE = D_VISIT_TAB_FIELDS.UNITCODE
                 LEFT JOIN D_ADD_DIR_VALUES on D_VISIT_FIELDS.ADD_DIR_VALUE = D_ADD_DIR_VALUES.id
        where D_VISIT_FIELDS.PID = {old_action}
                 """)
            rows = result.fetchall()
            json_results = []
            for row in rows:
                json_row = dict(zip(result.keys(), row))
                json_results.append(json_row)
            return json_results

    def get_bast_rb_value(self, rb_name: str, code: Union[int, str]):
        with db_oracle.session_scope() as session1:
            result = session1.execute(f"""
            select NAME as "value" from {rb_name} WHERE CODE = '{code}'
            """)
            row = result.fetchone()
            if getattr(row, "value", None) is None:
                result = session1.execute(f"""
                select NAME as "value" from {rb_name} WHERE NAME = '{code}'
                """)
                row = result.fetchone()
        return row.value

    def find_keys(self, dictionary, value):
        for key, val in dictionary.items():
            if value in val:
                return key
        return None

    def find_events(self, client_id: int):
        event_ids = self.session.query(Event).filter(Event.client_id == client_id).all()
        for event in event_ids:
            self.find_actions(event.id)

    def find_actions(self, event_id):
        actions = self.session.query(Action).filter(Action.event_id == event_id, Action.deleted == 0).order_by(
            Action.id).all()
        for row in actions:
            # маппинг формата actionttype_id  перенесенного из барса и actiontype_id в висте ( в который переливать данные)
            actiontype_map = {
                67979: [78445636, 78445624, 78445645, 78445663, 78437689, 78445651, 78445654, 78445648, 78445633,
                        78445627, 78445660, 78445621, 78399862, 78399952, 78445597, 78445603, 78506239, 78506911,
                        78506914, 97510997, 97511080, 97511461, 97511481, 98909421, 98909486],
                69165: [86391784],  # 396038604
                69156: [86391797],  # 372364712
                69159: [86391768],  # 372345307
                69162: [86482529],  # 374485107
                69163: [93361917],  # 386410919
                69164: [86391801],  # 443597216
                69167: [88014991],  # 384148054
                69168: [86391780],  # 373461147
                69152: [86398786],  # 375146427
                69157: [86391792],  # 372421538
                419294589: [87988431],
                419294588: [91093133],
                419294591: [374045742],
                419294590: [86391776]
                # маппинг формата actyiontype из висты [actiontype из ККОД (скрипт маракулина)]
            }
            actiontype = self.find_keys(actiontype_map, row.actionType_id)
            if actiontype:
                self.process_action(row.id, actiontype)
        self.session.commit()

    def fined_events(self, actiontypes):
        smth = self.session.query(Action).filter(Action.actionType_id.in_(actiontypes), Action.deleted == 0).all()
        result = set([r.event_id for r in smth])
        print(f"{len(result)} ВСЕГО")
        return result


class OracleBase:
    def test(self):
        try:
            with db_oracle.session_scope() as session:
                result = session.execute("""
select D_VISIT_TAB_FIELDS.F_NAME as "bars_field",
       D_VISIT_FIELDS.STR_VALUE as "bars_str_value",
       D_VISIT_FIELDS.DAT_VALUE as "bars_date_value",
       D_EXTRA_DICT_VALUES.NOTE as "bars_extra_value",
       D_VISIT_FIELDS.NUM_VALUE as "bars_num_value",
       D_UNITLIST.TABLENAME as "bars_table_name",
       D_VISIT_TAB_FIELDS.EDIT_METHOD as "bars_edit_method",
       D_ADD_DIR_VALUES.STR_VALUE as "bars_add_dir_value",
              CASE
           WHEN D_VISIT_TAB_FIELDS.EDIT_METHOD = 5 AND (D_VISIT_FIELDS.STR_VALUE = 0 OR D_VISIT_FIELDS.NUM_VALUE = 0)
               THEN 'нет'
           WHEN D_VISIT_TAB_FIELDS.EDIT_METHOD = 5
               THEN 'да'
           ELSE NULL
       END AS "bars_edit_method_result"
from D_VISIT_FIELDS
         join D_VISIT_TAB_FIELDS on D_VISIT_FIELDS.TEMPLATE_FIELD = D_VISIT_TAB_FIELDS.ID
         LEFT JOIN D_EXTRA_DICT_VALUES on D_EXTRA_DICT_VALUES.PID = D_VISIT_TAB_FIELDS.EXTRA_DICT and
                                          D_EXTRA_DICT_VALUES.NUM_VALUE = D_VISIT_FIELDS.NUM_VALUE
         LEFT JOIN D_UNITLIST on D_UNITLIST.UNITCODE = D_VISIT_TAB_FIELDS.UNITCODE
         LEFT JOIN D_ADD_DIR_VALUES on D_VISIT_FIELDS.ADD_DIR_VALUE = D_ADD_DIR_VALUES.id
where D_VISIT_FIELDS.PID in (248288668)
         """)
                rows = result.fetchall()
                json_results = []
                for row in rows:
                    json_row = dict(zip(result.keys(), row))
                    json_results.append(json_row)
                return json_results
        except Exception as e:
            print(f"Failed to connect to Oracle database: {e}")


def process_event(event_id):
    print(event_id)
    if event_id != 244088331:
        actions = c.find_actions(event_id)
        return actions


logging.basicConfig(filename='client_processing.log',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def process_message(client_id):
    # Создаем новый экземпляр CMergeActions для каждого потока
    c = CMergeActions()
    print(f"Consumed client ID: {client_id}")
    # Process the consumed client ID
    try:
        c.find_events(client_id)
    except Exception as e:
        with open('error_clients.txt', 'a') as error_file:
            error_file.write(f"{client_id},")
        logging.error(f"Error processing client ID: {client_id}, Error: {e}")


def callback(ch, method, properties, body, executor):
    client_id = struct.unpack('i', body)[0]
    executor.submit(process_message, client_id)


if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='client_bars')

    max_workers = 10  # Задайте оптимальное количество потоков для вашего процессора

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        def wrapped_callback(ch, method, properties, body):
            callback(ch, method, properties, body, executor)


        channel.basic_consume(queue='client_bars', on_message_callback=wrapped_callback, auto_ack=True)
        logging.info('Started consuming...')
        channel.start_consuming()