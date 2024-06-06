import contextlib
from typing import Dict, Type, Union

import sqlalchemy
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.sql import Selectable

from database.models import ModelBase
import datetime as dt


class Singleton(type):
    _instances: Dict[Type, Dict[str, object]] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = {}
        key = str(args) + str(kwargs)
        if key not in cls._instances[cls]:
            cls._instances[cls][key] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls][key]


class Database(metaclass=Singleton):
    _instance: 'Database' = None

    def __init__(self, db_config: dict, string=None) -> None:
        self._config = db_config
        self.engine = sqlalchemy.create_engine(self.prepare_connection_string(self._config) if not string else string,
                                               echo=False,
                                               encoding='utf8',
                                               convert_unicode=True)
        self.connection = self.engine.connect()

    @contextlib.contextmanager
    def session_scope(self) -> Session:
        session = self._get_session()
        try:
            yield session
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise
        finally:
            session.close()

    def insert_if_not_exists(self, table, **data):
        with self.session_scope() as session:
            result = session.query(table).filter_by(**data).first()
            if not result:
                session.merge(table(**data))
                session.commit()
            return session.query(table).filter_by(**data).first() if not result else result

    def execute(self, stmt):
        with self.session_scope() as session:
            result = session.execute(stmt).scalars().all()
            return result

    def get_value(self, stmt: Union[str, Selectable]):
        with self.session_scope() as session:
            return session.execute(stmt).scalars().first()

    def get_record(self, stmt: Union[str, Selectable]):
        with self.session_scope() as session:
            return session.execute(stmt).first()

    def get_record_list(self, stmt: Union[str, Selectable]):
        with self.session_scope() as session:
            return session.execute(stmt).all()

    def test_(self, smth):
        with self.session_scope() as session:
            return session.query(smth).all()

    def update_record(self, model, condition: list, values: dict):
        """
        :return: True, если запись обновлена успешно. False - если такой записи нет в БД
        """
        with self.session_scope() as session:
            res = session.execute(
                select(model)
                .where(*condition)
            ).first()
            if res:
                res = res[0]
                for key, value in values.items():
                    setattr(res, key, value)
                session.add(res)
                session.flush()
                return True

            return False

    def update_records(self, model, condition: list, values: dict):
        with self.session_scope() as session:
            for res in session.execute(
                    select(model)
                    .where(*condition)
            ).all():
                res = res[0]
                for key, value in values.items():
                    setattr(res, key, value)
                session.add(res)

    @staticmethod
    def prepare_connection_string(config: dict):
        user = config.pop('user') or ''
        password = config.pop('password') or ''
        host = config.pop('host')
        port = config.pop('port') or ''
        database = config.pop('database') or ''
        engine = config.pop('engine')
        return (f'{engine}://{user}{":" if user and password else ""}'
                f'{password}{"@" if user and password else ""}{host}{":" if port else ""}{port}'
                f'{"/" if database else ""}{database}{"?" if config else ""}'
                f'{"&".join(f"{key}={value}" for key, value in config.items())}')

    @staticmethod
    def prepare_model(model: ModelBase):
        """
        Заполняет дефотные поля
        Можно сюда тоже что-нибудь добавить, если встретите
        """
        if hasattr(model, 'createDatetime'):
            model.createDatetime = dt.datetime.now()
        if hasattr(model, 'modifyDatetime'):
            model.modifyDatetime = dt.datetime.now()
        if hasattr(model, 'deleted'):
            model.deleted = 0
        if hasattr(model, 'createPerson_id'):
            model.createPerson_id = 1
        if hasattr(model, 'modifyPerson_id'):
            model.modifyPerson_id = 1
        return model

    # ------ PRIVATE ------ #

    def _get_session(self) -> Session:
        return sqlalchemy.orm.sessionmaker(bind=self.engine)()
