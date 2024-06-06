from sqlalchemy import (CHAR, DECIMAL, TIMESTAMP, Column, Computed, Date,
                        DateTime, Enum, Float, ForeignKey, Index, LargeBinary,
                        String, Table, Text, Time, TEXT)
from sqlalchemy import text as alchemy_text
from sqlalchemy.dialects.mysql import (BIGINT, DATETIME, INTEGER, LONGBLOB,
                                       LONGTEXT, MEDIUMBLOB, MEDIUMTEXT,
                                       SMALLINT, TINYINT, TINYTEXT, VARCHAR, BIT)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import ColumnProperty, InstrumentedAttribute, relationship


class ModelBase(object):
    def __repr__(self) -> str:
        vals = ", ".join(f"{v.key}={getattr(self, v.key)}" for v in self.__class__.__dict__.values() if
                         isinstance(v, InstrumentedAttribute) and isinstance(v.property, ColumnProperty))
        return f'<{self.__class__.__name__} {vals}>'

    def __str__(self) -> str:
        return repr(self)


Base = declarative_base(cls=ModelBase)
metadata = Base.metadata

class AISControl(Base):
    __tablename__ = 'AISControl'
    __table_args__ = {'comment': 'Расписание АИС Информ'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(11))
    department = Column(Text)
    begDate = Column(Date)
    endDate = Column(Date)
    begTime = Column(Text)
    endTime = Column(Text)
    comments = Column(Text)
    aisId = Column(Text)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    aisDayId = Column(INTEGER(11))
    attendanceLimit = Column(INTEGER(11))


t_AISInformConnect = Table(
    'AISInformConnect', metadata,
    Column('address', Text),
    Column('login', Text),
    Column('password', Text)
)


t_Account12 = Table(
    'Account12', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('createDatetime', DateTime, nullable=False),
    Column('createPerson_id', INTEGER(11)),
    Column('modifyDatetime', DateTime, nullable=False),
    Column('modifyPerson_id', INTEGER(11)),
    Column('deleted', TINYINT(1), nullable=False, server_default=alchemy_text("0")),
    Column('contract_id', INTEGER(11), nullable=False),
    Column('orgStructure_id', INTEGER(11)),
    Column('payer_id', INTEGER(11), nullable=False),
    Column('settleDate', Date, nullable=False),
    Column('number', String(64), server_default=alchemy_text("''")),
    Column('date', Date, nullable=False),
    Column('amount', DECIMAL(10, 2), nullable=False),
    Column('uet', DECIMAL(10, 2), nullable=False),
    Column('sum', DECIMAL(10, 2), nullable=False),
    Column('exposeDate', Date),
    Column('payedAmount', DECIMAL(10, 2), nullable=False),
    Column('payedSum', DECIMAL(10, 2), nullable=False),
    Column('refusedAmount', DECIMAL(10, 2), nullable=False),
    Column('refusedSum', DECIMAL(10, 2), nullable=False),
    Column('format_id', INTEGER(11))
)


class ActionPropertyTemplate(Base):
    __tablename__ = 'ActionPropertyTemplate'
    __table_args__ = {'comment': 'Шаблоны свойств действий'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    group_id = Column(INTEGER(11))
    parentCode = Column(String(20), nullable=False)
    code = Column(String(64), nullable=False)
    federalCode = Column(String(64), nullable=False)
    regionalCode = Column(String(64), nullable=False)
    name = Column(String(120), nullable=False)
    abbrev = Column(String(64), nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    service_id = Column(INTEGER(11))


class ActionPropertyImageMap(Base):
    __tablename__ = 'ActionProperty_ImageMap'
    __table_args__ = {'comment': 'Маркировка изображения'}

    id = Column(INTEGER(11), primary_key=True)
    index = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    value = Column(MEDIUMTEXT)


class ActionPropertyReference(Base):
    __tablename__ = 'ActionProperty_Reference'

    id = Column(INTEGER(11), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False)
    value = Column(INTEGER(11))


t_ActionType_Service66 = Table(
    'ActionType_Service66', metadata,
    Column('master_id', Float(10, True)),
    Column('idx', Float(10, True)),
    Column('finance_id', Float(10, True)),
    Column('service_id', Float(10, True))
)


class ActionTestResult(Base):
    __tablename__ = 'Action_TestResults'
    __table_args__ = {'comment': 'Данные из лабараторного анализатора'}

    id = Column(INTEGER(11), primary_key=True)
    action_id = Column(INTEGER(16))
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    WBC = Column(String(64))
    RBC = Column(String(64))
    HGB = Column(String(64))
    HCT = Column(String(64))
    MCV = Column(String(64))
    MCH = Column(String(64))
    MCHC = Column(String(64))
    PLT = Column(String(64))
    LYM_P = Column(String(64))
    MXD_P = Column(String(64))
    NEUT_P = Column(String(64))
    LYM = Column(String(64))
    MXD = Column(String(64))
    NEUT = Column(String(64))
    RDW_SD = Column(String(64))
    RDW_CV = Column(String(64))
    PDW = Column(String(64))
    MPV = Column(String(64))
    P_LCR = Column(String(64))
    PCT = Column(String(64))
    isLoaded = Column(TINYINT(1), server_default=alchemy_text("0"))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))


class AdditionalFeaturesUrl(Base):
    __tablename__ = 'AdditionalFeaturesUrl'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(128), nullable=False)
    template = Column(String(256), nullable=False)
    tabRegistry = Column(INTEGER(1), server_default=alchemy_text("0"))
    tabEvents = Column(INTEGER(1), server_default=alchemy_text("0"))
    tabAmbCard = Column(INTEGER(1), server_default=alchemy_text("0"))
    tabActions = Column(INTEGER(1), server_default=alchemy_text("0"))


class AddressHouseCopy(Base):
    __tablename__ = 'AddressHouse_copy'
    __table_args__ = {'comment': 'Дома'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    KLADRCode = Column(String(13), nullable=False)
    KLADRStreetCode = Column(String(17), nullable=False)
    number = Column(String(8), nullable=False)
    corpus = Column(String(8), nullable=False)
    litera = Column(String(8))
    KLADRCode_old = Column(String(13), nullable=False)
    KLADRStreetCode_old = Column(String(17), nullable=False)


class AgreementPatientPrint(Base):
    __tablename__ = 'AgreementPatientPrints'
    __table_args__ = {'comment': 'Таблица, шаблонов эпикризов.'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(INTEGER(11), nullable=False)
    client_id = Column(INTEGER(11))
    template_id = Column(INTEGER(11))
    dateTime = Column(DateTime, nullable=False)


class AppLock(Base):
    __tablename__ = 'AppLock'
    __table_args__ = {'comment': 'Прикладные блокировки'}

    id = Column(BIGINT(20), primary_key=True)
    lockTime = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("'0000-00-00 00:00:00'"))
    retTime = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("'0000-00-00 00:00:00'"))
    connectionId = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    person_id = Column(INTEGER(11))
    addr = Column(String(255), nullable=False)
    lockType = Column(TINYINT(3), server_default=alchemy_text("0"))
    lockCount = Column(TINYINT(3), server_default=alchemy_text("0"))


class AttachedClientInfo(Base):
    __tablename__ = 'AttachedClientInfo'
    __table_args__ = {'comment': 'Информация о прикрепленном пациенте'}

    id = Column(INTEGER(11), primary_key=True)
    senderCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    lastName = Column(String(30), nullable=False, server_default=alchemy_text("''"))
    firstName = Column(String(30), nullable=False, server_default=alchemy_text("''"))
    patrName = Column(String(30), nullable=False, server_default=alchemy_text("''"))
    birthDate = Column(Date)
    sex = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    SNILS = Column(CHAR(11), nullable=False, server_default=alchemy_text("''"))
    docType = Column(TINYINT(1))
    docSerial = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    docNumber = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    policyType = Column(TINYINT(1))
    policySerial = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    policyNumber = Column(String(35), nullable=False, server_default=alchemy_text("''"))
    insurerCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    internalId = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    regDistrict = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    regCity = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    regLocality = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    regStreet = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    regHouse = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    regCorpus = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    regFlat = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    locDistrict = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    locCity = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    locLocality = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    locStreet = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    locHouse = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    locCorpus = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    locFlat = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    attachType = Column(TINYINT(1), server_default=alchemy_text("0"))
    orgCode = Column(CHAR(16), nullable=False)
    sectionCode = Column(CHAR(16), nullable=False)
    begDate = Column(Date)
    endDate = Column(Date)
    doctorSNILS = Column(CHAR(11), nullable=False, server_default=alchemy_text("''"))
    deattachReason = Column(TINYINT(1), server_default=alchemy_text("0"))
    syncStatus = Column(TINYINT(1), server_default=alchemy_text("0"))
    client_id = Column(INTEGER(11))
    attach_id = Column(INTEGER(11))
    orgStructure_id = Column(INTEGER(11))


class CalendarException(Base):
    __tablename__ = 'CalendarExceptions'
    __table_args__ = {'comment': 'Календарные праздники и переносы дней'}

    id = Column(INTEGER(5), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    date = Column(Date, nullable=False)
    endDate = Column(Date)
    isHoliday = Column(TINYINT(1), nullable=False)
    startYear = Column(SMALLINT(4))
    finishYear = Column(SMALLINT(4))
    fromDate = Column(Date)
    text = Column(String(250), nullable=False)


class CashBoxOperationLogger(Base):
    __tablename__ = 'CashBoxOperationLogger'

    id = Column(INTEGER(11), primary_key=True)
    datetime = Column(DateTime)
    block_id = Column(Text)
    operation = Column(Text)
    description = Column(Text)
    log = Column(Text)
    type = Column(Text)


class CashierInfo(Base):
    __tablename__ = 'CashierInfo'

    id = Column(INTEGER(11), primary_key=True)
    Name = Column(String(32))
    INN = Column(String(20))
    Open_date = Column(DateTime)
    Close_date = Column(DateTime)
    CashboxNumber = Column(String(32))


class ChemyFormClassifier(Base):
    __tablename__ = 'ChemyFormClassifier'
    __table_args__ = {'comment': 'Классификатор лекарственных форм'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    name = Column(String(255))


class ChemyClassifier(Base):
    __tablename__ = 'Chemy_classifier'
    __table_args__ = {'comment': 'Справочник "Анатомо-терапевтическо-химическая классификация"'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    name = Column(String(250))
    IdAnatomicTherapeuticChemicalClassification = Column(INTEGER(11))
    num = Column(INTEGER(11))
    latName = Column(String(250))
    high = Column(INTEGER(11))
    version = Column(Date)
    DateBegin = Column(Date)
    DateEnd = Column(Date)


class ClientAttachCopy(Base):
    __tablename__ = 'ClientAttach_copy'
    __table_args__ = {'comment': 'Прикрепление пациентов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(INTEGER(11), nullable=False)
    attachType_id = Column(INTEGER(11), nullable=False)
    LPU_id = Column(INTEGER(11), nullable=False)
    netType = Column(INTEGER(11))
    orgStructure_id = Column(INTEGER(11))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date)
    document_id = Column(INTEGER(11))
    detachment_id = Column(INTEGER(11))
    sentToTFOMS = Column(TINYINT(1), nullable=False)
    errorCode = Column(String(256))
    reason = Column(TINYINT(4), server_default=alchemy_text("0"))


class ClientDispanserization(Base):
    __tablename__ = 'ClientDispanserization'
    __table_args__ = {'comment': 'Таблица, данных о диспансеризации.'}

    id = Column(INTEGER(11), primary_key=True)
    create_datetime = Column(DateTime, nullable=False)
    client_id = Column(INTEGER(11), nullable=False)
    code = Column(String(8), nullable=False)
    date_begin = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    codeMO = Column(String(8), nullable=False)


class ClientPolicyCopy(Base):
    __tablename__ = 'ClientPolicy_copy'
    __table_args__ = {'comment': 'Полисы пациентов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(INTEGER(11), nullable=False)
    insurer_id = Column(INTEGER(11))
    policyType_id = Column(INTEGER(11))
    policyKind_id = Column(INTEGER(11))
    serial = Column(String(16), nullable=False)
    number = Column(String(35), nullable=False)
    begDate = Column(Date, nullable=False)
    endDate = Column(Date)
    dischargeDate = Column(Date)
    name = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    note = Column(String(200), nullable=False, server_default=alchemy_text("''"))
    insuranceArea = Column(String(13), nullable=False)
    isSearchPolicy = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    franchisePercent = Column(Float, server_default=alchemy_text("0"))


class ClientRecipeExport(Base):
    __tablename__ = 'ClientRecipeExport'
    __table_args__ = {'comment': 'Информация об отправке данных пациента в МИАЦ (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(INTEGER(11), nullable=False)
    sentToMiac = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    errorCode = Column(String(250))


class ClientQuotingDiscussion(Base):
    __tablename__ = 'Client_QuotingDiscussion'
    __table_args__ = {'comment': 'Переговоры по квоте'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    dateMessage = Column(DateTime, nullable=False)
    agreementType_id = Column(INTEGER(11))
    responsiblePerson_id = Column(INTEGER(11))
    cosignatory = Column(String(25))
    cosignatoryPost = Column(String(20))
    cosignatoryName = Column(String(50))
    remark = Column(String(128))


class ClinicalTrialsDate(Base):
    __tablename__ = 'Clinical_Trials_Date'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp() ON UPDATE current_timestamp()"))
    ticketValue = Column(Text)
    person_id = Column(String(64))
    event_id = Column(String(64))
    action_id = Column(String(64))


t_ContrTspr = Table(
    'ContrTspr', metadata,
    Column('ID', INTEGER(11)),
    Column('MASTER_ID', INTEGER(11)),
    Column('TARIFFTYPE', INTEGER(1)),
    Column('BEGDATE', DateTime),
    Column('ENDDATE', DateTime)
)


t_Contract_Tariff_s12 = Table(
    'Contract_Tariff_s12', metadata,
    Column('Column1', String(255)),
    Column('Column2', String(255)),
    Column('Column3', String(255)),
    Column('Column4', String(255)),
    Column('Column5', String(255)),
    Column('Column6', String(255)),
    Column('Column7', String(255)),
    Column('Column8', String(255)),
    Column('Column9', String(255)),
    Column('Column10', String(255)),
    Column('Column11', String(255)),
    Column('Column12', String(255)),
    Column('Column13', String(255)),
    Column('Column14', String(255)),
    Column('Column15', String(255)),
    Column('Column16', String(255)),
    Column('Column17', String(255)),
    Column('Column18', String(255)),
    Column('Column19', String(255)),
    Column('Column20', String(255)),
    Column('Column21', String(255)),
    Column('Column22', String(255)),
    Column('Column23', String(255)),
    Column('Column24', String(255)),
    Column('Column25', String(255)),
    Column('Column26', String(255)),
    Column('Column27', String(255)),
    Column('Column28', String(255)),
    Column('Column29', String(255)),
    Column('Column30', String(255)),
    Column('Column31', String(255)),
    Column('Column32', String(255)),
    Column('Column33', String(255)),
    Column('Column34', String(255))
)


t_DD2019 = Table(
    'DD2019', metadata,
    Column('PROF_NAME', String(100)),
    Column('PROF_CODE', INTEGER(11)),
    Column('ID_PRVS', INTEGER(11)),
    Column('PRVS_NAME', String(50)),
    Column('PRVS_CODE', INTEGER(11)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('TYPE_NAME', String(50)),
    Column('PRVS_PR_G', INTEGER(11)),
    Column('PRVS_PR_SK', INTEGER(11)),
    Column('CODE', String(50)),
    Column('IDSERVDATA', INTEGER(11)),
    Column('SERV_NAME', String(100)),
    Column('tariff', String(50))
)


t_DD_age = Table(
    'DD_age', metadata,
    Column('code', String(255)),
    Column('age', String(255))
)


class DatabaseUpdateInfo(Base):
    __tablename__ = 'DatabaseUpdateInfo'
    __table_args__ = {'comment': 'Информация о сделанных апдейтах базы.'}

    id = Column(INTEGER(11), primary_key=True)
    revision = Column(String(16), nullable=False)
    user = Column(String(64), nullable=False)
    execDatetime = Column(DateTime)
    updateDate = Column(Date)
    issueNumber = Column(String(16))
    note = Column(String(128), nullable=False)
    completed = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    updateNumber = Column(String(32))


class DoseClassifier(Base):
    __tablename__ = 'Dose_classifier'
    __table_args__ = {'comment': 'Классификатор единиц измерения'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(String(64))
    version = Column(Date)


t_DoublesForDelete = Table(
    'DoublesForDelete', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('m', INTEGER(11), nullable=False),
    Column('s', INTEGER(11))
)


class DrugDeliveryType(Base):
    __tablename__ = 'DrugDeliveryType'
    __table_args__ = {'comment': 'Тип выдачи препарата'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(10))
    name = Column(String(64))


class DrugLPR78(Base):
    __tablename__ = 'DrugLPR78'
    __table_args__ = {'comment': 'ЛП и МИ льготных рецептов (СПб)'}

    id = Column(INTEGER(11), primary_key=True)
    nomk_ls = Column(String(100))
    name_med = Column(String(100))
    mnn = Column(String(100))
    asmnn_l = Column(String(100))
    name_fct = Column(String(100))
    flag_kek = Column(String(100))
    ko_ost = Column(String(100))
    MI = Column(String(100))
    D_LS_doc = Column(String(100))
    N_FV = Column(String(100))
    NAME_LF_L = Column(String(100))
    NAME_LF_R = Column(String(100))
    validity = Column(INTEGER(11))
    view_packing = Column(INTEGER(11))
    quantity = Column(INTEGER(11))
    signature = Column(Text)


class EQueueTablePerson(Base):
    __tablename__ = 'EQueueTablePerson'
    __table_args__ = {'comment': 'Электронная очередь к врачу'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(INTEGER(11), nullable=False)
    office = Column(String(30), nullable=False)


class EmergencyBrigadeTemplate(Base):
    __tablename__ = 'EmergencyBrigadeTemplate'

    id = Column(INTEGER(11), primary_key=True)
    car_id = Column(INTEGER(11), nullable=False)
    driver_id = Column(INTEGER(11), nullable=False)
    doctor_id = Column(INTEGER(11))
    paramedic_id = Column(INTEGER(11))
    orderly_id = Column(INTEGER(11))
    inWork = Column(CHAR(1), nullable=False, server_default=alchemy_text("'0'"))
    group_id = Column(INTEGER(11))
    deleted = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    counter = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))


class EmergencyCallReason(Base):
    __tablename__ = 'EmergencyCallReason'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(String(50))


class EmergencyCallTemp(Base):
    __tablename__ = 'EmergencyCallTemp'
    __table_args__ = {'comment': 'таблица обработки вызовов'}

    id = Column(INTEGER(11), primary_key=True)
    callStatus = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientUnknown = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientLastName = Column(VARCHAR(128), nullable=False, server_default=alchemy_text("''"))
    patientFirstName = Column(VARCHAR(255), server_default=alchemy_text("''"))
    patientPatrName = Column(VARCHAR(255), server_default=alchemy_text("''"))
    patientSex = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientBDate = Column(Date)
    patientAge = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    patientDocType = Column(INTEGER(11), nullable=False, server_default=alchemy_text("1"))
    patientDocSerial = Column(VARCHAR(64), nullable=False, server_default=alchemy_text("''"))
    patientDocNumber = Column(VARCHAR(64), nullable=False, server_default=alchemy_text("''"))
    patientNote = Column(VARCHAR(255))
    patientInsurer = Column(VARCHAR(255))
    patientPolisSerial = Column(VARCHAR(16))
    patientPolisNumber = Column(VARCHAR(64))
    patientPolisFrom = Column(Date)
    patientPolisTo = Column(Date)
    callSource = Column(VARCHAR(128))
    callPhone = Column(VARCHAR(255))
    callId = Column(VARCHAR(255))
    callContract = Column(INTEGER(11))
    callReason = Column(VARCHAR(255))
    callCause = Column(INTEGER(11))
    callStreet = Column(VARCHAR(255))
    callHouse = Column(VARCHAR(16))
    callKorp = Column(VARCHAR(16))
    callFrontRoom = Column(String(45))
    callApt = Column(VARCHAR(255))
    callFlat = Column(VARCHAR(8))
    callHousePhone = Column(VARCHAR(16))
    callSide = Column(INTEGER(1), server_default=alchemy_text("0"))
    callPatType = Column(INTEGER(11))
    callType = Column(INTEGER(11))
    callDateTime = Column(DateTime)
    callAssignDateTime = Column(DateTime)
    callBrigade = Column(INTEGER(11))
    callCloseDateTime = Column(DateTime)
    callDiagnosis = Column(VARCHAR(255))
    callHospital = Column(VARCHAR(128))
    callHospitalOrder = Column(VARCHAR(64))
    callComment = Column(VARCHAR(255))
    callResultOms = Column(INTEGER(11))
    callPlace = Column(INTEGER(11))
    callRecvMethod = Column(INTEGER(11))
    callDelay = Column(INTEGER(11))
    callResultSmp = Column(INTEGER(11))
    callAccident = Column(INTEGER(11))
    callDeath = Column(INTEGER(11))
    callEbriety = Column(INTEGER(11))
    callPlaceType = Column(INTEGER(11))
    callTransport = Column(INTEGER(11))
    callTransportResult = Column(INTEGER(11))
    callCancelPerson = Column(VARCHAR(255))
    callActive = Column(INTEGER(11))
    callNoLPU = Column(INTEGER(11))
    callActiveDateTime = Column(DateTime)
    callDisease = Column(INTEGER(1))
    callBirth = Column(INTEGER(1))
    callPregnancyFailure = Column(INTEGER(1))
    operatorId = Column(INTEGER(11))
    callActiveLpu = Column(VARCHAR(255))
    callDriveStartDateTime = Column(DateTime)
    callDriveStopDateTime = Column(DateTime)
    callServiceStartDateTime = Column(DateTime)
    callServiceStopDateTime = Column(DateTime)
    callReturnDateTime = Column(DateTime)
    callReanimation = Column(INTEGER(1))
    callProfile = Column(INTEGER(11))
    callAction = Column(INTEGER(11))
    callBrigadeMembers = Column(VARCHAR(255))
    isExported = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    callGroupId = Column(INTEGER(11), nullable=False, server_default=alchemy_text("1"))
    callDiseaseType = Column(INTEGER(11))
    callIdDay = Column(String(255))
    callEpidNo = Column(INTEGER(11))
    callPhone03 = Column(String(255))
    callDispatcherPhone = Column(String(255))
    patientRegion = Column(VARCHAR(255))
    patientArea = Column(VARCHAR(255))
    patientStreetRegistered = Column(VARCHAR(255))
    patientHouseRegistered = Column(VARCHAR(16))
    patientKorpRegistered = Column(VARCHAR(16))
    patientFlatRegistered = Column(VARCHAR(128))
    patientNotLocal = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientBirthPlace = Column(VARCHAR(255))
    patientSNILS = Column(VARCHAR(255))
    patientDocOrigin = Column(VARCHAR(255))
    patientDocDate = Column(Date)
    patientPolicyType = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientJob = Column(VARCHAR(255))
    patientPost = Column(VARCHAR(255))
    patientNationality = Column(INTEGER(11))
    callSendDoctor = Column(VARCHAR(128), server_default=alchemy_text("''"))
    callActiveAccepted = Column(VARCHAR(128), server_default=alchemy_text("''"))
    callBrigadeType = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientNamePolicy = Column(VARCHAR(255))
    patientRelation = Column(INTEGER(11))
    callParentLinkType = Column(INTEGER(11))
    callFreeInputCheckbox = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    callParentLastName = Column(VARCHAR(50), nullable=False, server_default=alchemy_text("''"))
    callParentFirstName = Column(VARCHAR(50), nullable=False, server_default=alchemy_text("''"))
    callParentPatrName = Column(VARCHAR(50), nullable=False, server_default=alchemy_text("''"))
    callParentBDate = Column(Date)
    patientNewBorn = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientFreeInputCheckboxPar = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientFreeInputPar = Column(VARCHAR(128), server_default=alchemy_text("''"))
    patientNonresident = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    patientLocalityKLADR = Column(String(64), server_default=alchemy_text("''"))
    patientLocalityRegistered = Column(VARCHAR(255))
    patientLocalityRegisteredTemp = Column(VARCHAR(255))
    patientStreetRegisteredTemp = Column(VARCHAR(255))
    patientHouseRegisteredTemp = Column(VARCHAR(255))
    patientKorpRegisteredTemp = Column(VARCHAR(255))
    patientFlatRegisteredTemp = Column(VARCHAR(255))
    callFreeInputCheckboxTemp = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    callFreeInput = Column(VARCHAR(255), server_default=alchemy_text("''"))
    callFreeInputTemp = Column(VARCHAR(255), server_default=alchemy_text("''"))
    callParentDocType = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    callParentDocSerial = Column(VARCHAR(64), nullable=False, server_default=alchemy_text("''"))
    callParentDocNumber = Column(VARCHAR(64), nullable=False, server_default=alchemy_text("''"))


class EmergencyCar(Base):
    __tablename__ = 'EmergencyCars'
    __table_args__ = {'comment': 'Машины скорой помощи'}

    id = Column(INTEGER(11), primary_key=True)
    number = Column(VARCHAR(16), nullable=False)
    comment = Column(VARCHAR(64))
    group_id = Column(INTEGER(11), nullable=False, server_default=alchemy_text("1"))
    deleted = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))


class EmergencyGroup(Base):
    __tablename__ = 'EmergencyGroup'
    __table_args__ = {'comment': 'группы скорой помощи'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(64))
    code = Column(VARCHAR(16))
    regionalCode = Column(VARCHAR(16))
    orgName = Column(VARCHAR(128))


class EmergencyMedicament(Base):
    __tablename__ = 'EmergencyMedicaments'

    id = Column(INTEGER(11), primary_key=True)
    medicament_id = Column(INTEGER(11), nullable=False)
    date = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp()"))
    balance = Column(Float, nullable=False, server_default=alchemy_text("0"))
    serial = Column(VARCHAR(32))
    expDate = Column(Date)
    personId = Column(String(255), nullable=False)


class EmergencyMedicamentsBrigade(Base):
    __tablename__ = 'EmergencyMedicamentsBrigade'

    id = Column(INTEGER(11), primary_key=True)
    brigade_id = Column(INTEGER(11), nullable=False)
    medicament_id = Column(INTEGER(11), nullable=False)
    balance = Column(Float, nullable=False, server_default=alchemy_text("0"))
    updateDate = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp()"))
    minRest = Column(String(255), nullable=False, server_default=alchemy_text("'20'"))
    replenishment = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))


class EmergencyMedicamentsBrigadeExt(Base):
    __tablename__ = 'EmergencyMedicamentsBrigadeExt'

    id = Column(INTEGER(11), primary_key=True)
    brigade_id = Column(INTEGER(11), nullable=False)
    medicament_id = Column(INTEGER(11), nullable=False)
    balance = Column(Float, nullable=False, server_default=alchemy_text("0"))
    minRest = Column(String(255), nullable=False, server_default=alchemy_text("'20'"))
    replenishment = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    taken = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    updateDate = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp()"))
    personId = Column(String(255), nullable=False)


class EmergencyMedicamentsBrigadeExtWork(Base):
    __tablename__ = 'EmergencyMedicamentsBrigadeExtWork'

    id = Column(INTEGER(11), primary_key=True)
    brigade_id = Column(INTEGER(11), nullable=False)
    medicament_id = Column(INTEGER(11), server_default=alchemy_text("0"))
    balance = Column(Float, nullable=False, server_default=alchemy_text("0"))
    minRest = Column(String(255), nullable=False, server_default=alchemy_text("'20'"))
    replenishment = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    taken = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    updateDate = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp()"))
    personId = Column(String(255), nullable=False)


class EmergencyMedicamentsCall(Base):
    __tablename__ = 'EmergencyMedicamentsCall'

    id = Column(INTEGER(11), primary_key=True)
    callId = Column(INTEGER(11))
    medicamentBrigade_id = Column(INTEGER(11))
    balance = Column(Float)
    dateDebit = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp()"))


class EmergencyMedicamentsCallExt(Base):
    __tablename__ = 'EmergencyMedicamentsCallExt'

    id = Column(INTEGER(11), primary_key=True)
    idClient = Column(INTEGER(11))
    callId = Column(INTEGER(11))
    medicamentBrigade_id = Column(INTEGER(11))
    medicament = Column(String(255))
    balance = Column(Float)
    dateDebit = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp()"))


class EmergencyMedicamentsStoreBag(Base):
    __tablename__ = 'EmergencyMedicamentsStoreBag'

    id = Column(INTEGER(11), primary_key=True)
    medicament_id = Column(INTEGER(11), nullable=False)
    expDate = Column(INTEGER(11), nullable=False)
    amountPack = Column(INTEGER(11))
    minRest = Column(INTEGER(11), nullable=False)
    balance = Column(Float, nullable=False, server_default=alchemy_text("0"))
    replenishment = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    order = Column(INTEGER(11), server_default=alchemy_text("0"))
    taken = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    putDate = Column(DateTime)
    personId = Column(String(255), nullable=False)


class EmergencyMedicamentsCopy(Base):
    __tablename__ = 'EmergencyMedicaments_Copy'

    id = Column(INTEGER(11), primary_key=True)
    medicament_id = Column(INTEGER(11), nullable=False)
    date = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp()"))
    balance = Column(Float, nullable=False, server_default=alchemy_text("0"))
    serial = Column(String(32))
    expDate = Column(Date)
    personId = Column(String(255), nullable=False)


class EmergencyPersonnel(Base):
    __tablename__ = 'EmergencyPersonnel'
    __table_args__ = {'comment': 'список сотрудников CМП'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(INTEGER(11), nullable=False)
    type_id = Column(INTEGER(11))
    group_id = Column(INTEGER(11))


t_EpicrisisProperty = Table(
    'EpicrisisProperty', metadata,
    Column('id', INTEGER(11)),
    Column('idx_section', INTEGER(11), nullable=False),
    Column('name', String(64), nullable=False),
    Column('type', String(64), nullable=False),
    Column('defaultValue', Text),
    Column('htmlTemplate', Text),
    Column('valueDomain', String(120)),
    Column('orgStruct', String(120)),
    Column('isRequired', TINYINT(1)),
    Column('isEditable', TINYINT(1)),
    Column('idTable', INTEGER(11), nullable=False),
    Column('description', String(200)),
    comment='Таблица свойств разделов эпикризов.'
)


t_EpicrisisSections = Table(
    'EpicrisisSections', metadata,
    Column('id', INTEGER(11)),
    Column('idx', INTEGER(11), nullable=False),
    Column('name', String(64), nullable=False),
    Column('id_rbEpicrisSections', INTEGER(11)),
    Column('isEditable', TINYINT(1)),
    Column('isRequired', TINYINT(1)),
    Column('description', String(200)),
    comment='Таблица разделов эпикризов.'
)


class Event(Base):
    __tablename__ = 'Event'
    __table_args__ = {'comment': 'Событие/Inspection'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    externalId = Column(String(30), nullable=False)
    eventType_id = Column(ForeignKey('EventType.id'), nullable=False)
    org_id = Column(INTEGER(11))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'))
    contract_id = Column(ForeignKey('Contract.id'))
    prevEventDate = Column(DateTime)
    setDate = Column(DateTime, nullable=False)
    setPerson_id = Column(ForeignKey('Person.id'))
    execDate = Column(DateTime)
    execPerson_id = Column(ForeignKey('Person.id'))
    isPrimary = Column(TINYINT(1), nullable=False)
    order = Column(TINYINT(1), nullable=False)
    result_id = Column(ForeignKey('rbResult.id'))
    nextEventDate = Column(DateTime)
    payStatus = Column(INTEGER(11), nullable=False)
    typeAsset_id = Column(ForeignKey('rbEmergencyTypeAsset.id'))
    note = Column(Text, nullable=False)
    curator_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    assistant_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    pregnancyWeek = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    MES_id = Column(INTEGER(11))
    HTG_id = Column(INTEGER(11))
    KSG_id = Column(INTEGER(11))
    mesSpecification_id = Column(ForeignKey('rbMesSpecification.id', ondelete='SET NULL'))
    relegateOrg_id = Column(ForeignKey('Organisation.id', ondelete='CASCADE', onupdate='CASCADE'))
    totalCost = Column(Float(asdecimal=True), nullable=False)
    patientModel_id = Column(ForeignKey('rbPatientModel.id'))
    cureType_id = Column(ForeignKey('rbCureType.id'))
    cureMethod_id = Column(ForeignKey('rbCureMethod.id'))
    prevEvent_id = Column(ForeignKey('Event.id'))
    goal_id = Column(ForeignKey('rbEventGoal.id'))
    hmpKind_id = Column(ForeignKey('rbHighTechCureKind.id'))
    hmpMethod_id = Column(ForeignKey('rbHighTechCureMethod.id'))
    outgoingOrg_id = Column(ForeignKey('Organisation.id'))
    outgoingRefNumber = Column(String(10), server_default=alchemy_text("''"))
    referral_id = Column(ForeignKey('Referral.id'))
    littleStranger_id = Column(ForeignKey('Event_LittleStranger.id', ondelete='SET NULL'))
    eventCostPrinted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    exposeConfirmed = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    ZNOFirst = Column(TINYINT(1), server_default=alchemy_text("0"))
    ZNOMorph = Column(TINYINT(1), server_default=alchemy_text("0"))
    hospParent = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    clientPolicy_id = Column(ForeignKey('ClientPolicy.id'))
    cycleDay = Column(INTEGER(11))
    locked = Column(TINYINT(1))
    dispByMobileTeam = Column(TINYINT(1), server_default=alchemy_text("0"))
    orgStructure_id = Column(INTEGER(11))
    MSE = Column(TINYINT(1), server_default=alchemy_text("0"))
    isClosed = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    vista_system = Column(INTEGER(11), server_default=alchemy_text("0"))
    isStage = Column(TINYINT(1), server_default=alchemy_text("0"))
    isCrime = Column(TINYINT(1), server_default=alchemy_text("0"))
    signedDocuments = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    signDateTime = Column(DateTime)
    KSGCriterion = Column(INTEGER(11), server_default=alchemy_text("0"))
    transfId = Column(INTEGER(11))
    kslp_coefficient = Column(Float(asdecimal=True))
    fixate = Column(TINYINT(1))

    assistant = relationship('Person', primaryjoin='Event.assistant_id == Person.id')
    clientPolicy = relationship('ClientPolicy')
    client = relationship('Client')
    contract = relationship('Contract')
    createPerson = relationship('Person', primaryjoin='Event.createPerson_id == Person.id')
    curator = relationship('Person', primaryjoin='Event.curator_id == Person.id')
    cureMethod = relationship('RbCureMethod')
    cureType = relationship('RbCureType')
    eventType = relationship('EventType')
    execPerson = relationship('Person', primaryjoin='Event.execPerson_id == Person.id')
    goal = relationship('RbEventGoal')
    hmpKind = relationship('RbHighTechCureKind')
    hmpMethod = relationship('RbHighTechCureMethod')
    littleStranger = relationship('EventLittleStranger')
    mesSpecification = relationship('RbMesSpecification')
    modifyPerson = relationship('Person', primaryjoin='Event.modifyPerson_id == Person.id')
    outgoingOrg = relationship('Organisation', primaryjoin='Event.outgoingOrg_id == Organisation.id')
    patientModel = relationship('RbPatientModel')
    prevEvent = relationship('Event', remote_side=[id])
    referral = relationship('Referral', primaryjoin='Event.referral_id == Referral.id')
    relegateOrg = relationship('Organisation', primaryjoin='Event.relegateOrg_id == Organisation.id')
    result = relationship('RbResult')
    setPerson = relationship('Person', primaryjoin='Event.setPerson_id == Person.id')
    typeAsset = relationship('RbEmergencyTypeAsset')


class EventDDList(Base):
    __tablename__ = 'EventDDList'

    event_id = Column(INTEGER(11), primary_key=True)


class EventTypeIEMK(Base):
    __tablename__ = 'EventType_IEMK'
    __table_args__ = {'comment': 'Список ActionType добавленных в Event, для автмоатической отправки случая в ИЭМК'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(INTEGER(11), nullable=False)
    actionType_id = Column(INTEGER(11), nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))


class EventLittleStranger(Base):
    __tablename__ = 'Event_LittleStranger'
    __table_args__ = {'comment': 'Признак новорожденного (i717)'}

    id = Column(INTEGER(11), primary_key=True)
    birthDate = Column(Date)
    sex = Column(TINYINT(4))
    currentNumber = Column(TINYINT(2), nullable=False, server_default=alchemy_text("1"))
    multipleBirths = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    birthWeight = Column(DECIMAL(6, 2), nullable=False, server_default=alchemy_text("0.00"))


class GRKMCardReasonCloseList(Base):
    __tablename__ = 'GRKMCardReasonCloseList'
    __table_args__ = {'comment': 'Список причин закрытия карты с кодами'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    updateDatetime = Column(DateTime, nullable=False)
    code = Column(String(45))
    name = Column(String(45))


class GRKMCodeArea(Base):
    __tablename__ = 'GRKMCodeAreas'
    __table_args__ = {'comment': 'Справочник районов ГРКМ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    updateDatetime = Column(DateTime, nullable=False)
    code = Column(String(45))
    name = Column(String(45))


class GRKMMo(Base):
    __tablename__ = 'GRKMMo'
    __table_args__ = {'comment': 'Справочник мед организаций ГРКМ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    updateDatetime = Column(DateTime, nullable=False)
    code = Column(String(45))
    name = Column(String(256))
    guid = Column(String(45))
    isArchived = Column(TINYINT(4))


class GRKMOperation(Base):
    __tablename__ = 'GRKMOperations'
    __table_args__ = {'comment': 'Операции которые должен выполнить сервис'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    updateDatetime = Column(DateTime, nullable=False)
    cardNumber = Column(INTEGER(11))
    person_id = Column(INTEGER(11), nullable=False)
    client_id = Column(INTEGER(11), nullable=False)
    event_id = Column(INTEGER(11), nullable=False)
    operation = Column(String(20), nullable=False)
    requestJsonData = Column(Text)
    status = Column(String(30), nullable=False)
    errorText = Column(Text)


class GRKMPerson(Base):
    __tablename__ = 'GRKMPerson'
    __table_args__ = {'comment': 'Справочник врачей ГРКМ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    updateDatetime = Column(DateTime, nullable=False)
    guid = Column(String(45))
    FIO = Column(String(145))


class GRKMRouteCard(Base):
    __tablename__ = 'GRKMRouteCards'
    __table_args__ = {'comment': 'Карты Маршрутизации полученные методом GetCargs'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    updateDatetime = Column(DateTime, nullable=False)
    cardNumber = Column(String(45), nullable=False)
    patientFIO = Column(String(60), nullable=False)
    cardStatus = Column(String(60), nullable=False)
    patientBirthDate = Column(DateTime)
    pickledRouteCardDict = Column(Text, nullable=False)


class GlobalPreference(Base):
    __tablename__ = 'GlobalPreferences'
    __table_args__ = {'comment': 'Глобальные настройки'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(32), nullable=False)
    name = Column(String(400), nullable=False)
    value = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    note = Column(String(64))


class HistoryRingingList(Base):
    __tablename__ = 'HistoryRingingList'
    __table_args__ = {'comment': 'Описывает хранимую историю обзвонов, реализует протjкол общения с Asterix'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    FIO = Column(String(128))
    sex = Column(String(2))
    contact = Column(String(45))
    actionCreateDatetime = Column(DateTime)
    event = Column(String(128))
    eventDate = Column(Date)
    eventTime = Column(Time)
    action_id = Column(INTEGER(11))
    action_type = Column(String(45))
    contactType = Column(INTEGER(11))
    lastCallDatetime = Column(DateTime)
    callStatus = Column(INTEGER(11), server_default=alchemy_text("0"))


class HomeRequestType(Base):
    __tablename__ = 'HomeRequestType'
    __table_args__ = {'comment': 'Тип заявки вызова врача на дом'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)


t_HospRes = Table(
    'HospRes', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


t_ID_SMO_REG = Table(
    'ID_SMO_REG', metadata,
    Column('ID_SMO_REG', INTEGER(11)),
    Column('SMO_S_NAME', String(20)),
    Column('SMO_L_NAME', String(254)),
    Column('NAME_TER', String(100)),
    Column('TER_CODE', INTEGER(11))
)


class IEMKStorage(Base):
    __tablename__ = 'IEMKStorage'
    __table_args__ = {'comment': 'Хранилище файлов ИЭМК'}

    id = Column(INTEGER(11), primary_key=True)
    path = Column(String(512))


t_IdCase = Table(
    'IdCase', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class InternationalPillsName(Base):
    __tablename__ = 'InternationalPillsNames'
    __table_args__ = {'comment': 'Классификатор международных непатентованных наименований лекарственных средств'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(String(250))
    master_id = Column(String(64))
    latNameMNN = Column(String(250))
    MNN = Column(INTEGER(11))
    version = Column(Date)


t_LAB_ISL = Table(
    'LAB_ISL', metadata,
    Column('CODE', String(50)),
    Column('NAME', String(250)),
    Column('PRICE', String(50))
)


t_MESDifference = Table(
    'MESDifference', metadata,
    Column('id', INTEGER(11)),
    Column('MESID', INTEGER(11)),
    Column('eventMes_id', INTEGER(11)),
    Column('createDatetime', DateTime)
)


class MKB(Base):
    __tablename__ = 'MKB'

    id = Column(INTEGER(11), primary_key=True)
    ClassID = Column(String(8), nullable=False)
    ClassName = Column(String(150), nullable=False)
    BlockID = Column(String(9), nullable=False)
    BlockName = Column(String(160), nullable=False)
    DiagID = Column(String(8), nullable=False)
    DiagName = Column(String(500))
    Prim = Column(String(1), nullable=False)
    sex = Column(TINYINT(1), nullable=False)
    age = Column(String(12), nullable=False)
    characters = Column(TINYINT(4), nullable=False)
    duration = Column(INTEGER(4), nullable=False)
    service_id = Column(INTEGER(11))
    MKBSubclass_id = Column(INTEGER(11))
    OMS = Column(TINYINT(1), server_default=alchemy_text("1"))
    MTR = Column(TINYINT(1), server_default=alchemy_text("1"))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    USL_OK1 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK2 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK3 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK4 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    SELF = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    ID_EIS = Column(INTEGER(11))


t_MKB120 = Table(
    'MKB120', metadata,
    Column('ID', INTEGER(11)),
    Column('CLASSID', String(8)),
    Column('CLASSNAME', String(150)),
    Column('BLOCKID', String(9)),
    Column('BLOCKNAME', String(160)),
    Column('DIAGID', String(8)),
    Column('DIAGNAME', String(160)),
    Column('PRIM', String(1)),
    Column('SEX', INTEGER(1)),
    Column('AGE', String(12)),
    Column('CHARACTERS', INTEGER(4)),
    Column('DURATION', INTEGER(4)),
    Column('SERVICE_ID', INTEGER(11)),
    Column('MKBSUBCLAS', INTEGER(11)),
    Column('OMS', INTEGER(1)),
    Column('MTR', INTEGER(1)),
    Column('BEGDATE', DateTime),
    Column('ENDDATE', DateTime),
    Column('USL_OK1', INTEGER(1)),
    Column('USL_OK2', INTEGER(1)),
    Column('USL_OK3', INTEGER(1)),
    Column('USL_OK4', INTEGER(1)),
    Column('SELF', INTEGER(1))
)


class MKBMorphology(Base):
    __tablename__ = 'MKB_Morphology'
    __table_args__ = {'comment': 'Морфология диагнозов МКБ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)
    version = Column(String(4))
    group = Column(String(16))
    bottomMKBRange1 = Column(String(8))
    topMKBRange1 = Column(String(8))
    bottomMKBRange2 = Column(String(8))
    topMKBRange2 = Column(String(8))
    begDate = Column(DateTime)
    endDate = Column(DateTime)


class MKBTree(Base):
    __tablename__ = 'MKB_Tree'

    id = Column(INTEGER(11), primary_key=True)
    DiagID = Column(String(9), nullable=False)
    DiagName = Column(String(500))
    parent_code = Column(String(9))
    Prim = Column(String(1), nullable=False)
    sex = Column(TINYINT(1), nullable=False)
    age = Column(String(12), nullable=False)
    characters = Column(TINYINT(4), nullable=False)
    duration = Column(INTEGER(4), nullable=False)
    service_id = Column(INTEGER(11))
    MKBSubclass_id = Column(INTEGER(11))
    OMS = Column(TINYINT(1), server_default=alchemy_text("1"))
    MTR = Column(TINYINT(1), server_default=alchemy_text("1"))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    USL_OK1 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK2 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK3 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK4 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    SELF = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    DNNeeded = Column(TINYINT(4), server_default=alchemy_text("0"))


class MKBBuckup(Base):
    __tablename__ = 'MKB_buckup'

    id = Column(INTEGER(11), primary_key=True)
    ClassID = Column(String(8), nullable=False)
    ClassName = Column(String(150), nullable=False)
    BlockID = Column(String(9), nullable=False)
    BlockName = Column(String(160), nullable=False)
    DiagID = Column(String(8), nullable=False)
    DiagName = Column(String(160), nullable=False)
    Prim = Column(String(1), nullable=False)
    sex = Column(TINYINT(1), nullable=False)
    age = Column(String(12), nullable=False)
    characters = Column(TINYINT(4), nullable=False)
    duration = Column(INTEGER(4), nullable=False)
    service_id = Column(INTEGER(11))
    MKBSubclass_id = Column(INTEGER(11))
    OMS = Column(TINYINT(1), server_default=alchemy_text("1"))
    MTR = Column(TINYINT(1), server_default=alchemy_text("1"))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    USL_OK1 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK2 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK3 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    USL_OK4 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    SELF = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))


class MSEExtarnalDocument(Base):
    __tablename__ = 'MSEExtarnalDocuments'
    __table_args__ = {'comment': 'Внешние документы РЭМД'}

    id = Column(INTEGER(11), primary_key=True)
    regDate = Column(Date)
    organizationName = Column(Text)
    type = Column(String(256))
    filePath = Column(Text)
    master_id = Column(INTEGER(11))
    IdSource = Column(String(512))
    MedDocumentType = Column(INTEGER(11))
    RegId = Column(String(128))


class MedicamentsBrigadeTest(Base):
    __tablename__ = 'MedicamentsBrigadeTest'

    id = Column(INTEGER(11), primary_key=True)
    medicament = Column(String(255))
    balance = Column(INTEGER(11), server_default=alchemy_text("0"))


class NDSCode(Base):
    __tablename__ = 'NDSCode'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11), nullable=False)
    label = Column(String(45), nullable=False)
    use_default_value = Column(TINYINT(1), nullable=False)


t_NSIRefBooks = Table(
    'NSIRefBooks', metadata,
    Column('id', INTEGER(11), nullable=False),
    Column('code', String(2553)),
    Column('name', String(2553)),
    Column('OID', String(2553)),
    Column('version', String(10)),
    Column('reference', String(2553))
)


class Notification(Base):
    __tablename__ = 'Notifications'
    __table_args__ = {'comment': 'Уведомления о получение услуг пациентами в других больницах'}

    flag_id = Column(String(40), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    modifyDatetime = Column(DateTime, nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    readed = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    person_id = Column(String(15))
    client_id = Column(String(15))
    mis_client_id = Column(String(30))
    netrika_client_id = Column(String(40))
    lastName = Column(String(30), nullable=False)
    firstName = Column(String(30), nullable=False)
    patrName = Column(String(64), nullable=False)
    birthDate = Column(Date, nullable=False)
    lastVisit = Column(DateTime)
    org_name = Column(Text)
    netrika_org_id = Column(String(40))
    MKB = Column(String(20))


class NotificationsKK(Base):
    __tablename__ = 'NotificationsKK'

    flag_id = Column(String(40), primary_key=True)
    status = Column(String(40), nullable=False)
    recieve_datetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    category = Column(String(40))
    author = Column(String(60))
    subject = Column(String(60))
    client_id = Column(INTEGER(11))
    mis_client_id = Column(String(50))
    netrika_client_id = Column(String(40))
    last_name = Column(String(60), nullable=False)
    first_name = Column(String(60), nullable=False)
    patr_name = Column(String(60), nullable=False)
    birth_date = Column(Date, nullable=False)
    org_name = Column(Text)
    org_netrika_id = Column(String(40))
    encounter_id = Column(String(20), nullable=False)
    encounter_class = Column(String(40))
    encounter_beg_datetime = Column(DateTime)
    encounter_end_datetime = Column(DateTime)
    mkb = Column(String(20))
    raw = Column(LONGTEXT)


t_Org = Table(
    'Org', metadata,
    Column('ID', INTEGER(11)),
    Column('CREATEDATE', DateTime),
    Column('CREATEPERS', INTEGER(11)),
    Column('MODIFYDATE', DateTime),
    Column('MODIFYPERS', INTEGER(11)),
    Column('DELETED', INTEGER(1)),
    Column('FULLNAME', String(250)),
    Column('SHORTNAME', String(64)),
    Column('TITLE', String(64)),
    Column('NET_ID', INTEGER(11)),
    Column('INFISCODE', String(12)),
    Column('OBSOLETEIN', String(60)),
    Column('OKVED', String(64)),
    Column('INN', String(15)),
    Column('KPP', String(15)),
    Column('OGRN', String(15)),
    Column('OKATO', String(15)),
    Column('OKPF_CODE', String(4)),
    Column('OKPF_ID', INTEGER(11)),
    Column('OKFS_CODE', INTEGER(11)),
    Column('OKFS_ID', INTEGER(11)),
    Column('OKPO', String(15)),
    Column('FSS', String(10)),
    Column('REGION', String(25)),
    Column('ADDRESS', String(250)),
    Column('CHIEF', String(64)),
    Column('PHONE', String(64)),
    Column('ACCOUNTANT', String(64)),
    Column('ISINSURER', INTEGER(1)),
    Column('ISCOMPULSO', INTEGER(1)),
    Column('ISVOLUNTAR', INTEGER(1)),
    Column('COMPULSORY', INTEGER(1)),
    Column('VOLUNTARYS', INTEGER(1)),
    Column('AREA', String(13)),
    Column('ISHOSPITAL', INTEGER(1)),
    Column('NOTES', Text),
    Column('HEAD_ID', INTEGER(11)),
    Column('MIACCODE', String(10)),
    Column('ISMEDICAL', INTEGER(1)),
    Column('ISARMYORG', INTEGER(1)),
    Column('CANOMITPOL', INTEGER(1)),
    Column('NETRICA_CO', String(64))
)


t_Orga1 = Table(
    'Orga1', metadata,
    Column('Column1', Float(10, True)),
    Column('Column2', DateTime),
    Column('Column3', String(255)),
    Column('Column4', DateTime),
    Column('Column5', String(255)),
    Column('Column6', Float(10, True)),
    Column('Column7', String(255)),
    Column('Column8', String(255)),
    Column('Column9', String(255)),
    Column('Column10', Float(10, True)),
    Column('Column11', String(255)),
    Column('Column12', String(255)),
    Column('Column13', String(255)),
    Column('Column14', String(255)),
    Column('Column15', String(255)),
    Column('Column16', String(255)),
    Column('Column17', String(255)),
    Column('Column18', String(255)),
    Column('Column19', String(255)),
    Column('Column20', Float(10, True)),
    Column('Column21', Float(10, True)),
    Column('Column22', String(255)),
    Column('Column23', String(255)),
    Column('Column24', String(255)),
    Column('Column25', String(255)),
    Column('Column26', String(255)),
    Column('Column27', String(255)),
    Column('Column28', String(255)),
    Column('Column29', Float(10, True)),
    Column('Column30', Float(10, True)),
    Column('Column31', Float(10, True)),
    Column('Column32', Float(10, True)),
    Column('Column33', Float(10, True)),
    Column('Column34', String(255)),
    Column('Column35', Float(10, True)),
    Column('Column36', String(255)),
    Column('Column37', String(255)),
    Column('Column38', String(255)),
    Column('Column39', Float(10, True)),
    Column('Column40', Float(10, True)),
    Column('Column41', Float(10, True)),
    Column('Column42', String(255))
)


class Organisation(Base):
    __tablename__ = 'Organisation'
    __table_args__ = {'comment': 'Организации, в т.ч. ЛПУ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    fullName = Column(String(255), nullable=False)
    shortName = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    net_id = Column(ForeignKey('rbNet.id', ondelete='SET NULL'))
    infisCode = Column(String(12), nullable=False)
    obsoleteInfisCode = Column(String(60), nullable=False)
    OKVED = Column(String(64), nullable=False)
    INN = Column(String(15), nullable=False)
    KPP = Column(String(15), nullable=False)
    OGRN = Column(String(15), nullable=False)
    OKATO = Column(String(15), nullable=False)
    OKPF_code = Column(String(4), nullable=False)
    OKPF_id = Column(INTEGER(11))
    OKFS_code = Column(INTEGER(11), nullable=False)
    OKFS_id = Column(INTEGER(11))
    OKPO = Column(String(15), nullable=False)
    FSS = Column(String(10), nullable=False)
    region = Column(String(25), nullable=False)
    address = Column(String(250), nullable=False)
    chief = Column(String(64), nullable=False)
    phone = Column(String(64), nullable=False)
    accountant = Column(String(64), nullable=False)
    isInsurer = Column(TINYINT(1), nullable=False)
    isCompulsoryInsurer = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isVoluntaryInsurer = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    compulsoryServiceStop = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    voluntaryServiceStop = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    area = Column(String(13), nullable=False)
    isHospital = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    notes = Column(TINYTEXT, nullable=False)
    head_id = Column(INTEGER(11))
    miacCode = Column(String(10), nullable=False)
    isMedical = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isArmyOrg = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    canOmitPolicyNumber = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    netrica_Code = Column(String(64))
    DATN = Column(Date, nullable=False, server_default=alchemy_text("'2000-01-01'"))
    DATO = Column(Date, nullable=False, server_default=alchemy_text("'2200-01-01'"))
    grkm_code = Column(String(8))
    reestrNumber = Column(INTEGER(10))
    llo_code = Column(String(20))
    llo_name = Column(String(100))
    isMSEBureau = Column(INTEGER(11))
    mse_code = Column(String(64))
    FOMSCode = Column(INTEGER(11))
    medOrgCode = Column(String(10))
    EGISZ_code = Column(String(512), nullable=False)
    fias_HouseGUID = Column(String(256))
    checkNumberLen = Column(TINYINT(4))
    numberLen = Column(INTEGER(11))

    net = relationship('RbNet')


t_Organisation_eis = Table(
    'Organisation_eis', metadata,
    Column('id', Float(10, True)),
    Column('createDatetime', DateTime),
    Column('createPerson_id', String(255)),
    Column('modifyDatetime', DateTime),
    Column('modifyPerson_id', String(255)),
    Column('deleted', Float(10, True)),
    Column('fullName', String(255)),
    Column('shortName', String(255)),
    Column('title', String(255)),
    Column('net_id', String(255)),
    Column('infisCode', String(255)),
    Column('obsoleteInfisCode', String(255)),
    Column('OKVED', String(255)),
    Column('INN', String(255)),
    Column('KPP', String(255)),
    Column('OGRN', String(255)),
    Column('OKATO', String(255)),
    Column('OKPF_code', String(255)),
    Column('OKPF_id', String(255)),
    Column('OKFS_code', Float(10, True)),
    Column('OKFS_id', String(255)),
    Column('OKPO', String(255)),
    Column('FSS', String(255)),
    Column('region', String(255)),
    Column('address', String(255)),
    Column('chief', String(255)),
    Column('phone', String(255)),
    Column('accountant', String(255)),
    Column('isInsurer', Float(10, True)),
    Column('isCompulsoryInsurer', Float(10, True)),
    Column('isVoluntaryInsurer', Float(10, True)),
    Column('compulsoryServiceStop', Float(10, True)),
    Column('voluntaryServiceStop', Float(10, True)),
    Column('area', String(255)),
    Column('isHospital', Float(10, True)),
    Column('notes', String(255)),
    Column('head_id', String(255)),
    Column('miacCode', String(255)),
    Column('isMedical', Float(10, True)),
    Column('isArmyOrg', Float(10, True)),
    Column('canOmitPolicyNumber', Float(10, True))
)


t_PP = Table(
    'PP', metadata,
    Column('kod', String(255)),
    Column('nam', String(255)),
    Column('price', Float(10, True))
)


class Person(Base):
    __tablename__ = 'Person'
    __table_args__ = {'comment': 'Сотрудники'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(12), nullable=False)
    federalCode = Column(String(16), nullable=False)
    regionalCode = Column(String(16), nullable=False)
    lastName = Column(String(30), nullable=False)
    firstName = Column(String(30), nullable=False)
    patrName = Column(String(30), nullable=False)
    post_id = Column(ForeignKey('rbPost.id'))
    speciality_id = Column(ForeignKey('rbSpeciality.id'))
    org_id = Column(ForeignKey('Organisation.id'))
    orgStructure_id = Column(INTEGER(11))
    office = Column(String(8), nullable=False)
    office2 = Column(String(8), nullable=False)
    tariffCategory_id = Column(ForeignKey('rbTariffCategory.id', ondelete='SET NULL'))
    finance_id = Column(ForeignKey('rbFinance.id'))
    retireDate = Column(Date)
    ambPlan = Column(SMALLINT(4), nullable=False)
    ambPlan2 = Column(SMALLINT(4), nullable=False)
    ambNorm = Column(SMALLINT(4), nullable=False)
    homPlan = Column(SMALLINT(4), nullable=False)
    homPlan2 = Column(SMALLINT(4), nullable=False)
    homNorm = Column(SMALLINT(4), nullable=False)
    expPlan = Column(SMALLINT(4), nullable=False)
    expNorm = Column(SMALLINT(4), nullable=False)
    login = Column(String(32), nullable=False)
    password = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    userProfile_id = Column(ForeignKey('rbUserProfile.id', ondelete='SET NULL'))
    retired = Column(TINYINT(1), nullable=False)
    birthDate = Column(Date, nullable=False)
    birthPlace = Column(String(64), nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    SNILS = Column(CHAR(11), nullable=False)
    INN = Column(CHAR(15), nullable=False)
    availableForExternal = Column(INTEGER(1), nullable=False, server_default=alchemy_text("1"))
    lastAccessibleTimelineDate = Column(Date)
    timelineAccessibleDays = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    canSeeDays = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    academicDegree = Column(TINYINT(4), nullable=False)
    typeTimeLinePerson = Column(INTEGER(11), nullable=False)
    addComment = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    commentText = Column(String(200))
    maritalStatus = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    contactNumber = Column(String(15), nullable=False, server_default=alchemy_text("''"))
    regType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    regBegDate = Column(Date)
    regEndDate = Column(Date)
    isReservist = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    employmentType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    occupationType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    citizenship_id = Column(ForeignKey('rbCitizenship.id'))
    isDefaultInHB = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    isInvestigator = Column(TINYINT(1))
    syncGUID = Column(String(36))
    qaLevel = Column(TINYINT(4), server_default=alchemy_text("0"))
    signature_cert = Column(Text)
    signature_key = Column(Text)
    cashier_code = Column(INTEGER(11))
    doctorRoomAccessDenied = Column(TINYINT(1), server_default=alchemy_text("0"))
    availableForScoreboard = Column(INTEGER(11), server_default=alchemy_text("1"))
    ecp_password = Column(String(100), server_default=alchemy_text("''"))
    grkmGUID = Column(String(45))
    ready_to_online_consultation = Column(INTEGER(11), server_default=alchemy_text("0"))
    disableSignDoc = Column(TINYINT(1), server_default=alchemy_text("0"))
    llo_login = Column(String(20))
    llo_password = Column(String(100))
    llo_code = Column(String(15))
    mse_speciality_id = Column(INTEGER(4))
    isVk = Column(TINYINT(1), server_default=alchemy_text("0"))
    qualification = Column(String(100), server_default=alchemy_text("''"))
    orgstructure_netrica_code = Column(String(64))

    citizenship = relationship('RbCitizenship', primaryjoin='Person.citizenship_id == RbCitizenship.id')
    createPerson = relationship('Person', remote_side=[id], primaryjoin='Person.createPerson_id == Person.id')
    finance = relationship('RbFinance', primaryjoin='Person.finance_id == RbFinance.id')
    modifyPerson = relationship('Person', remote_side=[id], primaryjoin='Person.modifyPerson_id == Person.id')
    org = relationship('Organisation')
    post = relationship('RbPost', primaryjoin='Person.post_id == RbPost.id')
    speciality = relationship('RbSpeciality', primaryjoin='Person.speciality_id == RbSpeciality.id')
    tariffCategory = relationship('RbTariffCategory', primaryjoin='Person.tariffCategory_id == RbTariffCategory.id')
    userProfile = relationship('RbUserProfile', primaryjoin='Person.userProfile_id == RbUserProfile.id')
    types = relationship('SmpPersonType', secondary='smpPerson')


class PersonPhoto(Base):
    __tablename__ = 'PersonPhoto'
    __table_args__ = {'comment': 'Хранение фотографий работников'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(INTEGER(11), nullable=False)
    photo = Column(LONGBLOB)


class PersonAddres(Base):
    __tablename__ = 'Person_Address'
    __table_args__ = {'comment': 'Адрес cотрудника'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(INTEGER(11), nullable=False)
    type = Column(TINYINT(4), nullable=False)
    address_id = Column(INTEGER(11))


class PersonDocument(Base):
    __tablename__ = 'Person_Document'
    __table_args__ = {'comment': 'Документы сотрудников'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(INTEGER(11), nullable=False)
    documentType_id = Column(INTEGER(11))
    serial = Column(String(8), nullable=False)
    number = Column(String(16), nullable=False)
    date = Column(Date, nullable=False)
    origin = Column(String(64), nullable=False)


class PersonOrder(Base):
    __tablename__ = 'Person_Order'
    __table_args__ = {'comment': 'Приказы по управлению персоналом'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(INTEGER(11), nullable=False)
    date = Column(Date, nullable=False)
    type = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    documentDate = Column(Date, nullable=False)
    documentNumber = Column(String(16), nullable=False)
    documentType_id = Column(INTEGER(11))
    salary = Column(String(64), nullable=False)
    validFromDate = Column(Date)
    validToDate = Column(Date)
    orgStructure_id = Column(INTEGER(11))
    post_id = Column(INTEGER(11))


class PopulationCount(Base):
    __tablename__ = 'PopulationCount'
    __table_args__ = {'comment': 'Численность населения'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(50), nullable=False)
    measureYear = Column(INTEGER(4), nullable=False)
    sex = Column(INTEGER(1), nullable=False)
    population = Column(INTEGER(11), nullable=False)
    plan = Column(INTEGER(11), nullable=False)


t_Prof = Table(
    'Prof', metadata,
    Column('code', Float(10, True)),
    Column('name', String(255)),
    Column('tarif', Float(10, True)),
    Column('kol', Float(10, True)),
    Column('Pedia1', Float(10, True)),
    Column('Pedia2', Float(10, True)),
    Column('Oftal', Float(10, True)),
    Column('Nevr', Float(10, True))
)


t_Profi2019 = Table(
    'Profi2019', metadata,
    Column('PROF_NAME', String(150)),
    Column('PROF_CODE', INTEGER(11)),
    Column('ID_PRVS', INTEGER(11)),
    Column('PRVS_NAME', String(50)),
    Column('PRVS_CODE', INTEGER(11)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('TYPE_NAME', String(50)),
    Column('PRVS_PR_G', INTEGER(11)),
    Column('PRVS_PR_SK', INTEGER(11)),
    Column('CODE', String(50)),
    Column('IDSERVDATA', INTEGER(11)),
    Column('SERV_NAME', String(100)),
    Column('Tariff', String(50))
)


class QueueControlGOV(Base):
    __tablename__ = 'QueueControlGOV'
    __table_args__ = {'comment': 'Доступ для районов очереди УО'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    gov_id = Column(INTEGER(11))


class QueueControlMKB(Base):
    __tablename__ = 'QueueControlMKB'
    __table_args__ = {'comment': 'Диагнозы очереди УО'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    diag_id = Column(String(8))
    diag_name = Column(String(160))


class QueueControlOrg(Base):
    __tablename__ = 'QueueControlOrgs'
    __table_args__ = {'comment': 'Доступ для организаций очереди УО'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    org_id = Column(INTEGER(11))


class QueueControlPayment(Base):
    __tablename__ = 'QueueControlPayment'
    __table_args__ = {'comment': 'Источники оплаты мед помощи очереди УО'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    payment_id = Column(INTEGER(11))


class QuotaType(Base):
    __tablename__ = 'QuotaType'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    _class = Column('class', TINYINT(1), nullable=False)
    group_code = Column(String(16))
    code = Column(String(16), nullable=False)
    name = Column(String(255), nullable=False)
    isObsolete = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))


class RecommendationAction(Base):
    __tablename__ = 'Recommendation_Action'
    __table_args__ = {'comment': 'Действия, созданные по рекомендациям'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    recommendation_id = Column(INTEGER(11), nullable=False)
    action_id = Column(INTEGER(11), nullable=False)
    amount = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    execDate = Column(Date)


class Referral(Base):
    __tablename__ = 'Referral'
    __table_args__ = {'comment': 'Направления, требуемые для ввода обращений'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    number = Column(String(30), nullable=False)
    recid = Column(INTEGER(11))
    status = Column(String(64))
    client_id = Column(ForeignKey('Client.id'))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE', onupdate='CASCADE'))
    policy_id = Column(ForeignKey('ClientPolicy.id'))
    doc_id = Column(ForeignKey('ClientDocument.id'))
    date = Column(DateTime, nullable=False)
    execDate = Column(DateTime)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    hospDate = Column(Date)
    relegateOrg_id = Column(ForeignKey('Organisation.id'))
    freeInput = Column(String(80))
    person = Column(String(80))
    speciality_id = Column(ForeignKey('rbSpeciality.id'))
    MKB = Column(String(8))
    type = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actionTypeCode = Column(String(32))
    isCancelled = Column(TINYINT(1), server_default=alchemy_text("0"))
    cancelPerson_id = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'))
    cancelDate = Column(DateTime)
    cancelReason = Column(INTEGER(11))
    notes = Column(Text)
    rationale = Column(Text)
    patientCondition = Column(Text)
    netrica_id = Column(String(64))
    approved = Column(TINYINT(1))
    isSend = Column(TINYINT(1), server_default=alchemy_text("0"))
    medProfile_id = Column(INTEGER(11))
    orgStructure = Column(INTEGER(11))
    clinicType = Column(INTEGER(3))
    hospBedProfile_id = Column(ForeignKey('rbHospitalBedProfile.id'))
    ticketNumber = Column(Text)
    isHospitalized = Column(TINYINT(1), server_default=alchemy_text("0"))
    relMoHospDate = Column(Date)
    examType = Column(INTEGER(11), server_default=alchemy_text("0"))
    regionalGuide_id = Column(INTEGER(11))
    hospitalisationType = Column(TINYINT(4))
    organ = Column(INTEGER(11), server_default=alchemy_text("0"))
    relegateOrgTo_id = Column(ForeignKey('Organisation.id'))
    goalType = Column(ForeignKey('rbGoalType2.id'))
    payment_id = Column(INTEGER(11))
    canEdit = Column(TINYINT(1), server_default=alchemy_text("0"))

    cancelPerson = relationship('Person')
    client = relationship('Client')
    doc = relationship('ClientDocument')
    event = relationship('Event', primaryjoin='Referral.event_id == Event.id')
    rbGoalType2 = relationship('RbGoalType2')
    hospBedProfile = relationship('RbHospitalBedProfile')
    policy = relationship('ClientPolicy')
    relegateOrgTo = relationship('Organisation', primaryjoin='Referral.relegateOrgTo_id == Organisation.id')
    relegateOrg = relationship('Organisation', primaryjoin='Referral.relegateOrg_id == Organisation.id')
    speciality = relationship('RbSpeciality')


class ReferralTypeFillSetting(Base):
    __tablename__ = 'ReferralTypeFillSettings'
    __table_args__ = {'comment': 'Описывает настройки полей при создании направления, 0 - не видимое, 1 - видимое, но не обязательное, 2- видимое и обязательное'}

    id = Column(INTEGER(11), primary_key=True)
    modifyPerson_id = Column(INTEGER(11), nullable=False)
    modifyDatetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    referralType_id = Column(INTEGER(11), nullable=False)
    number = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    dateIssuing = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    datePlanHosp = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    guide = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    btnGuide = Column(TINYINT(4), server_default=alchemy_text("1"))
    regionalGuide = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    btnRegionalGuide = Column(TINYINT(4), server_default=alchemy_text("1"))
    bedProfil = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    speciality = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    diagnos = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    checkupKind = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))


t_SPRAV_BED_PROFILE = Table(
    'SPRAV_BED_PROFILE', metadata,
    Column('ID_B_PROF', INTEGER(11)),
    Column('B_PROF', String(100)),
    Column('B_PROF_', String(50)),
    Column('ID_PRMP', INTEGER(11)),
    Column('PRMP_NAME', String(50))
)


t_SPRAV_CONSILIUM_TYPE = Table(
    'SPRAV_CONSILIUM_TYPE', metadata,
    Column('PR_CONS', INTEGER(11)),
    Column('FED_CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text)
)


t_SPRAV_DIAG = Table(
    'SPRAV_DIAG', metadata,
    Column('ID_DIAGNOS', INTEGER(11)),
    Column('DIAG_NAME', String(254)),
    Column('DIAG_CODE', String(7)),
    Column('ISSUBGROUP', INTEGER(6))
)


class SPRAVDRUGSSCHEME(Base):
    __tablename__ = 'SPRAV_DRUGS_SCHEMES'

    ID_DRUGS = Column(INTEGER(11), primary_key=True)
    DRUGS_CODE = Column(String(50))
    MNN = Column(String(100))
    DRUGS_NAME = Column(Text)
    Column1 = Column(String(50))
    Column2 = Column(String(50))
    DATE_BEGIN = Column(DateTime)
    DATE_END = Column(DateTime)
    FULL_NAME = Column(Text)


t_SPRAV_DRUGS_SC_LEKPR = Table(
    'SPRAV_DRUGS_SC_LEKPR', metadata,
    Column('ID_DRUGS', INTEGER(11)),
    Column('DRUGS_CODE', String(20)),
    Column('MNN_DR', String(100)),
    Column('DRUGS_NAME', String(254)),
    Column('FULL_NAME', Text),
    Column('ID_LEK_PR', INTEGER(11)),
    Column('MNN_LEK', Text),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime)
)


t_SPRAV_GROUP_NMKL = Table(
    'SPRAV_GROUP_NMKL', metadata,
    Column('GROUP_NMKL', INTEGER(11)),
    Column('ID_NMKL', INTEGER(11)),
    Column('NMKL_CODE', String(30)),
    Column('NMKL_N_ME', Text),
    Column('MULTI', TINYINT(1)),
    Column('LONG_IVL', TINYINT(1)),
    Column('LONG_MON', TINYINT(1)),
    Column('D_TE__EGIN', DateTime),
    Column('D_TE_END', DateTime)
)


t_SPRAV_LEK_PR = Table(
    'SPRAV_LEK_PR', metadata,
    Column('ID_LEK_PR', INTEGER(11)),
    Column('ID011', INTEGER(11)),
    Column('NUM_REG', String(254)),
    Column('DATE_REG', Date),
    Column('DATE_BEGIN', Date),
    Column('DATE_END', Date),
    Column('ORG_NAME', String(254)),
    Column('ORG_CTRY', String(254)),
    Column('TORG_NAME', String(254)),
    Column('MNN', String(254)),
    Column('FORMS', String(254)),
    Column('PROD_PHASE', String(254)),
    Column('DOCS', String(254)),
    Column('FARM_GROUP', String(254)),
    comment='Справочник лекарственных средств'
)


t_SPRAV_LPU_RF = Table(
    'SPRAV_LPU_RF', metadata,
    Column('ID_LPU_RF', INTEGER(11)),
    Column('CODE', String(6)),
    Column('NAME', String(255)),
    Column('ADDRESS', String(255)),
    Column('REGION', String(100)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime)
)


t_SPRAV_NMKL = Table(
    'SPRAV_NMKL', metadata,
    Column('ID_NMKL', INTEGER(11)),
    Column('CODE', String(30)),
    Column('NAME', String(254)),
    Column('DATE_BEGIN', Date),
    Column('DATE_END', Date)
)


t_SPRAV_ONK_HIMLUCH = Table(
    'SPRAV_ONK_HIMLUCH', metadata,
    Column('ID_TLUCH', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(50))
)


t_SPRAV_ONK_HIR = Table(
    'SPRAV_ONK_HIR', metadata,
    Column('ID_THIR', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(100)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text)
)


t_SPRAV_ONK_IGH = Table(
    'SPRAV_ONK_IGH', metadata,
    Column('ID_IGH', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(100)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('DIAG_TIP', INTEGER(11)),
    Column('DT_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_IGHRT = Table(
    'SPRAV_ONK_IGHRT', metadata,
    Column('ID_R_I', INTEGER(11)),
    Column('ID_IGH', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(100)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_LECH = Table(
    'SPRAV_ONK_LECH', metadata,
    Column('ID_TLECH', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text)
)


t_SPRAV_ONK_LEK_L = Table(
    'SPRAV_ONK_LEK_L', metadata,
    Column('ID_TLEK_L', INTEGER(11)),
    Column('FED_CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text)
)


t_SPRAV_ONK_LEK_V = Table(
    'SPRAV_ONK_LEK_V', metadata,
    Column('ID_TLEK_V', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(100)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text)
)


t_SPRAV_ONK_LUCH = Table(
    'SPRAV_ONK_LUCH', metadata,
    Column('ID_TLUCH', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text)
)


t_SPRAV_ONK_M = Table(
    'SPRAV_ONK_M', metadata,
    Column('ID_M', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(100)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_MRF = Table(
    'SPRAV_ONK_MRF', metadata,
    Column('ID_MRF', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('DIAG_TIP', INTEGER(11)),
    Column('DT_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_MRFT = Table(
    'SPRAV_ONK_MRFT', metadata,
    Column('ID_R_M', INTEGER(11)),
    Column('ID_MRF', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_N = Table(
    'SPRAV_ONK_N', metadata,
    Column('ID_N', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(150)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_REASONS = Table(
    'SPRAV_ONK_REASONS', metadata,
    Column('DS1_T', INTEGER(11)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', Date),
    Column('DATE_END', Date),
    Column('FULL_NAME', String(255))
)


t_SPRAV_ONK_STAD = Table(
    'SPRAV_ONK_STAD', metadata,
    Column('ID_ST', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('CODE', INTEGER(11)),
    Column('NAME', String(50)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_T = Table(
    'SPRAV_ONK_T', metadata,
    Column('ID_T', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('CODE', INTEGER(11)),
    Column('NAME', Text),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('FULL_NAME', Text),
    Column('observation_IEMK', String(5))
)


t_SPRAV_ONK_TNM = Table(
    'SPRAV_ONK_TNM', metadata,
    Column('CODE', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('ID_ST', INTEGER(11)),
    Column('ID_T', String(50)),
    Column('ID_N', INTEGER(11)),
    Column('ID_M', INTEGER(11)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime)
)


t_SPRAV_ONK_TNM_copy = Table(
    'SPRAV_ONK_TNM_copy', metadata,
    Column('CODE', INTEGER(11)),
    Column('DS_CODE', String(50)),
    Column('ID_ST', INTEGER(11)),
    Column('ID_T', String(50)),
    Column('ID_N', INTEGER(11)),
    Column('ID_M', INTEGER(11)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime)
)


t_SPRAV_PRVS_PROFILE = Table(
    'SPRAV_PRVS_PROFILE', metadata,
    Column('ID_RECORD', INTEGER(11)),
    Column('ID_PROFILE', INTEGER(11)),
    Column('PROF_NAME', String(200)),
    Column('PROF_CODE', String(10)),
    Column('ID_PRVS', INTEGER(11)),
    Column('PRVS_NAME', String(30)),
    Column('PRVS_CODE', String(10)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('IDPRVSTYPE', INTEGER(6)),
    Column('TYPE_NAME', String(40)),
    Column('PRVS_PR_G', INTEGER(6)),
    Column('PRVS_PR_SK', INTEGER(6)),
    Column('CODE', String(14)),
    Column('CODE_SHORT', String(10)),
    Column('IDSERVDATA', INTEGER(11)),
    Column('SERV_NAME', String(50)),
    Column('code_usl', String(255))
)


t_SPRAV_TARIFF = Table(
    'SPRAV_TARIFF', metadata,
    Column('ID_PROFILE', INTEGER(11)),
    Column('PROF_CODE', String(10)),
    Column('ZONE_TYPE', String(1)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime),
    Column('AMOUNT', INTEGER(6)),
    Column('TARIFF', Float(14, True)),
    Column('CASE_CAST', INTEGER(6)),
    Column('ID_TAR_SMO', INTEGER(6)),
    Column('PRILOZ', String(30))
)


class SendPackage(Base):
    __tablename__ = 'SendPackages'
    __table_args__ = {'comment': 'Таблица, переданых пакетов.'}

    id = Column(INTEGER(11), primary_key=True)
    createPerson = Column(INTEGER(11), nullable=False)
    createDateTime = Column(DateTime, nullable=False)
    event_id = Column(INTEGER(11))
    method = Column(String(64))
    message = Column(Text)
    result = Column(Text)
    status = Column(TINYINT(1), server_default=alchemy_text("0"))


class SmpEvent(Base):
    __tablename__ = 'SmpEvents'
    __table_args__ = {'comment': 'События СМП'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    eventId = Column(INTEGER(11), nullable=False)
    eventTime = Column(Time)
    callNumberId = Column(BIGINT(20), nullable=False)
    callDate = Column(Date)
    fio = Column(String(60))
    sex = Column(TINYINT(1))
    age = Column(INTEGER(3))
    contact = Column(String(15))
    address = Column(String(200))
    landmarks = Column(String(255))
    occasion = Column(String(400))
    callerName = Column(String(25))
    urgencyCategory = Column(String(15))
    callKind = Column(String(20))
    receiver = Column(String(60))
    result = Column(String(40))
    isDone = Column(TINYINT(1), server_default=alchemy_text("0"))


t_Spisok = Table(
    'Spisok', metadata,
    Column('id', String(255)),
    Column('name', String(255)),
    Column('chto-to', String(255)),
    Column('N', String(255)),
    Column('ymer', String(255)),
    Column('Net', String(255))
)


t_SpravYesNo = Table(
    'SpravYesNo', metadata,
    Column('id', INTEGER(9)),
    Column('deleted', TINYINT(1)),
    Column('code', String(24)),
    Column('name', String(100))
)


class StockMotion(Base):
    __tablename__ = 'StockMotion'

    id = Column(INTEGER(11), primary_key=True)
    type = Column(INTEGER(11))
    document = Column(String(45))
    date = Column(Date)
    group = Column(INTEGER(11))
    supplier_orgstructure_id = Column(INTEGER(11))
    supplier_person_id = Column(INTEGER(11))
    recipient_orgstructure_id = Column(INTEGER(11))
    recipient_person_id = Column(INTEGER(11))
    note = Column(String(45))


class StockRequisition(Base):
    __tablename__ = 'StockRequisition'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8))
    date = Column(Date, nullable=False)
    supplier_orgstructure_id = Column(INTEGER(11), nullable=False)
    supplier_person_id = Column(INTEGER(11))
    recipient_orgstructure_id = Column(INTEGER(11), nullable=False)
    recipient_person_id = Column(INTEGER(11))
    note = Column(String(45))


class StockRequisitionItem(Base):
    __tablename__ = 'StockRequisition_Item'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    nomenclature_id = Column(INTEGER(11))
    unit_id = Column(INTEGER(11))
    qnt = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    satisfiedQnt = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))


class StockWriteOff(Base):
    __tablename__ = 'StockWriteOff'

    id = Column(INTEGER(11), primary_key=True)
    date = Column(Date, nullable=False)
    orgstructure_id = Column(INTEGER(11))
    person_id = Column(INTEGER(11), nullable=False)


class StockWriteOffItem(Base):
    __tablename__ = 'StockWriteOff_Item'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11), nullable=False)
    nomenclature_id = Column(INTEGER(11), nullable=False)
    unit_id = Column(INTEGER(11), nullable=False)
    qnt = Column(INTEGER(11), nullable=False)
    reason = Column(String(50))


t_TempDDClient = Table(
    'TempDDClient', metadata,
    Column('id', INTEGER(11), nullable=False)
)


t_TempDDEvent2 = Table(
    'TempDDEvent2', metadata,
    Column('id', INTEGER(11), nullable=False)
)


class TempInvalidNumbersStore(Base):
    __tablename__ = 'TempInvalidNumbersStore'
    __table_args__ = {'comment': 'Хранит номера электронных больнычных листов, определяет \\nкем, кому  и когда  был или не  был назначен лист, когда лист получен, номер его партии'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11), nullable=False)
    person_id = Column(INTEGER(11))
    batchNumber = Column(INTEGER(11), nullable=False)
    status = Column(INTEGER(11), nullable=False)
    number = Column(String(32), nullable=False)
    master_id = Column(INTEGER(11))


t_UZI = Table(
    'UZI', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class User(Base):
    __tablename__ = 'User'
    __table_args__ = {'comment': "Пользователи ( для связи Person'ов)"}

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(128))
    password = Column(String(200))
    email = Column(String(128))
    createDatetime = Column(DateTime)


class UserPerson(Base):
    __tablename__ = 'User_Person'
    __table_args__ = {'comment': 'таблица для связи пользователей с несколькими учетками'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(INTEGER(11))
    user_id = Column(INTEGER(11))
    isPreferable = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))


class V011(Base):
    __tablename__ = 'V011'
    __table_args__ = {'comment': 'Справочник лекарственных средств'}

    ID011 = Column(INTEGER(11), primary_key=True)
    NUM_REG = Column(String(254))
    DATE_REG = Column(Date)
    ORG_NAME = Column(String(254))
    ORG_CTRY = Column(String(254))
    TORG_NAME = Column(String(254))
    MNN = Column(String(254))
    FORMS = Column(String(254))
    PROD_PHASE = Column(String(254))
    DOCS = Column(String(254))
    FARM_GROUP = Column(String(254))


t_VZROS_MES = Table(
    'VZROS_MES', metadata,
    Column('code', String(255)),
    Column('name', String(255)),
    Column('price', Float(10, True)),
    Column('master', String(255))
)


class ZNOInfoDoneCure(Base):
    __tablename__ = 'ZNOInfo_DoneCure'
    __table_args__ = {'comment': 'Проведенное лечение'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(11))
    master_id = Column(INTEGER(11), nullable=False)
    action_id = Column(INTEGER(11))
    consilium = Column(INTEGER(11))
    consiliumDate = Column(Date)
    surgeryCure = Column(INTEGER(11))
    deTumorCycle = Column(INTEGER(11))
    deTumorLine = Column(INTEGER(11))
    deTumorDrugs = Column(INTEGER(11))
    radiationTherapy = Column(INTEGER(11))
    radiationTherapySod = Column(String(8))
    chemyTherapy = Column(INTEGER(11))
    chemyTherapySod = Column(String(8))
    chemyDrugs = Column(INTEGER(11))
    pptr = Column(TINYINT(1))


class ZNOInfoHistology(Base):
    __tablename__ = 'ZNOInfo_Histology'
    __table_args__ = {'comment': 'Информация о гистологиях'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(11))
    master_id = Column(INTEGER(11), nullable=False)
    histology_type = Column(INTEGER(11))
    histology_value = Column(INTEGER(11))


class ZNOInfoImmunology(Base):
    __tablename__ = 'ZNOInfo_Immunology'
    __table_args__ = {'comment': 'Иммуногистохимия/маркёры'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(11))
    master_id = Column(INTEGER(11), nullable=False)
    igh_id = Column(INTEGER(11))
    ighrt_id = Column(INTEGER(11))


class ZONETYPE(Base):
    __tablename__ = 'ZONE_TYPE'
    __table_args__ = {'comment': 'Таблица типов медицинских сетей'}

    NETWORK_FULL_NAME = Column(String(125))
    ID_ZONE_TYPE = Column(INTEGER(2), primary_key=True)
    NETWORK_NAME = Column(String(50), nullable=False)
    ID_ZONE_GROUP = Column(INTEGER(10), nullable=False)
    ZONE_GROUP_NAME = Column(String(30), nullable=False)
    AGE_MIN = Column(INTEGER(5))
    AGE_MAX = Column(INTEGER(5))
    SEX = Column(String(1))


t_a = Table(
    'a', metadata,
    Column('Column1', String(255)),
    Column('Column2', String(255)),
    Column('Column3', String(255)),
    Column('Column4', INTEGER(11))
)


class AcuteCoronarySyndromeType(Base):
    __tablename__ = 'acute_coronary_syndrome_types'
    __table_args__ = {'comment': 'ВИМИС. Виды острого коронарного синдрома (1.2.643.5.1.13.13.99.2.727) v1.1'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(Text)


class AdverseOutcomeInAcuteCoronarySyndromeRiskCategory(Base):
    __tablename__ = 'adverse_outcome_in_acute_coronary_syndrome_risk_categories'
    __table_args__ = {'comment': 'ВИМИС. Категории риска неблагоприятного исхода при остром коронарном синдроме без подъема сегмента ST ( 1.2.643.5.1.13.13.99.2.736) v1.1'}

    Id = Column(INTEGER(11), primary_key=True)
    Criterion = Column(Text)
    Sort = Column(INTEGER(11))
    Parent_id = Column(Float(asdecimal=True))


class AnatomicalLocation(Base):
    __tablename__ = 'anatomical_locations'
    __table_args__ = {'comment': 'Анатомические локализации (1.2.643.5.1.13.13.11.1477) v4.7'}

    ID = Column(INTEGER(11), primary_key=True)
    ID_PARENT = Column(Float(asdecimal=True))
    NAME = Column(Text)
    NAME_ENG = Column(Text)
    SNOMED_CT = Column(Float(asdecimal=True))
    ANATOMIC_FIELD = Column(Text)
    LATERALITY = Column(Text)
    SYNONYMS = Column(Text)


class AnesthesiaType(Base):
    __tablename__ = 'anesthesia_types'
    __table_args__ = {'comment': 'Виды анестезии (1.2.643.5.1.13.13.11.1033) v4.1'}

    ID = Column(INTEGER(11), primary_key=True)
    Name = Column(Text)
    Parent = Column(Float(asdecimal=True))
    Group = Column(Text)
    Synonym = Column(Text)


t_august_price = Table(
    'august_price', metadata,
    Column('code', String(255)),
    Column('name', String(255)),
    Column('price', Float(10, True))
)


class BaseDocumentType(Base):
    __tablename__ = 'base_document_types'
    __table_args__ = {'comment': 'Типы документов оснований (1.2.643.5.1.13.13.99.2.724) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    Name = Column(Text)


class BenefitCodesCategoriesMatching(Base):
    __tablename__ = 'benefit_codes_categories_matching'
    __table_args__ = {'comment': 'Сопоставление кодов льгот с льготными категориями граждан из Федерального закона №178-ФЗ (1.2.643.5.1.13.13.99.2.713) v3.5'}

    ID = Column(INTEGER(11), primary_key=True)
    NPA = Column(String(128))
    RECID = Column(String(50))
    ID_FORM = Column(INTEGER(11))
    NAME_FORM = Column(String(512))
    ID_541 = Column(String(512))


t_blood = Table(
    'blood', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class ChemicalToxicMethod(Base):
    __tablename__ = 'chemical_toxic_methods'
    __table_args__ = {'comment': 'Методы химико-токсикологических исследований (1.2.643.5.1.13.13.99.2.743) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    Methods = Column(String(128))
    Attr_Method = Column(String(50))


class ChildPhysicalMedGroup(Base):
    __tablename__ = 'child_physical_med_group'
    __table_args__ = {'comment': 'Медицинские группы для занятий несовершеннолетними физической культурой (1.2.643.5.1.13.13.99.2.765) v.1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    DESCRIPTION = Column(Text)


t_code_usl = Table(
    'code_usl', metadata,
    Column('code_usl', String(50)),
    Column('code_sp', String(255)),
    Column('reg_sp', String(255)),
    Column('code_pr', String(255)),
    Column('reg_pr', String(255))
)


class ConditionsMedicalAssistance(Base):
    __tablename__ = 'conditions_medical_assistance'
    __table_args__ = {'comment': 'Условия оказания МП (1.2.643.5.1.13.13.99.2.322) v2.1'}

    CODE = Column(INTEGER(11), primary_key=True)
    NAME = Column(String(128))
    COMMENTS = Column(String(256))


class ConsumerMeasurementUnit(Base):
    __tablename__ = 'consumer_measurement_units'
    __table_args__ = {'comment': 'ЕСКЛП. Потребительские единицы измерения (1.2.643.5.1.13.13.99.2.612) v2.55'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME_UNIT = Column(String(50))
    OKEI_CODE = Column(INTEGER(11))


class CouncilResult(Base):
    __tablename__ = 'council_results'
    __table_args__ = {'comment': 'Результаты консилиума (1.2.643.5.1.13.13.99.2.349) v1.3'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class CouncilType(Base):
    __tablename__ = 'council_type'
    __table_args__ = {'comment': 'Тип консилиума (1.2.643.5.1.13.13.99.2.780) v1.3'}

    ID = Column(INTEGER(11), primary_key=True)
    Type_of_concilium = Column(Text)


class CriticalObstetricConditionCriterion(Base):
    __tablename__ = 'critical_obstetric_condition_criteria'
    __table_args__ = {'comment': 'ВИМИС. Критерии критического акушерского состояния (1.2.643.5.1.13.13.99.2.774) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    ID_PARENT_SIGN = Column(Float(asdecimal=True))
    ID_PARENT = Column(Float(asdecimal=True))


class CriticalObstetricConditionPatientCategory(Base):
    __tablename__ = 'critical_obstetric_condition_patient_category'
    __table_args__ = {'comment': 'ВИМИC. Категория пациентки при критическом акушерском состоянии (1.2.643.5.1.13.13.99.2.775) v1.1'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(Text)


class Ctr(Base):
    __tablename__ = 'ctr'
    __table_args__ = {'comment': 'Тариф договора'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(INTEGER(11), nullable=False)
    eventType_id = Column(INTEGER(11))
    tariffType = Column(TINYINT(1), nullable=False)
    service_id = Column(INTEGER(11))
    tariffCategory_id = Column(INTEGER(11))
    begDate = Column(Date)
    endDate = Column(Date)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    attachType_id = Column(INTEGER(11))
    attachLPU_id = Column(INTEGER(11))
    unit_id = Column(INTEGER(11))
    amount = Column(Float(asdecimal=True), nullable=False)
    uet = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    price = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag1Start = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag1Sum = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag1Price = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag2Start = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag2Sum = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag2Price = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    limitationExceedMode = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    limitation = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    priceEx = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    limitation2ExceedMode = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    limitation2 = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    priceEx2 = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    MKB = Column(String(64), nullable=False)
    federalPrice = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    federalLimitation = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    speciality_id = Column(INTEGER(11))
    vat = Column(DECIMAL(3, 2), nullable=False, server_default=alchemy_text("0.00"))


t_dd20 = Table(
    'dd20', metadata,
    Column('ID_HISTORY', INTEGER(11)),
    Column('SURNAME', String(255)),
    Column('NAME', String(255)),
    Column('SECOND_NAME', String(255)),
    Column('SEX', String(255)),
    Column('BIRTHDAY', Date),
    Column('POLIS_SERIA', String(255)),
    Column('POLIS_NUMBER', String(255)),
    Column('PHONE_HOME', String(255)),
    Column('PHONE_WORK', String(255)),
    Column('ADRESS_REG', String(255)),
    Column('ADRESS_LOC', String(255)),
    Column('CODE_SMO', String(255))
)


t_dd202 = Table(
    'dd202', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('ID_HISTORY', INTEGER(11)),
    Column('SURNAME', String(255)),
    Column('NAME', String(255)),
    Column('SECOND_NAME', String(255)),
    Column('SEX', String(255)),
    Column('BIRTHDAY', Date),
    Column('POLIS_SERIA', String(255)),
    Column('POLIS_NUMBER', String(255)),
    Column('PHONE_HOME', String(255)),
    Column('PHONE_WORK', String(255)),
    Column('ADRESS_REG', String(255)),
    Column('ADRESS_LOC', String(255)),
    Column('CODE_SMO', String(255))
)


t_dd203 = Table(
    'dd203', metadata,
    Column('client', INTEGER(11), nullable=False),
    Column('house_id', INTEGER(11), nullable=False)
)


t_dd204 = Table(
    'dd204', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('master_id', INTEGER(11), nullable=False),
    Column('house_id', INTEGER(11), nullable=False),
    Column('firstFlat', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('lastFlat', INTEGER(11), nullable=False, server_default=alchemy_text("0"))
)


t_dd205 = Table(
    'dd205', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('master_id', INTEGER(11), nullable=False),
    Column('house_id', INTEGER(11), nullable=False),
    Column('firstFlat', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('lastFlat', INTEGER(11), nullable=False, server_default=alchemy_text("0"))
)


t_dd206 = Table(
    'dd206', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('master_id', INTEGER(11), nullable=False),
    Column('house_id', INTEGER(11), nullable=False),
    Column('firstFlat', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('lastFlat', INTEGER(11), nullable=False, server_default=alchemy_text("0"))
)


class DeathAndCarAccidentRelationship(Base):
    __tablename__ = 'death_and_car_accident_relationship'
    __table_args__ = {'comment': 'Связь смерти с ДТП (1.2.643.5.1.13.13.99.2.24) v1.4'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class DeathCauseGroundsEstablishing(Base):
    __tablename__ = 'death_cause_grounds_establishing'
    __table_args__ = {'comment': 'Основания для установления причины смерти (1.2.643.5.1.13.13.99.2.23) v3.2'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    F_106_u = Column(Float(asdecimal=True))
    NAME_F_106_u = Column(Text)
    F_106_2_u = Column(Float(asdecimal=True))
    NAME_F_106_2_u = Column(Text)


class DeathCauseType(Base):
    __tablename__ = 'death_cause_type'
    __table_args__ = {'comment': 'Род причины смерти (1.2.643.5.1.13.13.99.2.21) v5.1'}

    ID = Column(INTEGER(11), primary_key=True)
    Name = Column(Text)
    CODE_106_u = Column(Float(asdecimal=True))
    NAME_106_u = Column(Text)
    CODE_106_2_u = Column(Float(asdecimal=True))
    NAME_106_2_u = Column(Text)
    Sort = Column(INTEGER(11))
    Parent = Column(Float(asdecimal=True))


class DeathPlacesType(Base):
    __tablename__ = 'death_places_types'
    __table_args__ = {'comment': 'Типы мест наступления смерти (1.2.643.5.1.13.13.99.2.20) v5.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    F_106u = Column(Float(asdecimal=True))
    NAME_F_106u = Column(Text)
    F_58_1u = Column('F_58-1u', Float(asdecimal=True))
    NAME_F_58_1u = Column('NAME_F_58-1u', Text)
    F_106_2u = Column('F_106-2u', Float(asdecimal=True))
    NAME_F_106_2u = Column('NAME_F_106-2u', Text)


class DecisionOnHospitalizationUponAdmission(Base):
    __tablename__ = 'decision_on_hospitalization_upon_admission'
    __table_args__ = {'comment': 'Решение о госпитализации в медицинскую организацию при поступлении (1.2.643.5.1.13.13.11.1512) v1.2'}

    Id = Column(INTEGER(11), primary_key=True)
    Decision = Column(String(256))


class DeliveryAssessedClinicalParametersValue(Base):
    __tablename__ = 'delivery_assessed_clinical_parameters_values'
    __table_args__ = {'comment': 'ВИМИС. Значения клинических параметров, оцениваемых при родоразрешении (1.2.643.5.1.13.13.99.2.915) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    SORT = Column(INTEGER(11))
    P_ID = Column(Float(asdecimal=True))
    FETUS_SIGN = Column(Float(asdecimal=True))


class DeterminedDeathCauseHealthWorkerType(Base):
    __tablename__ = 'determined_death_cause_health_worker_type'
    __table_args__ = {'comment': 'Тип медицинского работника, установившего причины смерти (1.2.643.5.1.13.13.99.2.22) v5.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    CODE_106_u = Column(Float(asdecimal=True))
    NAME_106_u = Column(Text)
    CODE_106_2_u = Column(Float(asdecimal=True))
    NAME_106_2_u = Column(Text)
    ACTUAL = Column(Text)


class DiagnosisValidityDegree(Base):
    __tablename__ = 'diagnosis_validity_degree'
    __table_args__ = {'comment': 'Степень обоснованности диагноза (1.2.643.5.1.13.13.11.1076) v3.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    SORT = Column(INTEGER(11))
    ID_PARENT = Column(Float(asdecimal=True))


class DiseaseNature(Base):
    __tablename__ = 'disease_nature'
    __table_args__ = {'comment': 'Характер заболевания (1.2.643.5.1.13.13.11.1049) v3.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    F_025_1u = Column('F_025-1u', INTEGER(11))


class DiseasesAndHealthrelatedProblemsClassification(Base):
    __tablename__ = 'diseases_and_healthrelated_problems_classification'
    __table_args__ = {'comment': 'Международная статистическая классификация болезней и проблем, связанных со здоровьем (10-й пересмотр) (1.2.643.5.1.13.13.11.1005) v2.21'}

    ID = Column(INTEGER(11), primary_key=True)
    REC_CODE = Column(Text)
    MKB_CODE = Column(Text)
    MKB_NAME = Column(Text)
    ACTUAL = Column(INTEGER(11))
    ID_PARENT = Column(Float(asdecimal=True))
    ADDL_CODE = Column(Float(asdecimal=True))
    DATE = Column(Text)


class DiseasesClassification(Base):
    __tablename__ = 'diseases_classification'
    __table_args__ = {'comment': 'МКБ-10 (1.2.643.5.1.13.13.11.1005) v2.21'}

    ID = Column(INTEGER(11), primary_key=True)
    REC_CODE = Column(String(50))
    MKB_CODE = Column(String(50))
    MKB_NAME = Column(String(128))
    ID_PARENT = Column(INTEGER(11))
    ADDL_CODE = Column(INTEGER(11))
    ACTUAL = Column(INTEGER(11))
    DATE = Column(Date)


class DispensaryType(Base):
    __tablename__ = 'dispensary_type'
    __table_args__ = {'comment': 'ФРМО. Номенклатура медицинских организаций по виду медицинской деятельности (1.2.643.5.1.13.13.99.2.289) v1.2'}

    id = Column(INTEGER(11), primary_key=True)
    parentId = Column(INTEGER(11))
    agencyKind = Column(String(256))


class DloDrugstoreRemain(Base):
    __tablename__ = 'dlo_DrugstoreRemains'
    __table_args__ = {'comment': 'Информация о препаратах в аптеках'}

    id = Column(INTEGER(11), primary_key=True)
    drugstore_id = Column(String(50))
    drugstoreName = Column(String(128))
    productUnifyId = Column(String(50))
    productName = Column(String(250))
    producerName = Column(String(50))
    countryName = Column(String(50))
    mnn = Column(String(100))
    trn = Column(String(100))
    cureform = Column(String(50))
    dosage = Column(String(50))
    package = Column(SMALLINT(6), nullable=False)
    denominator = Column(SMALLINT(6), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    quantity = Column(DECIMAL(8, 2), nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    syncDateTime = Column(DateTime, nullable=False)


class DloRbDosage(Base):
    __tablename__ = 'dlo_rbDosage'
    __table_args__ = {'comment': 'Справочник дозировок (ДЛО)'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11), nullable=False)
    name = Column(String(50), nullable=False)
    miacCode = Column(String(30), nullable=False)


class DloRbIssueForm(Base):
    __tablename__ = 'dlo_rbIssueForm'
    __table_args__ = {'comment': 'Справочник форм выпуска (ДЛО)'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11), nullable=False)
    name = Column(String(50), nullable=False)
    latinName = Column(String(100))
    miacCode = Column(TINYINT(4), nullable=False)


class DloRbMNN(Base):
    __tablename__ = 'dlo_rbMNN'
    __table_args__ = {'comment': 'Справочник МНН (ДЛО)'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11), nullable=False)
    name = Column(String(100), nullable=False, server_default=alchemy_text("'0'"))
    latinName = Column(String(100), nullable=False, server_default=alchemy_text("'0'"))
    miacCode = Column(String(100))


class DloRbTradeName(Base):
    __tablename__ = 'dlo_rbTradeName'
    __table_args__ = {'comment': 'Справочник торговых наименований (ДЛО)'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(String(100), nullable=False)
    latinName = Column(String(100), nullable=False)
    miacCode = Column(String(100))


t_dms1 = Table(
    'dms1', metadata,
    Column('code', String(255)),
    Column('name', String(255)),
    Column('price', String(255))
)


t_dn_v51 = Table(
    'dn_v51', metadata,
    Column('id', String(50)),
    Column('lastName', String(50)),
    Column('firstName', String(50)),
    Column('patrName', String(50)),
    Column('birthDate', Date),
    Column('address', String(512)),
    Column('mkb', String(512)),
    Column('month', INTEGER(11)),
    Column('code', String(255))
)


class DoctorsConsultationHoldingForm(Base):
    __tablename__ = 'doctors_consultation_holding_form'
    __table_args__ = {'comment': 'Форма проведения консилиума врачей (врачебной комиссии) (1.2.643.5.1.13.13.11.1508) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class DocumentedEventsType(Base):
    __tablename__ = 'documented_events_types'
    __table_args__ = {'comment': 'Типы документированных событий (1.2.643.5.1.13.13.99.2.726) v3.4'}

    ID = Column(INTEGER(11), primary_key=True)
    Types = Column(Text)
    DOC_OID = Column(Text)
    PARENT_ID = Column(Float(asdecimal=True))


class DocumentsForm(Base):
    __tablename__ = 'documents_form'
    __table_args__ = {'comment': 'Формы документов (1.2.643.5.1.13.13.99.2.1008) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(String(50))
    SYNONYM = Column(String(50))


class DrugDistributionFrequency(Base):
    __tablename__ = 'drug_distribution_frequency'
    __table_args__ = {'comment': 'Периодичность отпуска лекарственных препаратов (1.2.643.5.1.13.13.99.2.687) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    Name = Column(String(50))


t_expdataP51Attach = Table(
    'expdataP51Attach', metadata,
    Column('id', INTEGER(11)),
    Column('client_id', INTEGER(11)),
    Column('MO', String(50)),
    Column('infis', INTEGER(11)),
    Column('MO_name', String(50)),
    Column('id_net', INTEGER(11))
)


class FamilyAndOtherTy(Base):
    __tablename__ = 'family_and_other_ties'
    __table_args__ = {'comment': 'Родственные и иные связи (1.2.643.5.1.13.13.99.2.14) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    NAME_F_106_u = Column(Text)
    NAME_F_106_2_u = Column(Text)


class FamilyStatu(Base):
    __tablename__ = 'family_status'
    __table_args__ = {'comment': 'Семейное положение (1.2.643.5.1.13.13.99.2.15) v4.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    F_106_2_u = Column(INTEGER(11))
    F_106_u = Column(INTEGER(11))
    CODE_ZAGS_NALOG = Column(INTEGER(11))
    F_013_u = Column(INTEGER(11))


class FdlrLaboratoryStudiesProfile(Base):
    __tablename__ = 'fdlr_laboratory_studies_profiles'
    __table_args__ = {'comment': 'Федеральный справочник лабораторных исследований. Профили лабораторных исследований (1.2.643.5.1.13.13.11.1437) v3.24'}

    ID = Column(INTEGER(11), primary_key=True)
    Description = Column(Text)
    Comments = Column(Text)
    CodeNMS = Column(Text)


t_fizio = Table(
    'fizio', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class Form14(Base):
    __tablename__ = 'form14'

    id = Column(INTEGER(10), primary_key=True)
    diseaseName = Column(String(150))
    row_code = Column(String(50))
    mkb_range = Column(String(150))
    mkb = Column(String(50))
    reportNumber = Column(String(10))


class FrmoDepartmentsAndOffice(Base):
    __tablename__ = 'frmo_departments_and_offices'
    __table_args__ = {'comment': 'ФРМО. Справочник отделений и кабинетов (1.2.643.5.1.13.13.99.2.115) v2.1132'}

    id = Column(INTEGER(11), primary_key=True)
    mo_oid = Column(Text)
    depart_oid = Column(Text)
    depart_create_date = Column(Text)
    depart_modify_date = Column(Text)
    depart_name = Column(Text)
    depart_type_id = Column(INTEGER(11))
    depart_type_name = Column(Text)
    depart_kind_id = Column(INTEGER(11))
    depart_kind_name = Column(Text)
    separate_depart_boolean = Column(Text)
    oid = Column(Text)
    ambulance_subdivision_id = Column(Float(asdecimal=True))
    ambulance_subdivision_name = Column(Text)
    ambulance_room_count = Column(Float(asdecimal=True))
    building_id = Column(INTEGER(11))
    building_create_date = Column(Text)
    building_modify_date = Column(Text)
    building_name = Column(Text)
    building_build_year = Column(INTEGER(11))
    building_floor_count = Column(INTEGER(11))
    building_has_trouble = Column(Text)
    building_address_post_index = Column(Float(asdecimal=True))
    building_address_cadastral_number = Column(Text)
    building_address_latitude = Column(Float(asdecimal=True))
    building_address_longtitude = Column(Float(asdecimal=True))
    building_address_region_id = Column(Float(asdecimal=True))
    building_address_region_name = Column(Text)
    building_address_aoid_area = Column(Text)
    building_address_aoid_street = Column(Text)
    building_address_houseid = Column(Text)
    building_address_prefix_area = Column(Text)
    building_address_area_name = Column(Text)
    building_address_prefix_street = Column(Text)
    building_address_street_name = Column(Text)
    building_address_house = Column(Text)
    building_address_fias_version = Column(Float(asdecimal=True))
    hospital_name = Column(Text)
    hospital_subdivision_id = Column(Float(asdecimal=True))
    hospital_subdivision_name = Column(Text)
    separate_depart_text = Column(Text)
    lab_subdivision_id = Column(Text)
    lab_subdivision_name = Column(Text)
    lab_room_count = Column(Text)
    lab_exam_per_shift = Column(Text)
    depart_liquidation_date = Column(Text)
    hospital_liquidation_date = Column(Text)
    building_address_building = Column(Text)
    building_address_struct = Column(Text)


t_gr = Table(
    'gr', metadata,
    Column('code', String(255)),
    Column('name', String(255)),
    Column('Column3', String(255)),
    Column('Column4', String(255))
)


class HealthGroup(Base):
    __tablename__ = 'health_groups'
    __table_args__ = {'comment': 'Группы здоровья (1.2.643.5.1.13.13.99.2.766) v3.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    AGE_GROUP = Column(INTEGER(11), nullable=False)
    SORT = Column(INTEGER(11), nullable=False)


class HighTechMedicalCareCouponStage(Base):
    __tablename__ = 'high_tech_medical_care_coupon_stages'
    __table_args__ = {'comment': 'Этапы талона на оказание высокотехнологичной медицинской помощи (1.2.643.5.1.13.13.11.1554) v1.2'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    DESCR = Column(Text)


class HighTechMedicalCareType(Base):
    __tablename__ = 'high_tech_medical_care_types'
    __table_args__ = {'comment': 'Виды высокотехнологичной медицинской помощи (1.2.643.5.1.13.13.11.1493) v2.12'}

    ID = Column(INTEGER(11), primary_key=True)
    PROFILE = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    ID_PROFILE = Column(INTEGER(11), nullable=False)
    NAME = Column(Text, nullable=False, server_default=alchemy_text("''"))
    ID_NAME = Column(INTEGER(11), nullable=False)
    ICD_10 = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    MODEL = Column(Text, nullable=False, server_default=alchemy_text("''"))
    ID_MODEL = Column(INTEGER(11), nullable=False)
    TREATMENT = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    ID_TREATMENT = Column(INTEGER(11), nullable=False)
    METHOD = Column(Text, nullable=False, server_default=alchemy_text("''"))
    ID_METHOD = Column(INTEGER(11), nullable=False)
    GROUP = Column(INTEGER(11), nullable=False)
    PART = Column(INTEGER(11), nullable=False)
    FINANCE = Column(INTEGER(11))
    SORT = Column(INTEGER(11), nullable=False)
    DATE_BEGIN = Column(Date, nullable=False)
    DATE_END = Column(Date, nullable=False)


t_hirurg = Table(
    'hirurg', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class HmcFinancingForm(Base):
    __tablename__ = 'hmc_financing_forms'
    __table_args__ = {'comment': 'ВМП. Формы финансирования (1.2.643.5.1.13.13.99.2.864) v1.1'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(50))
    razdel = Column(INTEGER(11))
    parent = Column(INTEGER(11))


class HmcType(Base):
    __tablename__ = 'hmc_types'
    __table_args__ = {'comment': 'Виды ВМП (1.2.643.5.1.13.13.11.1493) v2.12'}

    ID = Column(INTEGER(11), primary_key=True)
    PROFILE = Column(String(50))
    ID_PROFILE = Column(INTEGER(11))
    NAME = Column(String(512))
    ID_NAME = Column(INTEGER(11))
    ICD_10 = Column(String(50))
    MODEL = Column(String(512))
    ID_MODEL = Column(INTEGER(11))
    TREATMENT = Column(String(50))
    ID_TREATMENT = Column(INTEGER(11))
    METHOD = Column(String(512))
    ID_METHOD = Column(INTEGER(11))
    GROUP_HMC = Column(INTEGER(11))
    PART = Column(INTEGER(11))
    FINANCE = Column(INTEGER(11))
    SORT = Column(INTEGER(11))
    DATE_BEGIN = Column(Date)
    DATE_END = Column(Date)


class HospitalPerformedSurgicalOperationsGroup(Base):
    __tablename__ = 'hospital_performed_surgical_operations_groups'
    __table_args__ = {'comment': 'Группы хирургических операций, проводимых в стационаре (1.2.643.5.1.13.13.11.1359) v3.2'}

    CODE = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    CODE_F14 = Column(Text)
    SORT = Column(INTEGER(11))
    PARENT = Column(Float(asdecimal=True))


class HospitalizationOrPresentationType(Base):
    __tablename__ = 'hospitalization_or_presentation_type'
    __table_args__ = {'comment': 'Вид случая госпитализации или обращения (первичный, повторный) (1.2.643.5.1.13.13.11.1007) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class HospitalizationOutcome(Base):
    __tablename__ = 'hospitalization_outcomes'
    __table_args__ = {'comment': 'Исходы госпитализации (1.2.643.5.1.13.13.11.1470) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    S_NAME = Column(Text)
    MED_FORM = Column(Text)


class HospitalizationUrgency(Base):
    __tablename__ = 'hospitalization_urgency'
    __table_args__ = {'comment': 'Срочность госпитализации (1.2.643.5.1.13.13.99.2.256) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class HumanBodyImplantedMedicalDevicesType(Base):
    __tablename__ = 'human_body_implanted_medical_devices_types'
    __table_args__ = {'comment': 'Виды медицинских изделий, имплантируемых в организм человека, и иных устройств для пациентов с ограниченными возможностями (1.2.643.5.1.13.13.11.1079) v4.1'}

    ID = Column(INTEGER(11), primary_key=True)
    PARENT = Column(Float(asdecimal=True))
    NAME = Column(Text)
    ACTUAL = Column(Text)
    EXISTENCE_NPA = Column(Text)
    ORDER = Column(Float(asdecimal=True))
    RZN = Column(Float(asdecimal=True))


class Icd10AlphabeticalIndex(Base):
    __tablename__ = 'icd10_alphabetical_index'
    __table_args__ = {'comment': 'Алфавитный указатель МКБ-10 (1.2.643.5.1.13.13.11.1489) v2.26'}

    ID = Column(INTEGER(11), primary_key=True)
    S_NAME = Column(Text)
    ICD_10 = Column(Text)
    SORT = Column(INTEGER(11))


class ImmunoMedProd(Base):
    __tablename__ = 'immuno_med_prod'
    __table_args__ = {'comment': 'Иммунобиологические лекарственные препараты (1.2.643.5.1.13.13.11.1078) v4.5'}

    ID = Column(INTEGER(11), primary_key=True)
    GROUPMIBP = Column(Text)
    GROUPNAME = Column(Text)
    GROUPNAME_ENG = Column(Text)
    TRADENAME = Column(Text)
    TRADENAME_ENG = Column(Text)
    DISEASEGROUP = Column(Text)
    ATC = Column(Text)
    DRUGFORM = Column(Text)
    DRUGFORMGR = Column(Text)
    DRUGFORMSH = Column(Text)
    DRUGPACK = Column(Text)
    DRUGPACKGR = Column(Text)
    DOZA = Column(Text)
    NUM_DOSA = Column(INTEGER(11))
    MASS = Column(Text)
    ICD10 = Column(Text)
    NAMESH = Column(Text)
    PRODUCER = Column(Text)
    PRODUCER_ENG = Column(Text)
    COUNTRY = Column(Text)
    ACTUAL = Column(Text)
    BARCODE = Column(Text)
    SCTID = Column(INTEGER(11))
    ASSOC = Column(Float(asdecimal=True))
    CALENDAR = Column(Float(asdecimal=True))
    EPID = Column(Text)
    ACTIVE = Column(Text)


class ImmunoPrepType(Base):
    __tablename__ = 'immuno_prep_type'
    __table_args__ = {'comment': 'Тип иммунобиологического препарата (1.2.643.5.1.13.13.99.2.848) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class JobTicketDeleted(Base):
    __tablename__ = 'jobTicket_deleted'
    __table_args__ = {'comment': 'Для перехвата удаляемых записей по Job_Ticket'}

    id = Column(INTEGER(11), primary_key=True)
    deleteDateTime = Column(DateTime, nullable=False)
    deletePerson_id = Column(INTEGER(11))
    deleted_actProp_jobTicket = Column(INTEGER(11))
    modifiedAction_id = Column(INTEGER(11))
    deleted_jobTicket = Column(INTEGER(11))
    deleted_master_id = Column(INTEGER(11), nullable=False)
    deleted_idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    deleted_datetime = Column(DateTime, nullable=False)
    deleted_resTimestamp = Column(TIMESTAMP)
    deleted_resConnectionId = Column(INTEGER(11))
    deleted_jobTicketType_id = Column(INTEGER(11))
    deleted_status = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    deleted_begDateTime = Column(DateTime)
    deleted_endDateTime = Column(DateTime)
    deleted_label = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    deleted_note = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    deleted_eQueueTicket_id = Column(INTEGER(11))
    deleted_person_id = Column(INTEGER(11))
    deleted_quota_id = Column(INTEGER(11))


t_kardio = Table(
    'kardio', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class KillipAcuteHeartFailureClassification(Base):
    __tablename__ = 'killip_acute_heart_failure_classification'
    __table_args__ = {'comment': 'Классификация острой сердечной недостаточности по Киллип (Killip) (1.2.643.5.1.13.13.99.2.481) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    S_PREFIX = Column(Text)


t_konsultation = Table(
    'konsultation', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


t_lab = Table(
    'lab', metadata,
    Column('codeLis', String(255)),
    Column('name', String(255)),
    Column('fullName', String(255)),
    Column('codeMiac', String(255)),
    Column('Col1', String(255)),
    Column('Col2', String(255)),
    Column('loinc', String(255)),
    Column('group', String(255)),
    Column('tisue', String(255))
)


t_lab20 = Table(
    'lab20', metadata,
    Column('КодЛИС', String(255)),
    Column('Наименование', String(255)),
    Column('ПолноеНаименование', String(255)),
    Column('code', String(255)),
    Column('Column1', String(255)),
    Column('Column2', String(255)),
    Column('КодЛОИНК', String(255)),
    Column('ГруппаОбработки', String(255)),
    Column('Материал', String(255))
)


class LaboratoryMaterialsAndSamplesDirectory(Base):
    __tablename__ = 'laboratory_materials_and_samples_directory'
    __table_args__ = {'comment': 'Федеральный справочник лабораторных исследований. Справочник лабораторных материалов и образцов (1.2.643.5.1.13.13.11.1081) v3.1'}

    ID = Column(INTEGER(11), primary_key=True)
    GROUP = Column(Text)
    ID_MATTER = Column(INTEGER(11))
    MATTER = Column(Text)
    SPECIMEN = Column(Text)
    Sort = Column(INTEGER(11))


t_labs = Table(
    'labs', metadata,
    Column('Code', String(255)),
    Column('Name', String(255)),
    Column('Price', String(255))
)


t_loinc = Table(
    'loinc', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class Lol(Base):
    __tablename__ = 'lol'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(15), nullable=False)
    name = Column(String(255), nullable=False)
    context = Column(String(64), nullable=False)


class MeasurementUnit(Base):
    __tablename__ = 'measurement_units'
    __table_args__ = {'comment': 'Единицы измерения (1.2.643.5.1.13.13.11.1358) v3.12'}

    ID = Column(INTEGER(11), primary_key=True)
    FULLNAME = Column(String(255), nullable=False)
    SHORTNAME = Column(String(255), nullable=False)
    PRINTNAME = Column(String(255), nullable=False)
    MEASUREMENT = Column(String(255), nullable=False)
    UCUM = Column(String(255))
    COEFFICIENT = Column(String(255))
    FORMULA = Column(String(255))
    CONVERSION_ID = Column(INTEGER(11), nullable=False)
    CONVERSION_NAME = Column(String(255), nullable=False)
    OKEI_CODE = Column(String(255))
    NSI_CODE_EEC = Column(String(255))
    NSI_ELEMENT_CODE_EEC = Column(String(255))


class MedicalAndSocialExpertisePreferredForm(Base):
    __tablename__ = 'medical_and_social_expertise_preferred_form'
    __table_args__ = {'comment': 'Предпочтительная форма проведения медико-социальной экспертизы (1.2.643.5.1.13.13.99.2.970) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(String(50))
    NAME_088_488_551 = Column(String(50))
    CODE = Column(INTEGER(11))


t_medical_and_social_expertise_receiving_notification_method = Table(
    'medical_and_social_expertise_receiving_notification_method', metadata,
    Column('ID', INTEGER(11), nullable=False),
    Column('NOTIFICATION', String(256)),
    Column('CODE', INTEGER(11)),
    Column('NAME', MEDIUMTEXT)
)


class MedicalCareForm(Base):
    __tablename__ = 'medical_care_forms'
    __table_args__ = {'comment': 'Формы оказания медицинской помощи (1.2.643.5.1.13.13.11.1551) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    S_NAME = Column(Text)


class MedicalCareProvisionCondition(Base):
    __tablename__ = 'medical_care_provision_conditions'
    __table_args__ = {'comment': 'Условия оказания медицинской помощи (1.2.643.5.1.13.13.99.2.322) v2.1'}

    CODE = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    COMMENTS = Column(Text)


class MedicalCertificatesEducationClassifier(Base):
    __tablename__ = 'medical_certificates_education_classifier'
    __table_args__ = {'comment': 'Классификатор образования для медицинских свидетельств (1.2.643.5.1.13.13.99.2.16) v4.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    CODE_106_u = Column(INTEGER(11))
    CODE_106_2_u = Column(INTEGER(11))
    ACTUAL = Column(INTEGER(11))
    CODE_ZAGS_NALOG = Column(INTEGER(11))
    CODE_103_u = Column(INTEGER(11))
    CODE_013_u = Column(INTEGER(11))


class MedicalCommissionGoal(Base):
    __tablename__ = 'medical_commission_goals'
    __table_args__ = {'comment': 'Цели проведения врачебной комиссии (консилиума врачей) (1.2.643.5.1.13.13.11.1506) v2.3'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    CONSULTATION = Column(Text)
    COMMISSION = Column(Text)
    NPA = Column(Text)


class MedicalDeathCertificateType(Base):
    __tablename__ = 'medical_death_certificate_type'
    __table_args__ = {'comment': 'Вид медицинского свидетельства о смерти (1.2.643.5.1.13.13.99.2.19) v1.2'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class MedicalDevicesDirectory(Base):
    __tablename__ = 'medical_devices_directory'
    __table_args__ = {'comment': 'ФРЛЛО. Справочник медицинских изделий согласно каталогу товаров, работ, услуг для обеспечения государственных и муниципальных нужд (1.2.643.5.1.13.13.99.2.604) v1.128'}

    ID = Column(INTEGER(11), primary_key=True)
    CODE = Column(Text)
    KTRU_CODE = Column(Text)
    OKPD2_CODE = Column(Text)
    NAME = Column(Text)
    IS_TEMPLATE = Column(Text)
    APPLICATION_DATE_START = Column(Text)
    OKEI_CODE = Column(Float(asdecimal=True))
    PARENT_CODE = Column(Text)
    CHARACTERISTICS = Column(Text)
    RZN_CODE = Column(Text)
    DESCRIPTION = Column(Text)
    APPLICATION_DATE_END = Column(Text)


class MedicalDocumentType(Base):
    __tablename__ = 'medical_document_types'
    __table_args__ = {'comment': 'Виды медицинской документации (1.2.643.5.1.13.13.11.1522) v5.15'}

    RECID = Column(INTEGER(11), primary_key=True)
    OID = Column(String(255), nullable=False)
    Synonym_OID = Column(String(255))
    Name = Column(Text, nullable=False)
    Synonym = Column(String(255))
    NPA = Column(Text)
    Date_NPA = Column(String(255))
    Form = Column(String(255))
    TYPE = Column(String(255), nullable=False)
    CODE_ZAGS_NALOG = Column(String(255))
    ACTUAL = Column(TINYINT(1), nullable=False)


class MedicalProceduresAndManipulation(Base):
    __tablename__ = 'medical_procedures_and_manipulations'
    __table_args__ = {'comment': 'Медицинские процедуры и манипуляции (1.2.643.5.1.13.13.99.2.785) v1.3'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    S_CODE = Column(Text)


class MedicalServiceStatu(Base):
    __tablename__ = 'medical_service_status'
    __table_args__ = {'comment': 'Статус выполнения медицинской услуги (1.2.643.5.1.13.13.99.2.350) v2.1'}

    CODE = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    SORT = Column(INTEGER(11))
    PARENT = Column(Float(asdecimal=True))


class MedicalServicesAndExpensiveTreatment(Base):
    __tablename__ = 'medical_services_and_expensive_treatment'
    __table_args__ = {'comment': 'Медицинские услуги и дорогостоящее лечение (1.2.643.5.1.13.13.99.2.847) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class MedicalServicesNomenclature(Base):
    __tablename__ = 'medical_services_nomenclature'
    __table_args__ = {'comment': 'Номенклатура медицинских услуг (1.2.643.5.1.13.13.11.1070) 2.10'}

    ID = Column(INTEGER(11), primary_key=True)
    S_CODE = Column(Text)
    NAME = Column(Text)
    REL = Column(INTEGER(11))
    DATEOUT = Column(Text)


class MedicalSitesType(Base):
    __tablename__ = 'medical_sites_types'
    __table_args__ = {'comment': 'ФРМО. Типы врачебных участков (1.2.643.5.1.13.13.99.2.639) v1.1'}

    id = Column(INTEGER(11), primary_key=True)
    site = Column(Text)


class MedicalWorkerPosition(Base):
    __tablename__ = 'medical_worker_positions'
    __table_args__ = {'comment': 'Должности медицинских и фармацевтических работников (1.2.643.5.1.13.13.11.1002) v7.6'}

    ID = Column(INTEGER(11), primary_key=True)
    PID = Column(INTEGER(11))
    SORT = Column(INTEGER(11), nullable=False)
    NAME = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    EQUIVALENT = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    NORMATIVE = Column(INTEGER(11))
    GROUP = Column(INTEGER(11))
    FORM_30 = Column(INTEGER(11))
    ACTUAL = Column(TINYINT(1))
    DATA_END = Column(Date)
    COMMENT = Column(Text, nullable=False, server_default=alchemy_text("''"))


class MedicineRoutesInsertion(Base):
    __tablename__ = 'medicine_routes_insertion'
    __table_args__ = {'comment': 'Пути введения лекарственных препаратов, в том числе для льготного обеспечения граждан лекарственными средствами ( \t1.2.643.5.1.13.13.11.1468) v2.3'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME_RUS = Column(String(50))
    NAME_ENG = Column(String(50))
    PARENT = Column(INTEGER(11))
    NSI_CODE_EEC = Column(INTEGER(11))
    NSI_ELEMENT_CODE_EEC = Column(INTEGER(11))


class MoRfRegister(Base):
    __tablename__ = 'mo_rf_register'
    __table_args__ = {'comment': 'Реестр МО РФ (1.2.643.5.1.13.13.11.1461) v6.757'}

    id = Column(INTEGER(11), primary_key=True)
    oid = Column(String(255))
    oldOid = Column(String(255))
    nameFull = Column(String(255))
    nameShort = Column(String(255))
    parentId = Column(String(255))
    medicalSubjectId = Column(INTEGER(11))
    medicalSubjectName = Column(String(255))
    inn = Column(String(255))
    kpp = Column(String(255))
    ogrn = Column(String(255))
    regionId = Column(INTEGER(11))
    regionName = Column(String(255))
    organizationType = Column(INTEGER(11))
    moDeptId = Column(INTEGER(11))
    moDeptName = Column(String(255))
    founder = Column(String(255))
    deleteDate = Column(DateTime)
    deleteReason = Column(String(255))
    createDate = Column(DateTime)
    modifyDate = Column(DateTime)
    moLevel = Column(String(255))
    moAgencyKindId = Column(INTEGER(11))
    moAgencyKind = Column(String(255))
    profileAgencyKindId = Column(INTEGER(11))
    profileAgencyKind = Column(String(255))
    postIndex = Column(String(255))
    cadastralNumber = Column(String(255))
    latitude = Column(String(255))
    longtitude = Column(String(255))
    fiasVersion = Column(INTEGER(11))
    aoidArea = Column(String(255))
    aoidStreet = Column(String(255))
    houseid = Column(String(255))
    addrRegionId = Column(INTEGER(11))
    addrRegionName = Column(String(255))
    territoryCode = Column(String(255))
    isFederalCity = Column(String(255))
    areaName = Column(String(255))
    prefixArea = Column(String(255))
    streetName = Column(String(255))
    prefixStreet = Column(String(255))
    house = Column(String(255))
    building = Column(String(255))
    struct = Column(String(255))
    parentOspOid = Column(String(255))
    ospOid = Column(String(255))
    childrenOspOid = Column(String(255))


class MorbidityAndMortalityExternalCausesIcd10AlphabeticalIndex(Base):
    __tablename__ = 'morbidity_and_mortality_external_causes_icd10_alphabetical_index'
    __table_args__ = {'comment': 'Алфавитный указатель МКБ-10, внешние причины заболеваемости и смертности (1.2.643.5.1.13.13.99.2.692) v1.5'}

    ID = Column(INTEGER(11), primary_key=True)
    S_NAME = Column(Text)
    ICD_10 = Column(Text)
    SORT = Column(INTEGER(11))


class MseAction(Base):
    __tablename__ = 'mse_actions'
    __table_args__ = {'comment': 'Результаты исследований'}

    id = Column(INTEGER(11), primary_key=True)
    action_id = Column(INTEGER(11))
    type = Column(TINYINT(1))
    note = Column(Text)
    result = Column(Text)
    master_id = Column(INTEGER(11))


class MseResultDatum(Base):
    __tablename__ = 'mse_result_data'

    id = Column(INTEGER(11), primary_key=True)
    xml = Column(Text)
    event_id = Column(INTEGER(11))


t_netricaAccessVaccination = Table(
    'netricaAccessVaccination', metadata,
    Column('id', INTEGER(11)),
    Column('code', INTEGER(11)),
    Column('name', String(18)),
    Column('StageStatus', INTEGER(11))
)


t_netricaContraindication = Table(
    'netricaContraindication', metadata,
    Column('id', String(8)),
    Column('code', INTEGER(11)),
    Column('parent_id', INTEGER(11)),
    Column('name', String(101))
)


class NetricaCountry(Base):
    __tablename__ = 'netricaCountry'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(String(100))


class NetricaCulturalevent(Base):
    __tablename__ = 'netricaCulturalevents'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    code = Column(String(8))
    name = Column(String(64))


class NetricaHospChannel(Base):
    __tablename__ = 'netricaHospChannel'

    id = Column(INTEGER(10), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("'2017-01-01 00:00:00'"))
    createPerson_id = Column(INTEGER(5), nullable=False, server_default=alchemy_text("1"))
    modifyDatetime = Column(DateTime, server_default=alchemy_text("'2017-01-01 00:00:00'"))
    modifyPerson_id = Column(INTEGER(5), nullable=False, server_default=alchemy_text("1"))
    deleted = Column(INTEGER(2), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(255))
    name = Column(String(255))


class NetricaIntoxicationType(Base):
    __tablename__ = 'netricaIntoxicationType'
    __table_args__ = {'comment': 'Справочник «Вид транспортировки»'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    code = Column(String(8))
    name = Column(String(64))


class NetricaObsled(Base):
    __tablename__ = 'netricaObsled'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8))
    name = Column(String(255))


class NetricaPatientConditionOnAdmission(Base):
    __tablename__ = 'netricaPatientConditionOnAdmission'
    __table_args__ = {'comment': 'Классификатор состояний при обращении (поступлении) в медицинскую организацию'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    code = Column(String(8))
    name = Column(String(64))


class NetricaRegion(Base):
    __tablename__ = 'netricaRegion'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    code = Column(String(8))
    name = Column(String(64))


t_netricaRiskGroup = Table(
    'netricaRiskGroup', metadata,
    Column('id', String(8)),
    Column('code', INTEGER(11)),
    Column('name', String(229)),
    Column('short_name', String(10))
)


class NetricaSMO(Base):
    __tablename__ = 'netricaSMO'

    ID = Column(String(8), primary_key=True, server_default=alchemy_text("''"))
    SMOCOD = Column(INTEGER(11))
    OGRN = Column(Float(asdecimal=True))
    KPP = Column(INTEGER(11))
    NAM_SMOP = Column(String(204))
    NAM_SMOK = Column(String(99))
    ADDR_F = Column(String(95))
    FAM_RUK = Column(String(16))
    IM_RUK = Column(String(10))
    OT_RUK = Column(String(15))
    PHONE = Column(String(28))
    FAX = Column(String(28))
    HOT_LINE = Column(String(13))
    E_MAIL = Column(String(50))
    N_DOC = Column(String(14))
    D_START = Column(String(10))
    DATE_E = Column(String(10))
    D_BEGIN = Column(String(10))
    D_END = Column(String(1))


class NetricaSex(Base):
    __tablename__ = 'netricaSex'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    code = Column(String(8))
    name = Column(String(64))


t_netricaTransportIntern = Table(
    'netricaTransportIntern', metadata,
    Column('id', INTEGER(11)),
    Column('createDatetime', DateTime),
    Column('createPerson_id', INTEGER(11)),
    Column('modifyDatetime', DateTime),
    Column('modifyPerson_id', INTEGER(11)),
    Column('deleted', INTEGER(11)),
    Column('code', INTEGER(11)),
    Column('name', String(50))
)


class NetricaTypeFromDiseaseStart(Base):
    __tablename__ = 'netricaTypeFromDiseaseStart'
    __table_args__ = {'comment': 'Справочник времени доставки больного в стационар от начала заболевания (получения травмы)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    code = Column(String(8))
    name = Column(String(64))


t_netricaVaccinationType = Table(
    'netricaVaccinationType', metadata,
    Column('id', String(2)),
    Column('code', String(2)),
    Column('name', String(20)),
    Column('parent_id', String(23))
)


class NetricaYesNo(Base):
    __tablename__ = 'netricaYesNo'

    id = Column(INTEGER(9), primary_key=True)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    code = Column(String(24))
    name = Column(String(100))


class Netricagra(Base):
    __tablename__ = 'netricagra'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    code = Column(String(8))
    name = Column(String(200))


class NetricarbCitizenship(Base):
    __tablename__ = 'netricarbCitizenship'

    id = Column(String(8), primary_key=True, server_default=alchemy_text("''"))
    code = Column(INTEGER(11))
    name = Column(String(79))


t_netricazpv = Table(
    'netricazpv', metadata,
    Column('name', String(100)),
    Column('netrica_ZPV', String(50))
)


class NetricaСitizenship(Base):
    __tablename__ = 'netricaСitizenship'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    code = Column(String(8))
    name = Column(String(128))


t_new_price = Table(
    'new_price', metadata,
    Column('id', INTEGER(11)),
    Column('code', String(50)),
    Column('name', String(200)),
    Column('price', INTEGER(11))
)


class NewbornFullTerm(Base):
    __tablename__ = 'newborn_full_term'
    __table_args__ = {'comment': 'Доношенность новорожденного (1.2.643.5.1.13.13.99.2.18) v1.3'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class NosologicalDiagnosisType(Base):
    __tablename__ = 'nosological_diagnosis_type'
    __table_args__ = {'comment': 'Виды нозологических единиц диагноза (1.2.643.5.1.13.13.11.1077) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    FULL_NAME = Column(String(50))
    SHORT_NAME = Column(String(50))
    NAME_088_488_551 = Column(String(50))


class NosologicalUnitsOfDiagnosisType(Base):
    __tablename__ = 'nosological_units_of_diagnosis_types'
    __table_args__ = {'comment': 'Виды нозологических единиц диагноза (1.2.643.5.1.13.13.11.1077) v1.3'}

    ID = Column(INTEGER(11), primary_key=True)
    FULL_NAME = Column(Text)
    SHORT_NAME = Column(Text)


t_oftalmo = Table(
    'oftalmo', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


t_org_term = Table(
    'org_term', metadata,
    Column('netrica_code', String(50)),
    Column('name_po', Text),
    Column('name_mo', String(200)),
    Column('netrica_code_mo', String(50)),
    Column('Адрес', String(100)),
    Column('INN', Float(10, True)),
    Column('OGRN', Float(10, True)),
    Column('Type', String(50)),
    Column('no', TINYINT(1), server_default=alchemy_text("0"))
)


t_orgnetcode = Table(
    'orgnetcode', metadata,
    Column('id', INTEGER(11)),
    Column('createDatetime', DateTime),
    Column('createPerson_id', INTEGER(11)),
    Column('modifyDatetime', DateTime),
    Column('modifyPerson_id', INTEGER(11)),
    Column('deleted', INTEGER(11)),
    Column('fullName', String(250)),
    Column('shortName', String(100)),
    Column('title', String(100)),
    Column('net_id', INTEGER(11)),
    Column('infisCode', String(50)),
    Column('obsoleteInfisCode', INTEGER(11)),
    Column('OKVED', String(50)),
    Column('INN', Float(10, True)),
    Column('KPP', INTEGER(11)),
    Column('OGRN', Float(10, True)),
    Column('OKATO', Float(10, True)),
    Column('OKPF_code', INTEGER(11)),
    Column('OKPF_id', INTEGER(11)),
    Column('OKFS_code', INTEGER(11)),
    Column('OKFS_id', INTEGER(11)),
    Column('OKPO', INTEGER(11)),
    Column('FSS', String(255)),
    Column('region', String(50)),
    Column('address', String(100)),
    Column('chief', String(100)),
    Column('phone', String(100)),
    Column('accountant', String(50)),
    Column('isInsurer', INTEGER(11)),
    Column('isCompulsoryInsurer', INTEGER(11)),
    Column('isVoluntaryInsurer', INTEGER(11)),
    Column('compulsoryServiceStop', INTEGER(11)),
    Column('voluntaryServiceStop', INTEGER(11)),
    Column('area', Float(10, True)),
    Column('isHospital', INTEGER(11)),
    Column('notes', String(200)),
    Column('head_id', String(255)),
    Column('miacCode', INTEGER(11)),
    Column('isMedical', INTEGER(11)),
    Column('isArmyOrg', INTEGER(11)),
    Column('canOmitPolicyNumber', INTEGER(11)),
    Column('netrica_Code', String(50)),
    Column('DATN', DateTime),
    Column('DATO', DateTime),
    Column('reestrNumber', INTEGER(11))
)


t_otorinola = Table(
    'otorinola', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class OutcomesDisease(Base):
    __tablename__ = 'outcomes_disease'
    __table_args__ = {'comment': 'Исходы заболеваний (1.2.643.5.1.13.13.11.1491) v1.2'}

    CODE = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class PatientAlertType(Base):
    __tablename__ = 'patient_alert_types'
    __table_args__ = {'comment': 'Типы оповещения пациента (1.2.643.5.1.13.13.99.2.719) v1.1'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(Text)


class PatientOccupationalHazard(Base):
    __tablename__ = 'patient_occupational_hazards'
    __table_args__ = {'comment': 'Профессиональные вредности пациента при сборе анамнеза (1.2.643.5.1.13.13.11.1060) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    GROUP = Column(INTEGER(11))
    NAME = Column(Text, nullable=False, server_default=alchemy_text("''"))
    PARENT = Column(INTEGER(11))
    SCTID = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    NUMBER = Column(String(255), nullable=False, server_default=alchemy_text("''"))


class PmoDAndUdActivity(Base):
    __tablename__ = 'pmo_d_and_ud_activities'
    __table_args__ = {'comment': 'Мероприятия профилактического медицинского осмотра, диспансеризации и углубленной диспансеризации (1.2.643.5.1.13.13.99.2.822) v3.2'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    EVENT = Column(Text)
    SourceOfInformation = Column(Text)
    NUMBER_ACCOUNTING_FORM = Column(Text)
    PARENT_FNSI_KEY = Column(Text)


t_po_age = Table(
    'po_age', metadata,
    Column('code', String(255)),
    Column('age', String(255))
)


class PreferentialCitizensCategory(Base):
    __tablename__ = 'preferential_citizens_categories'
    __table_args__ = {'comment': 'Льготные категории граждан (1.2.643.5.1.13.13.99.2.541) v6.16'}

    code = Column(INTEGER(11), primary_key=True)
    ID = Column(Text)
    NAME = Column(Text)
    NAME_SHORT_FRLLO = Column(Text)
    DATA_BEGIN = Column(Text)
    NPA_BEGIN = Column(INTEGER(11))
    SOURCE = Column(INTEGER(11))
    CATEGORY = Column(Float(asdecimal=True))
    MONEY = Column(Text)
    ICD10 = Column(Text)


class PreferentialRecipeType(Base):
    __tablename__ = 'preferential_recipe_type'
    __table_args__ = {'comment': 'Тип назначений льготного рецепта (1.2.643.5.1.13.13.99.2.651) v1.2'}

    ID = Column(INTEGER(11), primary_key=True)
    PRESCRIPTION_TYPE = Column(String(64))


class PregnancyDeathAssociation(Base):
    __tablename__ = 'pregnancy_death_association'
    __table_args__ = {'comment': 'Связь смерти с беременностью (1.2.643.5.1.13.13.99.2.25) v1.4'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


t_price = Table(
    'price', metadata,
    Column('code', String(50)),
    Column('name', String(200)),
    Column('price', INTEGER(11))
)


t_prk = Table(
    'prk', metadata,
    Column('code', Float(10, True)),
    Column('name', String(255))
)


t_prochee = Table(
    'prochee', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


t_profile_med_pom = Table(
    'profile_med_pom', metadata,
    Column('code', String(255)),
    Column('name', String(255)),
    Column('group_n', String(255)),
    Column('group', String(255))
)


class ProvidedBenefitsType(Base):
    __tablename__ = 'provided_benefits_types'
    __table_args__ = {'comment': 'Виды предоставляемых льгот (1.2.643.5.1.13.13.99.2.605) v3.2'}

    ID = Column(INTEGER(11), primary_key=True)
    ID_LGOTA = Column(String(50))
    ID_LGOTA_LIST = Column(INTEGER(11))
    PERCENT = Column(INTEGER(11))
    DATA_BEGIN = Column(Date)
    NPA_BEGIN = Column(INTEGER(11))
    DATA_END = Column(Date)
    NPA_END = Column(String(50))


t_rb = Table(
    'rb', metadata,
    Column('Column1', String(255)),
    Column('Column2', String(255)),
    Column('Column3', String(255))
)


class RbActionAssistantType(Base):
    __tablename__ = 'rbActionAssistantType'
    __table_args__ = {'comment': 'Справочник типов ассистентов для мероприятий.'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64), nullable=False)
    name = Column(String(128), nullable=False)
    isEnabledFreeInput = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))


class RbActionTypeSimilarity(Base):
    __tablename__ = 'rbActionTypeSimilarity'
    __table_args__ = {'comment': 'Таблица схожести типов действий для возможности копирования данных между такими действиями.'}

    id = Column(INTEGER(11), primary_key=True)
    firstActionType_id = Column(INTEGER(11), nullable=False)
    secondActionType_id = Column(INTEGER(11), nullable=False)
    similarityType = Column(TINYINT(1))


class RbBirthPlace(Base):
    __tablename__ = 'rbBirthPlace'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


class RbBodyType(Base):
    __tablename__ = 'rbBodyType'
    __table_args__ = {'comment': 'Телосложение'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(String(64))


class RbCaseCast(Base):
    __tablename__ = 'rbCaseCast'
    __table_args__ = {'comment': 'Типы случая лечения.'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(6), nullable=False)
    name = Column(String(128), nullable=False)
    ID_INTER = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    ID_FINT = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    DEFAULT_ID_FINT = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))


class RbChildSerialNumber(Base):
    __tablename__ = 'rbChildSerialNumber'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


class RbCitizenship(Base):
    __tablename__ = 'rbCitizenship'
    __table_args__ = {'comment': 'Гражданство'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(4), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(80), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbCitizenship.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbCitizenship.modifyPerson_id == Person.id')


class RbClientAddressType(Base):
    __tablename__ = 'rbClientAddressType'
    __table_args__ = {'comment': 'Тип адреса пациента'}

    id = Column(INTEGER(11), primary_key=True)
    type = Column(INTEGER(11))
    code = Column(String(16))
    name = Column(String(128))


class RbClientMonitoringFrequence(Base):
    __tablename__ = 'rbClientMonitoringFrequence'
    __table_args__ = {'comment': 'Частота посещений пациента'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(12), nullable=False)
    name = Column(String(64), nullable=False)


class RbClientMonitoringKind(Base):
    __tablename__ = 'rbClientMonitoringKind'
    __table_args__ = {'comment': 'Справочник видов наблюдения пациента'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    group_id = Column(ForeignKey('rbClientMonitoringKind.id'))

    group = relationship('RbClientMonitoringKind', remote_side=[id])


t_rbClientMonitoringKind21 = Table(
    'rbClientMonitoringKind21', metadata,
    Column('ID', INTEGER(11)),
    Column('CODE', String(16)),
    Column('NAME', String(64))
)


class RbClientRemarkType(Base):
    __tablename__ = 'rbClientRemarkType'
    __table_args__ = {'comment': 'Справочник типов пометок паицента.'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)
    flatCode = Column(String(32), nullable=False)


class RbCloseCardReason(Base):
    __tablename__ = 'rbCloseCardReason'
    __table_args__ = {'comment': 'ГРКМ. Справочник причин закрытия карты'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    code = Column(String(12))
    name = Column(String(64))


class RbCompulsoryTreatmentKind(Base):
    __tablename__ = 'rbCompulsoryTreatmentKind'
    __table_args__ = {'comment': 'Справочник видов принудительного лечения'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(255), nullable=False)


class RbConsultationType(Base):
    __tablename__ = 'rbConsultationType'
    __table_args__ = {'comment': 'Типы консультаций - справочник: 1.2.643.5.1.13.13.11.1463'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(Text)
    name = Column(Text)


class RbDTypeGroupEi(Base):
    __tablename__ = 'rbDTypeGroup_eis'
    __table_args__ = {'comment': 'Согласие/Отказ пациента от 2 этапа диспансеризации ЕИС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(255), nullable=False)


class RbDayInfoAI(Base):
    __tablename__ = 'rbDayInfoAIS'
    __table_args__ = {'comment': 'Применить к дням АИС Информ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(Text, nullable=False, server_default=alchemy_text("''"))
    name = Column(Text, nullable=False, server_default=alchemy_text("''"))


class RbDecisionOUZ(Base):
    __tablename__ = 'rbDecisionOUZ'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


class RbDepartmentAI(Base):
    __tablename__ = 'rbDepartmentAIS'
    __table_args__ = {'comment': 'Справочник Отделений для АИС Информ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(Text, nullable=False, server_default=alchemy_text("''"))
    name = Column(Text, nullable=False, server_default=alchemy_text("''"))


class RbDiagnosisAffectedSide(Base):
    __tablename__ = 'rbDiagnosisAffectedSide'
    __table_args__ = {'comment': 'Сторона поражения'}

    id = Column(INTEGER(11), primary_key=True)
    egisz_code = Column(String(8))
    name = Column(Text)


class RbDiagnosisChangeReason(Base):
    __tablename__ = 'rbDiagnosisChangeReason'
    __table_args__ = {'comment': 'Статус продолжения или изменения заболевания {1.2.643.2.69.1.1.1.9}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(10))
    name = Column(String(255))


class RbDiagnosisMetastasesLocalization(Base):
    __tablename__ = 'rbDiagnosisMetastasesLocalization'
    __table_args__ = {'comment': 'Локализация отдаленных метастазов (при IV стадии заболевания)'}

    id = Column(INTEGER(11), primary_key=True)
    egisz_code = Column(String(8))
    name = Column(Text)


class RbDiagnosisNosologyType(Base):
    __tablename__ = 'rbDiagnosisNosologyType'
    __table_args__ = {'comment': 'Вид нозологических единиц диагноза'}

    id = Column(INTEGER(11), primary_key=True)
    egisz_code = Column(String(8))
    FULL_NAME = Column(Text)
    SHORT_NAME = Column(String(64))
    code = Column(INTEGER(11))
    name = Column(String(255))


class RbDiagnosisPrimaryPluralTumor(Base):
    __tablename__ = 'rbDiagnosisPrimaryPluralTumor'
    __table_args__ = {'comment': 'Первично–множественная опухоль'}

    id = Column(INTEGER(11), primary_key=True)
    egisz_code = Column(String(8))
    name = Column(Text)


class RbDiagnosisRationale(Base):
    __tablename__ = 'rbDiagnosisRationale'
    __table_args__ = {'comment': 'Степень обоснованности диагноза'}

    id = Column(INTEGER(11), primary_key=True)
    egisz_code = Column(String(8))
    name = Column(Text)


class RbDiagnosisTumorTopography(Base):
    __tablename__ = 'rbDiagnosisTumorTopography'
    __table_args__ = {'comment': 'Топография опухоли'}

    id = Column(INTEGER(11), primary_key=True)
    egisz_code = Column(String(8))
    code = Column(String(8))
    name = Column(Text)
    parent_code = Column(String(8))
    additional_localization = Column(Text)
    sort_field = Column(INTEGER(11))


class RbDictionary(Base):
    __tablename__ = 'rbDictionary'
    __table_args__ = {'comment': 'Пользовательский словарь проверки орфографии'}

    word = Column(String(63), primary_key=True)


class RbDisabilityGroup(Base):
    __tablename__ = 'rbDisabilityGroup'
    __table_args__ = {'comment': 'Группы инвалидности - справочник: 1.2.643.5.1.13.13.11.1053'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbDistrict(Base):
    __tablename__ = 'rbDistrict'
    __table_args__ = {'comment': 'Справочник районов населенного пункта, в котором расположено ЛПУ.'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)
    grkm_code = Column(String(8))


class RbDrug(Base):
    __tablename__ = 'rbDrug'
    __table_args__ = {'comment': 'Справочник формулярных наименований ЛС (кэш лекарств из 1с)'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(50), nullable=False)
    name = Column(String(300), nullable=False)
    unit_id = Column(INTEGER(11), nullable=False)
    quantity = Column(INTEGER(11), nullable=False)
    latinMNN = Column(String(128))


class RbECROperationType(Base):
    __tablename__ = 'rbECROperationType'
    __table_args__ = {'comment': 'Виды операций по кассе'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    isShowed = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))


class RbEGISZRegion(Base):
    __tablename__ = 'rbEGISZRegion'
    __table_args__ = {'comment': 'Субъекты Российской Федерации'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


class RbELNInvalidGroup(Base):
    __tablename__ = 'rbELNInvalidGroup'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(INTEGER(11))
    type = Column(TINYINT(1))
    code = Column(String(8))
    name = Column(String(80))


class RbELNInvalidLos(Base):
    __tablename__ = 'rbELNInvalidLoss'

    id = Column(TINYINT(11), primary_key=True)
    code = Column(String(8))
    name = Column(String(80))


class RbELNRelationType(Base):
    __tablename__ = 'rbELNRelationType'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(INTEGER(11))
    type = Column(TINYINT(1))
    code = Column(String(8))
    name = Column(String(80))


class RbEmergencyAction(Base):
    __tablename__ = 'rbEmergencyAction'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(129))
    code = Column(VARCHAR(16))


class RbEmergencyCallReason(Base):
    __tablename__ = 'rbEmergencyCallReason'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(VARCHAR(16))
    regionalCode = Column(VARCHAR(64))
    value = Column(VARCHAR(255))
    mkb = Column(VARCHAR(32), nullable=False, server_default=alchemy_text("'Z00.0'"))


class RbEmergencyCallSource(Base):
    __tablename__ = 'rbEmergencyCallSource'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(VARCHAR(16))
    regionalCode = Column(VARCHAR(64))
    value = Column(VARCHAR(255))


class RbEmergencyMKB(Base):
    __tablename__ = 'rbEmergencyMKB'

    id = Column(INTEGER(11), primary_key=True)
    mkb = Column(VARCHAR(16), nullable=False)
    name = Column(VARCHAR(128), nullable=False)


class RbEmergencyMedication(Base):
    __tablename__ = 'rbEmergencyMedications'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    regionalCode = Column(String(64))
    name = Column(VARCHAR(255), nullable=False)
    minRest = Column(INTEGER(11), nullable=False, server_default=alchemy_text("50"))
    minQuantity = Column(INTEGER(11), server_default=alchemy_text("0"))
    amountPack = Column(INTEGER(11), nullable=False, server_default=alchemy_text("1"))


class RbEmergencyPatientFlag(Base):
    __tablename__ = 'rbEmergencyPatientFlags'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(VARCHAR(64))
    code = Column(VARCHAR(16))


class RbEmergencyProfile(Base):
    __tablename__ = 'rbEmergencyProfile'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(128))
    code = Column(VARCHAR(16))
    specialization = Column(VARCHAR(64))


class RbEmergencyRole(Base):
    __tablename__ = 'rbEmergencyRole'

    id = Column(INTEGER(11), primary_key=True)
    regionalCode = Column(VARCHAR(64))
    name = Column(VARCHAR(255))
    code = Column(VARCHAR(255))
    operator = Column(INTEGER(1), nullable=False, server_default=alchemy_text("1"))
    close = Column(INTEGER(1), nullable=False, server_default=alchemy_text("1"))
    medicaments = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    reports = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    config = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))


class RbEpicrisisPropertyType(Base):
    __tablename__ = 'rbEpicrisisPropertyType'
    __table_args__ = {'comment': 'Таблица типов шаблонов свойств разделов эпикризов'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)


class RbEpicrisisSection(Base):
    __tablename__ = 'rbEpicrisisSections'
    __table_args__ = {'comment': 'Таблица разделов эпикризов.'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(String(200))


class RbEventKind(Base):
    __tablename__ = 'rbEventKind'
    __table_args__ = {'comment': 'Виды событий'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)


class RbExaminationType(Base):
    __tablename__ = 'rbExaminationType'
    __table_args__ = {'comment': ' Вид назначенного обследования .Справочник создан по 5343 ~0022330 данные из SPRAV_OBS_TYPE.DBF'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)


class RbExtraKSLP(Base):
    __tablename__ = 'rbExtraKSLP'
    __table_args__ = {'comment': 'Справочник отдельных КСЛП'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64), nullable=False)
    name = Column(Text, nullable=False)
    coefficient = Column(Float(asdecimal=True))
    begDate = Column(Date)
    endDate = Column(Date)
    can_select = Column(TINYINT(1), server_default=alchemy_text("0"))
    short_name = Column(String(15))


class RbFilial(Base):
    __tablename__ = 'rbFilials'

    id = Column(INTEGER(10), primary_key=True)
    createDatetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(10))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(INTEGER(10))
    shortName = Column(String(45), nullable=False)
    fullName = Column(String(45), nullable=False)


class RbFinance(Base):
    __tablename__ = 'rbFinance'
    __table_args__ = {'comment': 'Источники финансирования'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    idx = Column(INTEGER(11), server_default=alchemy_text("0"))
    name = Column(String(64), nullable=False)
    netrica_Code = Column(String(65))
    netricaCode = Column(String(64))

    createPerson = relationship('Person', primaryjoin='RbFinance.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbFinance.modifyPerson_id == Person.id')


class RbGOV(Base):
    __tablename__ = 'rbGOV'
    __table_args__ = {'comment': 'Справочник Нетрики gov'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(CHAR(10), nullable=False)
    name = Column(Text)
    shortName = Column(Text)


class RbGoalType2(Base):
    __tablename__ = 'rbGoalType2'

    id = Column(INTEGER(11), primary_key=True)
    ID_GOAL = Column(INTEGER(11), nullable=False)
    GOAL_NAME = Column(Text)


class RbHospResult(Base):
    __tablename__ = 'rbHospResult'
    __table_args__ = {'comment': 'Исходы случаев госпитализации (1.2.643.5.1.13.13.99.2.307)'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(256))


class RbHospitalBedProfileCopy(Base):
    __tablename__ = 'rbHospitalBedProfile_copy'
    __table_args__ = {'comment': 'Профиль койки'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8), nullable=False)
    regionalCode = Column(String(16), server_default=alchemy_text("'NULL'"))
    name = Column(String(512), server_default=alchemy_text("'NULL'"))
    service_id = Column(INTEGER(11))
    eisCode = Column(String(15), server_default=alchemy_text("'NULL'"))
    paidFlag = Column(TINYINT(1), server_default=alchemy_text("0"))


class RbHospitalizationPurpose(Base):
    __tablename__ = 'rbHospitalizationPurpose'
    __table_args__ = {'comment': 'Справочник целей госпитализации'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(32), nullable=False)
    name = Column(String(256), nullable=False)


class RbIEMKDocument(Base):
    __tablename__ = 'rbIEMKDocument'
    __table_args__ = {'comment': 'Справочник посылаемых документов ИЭМК'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    applicability = Column(INTEGER(11), nullable=False)
    mark = Column(TINYINT(1))
    actionType_id = Column(INTEGER(11))
    EGISZ_code = Column(String(50))
    type = Column(String(10))
    netrica_Code = Column(String(5))
    IEMK_OID = Column(String(64))
    isVisibleInJobTicket = Column(TINYINT(1), server_default=alchemy_text("0"))


class RbImmunobiologicalPill(Base):
    __tablename__ = 'rbImmunobiologicalPills'
    __table_args__ = {'comment': 'Иммунобиологические препараты для специфической профилактики, диагностики и терапии {1.2.643.5.1.13.13.11.1078}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))
    groupname = Column(String(500))


class RbImmunsationStatu(Base):
    __tablename__ = 'rbImmunsationStatus'
    __table_args__ = {'comment': 'Статус проведения иммунизации {1.2.643.2.69.1.1.1.172}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))


class RbInfectionCode(Base):
    __tablename__ = 'rbInfectionCode'
    __table_args__ = {'comment': 'Код инфекции {1.2.643.2.69.1.1.1.130}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))
    fullname = Column(String(500))


class RbInfoSource(Base):
    __tablename__ = 'rbInfoSource'
    __table_args__ = {'comment': 'Справочник для источников информации'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(256), nullable=False)


class RbInstrumental(Base):
    __tablename__ = 'rbInstrumental'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(255))
    name = Column(String(255))


class RbJobTicketType(Base):
    __tablename__ = 'rbJobTicketType'
    __table_args__ = {'comment': 'Справочник типов номерков'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    code = Column(String(8))
    name = Column(String(8))


class RbKSGCriterion(Base):
    __tablename__ = 'rbKSGCriterion'
    __table_args__ = {'comment': 'Дополнительные критерии подбора КСГ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(128), nullable=False)
    name = Column(String(256), nullable=False)


class RbMSECitizenship(Base):
    __tablename__ = 'rbMSECitizenship'
    __table_args__ = {'comment': 'Категории гражданства при направлении на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEClientBodyType(Base):
    __tablename__ = 'rbMSEClientBodyType'
    __table_args__ = {'comment': 'Типы телосложения'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEClientEducationLevel(Base):
    __tablename__ = 'rbMSEClientEducationLevel'
    __table_args__ = {'comment': 'Уровень образования'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEClientLocOrg(Base):
    __tablename__ = 'rbMSEClientLocOrg'
    __table_args__ = {'comment': 'Местонахождение гражданина при направлении на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEClinicalPredict(Base):
    __tablename__ = 'rbMSEClinicalPredict'
    __table_args__ = {'comment': 'Клинический прогноз'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEClinicalResult(Base):
    __tablename__ = 'rbMSEClinicalResult'
    __table_args__ = {'comment': 'Клинические результаты'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEConsentInform(Base):
    __tablename__ = 'rbMSEConsentInform'
    __table_args__ = {'comment': 'Способы получения уведомления о МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEDiagnosisType(Base):
    __tablename__ = 'rbMSEDiagnosisType'
    __table_args__ = {'comment': 'Тип диагноза'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEDiagnostic(Base):
    __tablename__ = 'rbMSEDiagnostic'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(Text)
    mkb = Column(Text)
    nmu = Column(Text)
    name = Column(Text)
    date = Column(Text)
    is_primary = Column(INTEGER(11))
    section = Column(INTEGER(11))


class RbMSEDisabilityPrimary(Base):
    __tablename__ = 'rbMSEDisabilityPrimary'
    __table_args__ = {'comment': 'Тип установления инвалидности'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEDisabledDate(Base):
    __tablename__ = 'rbMSEDisabledDate'
    __table_args__ = {'comment': 'Срок, на который установлена инвалидность'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEDisabledPeriod(Base):
    __tablename__ = 'rbMSEDisabledPeriod'
    __table_args__ = {'comment': 'Период инвалидности'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEDisabledReason(Base):
    __tablename__ = 'rbMSEDisabledReason'
    __table_args__ = {'comment': 'Причины инвалидности'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEDisabledReason221121(Base):
    __tablename__ = 'rbMSEDisabledReason_221121'
    __table_args__ = {'comment': 'Причины инвалидности'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEDisabledWorkDate(Base):
    __tablename__ = 'rbMSEDisabledWorkDate'
    __table_args__ = {'comment': 'Срок, на который установлена степень утраты профессиональной трудоспособности'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


t_rbMSEDocumentType = Table(
    'rbMSEDocumentType', metadata,
    Column('id', INTEGER(11)),
    Column('code', INTEGER(11)),
    Column('name', Text),
    Column('displayName', Text),
    Column('netrica_code', INTEGER(11)),
    comment='Документы, удостоверяющие личность при направлении на МСЭ'
)


class RbMSEGoal(Base):
    __tablename__ = 'rbMSEGoal'
    __table_args__ = {'comment': 'Цели направления на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEGoal221121(Base):
    __tablename__ = 'rbMSEGoal_221121'
    __table_args__ = {'comment': 'Цели направления на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEInvalidReasonList(Base):
    __tablename__ = 'rbMSEInvalidReasonList'
    __table_args__ = {'comment': 'Список заболеваний'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEMedication(Base):
    __tablename__ = 'rbMSEMedication'
    __table_args__ = {'comment': '1.2.643.5.1.13.13.99.2.611'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(250))
    name = Column(Text)
    form = Column(String(150))
    dose = Column(String(250))


class RbMSEMilitaryStatu(Base):
    __tablename__ = 'rbMSEMilitaryStatus'
    __table_args__ = {'comment': 'Воинская обязанность при направлении на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEMilitaryStatus221121(Base):
    __tablename__ = 'rbMSEMilitaryStatus_221121'
    __table_args__ = {'comment': 'Воинская обязанность при направлении на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSENosologyType(Base):
    __tablename__ = 'rbMSENosologyType'
    __table_args__ = {'comment': 'Нозология заболевания'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEPrimary(Base):
    __tablename__ = 'rbMSEPrimary'
    __table_args__ = {'comment': 'Порядок обращения на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSERehResult(Base):
    __tablename__ = 'rbMSERehResults'
    __table_args__ = {'comment': 'Результаты лечения'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSERehabilitationPotential(Base):
    __tablename__ = 'rbMSERehabilitationPotential'
    __table_args__ = {'comment': 'Реабилитационный потенциал'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSERehabilitationPredict(Base):
    __tablename__ = 'rbMSERehabilitationPredict'
    __table_args__ = {'comment': 'Реабилитационный прогноз'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSEReprAuthority(Base):
    __tablename__ = 'rbMSEReprAuthority'
    __table_args__ = {'comment': 'Документы удостоверяющие полномочия представителя'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMSESex(Base):
    __tablename__ = 'rbMSESex'
    __table_args__ = {'comment': 'Пол пациента при направлении на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11))
    name = Column(Text)
    displayName = Column(Text)


class RbMailer(Base):
    __tablename__ = 'rbMailer'
    __table_args__ = {'comment': 'Параметры email-рассылок'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(63), nullable=False)
    name = Column(String(255), nullable=False)
    host = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    port = Column(INTEGER(10), nullable=False, server_default=alchemy_text("0"))
    use_ssl = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    username = Column(String(255))
    password = Column(String(255))
    mail_from = Column(String(255))
    cc = Column(Text)
    bcc = Column(Text)


class RbMeal(Base):
    __tablename__ = 'rbMeal'
    __table_args__ = {'comment': 'Рацион'}

    id = Column(INTEGER(10), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(256), nullable=False)
    amount = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    unit = Column(String(16), nullable=False)


class RbMedicalAidKind(Base):
    __tablename__ = 'rbMedicalAidKind'
    __table_args__ = {'comment': 'Вид мед.помощи'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    federalCode = Column(String(16), nullable=False)
    netrica_Code = Column(String(64))
    typeMedCare = Column(String(10))

    createPerson = relationship('Person', primaryjoin='RbMedicalAidKind.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMedicalAidKind.modifyPerson_id == Person.id')


class RbMedicalAidProfile(Base):
    __tablename__ = 'rbMedicalAidProfile'
    __table_args__ = {'comment': 'Профили мед.помощи, исп. при выставлении счетов в СПб. Остал'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    regionalCode = Column(String(16), nullable=False)
    federalCode = Column(String(16), nullable=False)
    name = Column(String(255), nullable=False)
    netrica_Code = Column(String(64))
    netrica_Code2 = Column(String(64))
    netrica_Code3 = Column(String(64))
    netrica_CodeRehabilitation = Column(String(64))

    createPerson = relationship('Person', primaryjoin='RbMedicalAidProfile.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMedicalAidProfile.modifyPerson_id == Person.id')


class RbMedicalAidType(Base):
    __tablename__ = 'rbMedicalAidType'
    __table_args__ = {'comment': 'Тип мед.помощи'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    federalCode = Column(String(16), nullable=False)
    netrica_Code = Column(String(65))
    dispStage = Column(String(255))

    createPerson = relationship('Person', primaryjoin='RbMedicalAidType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMedicalAidType.modifyPerson_id == Person.id')


class RbMedicalUseRoute(Base):
    __tablename__ = 'rbMedicalUseRoute'
    __table_args__ = {'comment': 'Способ применения медикамента'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    name = Column(String(255))


class RbMedicinesGroup(Base):
    __tablename__ = 'rbMedicinesGroup'
    __table_args__ = {'comment': 'Справочник групп ЛС'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(50), nullable=False)
    name = Column(String(300), nullable=False)


class RbMseSpeciality(Base):
    __tablename__ = 'rbMseSpeciality'
    __table_args__ = {'comment': 'Коды специальностей по справочнику 1.2.643.5.1.13.13.11.1002'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8), nullable=False)
    name = Column(String(300), nullable=False)


class RbMseStatusIgnore(Base):
    __tablename__ = 'rbMseStatusIgnore'
    __table_args__ = {'comment': 'Исключения при обновлении статуса направления на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    status = Column(INTEGER(11))
    result = Column(Text)


class RbNet(Base):
    __tablename__ = 'rbNet'
    __table_args__ = {'comment': 'Сеть (взрослая/детская/женская)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    sex = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    age = Column(String(9), nullable=False)
    flags = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbNet.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbNet.modifyPerson_id == Person.id')


class RbNewbornState(Base):
    __tablename__ = 'rbNewbornState'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


class RbODII(Base):
    __tablename__ = 'rbODII'
    __table_args__ = {'comment': 'Федеральный справочник инструментальных диагностических исследований: 1.2.643.5.1.13.13.11.1471'}

    code = Column(INTEGER(11))
    name = Column(Text)
    region = Column(Text)
    form30code = Column(Text)
    synonym = Column(Text)
    method = Column(Text)
    location = Column(Text)
    components = Column(Text)
    imp_data = Column(Text)
    action = Column(Text)
    side = Column(Text)
    prepare = Column(Text)
    contraindications = Column(Text)
    status = Column(Text)
    NMU = Column(Text)
    RadLex = Column(Text)
    LOINC = Column(Text)
    SNOMED_CT = Column('SNOMED CT', Text)
    sort = Column(Text)
    id = Column(INTEGER(11), primary_key=True)
    SNOMED_CT1 = Column('SNOMED_CT', Text)


class RbOperationsAnatom(Base):
    __tablename__ = 'rbOperationsAnatom'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(150))
    code = Column(String(50))


class RbPaymentMedicalCare(Base):
    __tablename__ = 'rbPaymentMedicalCare'
    __table_args__ = {'comment': 'Справочник Нетрики "Источники оплаты медицинской помощи" oid: 1.2.643.5.1.13.13.11.1039'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(Text)
    code = Column(INTEGER(11))
    fullCode = Column(Text)
    form = Column(Text)
    fullName = Column(Text)
    shortName = Column(Text)
    isActual = Column(INTEGER(11))


class RbPaymentMethod(Base):
    __tablename__ = 'rbPaymentMethod'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(30))


class RbPaymentType(Base):
    __tablename__ = 'rbPaymentType'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(110))


class RbPhysicalActivityMode(Base):
    __tablename__ = 'rbPhysicalActivityMode'
    __table_args__ = {'comment': 'Справочник Режимы физической активности'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)


t_rbPo = Table(
    'rbPo', metadata,
    Column('ID', INTEGER(11)),
    Column('CREATEDATE', DateTime),
    Column('CREATEPERS', INTEGER(11)),
    Column('MODIFYDATE', DateTime),
    Column('MODIFYPERS', INTEGER(11)),
    Column('CODE', String(8)),
    Column('FLATCODE', String(32)),
    Column('NAME', String(64)),
    Column('REGIONALCO', String(8)),
    Column('FEDERALCOD', String(16)),
    Column('KEY', String(6)),
    Column('HIGH', String(6)),
    Column('SYNCGUID', String(36)),
    Column('NETRICA_CO', String(64))
)


class RbPost(Base):
    __tablename__ = 'rbPost'
    __table_args__ = {'comment': 'Должность; см. MEDPOST.DBF'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    flatCode = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    federalCode = Column(String(16), nullable=False)
    key = Column(String(6), nullable=False)
    high = Column(String(6), nullable=False)
    syncGUID = Column(String(36))
    netrica_Code = Column(String(64))
    row_code = Column(String(10))
    netrica_Code_IEMK = Column(String(64))
    netrica_ZPV = Column(String(255))
    role_code = Column(String(10))
    EGISZ_name = Column(Text)
    EGISZ_code = Column(Text)

    createPerson = relationship('Person', primaryjoin='RbPost.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbPost.modifyPerson_id == Person.id')


class RbPregnantResult(Base):
    __tablename__ = 'rbPregnantResult'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


class RbPriorityAI(Base):
    __tablename__ = 'rbPriorityAIS'
    __table_args__ = {'comment': 'Приоритет Расписаний для АИС Информ'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(Text, nullable=False, server_default=alchemy_text("''"))
    name = Column(Text, nullable=False, server_default=alchemy_text("''"))


class RbProbeCode(Base):
    __tablename__ = 'rbProbeCode'
    __table_args__ = {'comment': 'Код пробы {1.2.643.2.69.1.1.1.131}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))


class RbProbeType(Base):
    __tablename__ = 'rbProbeType'
    __table_args__ = {'comment': 'Тип пробы {1.2.643.2.69.1.1.1.134}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))


t_rbRe = Table(
    'rbRe', metadata,
    Column('ID', INTEGER(11)),
    Column('CREATEDATE', DateTime),
    Column('CREATEPERS', INTEGER(11)),
    Column('MODIFYDATE', DateTime),
    Column('MODIFYPERS', INTEGER(11)),
    Column('CODE', String(32)),
    Column('NAME', String(64)),
    Column('NETRICA_CO', String(6))
)


class RbReactionCode(Base):
    __tablename__ = 'rbReactionCode'
    __table_args__ = {'comment': 'Основные клинические проявления патологических реакций для сбора аллергоанамнеза 1.2.643.5.1.13.13.11.1063'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(250))
    netrica_Code = Column(String(250))


class RbReasonsForRefusal(Base):
    __tablename__ = 'rbReasonsForRefusal'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(50))
    name = Column(String(255))


class RbReceptionType(Base):
    __tablename__ = 'rbReceptionType'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)


class RbReferralExamType(Base):
    __tablename__ = 'rbReferralExamType'
    __table_args__ = {'comment': 'Справочник видов исследований по направлению'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    name = Column(String(64))
    netrica_group = Column(String(64))
    netrica_code = Column(String(64))
    account_code = Column(String(64))


class RbReferralOrgan(Base):
    __tablename__ = 'rbReferralOrgan'
    __table_args__ = {'comment': 'Справочник областей исследований по направлению'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    name = Column(String(128))
    NRUZ_class_A_subsection = Column(String(64))
    netrica_code = Column(String(64))
    account_code = Column(String(64))


class RbReferralTypeSPB(Base):
    __tablename__ = 'rbReferralTypeSPB'
    __table_args__ = {'comment': 'Справочник типов направлений для Спб(Заменяет обычный rbReferalType). Реализует: еис sprav_d_type_group'}

    id = Column(INTEGER(11), primary_key=True)
    createDatatime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(11), nullable=False)
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11), nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(32), nullable=False)
    groupCode = Column(String(32), nullable=False)
    name = Column(String(256), nullable=False)
    groupName = Column(String(256), nullable=False)
    cnt_min = Column(INTEGER(11), nullable=False)
    cnt_max = Column(INTEGER(11), nullable=False)
    visibility = Column(TINYINT(1), server_default=alchemy_text("1"))


class RbResultIEMK(Base):
    __tablename__ = 'rbResultIEMK'
    __table_args__ = {'comment': 'Классификатор исходов заболеваний {1.2.643.5.1.13.2.1.1.122}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(10))
    name = Column(String(255))


class RbScale(Base):
    __tablename__ = 'rbScales'
    __table_args__ = {'comment': 'Таблица Шкал'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11), nullable=False)
    name = Column(String(30), nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isFree = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))


class RbService(Base):
    __tablename__ = 'rbService'
    __table_args__ = {'comment': 'Услуга (профиль ЕИС)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    group_id = Column(ForeignKey('rbServiceGroup.id', ondelete='SET NULL', onupdate='CASCADE'))
    code = Column(String(31), nullable=False)
    name = Column(String(255), nullable=False)
    eisLegacy = Column(TINYINT(1), nullable=False)
    nomenclatureLegacy = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    license = Column(TINYINT(1), nullable=False)
    infis = Column(String(31), nullable=False)
    begDate = Column(Date, nullable=False, server_default=alchemy_text("'2000-01-01'"))
    endDate = Column(Date, nullable=False, server_default=alchemy_text("'2200-01-01'"))
    medicalAidProfile_id = Column(ForeignKey('rbMedicalAidProfile.id', ondelete='SET NULL'))
    medicalAidKind_id = Column(ForeignKey('rbMedicalAidKind.id', ondelete='SET NULL'))
    medicalAidType_id = Column(ForeignKey('rbMedicalAidType.id', ondelete='SET NULL'))
    adultUetDoctor = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    adultUetAverageMedWorker = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    childUetDoctor = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    childUetAverageMedWorker = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    qualityLevel = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("1"))
    superviseComplexityFactor = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("1"))
    dopService_id = Column(INTEGER(11))
    category_id = Column(INTEGER(11))
    caseCast_id = Column(ForeignKey('rbCaseCast.id', onupdate='CASCADE'))
    netrica_Code = Column(String(65))
    Fed_code = Column(String(30))
    NMU_code = Column(String(16))
    EGISZ_name = Column(Text)
    EGISZ_code = Column(String(16))

    caseCast = relationship('RbCaseCast')
    createPerson = relationship('Person', primaryjoin='RbService.createPerson_id == Person.id')
    group = relationship('RbServiceGroup')
    medicalAidKind = relationship('RbMedicalAidKind')
    medicalAidProfile = relationship('RbMedicalAidProfile')
    medicalAidType = relationship('RbMedicalAidType')
    modifyPerson = relationship('Person', primaryjoin='RbService.modifyPerson_id == Person.id')


class RbService20200416(Base):
    __tablename__ = 'rbService20200416'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    name = Column(String(250))
    EU = Column(String(80))
    count = Column(INTEGER(11))
    sum_ch = Column(Float(asdecimal=True))
    sum_v = Column(Float(asdecimal=True))
    caseCast = Column(INTEGER(11))


class RbServiceGroup(Base):
    __tablename__ = 'rbServiceGroup'
    __table_args__ = {'comment': 'Группы услуг'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    regionalCode = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(64), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbServiceGroup.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbServiceGroup.modifyPerson_id == Person.id')


class RbServiceProfileCopy(Base):
    __tablename__ = 'rbService_Profile_copy'
    __table_args__ = {'comment': 'Профили мед.помощи, применяемые в зависимости от обстоятельс'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(INTEGER(11), nullable=False)
    speciality_id = Column(INTEGER(11))
    sex = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    age = Column(String(255), nullable=False, server_default=alchemy_text("''''''"))
    mkbRegExp = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    medicalAidProfile_id = Column(INTEGER(11))
    medicalAidKind_id = Column(INTEGER(11))
    medicalAidType_id = Column(INTEGER(11))
    eventProfile_id = Column(INTEGER(11))


t_rbSoc = Table(
    'rbSoc', metadata,
    Column('ID', INTEGER(11)),
    Column('CREATEDATE', DateTime),
    Column('CREATEPERS', INTEGER(11)),
    Column('MODIFYDATE', DateTime),
    Column('MODIFYPERS', INTEGER(11)),
    Column('CODE', String(8)),
    Column('NAME', String(250)),
    Column('SOCCODE', String(8)),
    Column('REGIONALCO', String(8)),
    Column('DOCUMENTTY', INTEGER(11)),
    Column('NETRICA_CO', String(64))
)


t_rbSp = Table(
    'rbSp', metadata,
    Column('ID', INTEGER(11)),
    Column('CREATEDATE', DateTime),
    Column('CREATEPERS', INTEGER(11)),
    Column('MODIFYDATE', DateTime),
    Column('MODIFYPERS', INTEGER(11)),
    Column('CODE', String(8)),
    Column('NAME', String(64)),
    Column('OKSONAME', String(60)),
    Column('OKSOCODE', String(8)),
    Column('FEDERALCOD', String(16)),
    Column('SERVICE_ID', INTEGER(11)),
    Column('PROVINCESE', INTEGER(11)),
    Column('OTHERSERVI', INTEGER(11)),
    Column('SEX', INTEGER(4)),
    Column('AGE', String(9)),
    Column('MKBFILTER', String(32)),
    Column('REGIONALCO', String(16)),
    Column('SHORTNAME', String(64)),
    Column('VERSSPEC', String(8)),
    Column('SYNCGUID', String(36)),
    Column('NETRICA_CO', String(64)),
    Column('FUNDINGSER', INTEGER(11))
)


class RbSpeciality(Base):
    __tablename__ = 'rbSpeciality'
    __table_args__ = {'comment': 'Специальности врачей; можно взять из ЕИС ОМС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    OKSOName = Column(String(60), nullable=False)
    OKSOCode = Column(String(8), nullable=False)
    federalCode = Column(String(16), nullable=False)
    service_id = Column(ForeignKey('rbService.id'))
    provinceService_id = Column(ForeignKey('rbService.id', ondelete='SET NULL', onupdate='CASCADE'))
    otherService_id = Column(ForeignKey('rbService.id', ondelete='SET NULL', onupdate='CASCADE'))
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    mkbFilter = Column(String(32), nullable=False)
    regionalCode = Column(String(16), nullable=False)
    shortName = Column(String(64))
    versSpec = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    syncGUID = Column(String(36))
    netrica_Code = Column(String(64))
    fundingService_id = Column(ForeignKey('rbService.id', onupdate='CASCADE'))
    shouldFillOncologyForm90 = Column(TINYINT(1), server_default=alchemy_text("0"))
    queueShareMode = Column(TINYINT(1), server_default=alchemy_text("0"))
    oldCode = Column(INTEGER(15))
    kind = Column(INTEGER(11), server_default=alchemy_text("0"))
    EGISZ_code = Column(String(255))
    EGISZ_name = Column(String(255))

    createPerson = relationship('Person', primaryjoin='RbSpeciality.createPerson_id == Person.id')
    fundingService = relationship('RbService', primaryjoin='RbSpeciality.fundingService_id == RbService.id')
    modifyPerson = relationship('Person', primaryjoin='RbSpeciality.modifyPerson_id == Person.id')
    otherService = relationship('RbService', primaryjoin='RbSpeciality.otherService_id == RbService.id')
    provinceService = relationship('RbService', primaryjoin='RbSpeciality.provinceService_id == RbService.id')
    service = relationship('RbService', primaryjoin='RbSpeciality.service_id == RbService.id')


class RbSpecialityV004(Base):
    __tablename__ = 'rbSpecialityV004'
    __table_args__ = {'comment': 'Специальности врачей; можно взять из ЕИС ОМС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    OKSOName = Column(String(60), nullable=False)
    OKSOCode = Column(String(8), nullable=False)
    federalCode = Column(String(16), nullable=False)
    service_id = Column(INTEGER(11))
    provinceService_id = Column(INTEGER(11))
    otherService_id = Column(INTEGER(11))
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    mkbFilter = Column(String(32), nullable=False)
    regionalCode = Column(String(16), nullable=False)
    shortName = Column(String(64))
    versSpec = Column(String(8), nullable=False, server_default=alchemy_text("''"))


class RbStockNomenclature(Base):
    __tablename__ = 'rbStockNomenclature'
    __table_args__ = {'comment': 'Номенклатура лекарственных средств'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    _class = Column('class', INTEGER(11), nullable=False)
    type = Column(INTEGER(11), nullable=False)
    code = Column(String(128), nullable=False)
    name = Column(String(255), nullable=False)
    characteristic = Column(String(127))
    kind = Column(String(127))
    article = Column(String(127))
    storage = Column(String(255))
    mnn = Column(String(255))
    issueForm = Column(String(127), nullable=False)
    concentration = Column(String(50), nullable=False)
    atc = Column(String(255), nullable=False)
    pku = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    baseUnit_id = Column(INTEGER(11), nullable=False)
    minIndivisibleUnit_id = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    packingUnit_id = Column(INTEGER(11), nullable=False)
    baseUnitsInMinIndivisibleUnit = Column(Float(asdecimal=True), nullable=False)
    minIndivisibleUnitsInPackingUnit = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("1"))
    codeRls = Column(INTEGER(11))
    shelfTime = Column(Date, nullable=False)
    deleted = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))


class RbStockNomenclatureConversion(Base):
    __tablename__ = 'rbStockNomenclatureConversion'

    id = Column(INTEGER(11), primary_key=True)
    nomenclature_id = Column(INTEGER(11), nullable=False)
    source_unit_id = Column(INTEGER(11), nullable=False)
    target_unit_id = Column(INTEGER(11), nullable=False)
    coefficient = Column(Float, nullable=False, server_default=alchemy_text("1"))


class RbStockNomenclatureGroup(Base):
    __tablename__ = 'rbStockNomenclatureGroup'
    __table_args__ = {'comment': 'Группы товаров в номенклатуре'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(128), nullable=False)
    name = Column(String(255), nullable=False)
    expirationDate = Column(Date, nullable=False)


class RbStopMonitoringReason(Base):
    __tablename__ = 'rbStopMonitoringReason'
    __table_args__ = {'comment': 'Справочник для причин прекращения наблюдения'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)


class RbTariffCategory(Base):
    __tablename__ = 'rbTariffCategory'
    __table_args__ = {'comment': 'Тарифная категория'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    federalCode = Column(String(16), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTariffCategory.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTariffCategory.modifyPerson_id == Person.id')


class RbTextDataCompleter(Base):
    __tablename__ = 'rbTextDataCompleter'
    __table_args__ = {'comment': 'Справочник для автозавершения текстовых полей'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(128), nullable=False)
    name = Column(String(256), nullable=False)


class RbThesaurus1(Base):
    __tablename__ = 'rbThesaurus1'

    Column1 = Column(String(255))
    id = Column(INTEGER(11), primary_key=True)


class RbTimeQuotingType(Base):
    __tablename__ = 'rbTimeQuotingType'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)


class RbTmRoleProfile(Base):
    __tablename__ = 'rbTmRoleProfile'
    __table_args__ = {'comment': 'Телемедицинская роль'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(50), nullable=False)
    name = Column(String(128), nullable=False)


class RbToothSectionState(Base):
    __tablename__ = 'rbToothSectionState'
    __table_args__ = {'comment': 'Состояние поверхностей зубов'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(32))
    flatCode = Column(String(32))
    name = Column(String(256))
    wholeTooth = Column(TINYINT(1))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))


class RbToothStatu(Base):
    __tablename__ = 'rbToothStatus'
    __table_args__ = {'comment': 'Статусы зубов для зубной формулы'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(32))
    name = Column(String(256), nullable=False)
    color = Column(String(10))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))


class RbTumorState(Base):
    __tablename__ = 'rbTumorState'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


class RbUserProfile(Base):
    __tablename__ = 'rbUserProfile'
    __table_args__ = {'comment': 'Профили пользователей'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbUserProfile.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbUserProfile.modifyPerson_id == Person.id')


class RbVaccineReaction(Base):
    __tablename__ = 'rbVaccineReaction'
    __table_args__ = {'comment': 'Реакция на вакцину {1.2.643.2.69.1.1.1.171}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))


t_rbVimisDiagnosis = Table(
    'rbVimisDiagnosis', metadata,
    Column('id', INTEGER(11), nullable=False),
    Column('mkbTree_id', INTEGER(11), nullable=False),
    Column('type', String(10))
)


class RbVitalParam(Base):
    __tablename__ = 'rbVitalParams'
    __table_args__ = {'comment': 'Справочник Витальные параметры'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11), nullable=False)
    name = Column(String(256), nullable=False)
    possible_values = Column(String(256))
    dict_OID = Column(String(64))


class RbWithdrawalReason(Base):
    __tablename__ = 'rbWithdrawalReason'
    __table_args__ = {'comment': 'Причина отвода {1.2.643.2.69.1.1.1.132}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))


class RbWithdrawalType(Base):
    __tablename__ = 'rbWithdrawalType'
    __table_args__ = {'comment': 'Тип отвода {1.2.643.2.69.1.1.1.133}'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20))
    name = Column(String(500))


class RbZNOClinicalGroup(Base):
    __tablename__ = 'rbZNOClinicalGroups'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(16))
    name = Column(String(128))


t_rb_insurance_companies2 = Table(
    'rb_insurance_companies2', metadata,
    Column('miacCode', String(10), nullable=False),
    Column('fullName', String(250), nullable=False),
    Column('infisCode', String(12), nullable=False)
)


class Rbd(Base):
    __tablename__ = 'rbd'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    event_purpose_id = Column(INTEGER(11))
    code = Column(String(8))
    name = Column(String(64))
    continued = Column(INTEGER(11))
    regional_code = Column(String(8))
    federal_code = Column(String(8))
    result_id = Column(INTEGER(11))
    begDate = Column(DateTime)
    endDate = Column(DateTime)
    filter_result = Column(INTEGER(11))
    netrica_code = Column(String(8))


class Rbdi(Base):
    __tablename__ = 'rbdi'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8))
    regional_code = Column(String(8))
    name = Column(String(64))
    group_id = Column(INTEGER(11))
    serial_for = Column(INTEGER(11))
    number_for = Column(INTEGER(11))
    federal_code = Column(String(8))
    soc_code = Column(String(8))
    doctemplate = Column(String(64))
    used_index = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    isdefault = Column(INTEGER(11))
    isforeigne = Column(INTEGER(11))
    netrica_code = Column(String(8))
    Column4 = Column(INTEGER(11))


class Rbmed(Base):
    __tablename__ = 'rbmed'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8))
    name = Column(String(120))
    descr = Column(String(120))
    regional_code = Column(String(8))
    federal_code = Column(String(8))
    begDate = Column(DateTime)
    endDate = Column(DateTime)
    netrica_code = Column(String(8))


t_rbmedaidprof = Table(
    'rbmedaidprof', metadata,
    Column('id', INTEGER(11)),
    Column('createDatetime', DateTime),
    Column('createPerson_id', String(255)),
    Column('modifyDatetime', DateTime),
    Column('modifyPerson_id', String(255)),
    Column('code', INTEGER(11)),
    Column('regionalCode', INTEGER(11)),
    Column('federalCode', INTEGER(11)),
    Column('name', String(100)),
    Column('netrica_Code', INTEGER(11)),
    Column('netrica_Code2', INTEGER(11)),
    Column('netrica_Code3', INTEGER(11))
)


class Rbmede(Base):
    __tablename__ = 'rbmede'
    __table_args__ = {'comment': 'Вид мед. помощи'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8))
    name = Column(String(120))
    regional_code = Column(String(8))
    federal_code = Column(String(8))
    netrica_code = Column(String(8))
    netrica_code1 = Column(String(8))


t_rbmedicalaidprofile1 = Table(
    'rbmedicalaidprofile1', metadata,
    Column('id', Float(10, True)),
    Column('createDatetime', DateTime),
    Column('createPerson_id', String(255)),
    Column('modifyDatetime', DateTime),
    Column('modifyPerson_id', Float(10, True)),
    Column('code', String(255)),
    Column('regionalCode', String(255)),
    Column('federalCode', String(255)),
    Column('name', String(255)),
    Column('netrica_Code', String(255))
)


class Rbmedt(Base):
    __tablename__ = 'rbmedt'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8))
    name = Column(String(120))
    regional_code = Column(String(8))
    federal_code = Column(String(8))
    dispStage = Column(INTEGER(11))
    netrica_code = Column(String(8))
    netrica_code1 = Column(String(8))


class Rbme(Base):
    __tablename__ = 'rbmes'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8))
    regional_code = Column(String(8))
    name = Column(String(120))
    done = Column(INTEGER(11))
    netrica_code = Column(String(8))


class Rbreal(Base):
    __tablename__ = 'rbreal'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8))
    left_name = Column(String(120))
    right_name = Column(String(120))
    isDirectGe = Column(INTEGER(11))
    isBackWard = Column(INTEGER(11))
    isDirectRe = Column(INTEGER(11))
    isBackWard1 = Column(INTEGER(11))
    isDirectP = Column(INTEGER(11))
    isBackWard2 = Column(INTEGER(11))
    isDirectDo = Column(INTEGER(11))
    isBackWard3 = Column(INTEGER(11))
    left_sex = Column(INTEGER(11))
    right_sex = Column(INTEGER(11))
    regional_code = Column(String(8))
    regional_re = Column(String(8))
    netrica_code = Column(String(8))


class Rbre(Base):
    __tablename__ = 'rbres'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    event_purpose_id = Column(INTEGER(11))
    code = Column(String(8))
    name = Column(String(120))
    continued = Column(INTEGER(11))
    isDeath = Column(INTEGER(11))
    regional_code = Column(String(8))
    federal_code = Column(String(8))
    notAccount = Column(INTEGER(11))
    counter_id = Column(INTEGER(11))
    begDate = Column(DateTime)
    endDate = Column(DateTime)
    netrica_code = Column(String(8))


t_rbresult1 = Table(
    'rbresult1', metadata,
    Column('id', Float(10, True)),
    Column('createDatetime', DateTime),
    Column('createPerson_id', String(255)),
    Column('modifyDatetime', DateTime),
    Column('modifyPerson_id', String(255)),
    Column('eventPurpose_id', Float(10, True)),
    Column('code', String(255)),
    Column('name', String(255)),
    Column('continued', Float(10, True)),
    Column('regionalCode', String(255)),
    Column('federalCode', String(255)),
    Column('notAccount', Float(10, True)),
    Column('counter_id', String(255)),
    Column('begDate', DateTime),
    Column('endDate', DateTime),
    Column('netrica_Code', String(255)),
    Column('attachType', String(255)),
    Column('socStatusClass', String(255)),
    Column('socStatusType', String(255)),
    Column('isDeath', Float(10, True))
)


class Rbscen(Base):
    __tablename__ = 'rbscen'
    __table_args__ = {'comment': 'Место выполнения визита, Классификатор мест обслуживания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    serviceModifier = Column(String(128))
    netrica_Code = Column(String(65))


class Rbso(Base):
    __tablename__ = 'rbso'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    code = Column(String(8))
    name = Column(String(200))
    soc_code = Column(String(8))
    regional_code = Column(String(8))
    federal_code = Column(String(8))
    document_type = Column(INTEGER(11))
    netrica_code = Column(String(8))
    netrica_code1 = Column(String(8))


t_rbspecNew = Table(
    'rbspecNew', metadata,
    Column('ID_PRVS', Float(10, True)),
    Column('PRVS_CODE', String(255)),
    Column('PRVS_NAME', String(255)),
    Column('DATE_BEGIN', DateTime),
    Column('DATE_END', DateTime)
)


class Rbun(Base):
    __tablename__ = 'rbun'
    __table_args__ = {'comment': 'Единицы измерения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    netrica_Code = Column(String(65))


class RcConditionType(Base):
    __tablename__ = 'rcConditionType'
    __table_args__ = {'comment': 'Тип Условия для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    name = Column(String(20), nullable=False, server_default=alchemy_text("''"))
    sign = Column(String(20), nullable=False)
    code = Column(String(20), nullable=False)


class RcFunction(Base):
    __tablename__ = 'rcFunction'
    __table_args__ = {'comment': 'Функции в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    function = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    description = Column(Text)
    hasSpace = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))


class RcParamType(Base):
    __tablename__ = 'rcParamType'
    __table_args__ = {'comment': 'Тип параметра для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(50), nullable=False, server_default=alchemy_text("''"))


class RcTable(Base):
    __tablename__ = 'rcTable'
    __table_args__ = {'comment': 'Таблицы в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    name = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    table = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    description = Column(Text)
    visible = Column(TINYINT(1), server_default=alchemy_text("1"))
    group = Column(String(265), server_default=alchemy_text("''"))


class RcValueType(Base):
    __tablename__ = 'rcValueType'
    __table_args__ = {'comment': 'Тип Значения для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(20), nullable=False, server_default=alchemy_text("''"))
    code = Column(String(20), nullable=False)


class RdFirstName(Base):
    __tablename__ = 'rdFirstName'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(20), nullable=False)
    sex = Column(TINYINT(1), nullable=False)


class RdPOLIS(Base):
    __tablename__ = 'rdPOLIS_S'

    id = Column(INTEGER(11), primary_key=True)
    CODE = Column(String(10), nullable=False)
    PAYER = Column(String(5), nullable=False)
    TYPEINS = Column(String(1), nullable=False)


class RdPatrName(Base):
    __tablename__ = 'rdPatrName'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(20), nullable=False)
    sex = Column(TINYINT(1), nullable=False)


class ReasonsForRefusingHospitalization(Base):
    __tablename__ = 'reasons_for_refusing_hospitalization'
    __table_args__ = {'comment': 'Причины отказов в госпитализации (1.2.643.5.1.13.13.11.1497) v3.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    SYSTEM = Column(INTEGER(11))


class RecipeExecutionPriority(Base):
    __tablename__ = 'recipe_execution_priority'
    __table_args__ = {'comment': 'Приоритет исполнения рецепта (1.2.643.5.1.13.13.99.2.609) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    Priority = Column(String(50))
    Priority_Latin = Column(String(50))
    Comments = Column(String(256))


class RecipeValidityPeriod(Base):
    __tablename__ = 'recipe_validity_period'
    __table_args__ = {'comment': ' \tСрок действия рецепта (1.2.643.5.1.13.13.99.2.608) v1.2'}

    ID = Column(INTEGER(11), primary_key=True)
    Period = Column(String(50))


class ReferralMse(Base):
    __tablename__ = 'referral_mse'

    id = Column(INTEGER(11), primary_key=True)
    fio = Column(String(300))
    age = Column(INTEGER(11))
    birthDate = Column(DateTime)
    sex = Column(String(2))
    citizenship = Column(String(100))
    militaryStatus = Column(String(200))
    addressCountry = Column(String(200))
    addressArea = Column(String(200))
    addressCity = Column(String(200))
    addressSubject = Column(String(200))
    addressHouse = Column(String(100))
    addressFlat = Column(INTEGER(11))
    addressIndex = Column(INTEGER(11))
    addressBOMJ = Column(TINYINT(1), server_default=alchemy_text("0"))
    locationOrg = Column(String(5))
    locationOGRN = Column(String(20))
    locationAddr = Column(String(300))
    contactPhone = Column(String(20))
    contactEmail = Column(String(100))
    client_id = Column(INTEGER(11))
    documentSNILS = Column(String(20))
    documentType = Column(String(100))
    documentSerial = Column(String(10))
    documentNumber = Column(String(20))
    documentInsWho = Column(String(300))
    documentInsDate = Column(Date)
    isRepresentative = Column(TINYINT(4))
    representativeFIO = Column(String(300))
    representativeBirthDate = Column(Date)
    representativeUdDocumentType = Column(String(100))
    representativeUdDocumentNumber = Column(String(50))
    representativeUdDocumentSerial = Column(String(10))
    representativeUdDocumentInsWho = Column(String(300))
    representativeUdDocumentInsDate = Column(Date)
    representativeDocumentType = Column(String(100))
    representativeDocumentSerial = Column(String(10))
    representativeDocumentNumber = Column(String(50))
    representativeDocumentInsDate = Column(Date)
    representativeDocumentInsWho = Column(String(300))
    representativeContactsPhone = Column(String(100))
    representativeContactsEmail = Column(String(100))
    representativeContactsSNILS = Column(String(50))
    representativeOrgName = Column(String(300))
    representativeOrgAddress = Column(String(300))
    representativeOrgOGRN = Column(String(50))
    isEducation = Column(TINYINT(1))
    educationOrgName = Column(String(300))
    educationOrgAddress = Column(String(300))
    educationLevel = Column(String(50))
    educationLevelVal = Column(String(50))
    educationSpeciality = Column(String(100))
    isWorking = Column(TINYINT(1))
    workingOrgName = Column(String(300))
    workingOrgAddress = Column(String(300))
    workingSpeciality = Column(String(300))
    workingQualification = Column(String(100))
    workingExp = Column(Float(asdecimal=True))
    workingCharacter = Column(String(300))
    protocolNumber = Column(String(100))
    protocolDate = Column(Date)
    protocolReferralDate = Column(Date)
    protocolReferralGoal = Column(String(50))
    otherGoals = Column(String(300))
    mseAtHome = Column(TINYINT(1))
    pallatativeMedicalCare = Column(TINYINT(1))
    anamnesisWeight = Column(String(10))
    anamnesisIndex = Column(String(10))
    anamnesisHeight = Column(String(10))
    anamnesisBodyType = Column(String(30))
    anamnesisHips = Column(String(30))
    anamnesisWaist = Column(String(30))
    anamnesisDailyVal = Column(String(30))
    anamnesisPhysics = Column(String(50))
    anamnesisChildWeight = Column(String(10))
    primaryMSE = Column(String(100))
    isPrevMSE = Column(TINYINT(1))
    prevMSEresults = Column(String(300))
    isVUT = Column(TINYINT(1))
    VUTresults = Column(String(300))
    clinicMedOrganisation = Column(String(100))
    clinicSickList = Column(MEDIUMTEXT)
    clinicAnamnesisVitae = Column(MEDIUMTEXT)
    clinicClientCondition = Column(MEDIUMTEXT)
    clinicDiagnosticInfo = Column(MEDIUMTEXT)
    clinisDiagnosis = Column(String(300))
    clinicClinicalPrediction = Column(String(100))
    clinicReaPrediction = Column(String(50))
    clinicReaPotential = Column(String(50))
    clinicRecommendationsReabilitation = Column(MEDIUMTEXT)
    clinicRecommendationsRecSurgery = Column(MEDIUMTEXT)
    clinicRecommendationsProtes = Column(MEDIUMTEXT)
    clinicHealthResTreatment = Column(MEDIUMTEXT)
    result = Column(String(200))
    send_in_iemk = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(INTEGER(11))
    firstName = Column(String(100))
    lastName = Column(String(100))
    patrName = Column(String(100))
    rec_org_id = Column(INTEGER(11))
    result_achievement = Column(INTEGER(11))
    result_number = Column(String(30))
    result_mse_number = Column(String(30))
    result_date = Column(Date)
    result_text = Column(String(4000))
    person_id = Column(INTEGER(11))
    addressStreet = Column(String(100))
    documentType_code = Column(String(20))
    signedByPerson = Column(TINYINT(1), server_default=alchemy_text("0"))
    signedByMO = Column(TINYINT(1), server_default=alchemy_text("0"))
    REMDStatus = Column(Text)
    REMDId = Column(String(20))
    otherContactPhone = Column(String(20))
    elnNumber = Column(String(20))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    work = Column(Text)
    locationAddrKLADR = Column(String(64))
    representativeOrgAddressKLADR = Column(String(64))
    workingOrgAddressKLADR = Column(String(64))
    medical_devices = Column(Text)
    special_care = Column(Text)
    client_complaints = Column(Text)
    client_policy = Column(Text)
    version_mse = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    consent_inform = Column(INTEGER(11))
    PatientAgreementReferral = Column(TINYINT(1), nullable=False)
    PatientAgreementForm = Column(TINYINT(1))
    PatientAgreementInformWay = Column(TINYINT(1))
    PatientAgreementInformWayText = Column(String(200))
    consentDate = Column(Date)
    org_id = Column(INTEGER(11))
    remd_status = Column(String(128), server_default=alchemy_text("''"))
    REMDMsg = Column(Text)
    invalid = Column(INTEGER(11))
    invalid_kind = Column(INTEGER(11))
    disabled_date = Column(INTEGER(11))
    invalid_period = Column(INTEGER(11))
    invalid_reason = Column(INTEGER(11))
    date_invalid = Column(Date)
    need_protesis = Column(INTEGER(11))
    consent_date = Column(DateTime)
    preferred_form = Column(INTEGER(11))
    receiving_notification_methods = Column(String(128))
    version_mkb = Column(TINYINT(1), server_default=alchemy_text("0"))
    addressLitera = Column(String(10))
    addressCorpus = Column(String(50))


class ReferralMseDiagnosi(Base):
    __tablename__ = 'referral_mse_diagnosis'
    __table_args__ = {'comment': 'Диагноз МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    main_diagnosis = Column(LONGTEXT)
    mkb = Column(String(10))
    main_complications = Column(Text)
    deleted = Column(TINYINT(4), server_default=alchemy_text("0"))
    type = Column(INTEGER(11), server_default=alchemy_text("0"))


class ReferralMseDiagnostic(Base):
    __tablename__ = 'referral_mse_diagnostic'

    id = Column(INTEGER(11), primary_key=True)
    diagnostic_id = Column(INTEGER(11))
    date = Column(Date)
    result = Column(Text)
    master_id = Column(INTEGER(11))
    deleted = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))


class ReferralMseMedication(Base):
    __tablename__ = 'referral_mse_medication'

    id = Column(INTEGER(11), primary_key=True)
    medication_id = Column(INTEGER(11))
    duration = Column(Text)
    treatment_frequency = Column(Text)
    reception_frequency = Column(Text)
    master_id = Column(INTEGER(11))
    deleted = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))


class ReferralMsePerson(Base):
    __tablename__ = 'referral_mse_person'
    __table_args__ = {'comment': 'Члены врачебной комиссии'}

    id = Column(INTEGER(11), primary_key=True)
    referral_mse_id = Column(INTEGER(11))
    person_id = Column(INTEGER(11))


class ReferralMseRepeat(Base):
    __tablename__ = 'referral_mse_repeat'
    __table_args__ = {'comment': 'Сведения о резульатах предыдущей МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    date_invalid = Column(Date)
    invalid = Column(String(64))
    invalid_period = Column(String(64), server_default=alchemy_text("'0'"))
    invalid_reason = Column(String(200), server_default=alchemy_text("'0'"))
    invalid_missing = Column(String(64))
    invalid_time = Column(String(64))
    invalid_date = Column(Date)
    invalid_grade = Column(String(64))
    deleted = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    invalid_kind = Column(INTEGER(11))
    disabled_date = Column(INTEGER(11))


class ReferralMseSign(Base):
    __tablename__ = 'referral_mse_sign'
    __table_args__ = {'comment': 'Подписи врачей направлений на МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    referral_mse_id = Column(INTEGER(11), nullable=False)
    person_id = Column(INTEGER(11))
    sign_date = Column(Date)
    is_vk = Column(TINYINT(1))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    file_id = Column(INTEGER(11))
    sign_id = Column(INTEGER(11))


class ReferralMseTempInvalid(Base):
    __tablename__ = 'referral_mse_temp_invalid'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(INTEGER(11))
    begDate = Column(Date)
    endDate = Column(Date)
    duration = Column(INTEGER(11))
    mkb = Column(String(5))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    number = Column(String(64))
    eln = Column(TINYINT(4))


class RelationshipType(Base):
    __tablename__ = 'relationship_type'
    __table_args__ = {'comment': 'Тип родственной связи (1.2.643.5.1.13.13.11.1021) v1.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)


class RemdCallback(Base):
    __tablename__ = 'remd_callback'

    id = Column(INTEGER(11), primary_key=True)
    recieved = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    document_type_name = Column(String(128))
    document_id = Column(INTEGER(11))
    document_type = Column(INTEGER(11))
    status = Column(String(64))
    message = Column(Text)
    fed_request_id = Column(String(256))
    remd_reg_number = Column(String(256))


t_ren = Table(
    'ren', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class ResidenceType(Base):
    __tablename__ = 'residence_type'
    __table_args__ = {'comment': 'Вид места жительства (1.2.643.5.1.13.13.11.1042) v3.2'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    SYNONYM = Column(Text)


class ResultsInterpretationCode(Base):
    __tablename__ = 'results_interpretation_codes'
    __table_args__ = {'comment': 'Справочник кодов интерпретации результатов (1.2.643.5.1.13.13.99.2.257) v1.1'}

    id = Column(INTEGER(11), primary_key=True)
    CODE = Column(Text)
    NAME = Column(Text)
    ORDER = Column(INTEGER(11))


class Riskfactor(Base):
    __tablename__ = 'riskfactors'

    id = Column(INTEGER(10), primary_key=True)
    createDatetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    eventId = Column(INTEGER(10))
    R03_0 = Column(TINYINT(1))
    R73_9 = Column(TINYINT(1))
    R63_5 = Column(TINYINT(1))
    Z72_0 = Column(TINYINT(1))
    Z72_1 = Column(TINYINT(1))
    Z72_2 = Column(TINYINT(1))
    Z72_3 = Column(TINYINT(1))
    Z72_4 = Column(TINYINT(1))
    Z80_83 = Column(TINYINT(1))
    absoluterisk = Column(TINYINT(1))
    relativerisk = Column(TINYINT(1))
    E78 = Column(TINYINT(1))
    E66 = Column(TINYINT(1))
    R54 = Column(TINYINT(1))


class RussianFederationSubject(Base):
    __tablename__ = 'russian_federation_subjects'
    __table_args__ = {'comment': 'Субъекты Российской Федерации (1.2.643.5.1.13.13.99.2.206) v6.4'}

    ID = Column(INTEGER(11), primary_key=True)
    SUBJECT = Column(Text)
    CODE_OKATO = Column(INTEGER(11))
    STATUS = Column(Text)
    OKATO_5 = Column(INTEGER(11))
    CODE_FNS = Column(INTEGER(11))
    SYNONYM = Column(Text)
    FED = Column(Float(asdecimal=True))


t_saq = Table(
    'saq', metadata,
    Column('Column1', String(255)),
    Column('Column2', String(255)),
    Column('Column3', String(255)),
    Column('Column4', String(255)),
    Column('Column5', String(255)),
    Column('Column6', String(255)),
    Column('Column7', String(255)),
    Column('Column8', String(255)),
    Column('Column9', String(255)),
    Column('Column10', String(255)),
    Column('Column11', String(255)),
    Column('Column12', String(255)),
    Column('Column13', String(255)),
    Column('Column14', String(255)),
    Column('Column15', String(255)),
    Column('Column16', String(255)),
    Column('Column17', String(255)),
    Column('Column18', String(255)),
    Column('Column19', String(255)),
    Column('Column20', String(255)),
    Column('Column21', String(255)),
    Column('Column22', String(255)),
    Column('Column23', String(255)),
    Column('Column24', String(255)),
    Column('Column25', String(255)),
    Column('Column26', String(255)),
    Column('Column27', String(255)),
    Column('Column28', String(255)),
    Column('Column29', String(255)),
    Column('Column30', String(255)),
    Column('Column31', String(255)),
    Column('Column32', String(255)),
    Column('Column33', String(255)),
    Column('Column34', String(255))
)


class SmnnNode(Base):
    __tablename__ = 'smnn_nodes'
    __table_args__ = {'comment': 'Узлы СМНН. ЕСКЛП (1.2.643.5.1.13.13.99.2.611) v4.114'}

    ID = Column(INTEGER(11), primary_key=True)
    SMNN_CODE = Column(Text)
    STANDARD_INN = Column(Text)
    STANDARD_FORM = Column(Text)
    STANDARD_DOZE = Column(Text)
    KTRU_CODE = Column(Text)
    NAME_UNIT = Column(Text)
    OKEI_CODE = Column(INTEGER(11))
    OKPD_2_CODE = Column(Text)
    ESSENTIAL_MEDICINES = Column(Text)
    NARCOTIC_PSYCHOTROPIC = Column(Text)
    CODE_ATC = Column(Text)
    NAME_ATC = Column(Text)
    TN = Column(Text)


t_smo = Table(
    'smo', metadata,
    Column('ID_SMO_REG', INTEGER(11)),
    Column('SMO_S_NAME', String(50)),
    Column('SMO_L_NAME', String(200)),
    Column('NAME_TER', String(50)),
    Column('TER_CODE', INTEGER(11))
)


class SmpCar(Base):
    __tablename__ = 'smpCars'
    __table_args__ = {'comment': 'Машины скорой помощи'}

    id = Column(INTEGER(11), primary_key=True)
    number = Column(VARCHAR(16), nullable=False)


class SmpWorkServicesType(Base):
    __tablename__ = 'smp_work_services_type'
    __table_args__ = {'comment': 'СМП. Справочник видов работ и услуг (1.2.643.5.1.13.13.99.2.706) v1.6'}

    id = Column(INTEGER(11), primary_key=True)
    parent = Column(INTEGER(11))
    name = Column(String(128))


class SocialPopulationGroup(Base):
    __tablename__ = 'social_population_groups'
    __table_args__ = {'comment': 'Социальные группы населения в учетной медицинской документации (1.2.643.5.1.13.13.11.1038) v13.2'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(String(64))
    BASE = Column(String(64))
    F_025u = Column(INTEGER(11))
    NAME_F_025u = Column(String(64))
    F_025_1u = Column('F_025-1u', INTEGER(11))
    NAME_F_025_1u_ = Column('NAME_F_025-1u,', String(50))
    F_025u_VMP = Column('F_025u-VMP', INTEGER(11))
    NAME_F_025u_VMP = Column('NAME_F_025u-VMP', String(50))
    F_103u = Column(INTEGER(11))
    NAME_F_103u = Column(String(50))
    F_106_u = Column(INTEGER(11))
    NAME_F_106_u = Column(String(50))
    F_106_2_u = Column(INTEGER(11))
    NAME_F_106_2_u = Column(String(50))
    F_066u_02 = Column('F_066u-02', INTEGER(11))
    NAME_F_066u_02 = Column('NAME_F_066u-02', String(50))
    F_58_1_u_ = Column('F_58-1_u,', String(50))
    NAME_F_58_1_u = Column('NAME_F_58-1_u', String(50))
    Referral_to_the_place_of_treatment = Column(Float(asdecimal=True))
    NAME_Referral_to_the_place_of_treatment = Column(String(50))
    F_095_u = Column(INTEGER(11))
    NAME_F_095_u = Column(String(50))
    F_110_u = Column(INTEGER(11))
    NAME_F_110_u = Column(String(50))
    F_013_u = Column(INTEGER(11))
    NAME_F_013_u = Column(String(64))
    F_035_u_02 = Column('F_035_u-02', INTEGER(11))
    NAME_F_035_u_02 = Column('NAME_F_035_u-02', String(128))
    F_030_PO_u_17 = Column(INTEGER(11))
    NAME_F_030_PO_u_17 = Column(String(50))
    F_131_u = Column(INTEGER(11))
    NAME_F_131_u = Column(String(64))


class Speciality(Base):
    __tablename__ = 'speciality'
    __table_args__ = {'comment': 'Справочник специальностей'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    federal_code = Column(String(8))
    netrica_code = Column(String(8))


class SpecializedNutrition(Base):
    __tablename__ = 'specialized_nutrition'
    __table_args__ = {'comment': 'ФРЛЛО. Справочник специализированного питания (1.2.643.5.1.13.13.99.2.603) v1.4'}

    CODE = Column(INTEGER(11), primary_key=True)
    NAME = Column(String(512))
    KTRU_CODE = Column(String(50))
    OKPD2_CODE = Column(String(50))
    PARENT_CODE = Column(String(50))
    DESCRIPTION = Column(String(256))
    CHARACTERISTICS = Column(String(50))
    OKEI_CODE = Column(INTEGER(11))
    IS_TEMPLATE = Column(TINYINT(1))
    APPLICATION_DATE_START = Column(Date)
    APPLICATION_DATE_END = Column(Date)


class SurgicalOperationsFederalDirectory(Base):
    __tablename__ = 'surgical_operations_federal_directory'
    __table_args__ = {'comment': 'Федеральный справочник хирургических операций (1.2.643.5.1.13.13.99.2.812) v1.5'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    ACCESS = Column(Text)
    LATER = Column(Float(asdecimal=True))
    NMY = Column(Text)
    FORM14 = Column(Float(asdecimal=True))
    SYNONYM = Column(Text)
    VMP = Column(Text)
    EQUIPMENT = Column(Text)


class TelemedicineConsultationGoal(Base):
    __tablename__ = 'telemedicine_consultation_goals'
    __table_args__ = {'comment': 'Цели телемедицинской консультации (1.2.643.5.1.13.13.99.2.46) v1.2'}

    ID = Column(INTEGER(11), primary_key=True)
    PURPOSE = Column(String(255))


t_temp = Table(
    'temp', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0"))
)


t_tmp_orgStructure_bookkeeperCode = Table(
    'tmp_orgStructure_bookkeeperCode', metadata,
    Column('id', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    Column('master_id', INTEGER(11)),
    Column('orgCode', String(16), nullable=False)
)


class TreatmentResult(Base):
    __tablename__ = 'treatment_results'
    __table_args__ = {'comment': 'Результаты обращения (1.2.643.5.1.13.13.11.1046) v4.1'}

    ID = Column(INTEGER(11), primary_key=True)
    NAME = Column(Text)
    FORM_025 = Column(Float(asdecimal=True))
    FORM_066 = Column(Float(asdecimal=True))
    NAME_SYNONYM = Column(Text)


class TumorProcessStage(Base):
    __tablename__ = 'tumor_process_stages'
    __table_args__ = {'comment': 'РР. Стадии опухолевого процесса (1.2.643.5.1.13.13.99.2.126) v2.1'}

    ID = Column(INTEGER(11), primary_key=True)
    CODE = Column(INTEGER(11))
    NAME = Column(Text)
    ID_PARENT = Column(Float(asdecimal=True))


t_urolog = Table(
    'urolog', metadata,
    Column('code', String(255)),
    Column('name', String(255))
)


class VaccineReaction(Base):
    __tablename__ = 'vaccine_reaction'
    __table_args__ = {'comment': 'Реакции на ввод вакцины (1.2.643.5.1.13.13.99.2.619) v1.2'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(Text)
    parent_id = Column(Float(asdecimal=True))


class VmRelease(Base):
    __tablename__ = 'vm_release'
    __table_args__ = {'comment': 'Актуальная версия клиента'}

    id = Column(INTEGER(11), primary_key=True)
    revision = Column(String(8), nullable=False)
    datetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    description = Column(String(255))


t_vsyakoe220218 = Table(
    'vsyakoe220218', metadata,
    Column('createDatetime', DateTime),
    Column('createPerson_id', String(255)),
    Column('modifyDatetime', DateTime),
    Column('modifyPerson_id', Float(10, True)),
    Column('deleted', Float(10, True)),
    Column('class', Float(10, True)),
    Column('group_id', Float(10, True)),
    Column('code', String(255)),
    Column('name', String(255)),
    Column('title', String(255)),
    Column('flatCode', String(255)),
    Column('sex', Float(10, True)),
    Column('age', String(255)),
    Column('office', String(255)),
    Column('showInForm', Float(10, True)),
    Column('genTimetable', Float(10, True)),
    Column('quotaType_id', String(255)),
    Column('context', String(255)),
    Column('amount', Float(10, True)),
    Column('amountEvaluation', Float(10, True)),
    Column('defaultStatus', Float(10, True)),
    Column('defaultDirectionDate', Float(10, True)),
    Column('defaultPlannedEndDate', Float(10, True)),
    Column('defaultEndDate', Float(10, True)),
    Column('defaultExecPerson_id', String(255)),
    Column('defaultSetPerson_id', String(255)),
    Column('defaultPersonInEvent', Float(10, True)),
    Column('defaultPersonInEditor', Float(10, True)),
    Column('defaultMKB', Float(10, True)),
    Column('defaultMorphology', Float(10, True)),
    Column('isMorphologyRequired', Float(10, True)),
    Column('defaultOrg_id', String(255)),
    Column('showTime', Float(10, True)),
    Column('maxOccursInEvent', Float(10, True)),
    Column('isMES', Float(10, True)),
    Column('nomenclativeService_id', String(255)),
    Column('isPreferable', Float(10, True)),
    Column('prescribedType_id', String(255)),
    Column('shedule_id', String(255)),
    Column('isRequiredCoordination', Float(10, True)),
    Column('isNomenclatureExpense', Float(10, True)),
    Column('hasAssistant', Float(10, True)),
    Column('propertyAssignedVisible', Float(10, True)),
    Column('propertyUnitVisible', Float(10, True)),
    Column('propertyNormVisible', Float(10, True)),
    Column('propertyEvaluationVisible', Float(10, True)),
    Column('serviceType', Float(10, True)),
    Column('actualAppointmentDuration', Float(10, True)),
    Column('isSubstituteEndDateToEvent', Float(10, True)),
    Column('isPrinted', Float(10, True)),
    Column('defaultMES', Float(10, True)),
    Column('frequencyCount', Float(10, True)),
    Column('frequencyPeriod', Float(10, True)),
    Column('frequencyPeriodType', Float(10, True)),
    Column('isStrictFrequency', Float(10, True)),
    Column('isFrequencyPeriodByCalendar', Float(10, True)),
    Column('counter_id', String(255)),
    Column('isCustomSum', Float(10, True)),
    Column('recommendationExpirePeriod', Float(10, True)),
    Column('recommendationControl', Float(10, True)),
    Column('isExecRequiredForEventExec', Float(10, True)),
    Column('locked', Float(10, True)),
    Column('isActiveGroup', Float(10, True)),
    Column('lis_code', String(255)),
    Column('filledLock', Float(10, True)),
    Column('defaultBeginDate', Float(10, True)),
    Column('refferalType_id', String(255)),
    Column('filterPosts', Float(10, True)),
    Column('filterSpecialities', Float(10, True)),
    Column('isIgnoreEventExecDate', Float(10, True)),
    Column('id1', Float(10, True)),
    Column('deleted1', Float(10, True)),
    Column('actionType_id', Float(10, True)),
    Column('idx', Float(10, True)),
    Column('template_id', String(255)),
    Column('name1', String(255)),
    Column('shortName', String(255)),
    Column('descr', String(255)),
    Column('unit_id', String(255)),
    Column('typeName', String(255)),
    Column('valueDomain', String(255)),
    Column('defaultValue', String(255)),
    Column('isVector', Float(10, True)),
    Column('norm', String(255)),
    Column('sex1', Float(10, True)),
    Column('age1', String(255)),
    Column('penalty', Float(10, True)),
    Column('visibleInJobTicket', Float(10, True)),
    Column('visibleInTableRedactor', Float(10, True)),
    Column('isAssignable', Float(10, True)),
    Column('test_id', String(255)),
    Column('defaultEvaluation', Float(10, True)),
    Column('canChangeOnlyOwner', Float(10, True)),
    Column('isActionNameSpecifier', Float(10, True)),
    Column('laboratoryCalculator', String(255)),
    Column('inActionsSelectionTable', Float(10, True)),
    Column('redactorSizeFactor', Float(10, True)),
    Column('isFrozen', Float(10, True)),
    Column('typeEditable', Float(10, True)),
    Column('visibleInDR', Float(10, True)),
    Column('userProfile_id', String(255)),
    Column('userProfileBehaviour', Float(10, True)),
    Column('copyModifier', Float(10, True))
)


t_vzros_mes = Table(
    'vzros_mes', metadata,
    Column('code', INTEGER(11)),
    Column('name', String(150)),
    Column('price', Float(10, True)),
    Column('kind', INTEGER(11)),
    Column('type', INTEGER(11)),
    Column('beg', String(50)),
    Column('end', String(50)),
    Column('contract', String(20), server_default=alchemy_text("'75'")),
    Column('eventtype', String(20), server_default=alchemy_text("'97'")),
    Column('ege', String(20), server_default=alchemy_text("'18г-'")),
    Column('unit', String(20), server_default=alchemy_text("'1'")),
    Column('amount', String(20), server_default=alchemy_text("'1'")),
    Column('tarifftype', String(20), server_default=alchemy_text("'9'")),
    Column('groupmes', String(20), server_default=alchemy_text("'36'")),
    Column('model', String(35), server_default=alchemy_text("'П.Н.00.00.9.1.1.0.0.О'"))
)


class WorkerProfession(Base):
    __tablename__ = 'worker_professions'
    __table_args__ = {'comment': 'Профессии рабочих и должностей служащих (1.2.643.5.1.13.13.99.2.855) v1.0'}

    ID = Column(INTEGER(11), primary_key=True)
    P_ID = Column(INTEGER(11))
    NAME = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    OKPDTR = Column(INTEGER(11))
    OKZ = Column(String(255), nullable=False, server_default=alchemy_text("''"))


class ActionTemplate(Base):
    __tablename__ = 'ActionTemplate'
    __table_args__ = {'comment': 'Описание шаблона действия'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False)
    group_id = Column(ForeignKey('ActionTemplate.id', ondelete='CASCADE'))
    code = Column(String(64), nullable=False)
    name = Column(String(255), nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    owner_id = Column(ForeignKey('Person.id', ondelete='CASCADE'))
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='SET NULL'))
    action_id = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='ActionTemplate.createPerson_id == Person.id')
    group = relationship('ActionTemplate', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='ActionTemplate.modifyPerson_id == Person.id')
    owner = relationship('Person', primaryjoin='ActionTemplate.owner_id == Person.id')
    speciality = relationship('RbSpeciality')


class AddressHouse(Base):
    __tablename__ = 'AddressHouse'
    __table_args__ = {'comment': 'Дома'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    KLADRCode = Column(String(13), nullable=False)
    KLADRStreetCode = Column(String(17), nullable=False)
    number = Column(String(8), nullable=False)
    corpus = Column(String(8), nullable=False)
    litera = Column(String(8))
    KLADRCode_old = Column(String(13), nullable=False)
    KLADRStreetCode_old = Column(String(17), nullable=False)

    createPerson = relationship('Person', primaryjoin='AddressHouse.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='AddressHouse.modifyPerson_id == Person.id')


t_AppLock_Detail = Table(
    'AppLock_Detail', metadata,
    Column('master_id', ForeignKey('AppLock.id', ondelete='CASCADE'), nullable=False),
    Column('tableName', String(64), nullable=False),
    Column('recordId', INTEGER(11), nullable=False),
    Column('recordIndex', INTEGER(11), nullable=False, server_default=alchemy_text("0")),
    comment='Подробности блокировки'
)


class AssignmentsTemplate(Base):
    __tablename__ = 'AssignmentsTemplate'
    __table_args__ = {'comment': 'Шаблоны назначений'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    modifyDatetime = Column(DateTime)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    group_id = Column(ForeignKey('AssignmentsTemplate.id', ondelete='SET NULL', onupdate='CASCADE'))
    name = Column(String(255), nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9))
    owner_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='SET NULL', onupdate='CASCADE'))

    createPerson = relationship('Person', primaryjoin='AssignmentsTemplate.createPerson_id == Person.id')
    group = relationship('AssignmentsTemplate', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='AssignmentsTemplate.modifyPerson_id == Person.id')
    owner = relationship('Person', primaryjoin='AssignmentsTemplate.owner_id == Person.id')
    speciality = relationship('RbSpeciality')


class Bank(Base):
    __tablename__ = 'Bank'
    __table_args__ = {'comment': 'Расчетный счет'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    BIK = Column(String(10), nullable=False)
    name = Column(String(500), nullable=False)
    branchName = Column(String(500), nullable=False)
    corrAccount = Column(String(20), nullable=False)
    subAccount = Column(String(20), nullable=False)
    treasuryAccount = Column(String(20), nullable=False)
    unifiedTreasuryAccount = Column(String(20), nullable=False)

    createPerson = relationship('Person', primaryjoin='Bank.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='Bank.modifyPerson_id == Person.id')


class ClientMonitoring(Base):
    __tablename__ = 'ClientMonitoring'
    __table_args__ = {'comment': 'Наблюдение пациента'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    client_id = Column(INTEGER(11), nullable=False)
    kind_id = Column(ForeignKey('rbClientMonitoringKind.id', onupdate='CASCADE'), nullable=False)
    frequence_id = Column(ForeignKey('rbClientMonitoringFrequence.id', ondelete='SET NULL', onupdate='CASCADE'))
    setDate = Column(Date, nullable=False)
    endDate = Column(Date)
    reason = Column(String(128), nullable=False)
    reason_id = Column(ForeignKey('rbStopMonitoringReason.id'))

    frequence = relationship('RbClientMonitoringFrequence')
    kind = relationship('RbClientMonitoringKind')
    reason1 = relationship('RbStopMonitoringReason')


class ClientMonitoringKindFrequence(Base):
    __tablename__ = 'ClientMonitoringKind_Frequence'
    __table_args__ = {'comment': 'Соответствие частоты посещений видам наблюдения'}

    id = Column(INTEGER(11), primary_key=True)
    kind_id = Column(ForeignKey('rbClientMonitoringKind.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    frequence_id = Column(ForeignKey('rbClientMonitoringFrequence.id', ondelete='CASCADE', onupdate='CASCADE'))

    frequence = relationship('RbClientMonitoringFrequence')
    kind = relationship('RbClientMonitoringKind')


class ClientQuoting(Base):
    __tablename__ = 'Client_Quoting'
    __table_args__ = {'comment': 'Квоты клиентов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(INTEGER(11))
    identifier = Column(String(16))
    quotaTicket = Column(String(18))
    quotaType_id = Column(INTEGER(11))
    stage = Column(INTEGER(2))
    directionDate = Column(DateTime, nullable=False)
    freeInput = Column(String(128))
    org_id = Column(INTEGER(11))
    amount = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    MKB = Column(String(8), nullable=False)
    status = Column(INTEGER(2), nullable=False, server_default=alchemy_text("0"))
    request = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    statment = Column(String(255))
    dateRegistration = Column(DateTime, nullable=False)
    dateEnd = Column(DateTime, nullable=False)
    orgStructure_id = Column(INTEGER(11))
    regionCode = Column(String(13))

    createPerson = relationship('Person', primaryjoin='ClientQuoting.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientQuoting.modifyPerson_id == Person.id')


class DentalFormula(Base):
    __tablename__ = 'DentalFormula'
    __table_args__ = {'comment': 'Зубная формула'}

    id = Column(INTEGER(11), primary_key=True)
    event_id = Column(ForeignKey('Event.id'), nullable=False)
    is_deciduous = Column(TINYINT(1))

    event = relationship('Event')


class ECROperation(Base):
    __tablename__ = 'ECROperation'
    __table_args__ = {'comment': 'Информация о проведенных по кассе операций'}

    id = Column(INTEGER(11), primary_key=True)
    checkType = Column(INTEGER(11))
    checkNumber = Column(INTEGER(11), nullable=False)
    checkSumm = Column(Float(asdecimal=True))
    closeType = Column(INTEGER(11))
    closeDatetime = Column(DateTime, nullable=False)
    operator = Column(INTEGER(11), nullable=False)
    session = Column(INTEGER(11))
    deviceInfo = Column(Text)
    operationType_id = Column(ForeignKey('rbECROperationType.id', ondelete='SET NULL'))
    isExpense = Column(TINYINT(4))
    substructure = Column(String(64), nullable=False)
    cashFlowArticle = Column(String(256), nullable=False)
    isPersonNatural = Column(TINYINT(4))
    personName = Column(String(128), nullable=False)
    documentInfo = Column(Text, nullable=False)
    description = Column(String(128), nullable=False)
    execPerson_id = Column(ForeignKey('Person.id'))
    succesful = Column(TINYINT(1))

    execPerson = relationship('Person')
    operationType = relationship('RbECROperationType')


class EmergencyBrigade(Base):
    __tablename__ = 'EmergencyBrigade'
    __table_args__ = {'comment': 'Справочник Бригады'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)
    deleted = Column(TINYINT(1), nullable=False)
    senior_person_id = Column(ForeignKey('Person.id'))

    senior_person = relationship('Person')


t_Epicrisis = Table(
    'Epicrisis', metadata,
    Column('id', INTEGER(11)),
    Column('name', String(64), nullable=False),
    Column('code', String(64)),
    Column('id_orgStructure', String(64), nullable=False),
    Column('event_id', INTEGER(11), nullable=False),
    Column('createDatetime', DateTime),
    Column('printTemplate', Text),
    Column('isDelete', TINYINT(1), server_default=alchemy_text("0")),
    Column('isDone', TINYINT(1), server_default=alchemy_text("0")),
    Column('personID', INTEGER(11)),
    Column('type', ForeignKey('rbIEMKDocument.id', onupdate='CASCADE'), server_default=alchemy_text("1")),
    comment='Таблица эпикризов.'
)


t_EpicrisisProperty_Table = Table(
    'EpicrisisProperty_Table', metadata,
    Column('id', ForeignKey('EpicrisisProperty.idTable', ondelete='CASCADE'), nullable=False),
    Column('idx_property', INTEGER(11), nullable=False),
    Column('value', Text),
    comment='Таблица значений таблиц свойств.'
)


class EventTypePerson(Base):
    __tablename__ = 'EventType_Person'

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(INTEGER(11))
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'))

    person = relationship('Person')


class EventKSLP(Base):
    __tablename__ = 'Event_KSLP'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id', onupdate='CASCADE'), nullable=False)
    KSLP_id = Column(ForeignKey('rbExtraKSLP.id', onupdate='CASCADE'), nullable=False)
    KSLP_coeff = Column(Float(asdecimal=True), server_default=alchemy_text("1"))

    KSLP = relationship('RbExtraKSLP')
    event = relationship('Event')


class EventOutgoingReferral(Base):
    __tablename__ = 'Event_OutgoingReferral'
    __table_args__ = {'comment': 'Информация о направлениях из ЛПУ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(INTEGER(11), nullable=False)
    number = Column(String(10), nullable=False)
    org_id = Column(ForeignKey('Organisation.id'), nullable=False)
    orgStructureProfile_id = Column(INTEGER(11))
    hospitalBedProfile_id = Column(INTEGER(11))
    plannedDate = Column(Date)

    createPerson = relationship('Person', primaryjoin='EventOutgoingReferral.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='EventOutgoingReferral.modifyPerson_id == Person.id')
    org = relationship('Organisation')


class EventPhysicalActivity(Base):
    __tablename__ = 'Event_PhysicalActivity'
    __table_args__ = {'comment': 'Режим физической активности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    physicalActivityMode_id = Column(ForeignKey('rbPhysicalActivityMode.id'), nullable=False)

    createPerson = relationship('Person', primaryjoin='EventPhysicalActivity.createPerson_id == Person.id')
    event = relationship('Event')
    modifyPerson = relationship('Person', primaryjoin='EventPhysicalActivity.modifyPerson_id == Person.id')
    physicalActivityMode = relationship('RbPhysicalActivityMode')


class GeoLocation(Base):
    __tablename__ = 'GeoLocations'

    id = Column(INTEGER(11), primary_key=True)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    createDate = Column(Date)
    createTime = Column(Time)
    person_id = Column(ForeignKey('Person.id'), nullable=False)

    person = relationship('Person')


class Geolocation(Base):
    __tablename__ = 'Geolocation'
    __table_args__ = {'comment': 'Геоданные врачей'}

    id = Column(INTEGER(11), primary_key=True)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    createDate = Column(DateTime)
    person_id = Column(ForeignKey('Person.id'), nullable=False)

    person = relationship('Person')


class InformerMessage(Base):
    __tablename__ = 'InformerMessage'
    __table_args__ = {'comment': 'Сообщения информатора'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False)
    subject = Column(String(128), nullable=False)
    text = Column(LONGTEXT, nullable=False)
    addressee = Column(ForeignKey('rbUserProfile.id', ondelete='SET NULL', onupdate='CASCADE'))

    rbUserProfile = relationship('RbUserProfile')
    createPerson = relationship('Person', primaryjoin='InformerMessage.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='InformerMessage.modifyPerson_id == Person.id')


class Licence(Base):
    __tablename__ = 'Licence'
    __table_args__ = {'comment': 'Лицензии'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    serial = Column(String(8), nullable=False)
    number = Column(String(16), nullable=False)
    date = Column(Date, nullable=False)
    person_id = Column(ForeignKey('Person.id'))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)

    createPerson = relationship('Person', primaryjoin='Licence.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='Licence.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='Licence.person_id == Person.id')


class MKBServiceSpeciality(Base):
    __tablename__ = 'MKBServiceSpeciality'
    __table_args__ = {'comment': 'Таблица соответствия специальности и услуги для диагнозов в справочнике МКБХ'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    modifyDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyPerson_id = Column(ForeignKey('Person.id'))
    speciality_id = Column(ForeignKey('rbSpeciality.id'))
    service_id = Column(ForeignKey('rbService.id'), nullable=False)
    mkb_id = Column(INTEGER(11), nullable=False)

    createPerson = relationship('Person', primaryjoin='MKBServiceSpeciality.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='MKBServiceSpeciality.modifyPerson_id == Person.id')
    service = relationship('RbService')
    speciality = relationship('RbSpeciality')


class OrgStructure(Base):
    __tablename__ = 'OrgStructure'
    __table_args__ = {'comment': 'Подразделения, отделения, участки'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    organisation_id = Column(INTEGER(11), nullable=False)
    code = Column(String(64), nullable=False)
    name = Column(String(256), nullable=False)
    parent_id = Column(ForeignKey('OrgStructure.id'))
    type = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    net_id = Column(ForeignKey('rbNet.id', ondelete='SET NULL'))
    chief_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    headNurse_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    isArea = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    hasHospitalBeds = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hasStocks = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hasDayStationary = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    infisCode = Column(String(16), nullable=False)
    infisInternalCode = Column(String(30), nullable=False)
    infisDepTypeCode = Column(String(30), nullable=False)
    availableForExternal = Column(INTEGER(1), nullable=False, server_default=alchemy_text("1"))
    address = Column(String(250), nullable=False)
    infisTariffCode = Column(String(16), nullable=False)
    inheritEventTypes = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    inheritActionTypes = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    inheritGaps = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    bookkeeperCode = Column(String(16), nullable=False)
    dayLimit = Column(TINYINT(3))
    storageCode = Column(String(64), nullable=False)
    miacHead_id = Column(INTEGER(11))
    salaryPercentage = Column(INTEGER(11), server_default=alchemy_text("0"))
    attachCode = Column(INTEGER(10))
    isVisibleInDR = Column(TINYINT(4), server_default=alchemy_text("1"))
    tfomsCode = Column(String(16))
    syncGUID = Column(Text)
    quota = Column(TINYINT(3), server_default=alchemy_text("0"))
    miacCode = Column(String(11))
    netrica_Code = Column(String(64))
    idLPU_egisz = Column(INTEGER(11))
    netrica_Code_UO = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    netrica_Code_IEMK = Column(String(64))
    EGISZ_code = Column(String(60))

    chief = relationship('Person', primaryjoin='OrgStructure.chief_id == Person.id')
    createPerson = relationship('Person', primaryjoin='OrgStructure.createPerson_id == Person.id')
    headNurse = relationship('Person', primaryjoin='OrgStructure.headNurse_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='OrgStructure.modifyPerson_id == Person.id')
    net = relationship('RbNet')
    parent = relationship('OrgStructure', remote_side=[id])


class OrgStructureAncestor(OrgStructure):
    __tablename__ = 'OrgStructure_Ancestors'
    __table_args__ = {'comment': 'Таблица для хранения "плоского" представления связей между подразделениями. Должна перезаписываться автоматически.'}

    id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'), primary_key=True)
    fullPath = Column(String(150))


class PersonFSSAliase(Base):
    __tablename__ = 'PersonFSSAliases'
    __table_args__ = {'comment': 'Таблица, доступных для врачей, псевдонимов сертификатов ФСС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    person_id = Column(ForeignKey('Person.id'), nullable=False)
    alias = Column(String(64), nullable=False)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    defalutMOsert = Column(TINYINT(1), server_default=alchemy_text("0"))
    password = Column(String(100), server_default=alchemy_text("''"))
    defaultVKsert = Column(TINYINT(1), server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='PersonFSSAliase.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='PersonFSSAliase.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='PersonFSSAliase.person_id == Person.id')


class PersonIdentificationLDE(Base):
    __tablename__ = 'PersonIdentificationLDES'
    __table_args__ = {'comment': 'Идентификаторы мед.работников в сервисе ОДЛИ (Нетрика)'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE'), nullable=False)
    orgCode = Column(String(36))
    practitionerId = Column(String(36))
    versionId = Column(String(36))
    version = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))

    person = relationship('Person')


class PersonIdentificationODII(Base):
    __tablename__ = 'PersonIdentificationODII'
    __table_args__ = {'comment': 'Идентификаторы врачей в сервисе ОДИИ (Нетрика)'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE'), nullable=False)
    orgCode = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    practitionerId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    versionId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    practitionerRoleId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    versionRoleId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    version = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    datetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))

    person = relationship('Person')


class PersonAward(Base):
    __tablename__ = 'Person_Awards'
    __table_args__ = {'comment': 'Награды сотрудника'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Person.id'), nullable=False)
    number = Column(String(20))
    name = Column(String(80), nullable=False)
    date = Column(Date, nullable=False)

    createPerson = relationship('Person', primaryjoin='PersonAward.createPerson_id == Person.id')
    master = relationship('Person', primaryjoin='PersonAward.master_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='PersonAward.modifyPerson_id == Person.id')


class PersonPreference(Base):
    __tablename__ = 'Person_Preferences'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('Person.id', onupdate='CASCADE'), nullable=False)
    name = Column(String(45), nullable=False)
    value = Column(String(45), nullable=False)

    master = relationship('Person')


class PersonSetting(Base):
    __tablename__ = 'Person_Settings'
    __table_args__ = {'comment': 'Настройки клиента МИС для сотрудника. (deprecated in r15018)'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    guiHider = Column(Text)

    master = relationship('Person')


class PersonTimeTemplate(Base):
    __tablename__ = 'Person_TimeTemplate'
    __table_args__ = {'comment': 'Персональный график'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Person.id'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    ambBegTime = Column(Time)
    ambEndTime = Column(Time)
    ambPlan = Column(SMALLINT(4), nullable=False)
    ambInterval = Column(SMALLINT(4), nullable=False)
    ambColor = Column(String(8))
    office = Column(String(8), nullable=False)
    ambBegTime2 = Column(Time)
    ambEndTime2 = Column(Time)
    ambPlan2 = Column(SMALLINT(4), nullable=False)
    ambInterval2 = Column(SMALLINT(4), nullable=False)
    ambColor2 = Column(String(8))
    office2 = Column(String(8), nullable=False)
    homBegTime = Column(Time)
    homEndTime = Column(Time)
    homPlan = Column(SMALLINT(4), nullable=False)
    homInterval = Column(SMALLINT(4), nullable=False)
    homBegTime2 = Column(Time)
    homEndTime2 = Column(Time)
    homPlan2 = Column(SMALLINT(4), nullable=False)
    homInterval2 = Column(SMALLINT(4), nullable=False)
    officeInter = Column(String(8), nullable=False)
    ambPlanInter = Column(SMALLINT(4), nullable=False)
    ambInterInterval = Column(SMALLINT(4), nullable=False)
    ambColorInter = Column(String(8))

    createPerson = relationship('Person', primaryjoin='PersonTimeTemplate.createPerson_id == Person.id')
    master = relationship('Person', primaryjoin='PersonTimeTemplate.master_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='PersonTimeTemplate.modifyPerson_id == Person.id')


class PersonUserProfile(Base):
    __tablename__ = 'Person_UserProfile'
    __table_args__ = {'comment': 'Связь между пользователем и набором его профилей прав.'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    userProfile_id = Column(ForeignKey('rbUserProfile.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))

    createPerson = relationship('Person', primaryjoin='PersonUserProfile.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='PersonUserProfile.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='PersonUserProfile.person_id == Person.id')
    userProfile = relationship('RbUserProfile')


class Quoting(Base):
    __tablename__ = 'Quoting'
    __table_args__ = {'comment': 'Квотирование'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    quotaType_id = Column(INTEGER(11))
    beginDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)
    limitation = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))
    used = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))
    confirmed = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))
    inQueue = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='Quoting.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='Quoting.modifyPerson_id == Person.id')


class QuotingRegion(Base):
    __tablename__ = 'Quoting_Region'
    __table_args__ = {'comment': 'Ограничение квотирования по региону'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(INTEGER(11))
    region_code = Column(String(13))
    limitation = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))
    used = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))
    confirmed = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))
    inQueue = Column(INTEGER(8), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='QuotingRegion.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='QuotingRegion.modifyPerson_id == Person.id')


class SPRAVKSGSHEMA(Base):
    __tablename__ = 'SPRAV_KSG_SHEMAS'
    __table_args__ = {'comment': 'спавочник соответствия стандарта MES и лекарствам'}

    id = Column(INTEGER(11), primary_key=True)
    mes_id = Column(INTEGER(11), nullable=False)
    drugs_id = Column(ForeignKey('SPRAV_DRUGS_SCHEMES.ID_DRUGS', ondelete='CASCADE'), nullable=False)

    drugs = relationship('SPRAVDRUGSSCHEME')


class SuiteReagent(Base):
    __tablename__ = 'SuiteReagent'
    __table_args__ = {'comment': 'Набор реагентов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False)
    code = Column(String(24), nullable=False)
    name = Column(String(64), nullable=False)
    releaseDate = Column(Date)
    supplyDate = Column(Date)
    startOperationDate = Column(Date)
    expiryDate = Column(Date)
    planTestQuantity = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    execTestQuantity = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    manufacturer = Column(String(128))
    storageConditions = Column(String(128))
    recipientPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))

    createPerson = relationship('Person', primaryjoin='SuiteReagent.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='SuiteReagent.modifyPerson_id == Person.id')
    recipientPerson = relationship('Person', primaryjoin='SuiteReagent.recipientPerson_id == Person.id')


class TreatmentPlan(Base):
    __tablename__ = 'TreatmentPlan'
    __table_args__ = {'comment': 'Сущность "План лечения"'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id'))
    name = Column(String(64), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    isPrimary = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    prepaymented = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    surcharged = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    balanced = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    percentPayment = Column(DECIMAL(5, 3), nullable=False, server_default=alchemy_text("50.000"))
    percentSurcharged = Column(DECIMAL(5, 3), nullable=False, server_default=alchemy_text("0.000"))
    isClosed = Column(TINYINT(1), server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='TreatmentPlan.createPerson_id == Person.id')
    event = relationship('Event')
    modifyPerson = relationship('Person', primaryjoin='TreatmentPlan.modifyPerson_id == Person.id')


class TreatmentPlanTemplate(Base):
    __tablename__ = 'TreatmentPlanTemplate'
    __table_args__ = {'comment': 'Шаблоны планов лечения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    modifyDatetime = Column(DateTime)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    group_id = Column(ForeignKey('TreatmentPlanTemplate.id', ondelete='SET NULL', onupdate='CASCADE'))
    name = Column(String(255), nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9))
    owner_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='SET NULL', onupdate='CASCADE'))

    createPerson = relationship('Person', primaryjoin='TreatmentPlanTemplate.createPerson_id == Person.id')
    group = relationship('TreatmentPlanTemplate', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='TreatmentPlanTemplate.modifyPerson_id == Person.id')
    owner = relationship('Person', primaryjoin='TreatmentPlanTemplate.owner_id == Person.id')
    speciality = relationship('RbSpeciality')


class ZNOInfo(Base):
    __tablename__ = 'ZNOInfo'
    __table_args__ = {'comment': 'Сведения о ЗНО'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    event_id = Column(INTEGER(11), nullable=False)
    MKB = Column(String(8), nullable=False)
    referralType = Column(INTEGER(11))
    stady = Column(INTEGER(11))
    stady_t = Column(INTEGER(11))
    stady_n = Column(INTEGER(11))
    stady_m = Column(INTEGER(11))
    reason = Column(INTEGER(11))
    haveRemoteMetastases = Column(TINYINT(1))
    histologyDate = Column(Date)
    contraindicationsSurgeryDate = Column(Date)
    contraindicationsChemotherapyDate = Column(Date)
    contraindicationsRadiationTherapyDate = Column(Date)
    rejectSurgeryDate = Column(Date)
    rejectChemotherapyDate = Column(Date)
    rejectRadiationTherapyDate = Column(Date)
    issueDate = Column(Date)
    referredFrom = Column(ForeignKey('Organisation.id'))
    referredTo = Column(ForeignKey('Organisation.id'))
    checkupType = Column(ForeignKey('rbExaminationType.id'))
    nomenclature = Column(INTEGER(11))
    contraindicationToHistologyDate = Column(Date)
    histologyNotConfirmDiagnosDate = Column(Date)
    consilium = Column(INTEGER(11))
    consiliumDate = Column(Date)
    height = Column(INTEGER(11))
    weight = Column(Float(asdecimal=True))
    bsa = Column(Float(asdecimal=True))
    radiotherapyFractionsCount = Column(INTEGER(11))
    NOTFULLDSH_1 = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    NOTFULLDSH_2 = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    enabledTab = Column(INTEGER(11))
    clinical_group = Column(INTEGER(11))
    tumor_state = Column(INTEGER(11))

    rbExaminationType = relationship('RbExaminationType')
    Organisation = relationship('Organisation', primaryjoin='ZNOInfo.referredFrom == Organisation.id')
    Organisation1 = relationship('Organisation', primaryjoin='ZNOInfo.referredTo == Organisation.id')


class ZNOInfoLEK(Base):
    __tablename__ = 'ZNOInfo_LEK'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ZNOInfo_DoneCure.id'))
    id_lek_pr = Column(INTEGER(11))
    date_inj = Column(Date)

    master = relationship('ZNOInfoDoneCure')


class MedicalDocumentConclusion(Base):
    __tablename__ = 'medical_document_conclusions'
    __table_args__ = {'comment': 'Перечень заключений в медицинских документах (1.2.643.5.1.13.13.99.2.725) v1.18'}

    ID = Column(INTEGER(11), primary_key=True)
    Name = Column(String(255), nullable=False)
    NameForm = Column(ForeignKey('medical_document_types.RECID'))

    medical_document_type = relationship('MedicalDocumentType')


class RbAccountExportFormat(Base):
    __tablename__ = 'rbAccountExportFormat'
    __table_args__ = {'comment': 'Формат экспорта счёта'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    prog = Column(String(128), nullable=False)
    preferentArchiver = Column(String(128), nullable=False)
    emailRequired = Column(TINYINT(1), nullable=False)
    emailTo = Column(String(64), nullable=False)
    subject = Column(String(128), nullable=False)
    message = Column(Text, nullable=False)

    createPerson = relationship('Person', primaryjoin='RbAccountExportFormat.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbAccountExportFormat.modifyPerson_id == Person.id')


class RbAccountType(Base):
    __tablename__ = 'rbAccountType'
    __table_args__ = {'comment': 'Справочник Тип Счета'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    modifyDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(64), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbAccountType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbAccountType.modifyPerson_id == Person.id')


class RbAccountingSystem(Base):
    __tablename__ = 'rbAccountingSystem'
    __table_args__ = {'comment': 'Внешняя учётная система (ЕИС ОМС и пр.)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    isEditable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    showInClientInfo = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isUnique = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    counter_id = Column(INTEGER(11))
    autoIdentificator = Column(TINYINT(1), server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbAccountingSystem.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbAccountingSystem.modifyPerson_id == Person.id')


class RbActionShedule(Base):
    __tablename__ = 'rbActionShedule'
    __table_args__ = {'comment': 'График выполнения действия'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    period = Column(TINYINT(2), nullable=False, server_default=alchemy_text("1"))

    createPerson = relationship('Person', primaryjoin='RbActionShedule.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbActionShedule.modifyPerson_id == Person.id')


class RbActionTypeIncompatibility(Base):
    __tablename__ = 'rbActionTypeIncompatibility'
    __table_args__ = {'comment': 'Таблица несовместимости типов действий (медикаментов)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    firstActionType_id = Column(INTEGER(11), nullable=False)
    secondActionType_id = Column(INTEGER(11), nullable=False)
    reason = Column(String(800), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbActionTypeIncompatibility.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbActionTypeIncompatibility.modifyPerson_id == Person.id')


class RbActivity(Base):
    __tablename__ = 'rbActivity'
    __table_args__ = {'comment': 'Виды(типы) деятельности врача'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    regionalCode = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbActivity.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbActivity.modifyPerson_id == Person.id')


class RbAgreementType(Base):
    __tablename__ = 'rbAgreementType'
    __table_args__ = {'comment': 'Типы согласования'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    quotaStatusModifier = Column(INTEGER(2), server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbAgreementType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbAgreementType.modifyPerson_id == Person.id')


class RbAttachType(Base):
    __tablename__ = 'rbAttachType'
    __table_args__ = {'comment': 'Тип прикрепления'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    temporary = Column(TINYINT(1), nullable=False)
    outcome = Column(TINYINT(4), nullable=False)
    finance_id = Column(ForeignKey('rbFinance.id'), nullable=False)
    grp = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbAttachType.createPerson_id == Person.id')
    finance = relationship('RbFinance')
    modifyPerson = relationship('Person', primaryjoin='RbAttachType.modifyPerson_id == Person.id')


class RbBloodType(Base):
    __tablename__ = 'rbBloodType'
    __table_args__ = {'comment': 'Группы крови'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbBloodType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbBloodType.modifyPerson_id == Person.id')


class RbCancellationReason(Base):
    __tablename__ = 'rbCancellationReason'
    __table_args__ = {'comment': 'Справочник причин аннулирования направлений'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8))
    name = Column(String(256))

    createPerson = relationship('Person')


class RbCarnotianIndex(Base):
    __tablename__ = 'rbCarnotianIndex'
    __table_args__ = {'comment': 'Справочник индексов Карновского'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(512), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbCarnotianIndex.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbCarnotianIndex.modifyPerson_id == Person.id')


class RbCashOperation(Base):
    __tablename__ = 'rbCashOperation'
    __table_args__ = {'comment': 'Кассовые операции'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbCashOperation.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbCashOperation.modifyPerson_id == Person.id')


class RbComplain(Base):
    __tablename__ = 'rbComplain'
    __table_args__ = {'comment': 'Жалобы'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    group_id = Column(ForeignKey('rbComplain.id', ondelete='SET NULL'))
    code = Column(String(64), nullable=False)
    name = Column(String(120), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbComplain.createPerson_id == Person.id')
    group = relationship('RbComplain', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='RbComplain.modifyPerson_id == Person.id')


class RbContactType(Base):
    __tablename__ = 'rbContactType'
    __table_args__ = {'comment': 'Различные способы связи с пациентом'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    mask = Column(String(64), server_default=alchemy_text("''"))
    maskEnabled = Column(TINYINT(1), server_default=alchemy_text("0"))
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbContactType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbContactType.modifyPerson_id == Person.id')


class RbContractType(Base):
    __tablename__ = 'rbContractType'
    __table_args__ = {'comment': 'Тип договора'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    code = Column(String(32), nullable=False)
    hasProfit = Column(INTEGER(11), nullable=False)
    finance_id = Column(ForeignKey('rbFinance.id'), nullable=False)

    finance = relationship('RbFinance')


class RbCounter(Base):
    __tablename__ = 'rbCounter'
    __table_args__ = {'comment': 'Счетчики'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    value = Column(BIGINT(11), nullable=False, server_default=alchemy_text("0"))
    prefix = Column(String(32))
    postfix = Column(String(32))
    separator = Column(String(8), server_default=alchemy_text("' '"))
    reset = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    startDate = Column(Date, nullable=False)
    resetDate = Column(Date)
    sequenceFlag = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbCounter.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbCounter.modifyPerson_id == Person.id')


class RbCureMethod(Base):
    __tablename__ = 'rbCureMethod'
    __table_args__ = {'comment': 'Справочник Методы лечения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(512), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    isObsolete = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbCureMethod.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbCureMethod.modifyPerson_id == Person.id')


class RbCureType(Base):
    __tablename__ = 'rbCureType'
    __table_args__ = {'comment': 'Справочник Виды лечения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(512), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    isObsolete = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbCureType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbCureType.modifyPerson_id == Person.id')


class RbDNDiagnose(Base):
    __tablename__ = 'rbDNDiagnoses'

    id = Column(INTEGER(11), primary_key=True)
    mkb_id = Column(INTEGER(11), nullable=False)
    min_periodicity = Column(TINYINT(3), nullable=False)
    speciality_id = Column(ForeignKey('rbSpeciality.id'), nullable=False)
    beg_date = Column(Date)
    end_date = Column(Date)

    speciality = relationship('RbSpeciality')


class RbDTypeEi(Base):
    __tablename__ = 'rbDType_eis'
    __table_args__ = {'comment': 'Тип направления (назначения) ЕИС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(255), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbDTypeEi.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDTypeEi.modifyPerson_id == Person.id')


class RbDeferredQueueStatu(Base):
    __tablename__ = 'rbDeferredQueueStatus'
    __table_args__ = {'comment': 'Статусы записей в ЖОС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    flatCode = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    isSelectable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    federalCode = Column(String(128))

    createPerson = relationship('Person', primaryjoin='RbDeferredQueueStatu.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDeferredQueueStatu.modifyPerson_id == Person.id')


class RbDiagnosisType(Base):
    __tablename__ = 'rbDiagnosisType'
    __table_args__ = {'comment': 'Тип диагноза'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    replaceInDiagnosis = Column(String(8), nullable=False)
    netrica_Code = Column(String(64))
    EGISZ_code = Column(String(16))
    EGISZ_name = Column(String(655))

    createPerson = relationship('Person', primaryjoin='RbDiagnosisType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDiagnosisType.modifyPerson_id == Person.id')


class RbDiet(Base):
    __tablename__ = 'rbDiet'
    __table_args__ = {'comment': 'Справочник Столы питания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    allow_meals = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbDiet.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDiet.modifyPerson_id == Person.id')


class RbDiseaseCharacter(Base):
    __tablename__ = 'rbDiseaseCharacter'
    __table_args__ = {'comment': 'Характер заболевания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    replaceInDiagnosis = Column(String(8), nullable=False)
    netrica_Code = Column(String(65))
    EIScode = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='RbDiseaseCharacter.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDiseaseCharacter.modifyPerson_id == Person.id')


class RbDiseasePhase(Base):
    __tablename__ = 'rbDiseasePhases'
    __table_args__ = {'comment': 'Фазы заболевания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    characterRelation = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbDiseasePhase.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDiseasePhase.modifyPerson_id == Person.id')


class RbDiseaseStage(Base):
    __tablename__ = 'rbDiseaseStage'
    __table_args__ = {'comment': 'Стадия заболевания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    characterRelation = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbDiseaseStage.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDiseaseStage.modifyPerson_id == Person.id')


class RbDispanser(Base):
    __tablename__ = 'rbDispanser'
    __table_args__ = {'comment': 'Отметки диспансерного наблюдения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    observed = Column(TINYINT(1), nullable=False)
    secondaryCode = Column(String(8))
    netrica_Code = Column(String(65))
    dispanser_circumstances = Column(String(10))
    EGISZ_code = Column(String(16))
    EGISZ_name = Column(Text)

    createPerson = relationship('Person', primaryjoin='RbDispanser.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDispanser.modifyPerson_id == Person.id')


class RbDocumentTypeGroup(Base):
    __tablename__ = 'rbDocumentTypeGroup'
    __table_args__ = {'comment': 'Группа типов документов (удостоверения, льготы и т.д.)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbDocumentTypeGroup.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDocumentTypeGroup.modifyPerson_id == Person.id')


class RbECOG(Base):
    __tablename__ = 'rbECOG'
    __table_args__ = {'comment': 'Справочник оценок больного по шкале ECOG'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(512), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbECOG.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbECOG.modifyPerson_id == Person.id')


class RbEmergencyAccident(Base):
    __tablename__ = 'rbEmergencyAccident'
    __table_args__ = {'comment': 'Справочник Несчастный случай'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyAccident.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyAccident.modifyPerson_id == Person.id')


class RbEmergencyCauseCall(Base):
    __tablename__ = 'rbEmergencyCauseCall'
    __table_args__ = {'comment': 'Справочник Повод к вызову'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)
    typeCause = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbEmergencyCauseCall.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyCauseCall.modifyPerson_id == Person.id')


class RbEmergencyDeath(Base):
    __tablename__ = 'rbEmergencyDeath'
    __table_args__ = {'comment': 'Справочник Смерть'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyDeath.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyDeath.modifyPerson_id == Person.id')


class RbEmergencyDiseased(Base):
    __tablename__ = 'rbEmergencyDiseased'
    __table_args__ = {'comment': 'Справочник Больной'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyDiseased.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyDiseased.modifyPerson_id == Person.id')


class RbEmergencyEbriety(Base):
    __tablename__ = 'rbEmergencyEbriety'
    __table_args__ = {'comment': 'Справочник Опьянение'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyEbriety.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyEbriety.modifyPerson_id == Person.id')


class RbEmergencyMethodTransportation(Base):
    __tablename__ = 'rbEmergencyMethodTransportation'
    __table_args__ = {'comment': 'Справочник Способ транспортировки'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyMethodTransportation.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyMethodTransportation.modifyPerson_id == Person.id')


class RbEmergencyPlaceCall(Base):
    __tablename__ = 'rbEmergencyPlaceCall'
    __table_args__ = {'comment': 'Справочник Место вызова'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyPlaceCall.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyPlaceCall.modifyPerson_id == Person.id')


class RbEmergencyPlaceReceptionCall(Base):
    __tablename__ = 'rbEmergencyPlaceReceptionCall'
    __table_args__ = {'comment': 'Справочник Место получения вызова'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyPlaceReceptionCall.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyPlaceReceptionCall.modifyPerson_id == Person.id')


class RbEmergencyReasondDelay(Base):
    __tablename__ = 'rbEmergencyReasondDelays'
    __table_args__ = {'comment': 'Справочник Причина задержки'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyReasondDelay.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyReasondDelay.modifyPerson_id == Person.id')


class RbEmergencyReceivedCall(Base):
    __tablename__ = 'rbEmergencyReceivedCall'
    __table_args__ = {'comment': 'Справочник Вызов получен'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyReceivedCall.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyReceivedCall.modifyPerson_id == Person.id')


class RbEmergencyResult(Base):
    __tablename__ = 'rbEmergencyResult'
    __table_args__ = {'comment': 'Справочник Результат'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'), server_default=alchemy_text("0"))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'), server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyResult.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyResult.modifyPerson_id == Person.id')


class RbEmergencyTransferredTransportation(Base):
    __tablename__ = 'rbEmergencyTransferredTransportation'
    __table_args__ = {'comment': 'Справочник Транспортировку перенес'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyTransferredTransportation.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyTransferredTransportation.modifyPerson_id == Person.id')


class RbEmergencyTypeAsset(Base):
    __tablename__ = 'rbEmergencyTypeAsset'
    __table_args__ = {'comment': 'Справочник Активное посещение'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    codeRegional = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEmergencyTypeAsset.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEmergencyTypeAsset.modifyPerson_id == Person.id')


class RbEpicrisisProperty(Base):
    __tablename__ = 'rbEpicrisisProperty'
    __table_args__ = {'comment': 'Таблица шаблонов свойств разделов эпикризов.'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(64), nullable=False)
    description = Column(String(200), nullable=False)
    type = Column(ForeignKey('rbEpicrisisPropertyType.id'), nullable=False, server_default=alchemy_text("2"))
    defaultValue = Column(String(21400), server_default=alchemy_text("'SELECT \"\" '"))
    valueDomain = Column(String(120))
    printAsTable = Column(TINYINT(1), server_default=alchemy_text("0"))

    rbEpicrisisPropertyType = relationship('RbEpicrisisPropertyType')


class RbEpicrisisTemplate(Base):
    __tablename__ = 'rbEpicrisisTemplates'
    __table_args__ = {'comment': 'Таблица, шаблонов эпикризов.'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(64), nullable=False)
    code = Column(String(64))
    id_orgStructure = Column(String(64), server_default=alchemy_text("' 39,'"))
    printTemplate = Column(String(512), nullable=False, server_default=alchemy_text("'\r<div style=\"font-size:16pt; text-align:center;\">\r\n	<b>\r\n		ГБУЗ «Городская клиническая больница имени Ф.И. Иноземцева<br/>\r\n		Департамента здравоохранения города Москвы»\r\n	</b>\r\n</div>\r\n<div style=\"font-size:14pt; text-align:center;\">\r\n	105187, г. Москва, ул. Фортунатовская, д. 1.\r\n</div>\r\n  '"))
    type = Column(ForeignKey('rbIEMKDocument.id', onupdate='CASCADE'))

    rbIEMKDocument = relationship('RbIEMKDocument')


class RbEquipmentType(Base):
    __tablename__ = 'rbEquipmentType'
    __table_args__ = {'comment': 'Справочник типов оборудования'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEquipmentType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEquipmentType.modifyPerson_id == Person.id')


class RbEventGoal(Base):
    __tablename__ = 'rbEventGoal'
    __table_args__ = {'comment': 'Цель обращения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    regionalCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    federalCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    eventTypePurpose_id = Column(INTEGER(11), nullable=False)
    visitCount = Column(String(7), nullable=False, server_default=alchemy_text("''"))
    netrica_Code = Column(String(64))

    createPerson = relationship('Person', primaryjoin='RbEventGoal.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEventGoal.modifyPerson_id == Person.id')


class RbEventOrder(Base):
    __tablename__ = 'rbEventOrder'
    __table_args__ = {'comment': 'Справочник порядков поступления (обращения)'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    modifyDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8))
    codeKK = Column(String(8))
    name = Column(String(64))
    eisCode = Column(String(1))
    begDate = Column(Date)
    endDate = Column(Date)

    createPerson = relationship('Person', primaryjoin='RbEventOrder.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEventOrder.modifyPerson_id == Person.id')


class RbEventProfile(Base):
    __tablename__ = 'rbEventProfile'
    __table_args__ = {'comment': 'Профили событий'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    regionalCode = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEventProfile.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEventProfile.modifyPerson_id == Person.id')


class RbEventTypePurpose(Base):
    __tablename__ = 'rbEventTypePurpose'
    __table_args__ = {'comment': 'Назначение типа события'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    regionalCode = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(64), nullable=False)
    federalCode = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbEventTypePurpose.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEventTypePurpose.modifyPerson_id == Person.id')


class RbExpenseServiceItem(Base):
    __tablename__ = 'rbExpenseServiceItem'
    __table_args__ = {'comment': 'Статьи затрат услуг'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbExpenseServiceItem.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbExpenseServiceItem.modifyPerson_id == Person.id')


class RbHealthGroup(Base):
    __tablename__ = 'rbHealthGroup'
    __table_args__ = {'comment': 'Группа здоровья'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbHealthGroup.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHealthGroup.modifyPerson_id == Person.id')


class RbHighTechCureKind(Base):
    __tablename__ = 'rbHighTechCureKind'
    __table_args__ = {'comment': 'Виды высокотехнологичной медицинской помощи'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(9), nullable=False)
    name = Column(String(400), nullable=False)
    regionalCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    federalCode = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbHighTechCureKind.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHighTechCureKind.modifyPerson_id == Person.id')


class RbHomeCallQueueStatu(Base):
    __tablename__ = 'rbHomeCallQueueStatus'
    __table_args__ = {'comment': 'Статус заявки вызова врача на дои'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    createPerson = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    flatCode = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    isSelectable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    federalCode = Column(String(128))

    Person = relationship('Person', primaryjoin='RbHomeCallQueueStatu.createPerson == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHomeCallQueueStatu.modifyPerson_id == Person.id')


class RbHospitalBedProfile(Base):
    __tablename__ = 'rbHospitalBedProfile'
    __table_args__ = {'comment': 'Профиль койки'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    regionalCode = Column(String(16))
    name = Column(String(512))
    service_id = Column(ForeignKey('rbService.id', ondelete='SET NULL'))
    eisCode = Column(String(15))
    paidFlag = Column(TINYINT(1), server_default=alchemy_text("0"))
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbHospitalBedProfile.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHospitalBedProfile.modifyPerson_id == Person.id')
    service = relationship('RbService')


class RbHospitalBedShedule(Base):
    __tablename__ = 'rbHospitalBedShedule'
    __table_args__ = {'comment': 'Режим койки'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbHospitalBedShedule.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHospitalBedShedule.modifyPerson_id == Person.id')


class RbHospitalBedType(Base):
    __tablename__ = 'rbHospitalBedType'
    __table_args__ = {'comment': 'Тип койки'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbHospitalBedType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHospitalBedType.modifyPerson_id == Person.id')


class RbHospitalBedsLocationCardType(Base):
    __tablename__ = 'rbHospitalBedsLocationCardType'
    __table_args__ = {'comment': 'РЎРїСЂР°РІРѕС‡РЅРёРє "РњРµСЃС‚Рѕ РЅР°С…РѕР¶РґРµРЅРёСЏ Р°РјР±СѓР»Р°С‚РѕСЂРЅРѕР№ РєР°СЂС‚С‹"'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(24), nullable=False)
    name = Column(String(32), nullable=False)
    color = Column(String(7))

    createPerson = relationship('Person', primaryjoin='RbHospitalBedsLocationCardType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHospitalBedsLocationCardType.modifyPerson_id == Person.id')


class RbHurtFactorType(Base):
    __tablename__ = 'rbHurtFactorType'
    __table_args__ = {'comment': 'Факторы вредности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(250), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbHurtFactorType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHurtFactorType.modifyPerson_id == Person.id')


class RbHurtType(Base):
    __tablename__ = 'rbHurtType'
    __table_args__ = {'comment': 'Тип вредности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(256), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbHurtType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbHurtType.modifyPerson_id == Person.id')


class RbImageMap(Base):
    __tablename__ = 'rbImageMap'
    __table_args__ = {'comment': 'Библиотека изображений'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    image = Column(MEDIUMBLOB, nullable=False)
    markSize = Column(INTEGER(2))

    createPerson = relationship('Person', primaryjoin='RbImageMap.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbImageMap.modifyPerson_id == Person.id')


class RbJobType(Base):
    __tablename__ = 'rbJobType'
    __table_args__ = {'comment': 'Типы ресурсов-услуг (работ)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    group_id = Column(ForeignKey('rbJobType.id', ondelete='SET NULL'))
    code = Column(String(64), nullable=False)
    regionalCode = Column(String(64), nullable=False)
    name = Column(String(128), nullable=False)
    listContext = Column(String(64), nullable=False)
    actionStatusChanger = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actionPersonChanger = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actionDateChanger = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    ticketDuration = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    showOnlyPayed = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    durationVisibility = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    ticketAssignWay = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    jobStatusModifier = Column(INTEGER(11))
    quotingMode = Column(TINYINT(1), server_default=alchemy_text("0"))
    useClosestOrgStructure = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    context = Column(String(64))
    labExchange = Column(TINYINT(4), server_default=alchemy_text("0"))
    instrumental = Column(TINYINT(1), server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbJobType.createPerson_id == Person.id')
    group = relationship('RbJobType', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='RbJobType.modifyPerson_id == Person.id')


class RbLaboratory(Base):
    __tablename__ = 'rbLaboratory'
    __table_args__ = {'comment': 'Лабораторные системы'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    protocol = Column(INTEGER(11), nullable=False)
    address = Column(Text, nullable=False)
    ownName = Column(String(128), nullable=False)
    labName = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbLaboratory.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbLaboratory.modifyPerson_id == Person.id')


class RbLocationCardType(Base):
    __tablename__ = 'rbLocationCardType'
    __table_args__ = {'comment': 'Справочник "Место нахождения амбулаторной карты"'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(24), nullable=False)
    name = Column(String(32), nullable=False)
    color = Column(String(7))

    createPerson = relationship('Person', primaryjoin='RbLocationCardType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbLocationCardType.modifyPerson_id == Person.id')


class RbMKBSubclas(Base):
    __tablename__ = 'rbMKBSubclass'
    __table_args__ = {'comment': 'субклассификация МКБ по 5 знаку'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbMKBSubclas.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMKBSubclas.modifyPerson_id == Person.id')


class RbMealTime(Base):
    __tablename__ = 'rbMealTime'
    __table_args__ = {'comment': 'Справочник Периоды питания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    begTime = Column(Time, nullable=False)
    endTime = Column(Time, nullable=False)

    createPerson = relationship('Person', primaryjoin='RbMealTime.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMealTime.modifyPerson_id == Person.id')


class RbMedicalAidUnit(Base):
    __tablename__ = 'rbMedicalAidUnit'
    __table_args__ = {'comment': 'Код единицы учета медицинской помощи'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(10), nullable=False)
    name = Column(String(64), nullable=False)
    descr = Column(String(64), nullable=False)
    regionalCode = Column(String(2), nullable=False)
    federalCode = Column(String(8), nullable=False)
    netrica_Code = Column(String(65))
    netricaCode = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='RbMedicalAidUnit.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMedicalAidUnit.modifyPerson_id == Person.id')


class RbMedicalGroup(Base):
    __tablename__ = 'rbMedicalGroup'
    __table_args__ = {'comment': 'Медицинская группа'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbMedicalGroup.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMedicalGroup.modifyPerson_id == Person.id')


class RbMedicament(Base):
    __tablename__ = 'rbMedicaments'
    __table_args__ = {'comment': 'Справочник медикаментов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbMedicament.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMedicament.modifyPerson_id == Person.id')


class RbMesSpecification(Base):
    __tablename__ = 'rbMesSpecification'
    __table_args__ = {'comment': 'Особенность выполнения МЭС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    regionalCode = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    done = Column(TINYINT(1), nullable=False)
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbMesSpecification.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbMesSpecification.modifyPerson_id == Person.id')


class RbNomenclature(Base):
    __tablename__ = 'rbNomenclature'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(INTEGER(11))
    group = Column(INTEGER(11), nullable=False)
    mnn = Column(String(45))
    name = Column(String(45), nullable=False)
    characteristic = Column(String(45))
    kind = Column(String(45))
    article = Column(String(45))
    producer = Column(String(45))
    best_before = Column(Date)
    unit_id = Column(INTEGER(11), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbNomenclature.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbNomenclature.modifyPerson_id == Person.id')


class RbNomenclatureClas(Base):
    __tablename__ = 'rbNomenclatureClass'
    __table_args__ = {'comment': 'Классы номенклатуры ЛСиИМН'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(128), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbNomenclatureClas.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbNomenclatureClas.modifyPerson_id == Person.id')


class RbNomenclatureAnalog(Base):
    __tablename__ = 'rbNomenclature_Analog'
    __table_args__ = {'comment': 'Счётчик аналогов для ЛСиИМН'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))

    createPerson = relationship('Person', primaryjoin='RbNomenclatureAnalog.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbNomenclatureAnalog.modifyPerson_id == Person.id')


class RbOBSTypeEi(Base):
    __tablename__ = 'rbOBSType_eis'
    __table_args__ = {'comment': 'Виды обследований ЕИС'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbOBSTypeEi.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbOBSTypeEi.modifyPerson_id == Person.id')


class RbOKF(Base):
    __tablename__ = 'rbOKFS'
    __table_args__ = {'comment': 'ОКФС (форма собственности)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    ownership = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbOKF.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbOKF.modifyPerson_id == Person.id')


class RbOKPF(Base):
    __tablename__ = 'rbOKPF'
    __table_args__ = {'comment': 'ОКПФ (организационно-правовая форма)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbOKPF.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbOKPF.modifyPerson_id == Person.id')


class RbOKVED(Base):
    __tablename__ = 'rbOKVED'
    __table_args__ = {'comment': 'ОКВЭД (виды экономической деятельности)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(10), nullable=False)
    div = Column(String(10), nullable=False)
    _class = Column('class', String(2), nullable=False)
    group_ = Column(String(2), nullable=False)
    vid = Column(String(2), nullable=False)
    OKVED = Column(String(8), nullable=False)
    name = Column(String(250), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbOKVED.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbOKVED.modifyPerson_id == Person.id')


class RbOrgStructureProfile(Base):
    __tablename__ = 'rbOrgStructureProfile'
    __table_args__ = {'comment': 'Профиль отделения. (на данный момент - только для исходящих направлений)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    federalCode = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbOrgStructureProfile.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbOrgStructureProfile.modifyPerson_id == Person.id')


class RbPatientModel(Base):
    __tablename__ = 'rbPatientModel'
    __table_args__ = {'comment': 'Справочник Модель пациента'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(512), nullable=False)
    MKB = Column(LONGTEXT, nullable=False)
    quotaType_id = Column(ForeignKey('QuotaType.id', ondelete='SET NULL'))
    isObsolete = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbPatientModel.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbPatientModel.modifyPerson_id == Person.id')
    quotaType = relationship('QuotaType')


class RbPayRefuseType(Base):
    __tablename__ = 'rbPayRefuseType'
    __table_args__ = {'comment': 'Причины отказа платежа'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(128), nullable=False)
    finance_id = Column(ForeignKey('rbFinance.id'), nullable=False)
    rerun = Column(TINYINT(1), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbPayRefuseType.createPerson_id == Person.id')
    finance = relationship('RbFinance')
    modifyPerson = relationship('Person', primaryjoin='RbPayRefuseType.modifyPerson_id == Person.id')


class RbPersonCategory(Base):
    __tablename__ = 'rbPersonCategory'
    __table_args__ = {'comment': 'Категория врача'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(4), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(40), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbPersonCategory.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbPersonCategory.modifyPerson_id == Person.id')


class RbPolicyKind(Base):
    __tablename__ = 'rbPolicyKind'
    __table_args__ = {'comment': 'Вид полиса (старый, временный, новый)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    regionalCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    federalCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    netrica_Code = Column(String(65), server_default=alchemy_text("'NULL'"))
    EGISZ_code = Column(String(16))
    EGISZ_name = Column(Text)

    createPerson = relationship('Person', primaryjoin='RbPolicyKind.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbPolicyKind.modifyPerson_id == Person.id')


class RbPolicyType(Base):
    __tablename__ = 'rbPolicyType'
    __table_args__ = {'comment': 'Тип полиса'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbPolicyType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbPolicyType.modifyPerson_id == Person.id')


class RbPrerecordQuotaType(Base):
    __tablename__ = 'rbPrerecordQuotaType'
    __table_args__ = {'comment': 'Тип квот для предварительной записи'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    defaultValue = Column(SMALLINT(4), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbPrerecordQuotaType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbPrerecordQuotaType.modifyPerson_id == Person.id')


class RbReasonOfAbsence(Base):
    __tablename__ = 'rbReasonOfAbsence'
    __table_args__ = {'comment': 'Причина отсутствия'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbReasonOfAbsence.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbReasonOfAbsence.modifyPerson_id == Person.id')


class RbReferralType(Base):
    __tablename__ = 'rbReferralType'
    __table_args__ = {'comment': 'Типы направлений'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    netrica_Code = Column(String(6))

    createPerson = relationship('Person', primaryjoin='RbReferralType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbReferralType.modifyPerson_id == Person.id')


class RbRelationType(Base):
    __tablename__ = 'rbRelationType'
    __table_args__ = {'comment': 'Типы связей пациента'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    leftName = Column(String(64), nullable=False)
    rightName = Column(String(64), nullable=False)
    isDirectGenetic = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isBackwardGenetic = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isDirectRepresentative = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isBackwardRepresentative = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isDirectEpidemic = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isBackwardEpidemic = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isDirectDonation = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isBackwardDonation = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    leftSex = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    rightSex = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    regionalCode = Column(String(64), nullable=False)
    regionalReverseCode = Column(String(64), nullable=False)
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbRelationType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbRelationType.modifyPerson_id == Person.id')


class RbScalesValue(Base):
    __tablename__ = 'rbScalesValues'
    __table_args__ = {'comment': 'Таблица Значений Шкал'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(INTEGER(11), nullable=False)
    name = Column(String(30), nullable=False)
    rbScales_id = Column(ForeignKey('rbScales.id'), nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    rbScales = relationship('RbScale')


class RbScene(Base):
    __tablename__ = 'rbScene'
    __table_args__ = {'comment': 'Место выполнения визита'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    serviceModifier = Column(String(128), nullable=False)
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbScene.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbScene.modifyPerson_id == Person.id')


class RbServiceCategory(Base):
    __tablename__ = 'rbServiceCategory'
    __table_args__ = {'comment': 'Параметры для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(3))
    name = Column(String(200))

    createPerson = relationship('Person', primaryjoin='RbServiceCategory.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbServiceCategory.modifyPerson_id == Person.id')


class RbServiceClas(Base):
    __tablename__ = 'rbServiceClass'
    __table_args__ = {'comment': 'Класс услуг'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    section = Column(String(10), nullable=False)
    code = Column(String(3), nullable=False)
    name = Column(String(200), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbServiceClas.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbServiceClas.modifyPerson_id == Person.id')


class RbServiceSection(Base):
    __tablename__ = 'rbServiceSection'
    __table_args__ = {'comment': 'Раздел услуг'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(10), nullable=False)
    name = Column(String(100), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbServiceSection.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbServiceSection.modifyPerson_id == Person.id')


class RbServiceType(Base):
    __tablename__ = 'rbServiceType'
    __table_args__ = {'comment': 'Тип услуг'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    section = Column(String(10), nullable=False)
    code = Column(String(3), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    _class = Column('class', TINYINT(1), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbServiceType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbServiceType.modifyPerson_id == Person.id')


class RbServiceContent(Base):
    __tablename__ = 'rbService_Contents'
    __table_args__ = {'comment': 'Состав сложных услуг'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbService.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    service_id = Column(ForeignKey('rbService.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    required = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbServiceContent.createPerson_id == Person.id')
    master = relationship('RbService', primaryjoin='RbServiceContent.master_id == RbService.id')
    modifyPerson = relationship('Person', primaryjoin='RbServiceContent.modifyPerson_id == Person.id')
    service = relationship('RbService', primaryjoin='RbServiceContent.service_id == RbService.id')


class RbServiceMKB(Base):
    __tablename__ = 'rbService_MKB'
    __table_args__ = {'comment': 'Связь услуг и МКБ'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('rbService.id'), nullable=False)
    mkb = Column(String(8), nullable=False)

    master = relationship('RbService')


class RbSocStatusClas(Base):
    __tablename__ = 'rbSocStatusClass'
    __table_args__ = {'comment': 'Классификатор социальных статусов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    group_id = Column(ForeignKey('rbSocStatusClass.id', ondelete='SET NULL'))
    code = Column(String(8), nullable=False)
    flatCode = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)
    tightControl = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isShowInClientInfo = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    autoCloseDate = Column(TINYINT(4), server_default=alchemy_text("0"))
    softControl = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbSocStatusClas.createPerson_id == Person.id')
    group = relationship('RbSocStatusClas', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='RbSocStatusClas.modifyPerson_id == Person.id')


class RbSofa(Base):
    __tablename__ = 'rbSofa'
    __table_args__ = {'comment': 'Шкала SOFA/ASA'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbSofa.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbSofa.modifyPerson_id == Person.id')


class RbSpecialityQueueShare(Base):
    __tablename__ = 'rbSpecialityQueueShare'
    __table_args__ = {'comment': 'Процентное отношение доступного количества номерков на прием к врачу в зависимости от текущей даты'}

    id = Column(INTEGER(11), primary_key=True)
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    day = Column(TINYINT(3), nullable=False, server_default=alchemy_text("0"))
    available = Column(TINYINT(3), nullable=False, server_default=alchemy_text("0"))

    speciality = relationship('RbSpeciality')


class RbStatusObservationClientType(Base):
    __tablename__ = 'rbStatusObservationClientType'
    __table_args__ = {'comment': 'Справочник "Статус наблюдения пациента"'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(24), nullable=False)
    name = Column(String(32), nullable=False)
    color = Column(String(7))

    createPerson = relationship('Person', primaryjoin='RbStatusObservationClientType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbStatusObservationClientType.modifyPerson_id == Person.id')


class RbStockRecipe(Base):
    __tablename__ = 'rbStockRecipe'
    __table_args__ = {'comment': 'Рецепт для производства ЛСиИМН'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', onupdate='CASCADE'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', onupdate='CASCADE'))
    deleted = Column(TINYINT(1), nullable=False)
    group_id = Column(ForeignKey('rbStockRecipe.id', ondelete='SET NULL', onupdate='CASCADE'))
    code = Column(String(32), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbStockRecipe.createPerson_id == Person.id')
    group = relationship('RbStockRecipe', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='RbStockRecipe.modifyPerson_id == Person.id')


class RbTempInvalidBreak(Base):
    __tablename__ = 'rbTempInvalidBreak'
    __table_args__ = {'comment': 'Нарушение режима ВУТ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    type = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(80), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTempInvalidBreak.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidBreak.modifyPerson_id == Person.id')


class RbTempInvalidDocument(Base):
    __tablename__ = 'rbTempInvalidDocument'
    __table_args__ = {'comment': 'Документ ВУТ, инвалидности или ограничения жизнедеятельности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    type = Column(TINYINT(2), nullable=False)
    code = Column(String(8), nullable=False)
    name = Column(String(80), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTempInvalidDocument.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidDocument.modifyPerson_id == Person.id')


class RbTempInvalidDuplicateReason(Base):
    __tablename__ = 'rbTempInvalidDuplicateReason'
    __table_args__ = {'comment': 'Причина выдачи дупликата документа временной нетрудоспособно'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTempInvalidDuplicateReason.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidDuplicateReason.modifyPerson_id == Person.id')


class RbTempInvalidELNResult(Base):
    __tablename__ = 'rbTempInvalidELN_Result'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    type = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(80), nullable=False)
    able = Column(TINYINT(1), nullable=False)
    closed = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbTempInvalidELNResult.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidELNResult.modifyPerson_id == Person.id')


class RbTempInvalidExtraReason(Base):
    __tablename__ = 'rbTempInvalidExtraReason'
    __table_args__ = {'comment': 'Дополнительные причины ВУТ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    type = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTempInvalidExtraReason.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidExtraReason.modifyPerson_id == Person.id')


class RbTempInvalidReason(Base):
    __tablename__ = 'rbTempInvalidReason'
    __table_args__ = {'comment': 'Причина временной нетрудоспособности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    type = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    requiredDiagnosis = Column(TINYINT(1), nullable=False)
    grouping = Column(TINYINT(1), nullable=False)
    primary = Column(INTEGER(11), nullable=False)
    prolongate = Column(INTEGER(11), nullable=False)
    restriction = Column(INTEGER(11), nullable=False)
    regionalCode = Column(String(3), nullable=False)
    netricaCode = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='RbTempInvalidReason.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidReason.modifyPerson_id == Person.id')


class RbTempInvalidResult(Base):
    __tablename__ = 'rbTempInvalidResult'
    __table_args__ = {'comment': 'Результат периода ВУТ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    type = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(80), nullable=False)
    able = Column(TINYINT(1), nullable=False)
    closed = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    status = Column(TINYINT(2), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTempInvalidResult.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidResult.modifyPerson_id == Person.id')


class RbTestGroup(Base):
    __tablename__ = 'rbTestGroup'
    __table_args__ = {'comment': 'Группы тестов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(32), nullable=False)
    group_id = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='RbTestGroup.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTestGroup.modifyPerson_id == Person.id')


class RbThesauru(Base):
    __tablename__ = 'rbThesaurus'
    __table_args__ = {'comment': 'Тезаурус: набор понятий и терминов для конструирования элеме'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    group_id = Column(ForeignKey('rbThesaurus.id', ondelete='CASCADE'))
    code = Column(String(20), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(250), nullable=False, server_default=alchemy_text("''"))
    template = Column(String(250), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbThesauru.createPerson_id == Person.id')
    group = relationship('RbThesauru', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='RbThesauru.modifyPerson_id == Person.id')


class RbTissueType(Base):
    __tablename__ = 'rbTissueType'
    __table_args__ = {'comment': 'Типы тканей'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(64), nullable=False)
    name = Column(String(128), nullable=False)
    group_id = Column(ForeignKey('rbTissueType.id', ondelete='SET NULL'))
    sex = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    counterManualInput = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    counterResetType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    issueExternalIdLimit = Column(INTEGER(11), server_default=alchemy_text("0"))
    masterActionType_id = Column(INTEGER(11))
    lis_id = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='RbTissueType.createPerson_id == Person.id')
    group = relationship('RbTissueType', remote_side=[id])
    modifyPerson = relationship('Person', primaryjoin='RbTissueType.modifyPerson_id == Person.id')


class RbTransf(Base):
    __tablename__ = 'rbTransf'
    __table_args__ = {'comment': 'Признак поступления / перевода для случая'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTransf.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTransf.modifyPerson_id == Person.id')


class RbTraumaType(Base):
    __tablename__ = 'rbTraumaType'
    __table_args__ = {'comment': 'Типы травмы'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTraumaType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTraumaType.modifyPerson_id == Person.id')


class RbUnit(Base):
    __tablename__ = 'rbUnit'
    __table_args__ = {'comment': 'Единицы измерения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(48), nullable=False)
    name = Column(String(64), nullable=False)
    netrica_Code = Column(String(9))
    print_name = Column(String(64), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbUnit.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbUnit.modifyPerson_id == Person.id')


class RbUserProfileHidden(Base):
    __tablename__ = 'rbUserProfile_Hidden'
    __table_args__ = {'comment': 'Список скрываемых элементов интерфейса для текущего профиля прав'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbUserProfile.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    objectName = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbUserProfileHidden.createPerson_id == Person.id')
    master = relationship('RbUserProfile')
    modifyPerson = relationship('Person', primaryjoin='RbUserProfileHidden.modifyPerson_id == Person.id')


class RbUserProfilePenalty(Base):
    __tablename__ = 'rbUserProfile_Penalty'
    __table_args__ = {'comment': 'Штрафы включенных элементов интерфейса для текущего профиля прав'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbUserProfile.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    objectName = Column(String(128), nullable=False)
    penalty = Column(String(15), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbUserProfilePenalty.createPerson_id == Person.id')
    master = relationship('RbUserProfile')
    modifyPerson = relationship('Person', primaryjoin='RbUserProfilePenalty.modifyPerson_id == Person.id')


class RbUserRight(Base):
    __tablename__ = 'rbUserRight'
    __table_args__ = {'comment': 'Права пользователей'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(64), nullable=False)
    name = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbUserRight.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbUserRight.modifyPerson_id == Person.id')


class RbVisitType(Base):
    __tablename__ = 'rbVisitType'
    __table_args__ = {'comment': 'Тип визита'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    serviceModifier = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbVisitType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbVisitType.modifyPerson_id == Person.id')


class RcField(Base):
    __tablename__ = 'rcField'
    __table_args__ = {'comment': 'Поля для запросов в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    name = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    field = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    ref_id = Column(INTEGER(11))
    rcTable_id = Column(ForeignKey('rcTable.id', ondelete='SET NULL', onupdate='CASCADE'))
    description = Column(Text)
    visible = Column(TINYINT(1), server_default=alchemy_text("1"))

    rcTable = relationship('RcTable')


class RcParam(Base):
    __tablename__ = 'rcParam'
    __table_args__ = {'comment': 'Параметры для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    code = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    title = Column(String(45), nullable=False, server_default=alchemy_text("''"))
    type_id = Column(ForeignKey('rcParamType.id', ondelete='SET NULL', onupdate='CASCADE'))
    valueType_id = Column(ForeignKey('rcValueType.id', ondelete='SET NULL', onupdate='CASCADE'))
    tableName = Column(String(30), nullable=False, server_default=alchemy_text("''"))

    type = relationship('RcParamType')
    valueType = relationship('RcValueType')


class RcQuery(Base):
    __tablename__ = 'rcQuery'
    __table_args__ = {'comment': 'Запрос'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    name = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    mainTable_id = Column(ForeignKey('rcTable.id', ondelete='SET NULL', onupdate='CASCADE'))
    stateTree = Column(String(256), server_default=alchemy_text("''"))
    referencedField = Column(String(256), server_default=alchemy_text("''"))
    text = Column(Text)

    mainTable = relationship('RcTable')


class SmpPersonType(Base):
    __tablename__ = 'smpPersonType'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(64))
    code = Column(String(10))
    post_id = Column(ForeignKey('rbPost.id'))

    post = relationship('RbPost')


class ActionType(Base):
    __tablename__ = 'ActionType'
    __table_args__ = {'comment': 'Описание мероприятия, связанного с событием: направления, вы'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    _class = Column('class', TINYINT(1), nullable=False)
    group_id = Column(ForeignKey('ActionType.id'))
    code = Column(String(20), nullable=False)
    name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    flatCode = Column(String(64), nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    office = Column(String(32), nullable=False)
    showInForm = Column(TINYINT(1), nullable=False)
    genTimetable = Column(TINYINT(1), nullable=False)
    quotaType_id = Column(ForeignKey('QuotaType.id', ondelete='SET NULL'))
    context = Column(String(64), nullable=False)
    amount = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("1"))
    amountEvaluation = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    defaultStatus = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    defaultDirectionDate = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    defaultPlannedEndDate = Column(TINYINT(1), nullable=False)
    defaultEndDate = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    defaultExecPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    defaultSetPerson_id = Column(ForeignKey('Person.id'))
    defaultPersonInEvent = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    defaultPersonInEditor = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    defaultMKB = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    defaultMorphology = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isMorphologyRequired = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    defaultOrg_id = Column(ForeignKey('Organisation.id', ondelete='SET NULL'))
    showTime = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    maxOccursInEvent = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    isMES = Column(INTEGER(11))
    nomenclativeService_id = Column(ForeignKey('rbService.id', ondelete='SET NULL'))
    isPreferable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    prescribedType_id = Column(ForeignKey('ActionType.id', ondelete='SET NULL', onupdate='CASCADE'))
    shedule_id = Column(ForeignKey('rbActionShedule.id', ondelete='SET NULL', onupdate='CASCADE'))
    isRequiredCoordination = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isNomenclatureExpense = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hasAssistant = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    propertyAssignedVisible = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    propertyUnitVisible = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    propertyNormVisible = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    propertyEvaluationVisible = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    serviceType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actualAppointmentDuration = Column(SMALLINT(6), nullable=False, server_default=alchemy_text("0"))
    isSubstituteEndDateToEvent = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isPrinted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    defaultMES = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    frequencyCount = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    frequencyPeriod = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    frequencyPeriodType = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    isStrictFrequency = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isFrequencyPeriodByCalendar = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    counter_id = Column(INTEGER(11))
    isCustomSum = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    recommendationExpirePeriod = Column(INTEGER(11), server_default=alchemy_text("0"))
    recommendationControl = Column(TINYINT(1), server_default=alchemy_text("0"))
    isExecRequiredForEventExec = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    locked = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isActiveGroup = Column(TINYINT(1), nullable=False)
    lis_code = Column(String(32))
    filledLock = Column(TINYINT(1), server_default=alchemy_text("0"))
    defaultBeginDate = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    refferalType_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    filterPosts = Column(TINYINT(1), server_default=alchemy_text("0"))
    filterSpecialities = Column(TINYINT(1), server_default=alchemy_text("0"))
    isIgnoreEventExecDate = Column(TINYINT(1), server_default=alchemy_text("0"))
    advancePaymentRequired = Column(TINYINT(1), server_default=alchemy_text("0"))
    checkPersonSet = Column(TINYINT(1), server_default=alchemy_text("1"))
    defaultIsUrgent = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    checkEnterNote = Column(TINYINT(1), server_default=alchemy_text("0"))
    formulaAlias = Column(String(10))
    isAllowedAfterDeath = Column(SMALLINT(1), server_default=alchemy_text("0"))
    isAllowedDateAfterDeath = Column(SMALLINT(1), server_default=alchemy_text("0"))
    eventStatusMod = Column(SMALLINT(1), server_default=alchemy_text("0"))
    defaultSetPersonInEvent = Column(TINYINT(4), server_default=alchemy_text("2"))
    consultationTypeId = Column(INTEGER(11))
    showAPOrg = Column(TINYINT(1), server_default=alchemy_text("1"))
    showAPNotes = Column(TINYINT(1), server_default=alchemy_text("1"))

    createPerson = relationship('Person', primaryjoin='ActionType.createPerson_id == Person.id')
    defaultExecPerson = relationship('Person', primaryjoin='ActionType.defaultExecPerson_id == Person.id')
    defaultOrg = relationship('Organisation')
    defaultSetPerson = relationship('Person', primaryjoin='ActionType.defaultSetPerson_id == Person.id')
    group = relationship('ActionType', remote_side=[id], primaryjoin='ActionType.group_id == ActionType.id')
    modifyPerson = relationship('Person', primaryjoin='ActionType.modifyPerson_id == Person.id')
    nomenclativeService = relationship('RbService')
    prescribedType = relationship('ActionType', remote_side=[id], primaryjoin='ActionType.prescribedType_id == ActionType.id')
    quotaType = relationship('QuotaType')
    refferalType = relationship('Person', primaryjoin='ActionType.refferalType_id == Person.id')
    shedule = relationship('RbActionShedule')


class SmpActionType(ActionType):
    __tablename__ = 'smpActionType'

    action_id = Column(ForeignKey('ActionType.id'), primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    code = Column(VARCHAR(10), nullable=False)


class Addres(Base):
    __tablename__ = 'Address'
    __table_args__ = {'comment': 'Адрес'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    house_id = Column(ForeignKey('AddressHouse.id'), nullable=False)
    flat = Column(String(6), nullable=False)
    regBegDate = Column(Date)
    regEndDate = Column(Date)

    createPerson = relationship('Person', primaryjoin='Addres.createPerson_id == Person.id')
    house = relationship('AddressHouse')
    modifyPerson = relationship('Person', primaryjoin='Addres.modifyPerson_id == Person.id')


class AddressAreaItem(Base):
    __tablename__ = 'AddressAreaItem'
    __table_args__ = {'comment': 'Дома и квартиры по участкам'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    LPU_id = Column(INTEGER(11), nullable=False)
    struct_id = Column(ForeignKey('OrgStructure.id'), nullable=False)
    house_id = Column(ForeignKey('AddressHouse.id'), nullable=False)
    flatRange = Column(TINYINT(4), nullable=False)
    begFlat = Column(INTEGER(11), nullable=False)
    endFlat = Column(INTEGER(11), nullable=False)
    begDate = Column(Date, nullable=False)
    endDate = Column(Date)

    createPerson = relationship('Person', primaryjoin='AddressAreaItem.createPerson_id == Person.id')
    house = relationship('AddressHouse')
    modifyPerson = relationship('Person', primaryjoin='AddressAreaItem.modifyPerson_id == Person.id')
    struct = relationship('OrgStructure')


class Client(Base):
    __tablename__ = 'Client'
    __table_args__ = {'comment': 'Главная запись пациента'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    attendingPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    lastName = Column(String(30), nullable=False)
    firstName = Column(String(30), nullable=False)
    patrName = Column(String(30), nullable=False)
    birthDate = Column(Date, nullable=False)
    birthTime = Column(Time, nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    SNILS = Column(CHAR(11), nullable=False)
    bloodType_id = Column(ForeignKey('rbBloodType.id', ondelete='SET NULL'))
    bloodDate = Column(Date)
    bloodNotes = Column(TINYTEXT, nullable=False)
    growth = Column(String(16), nullable=False)
    weight = Column(String(16), nullable=False)
    embryonalPeriodWeek = Column(String(16), nullable=False)
    birthPlace = Column(String(120), nullable=False, server_default=alchemy_text("''"))
    diagNames = Column(String(64), nullable=False)
    chartBeginDate = Column(Date)
    rbInfoSource_id = Column(ForeignKey('rbInfoSource.id', ondelete='SET NULL'))
    notes = Column(TINYTEXT, nullable=False)
    IIN = Column(String(15))
    isConfirmSendingData = Column(TINYINT(4))
    isUnconscious = Column(TINYINT(1), server_default=alchemy_text("0"))
    hasImplants = Column(TINYINT(1), server_default=alchemy_text("0"))
    hasProsthesis = Column(TINYINT(1), server_default=alchemy_text("0"))
    filial = Column(INTEGER(10))
    dataTransferConfirmationDate = Column(Date)
    Old_ID = Column(String(50))
    mpi = Column(String(256))
    injury = Column(String(2553))
    incidentPlace = Column(String(2553))
    incidentDate = Column(DateTime)

    attendingPerson = relationship('Person', primaryjoin='Client.attendingPerson_id == Person.id')
    bloodType = relationship('RbBloodType')
    createPerson = relationship('Person', primaryjoin='Client.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='Client.modifyPerson_id == Person.id')
    rbInfoSource = relationship('RbInfoSource')


class DentalFormulatooth(Base):
    __tablename__ = 'DentalFormulaTeeth'
    __table_args__ = {'comment': 'Записи для зубов зубной формулы'}

    id = Column(INTEGER(11), primary_key=True)
    formula_id = Column(ForeignKey('DentalFormula.id'), nullable=False)
    number = Column(String(2), nullable=False)
    is_deciduous = Column(TINYINT(1), server_default=alchemy_text("0"))
    status_id = Column(ForeignKey('rbToothStatus.id'))
    mobility = Column(INTEGER(11), server_default=alchemy_text("0"))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))

    formula = relationship('DentalFormula')
    status = relationship('RbToothStatu')


class DloDrugFormulary(Base):
    __tablename__ = 'DloDrugFormulary'
    __table_args__ = {'comment': 'Формуляр лекарственных средств ДЛО для подразделения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', onupdate='CASCADE'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', onupdate='CASCADE'))
    type = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    orgStructure_id = Column(ForeignKey('OrgStructure.id', onupdate='CASCADE'))
    isActive = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    isReadOnly = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='DloDrugFormulary.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='DloDrugFormulary.modifyPerson_id == Person.id')
    orgStructure = relationship('OrgStructure')


class DrugFormulary(Base):
    __tablename__ = 'DrugFormulary'
    __table_args__ = {'comment': 'Формуляр лекарственных средств для подразделения.'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    type = Column(INTEGER(11), server_default=alchemy_text("0"))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    isActive = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    orgStructure_id = Column(ForeignKey('OrgStructure.id', onupdate='CASCADE'), nullable=False)
    code1C = Column(String(100), nullable=False, server_default=alchemy_text("''"))

    orgStructure = relationship('OrgStructure')


class ECRCheckItem(Base):
    __tablename__ = 'ECRCheckItem'
    __table_args__ = {'comment': 'Элементы чека/кассовой операции'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ECROperation.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(256), nullable=False)
    quantity = Column(Float(asdecimal=True), nullable=False)
    price = Column(Float(asdecimal=True), nullable=False)
    accountItem_id = Column(INTEGER(11))
    succesful = Column(TINYINT(1))

    master = relationship('ECROperation')


class EmergencyBrigadePersonnel(Base):
    __tablename__ = 'EmergencyBrigade_Personnel'
    __table_args__ = {'comment': 'Состав бригады СМП'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('EmergencyBrigade.id'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    person_id = Column(ForeignKey('Person.id'), nullable=False)
    role_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    master = relationship('EmergencyBrigade')
    person = relationship('Person')


class EmergencyCall(Base):
    __tablename__ = 'EmergencyCall'
    __table_args__ = {'comment': 'Скорая помощь/Вызов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE'), nullable=False)
    numberCardCall = Column(String(64), nullable=False)
    brigade_id = Column(ForeignKey('EmergencyBrigade.id'))
    causeCall_id = Column(ForeignKey('rbEmergencyCauseCall.id'))
    whoCallOnPhone = Column(String(64), nullable=False)
    numberPhone = Column(String(32), nullable=False)
    begDate = Column(DateTime, nullable=False)
    passDate = Column(DateTime, nullable=False)
    departureDate = Column(DateTime, nullable=False)
    arrivalDate = Column(DateTime, nullable=False)
    finishServiceDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime)
    placeReceptionCall_id = Column(ForeignKey('rbEmergencyPlaceReceptionCall.id'))
    receivedCall_id = Column(ForeignKey('rbEmergencyReceivedCall.id'))
    reasondDelays_id = Column(ForeignKey('rbEmergencyReasondDelays.id'))
    resultCall_id = Column(ForeignKey('rbEmergencyResult.id'))
    accident_id = Column(ForeignKey('rbEmergencyAccident.id'))
    death_id = Column(ForeignKey('rbEmergencyDeath.id'))
    ebriety_id = Column(ForeignKey('rbEmergencyEbriety.id'))
    diseased_id = Column(ForeignKey('rbEmergencyDiseased.id'))
    placeCall_id = Column(ForeignKey('rbEmergencyPlaceCall.id'))
    methodTransport_id = Column(ForeignKey('rbEmergencyMethodTransportation.id'))
    transfTransport_id = Column(ForeignKey('rbEmergencyTransferredTransportation.id'))
    renunOfHospital = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    faceRenunOfHospital = Column(String(64), nullable=False)
    disease = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    birth = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    pregnancyFailure = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    noteCall = Column(Text, nullable=False)
    KLADRStreetCode = Column(String(17), nullable=False)
    house = Column(String(8), nullable=False)
    build = Column(String(8), nullable=False)
    flat = Column(String(8), nullable=False)
    address_freeInput = Column(String(200), nullable=False)

    accident = relationship('RbEmergencyAccident')
    brigade = relationship('EmergencyBrigade')
    causeCall = relationship('RbEmergencyCauseCall')
    createPerson = relationship('Person', primaryjoin='EmergencyCall.createPerson_id == Person.id')
    death = relationship('RbEmergencyDeath')
    diseased = relationship('RbEmergencyDiseased')
    ebriety = relationship('RbEmergencyEbriety')
    event = relationship('Event')
    methodTransport = relationship('RbEmergencyMethodTransportation')
    modifyPerson = relationship('Person', primaryjoin='EmergencyCall.modifyPerson_id == Person.id')
    placeCall = relationship('RbEmergencyPlaceCall')
    placeReceptionCall = relationship('RbEmergencyPlaceReceptionCall')
    reasondDelays = relationship('RbEmergencyReasondDelay')
    receivedCall = relationship('RbEmergencyReceivedCall')
    resultCall = relationship('RbEmergencyResult')
    transfTransport = relationship('RbEmergencyTransferredTransportation')


class EventScalesValue(Base):
    __tablename__ = 'EventScalesValues'
    __table_args__ = {'comment': 'Таблица Сохранения Выбранных Значений Шкал'}

    id = Column(INTEGER(11), primary_key=True)
    event_id = Column(ForeignKey('Event.id'), nullable=False)
    id_scales = Column(ForeignKey('rbScales.id'), nullable=False)
    id_scales_values = Column(ForeignKey('rbScalesValues.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    freeInput = Column(String(100), nullable=False, server_default=alchemy_text("''"))

    event = relationship('Event')
    rbScale = relationship('RbScale')
    rbScalesValue = relationship('RbScalesValue')


class EventType(Base):
    __tablename__ = 'EventType'
    __table_args__ = {'comment': 'Тип события'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    purpose_id = Column(ForeignKey('rbEventTypePurpose.id'))
    finance_id = Column(ForeignKey('rbFinance.id', ondelete='SET NULL'))
    scene_id = Column(ForeignKey('rbScene.id', ondelete='SET NULL'))
    visitServiceModifier = Column(String(128), nullable=False)
    visitServiceFilter = Column(String(32), nullable=False)
    visitFinance = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actionFinance = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    actionContract = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    period = Column(TINYINT(4), nullable=False)
    singleInPeriod = Column(TINYINT(4), nullable=False)
    isLong = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    dateInput = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    service_id = Column(ForeignKey('rbService.id', ondelete='SET NULL'))
    context = Column(String(64), nullable=False)
    form = Column(String(64), nullable=False)
    minDuration = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    maxDuration = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    showStatusActionsInPlanner = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    showDiagnosticActionsInPlanner = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    showCureActionsInPlanner = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    showMiscActionsInPlanner = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    limitStatusActionsInput = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    limitDiagnosticActionsInput = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    limitCureActionsInput = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    limitMiscActionsInput = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    showTime = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    medicalAidKind_id = Column(ForeignKey('rbMedicalAidKind.id'))
    medicalAidType_id = Column(ForeignKey('rbMedicalAidType.id'))
    eventProfile_id = Column(ForeignKey('rbEventProfile.id', ondelete='SET NULL'))
    mesRequired = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    defaultMesSpecification_id = Column(INTEGER(11))
    mesCodeMask = Column(String(64), server_default=alchemy_text("''"))
    mesNameMask = Column(String(64), server_default=alchemy_text("''"))
    counter_id = Column(ForeignKey('rbCounter.id'))
    isExternal = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    generateExternalIdOnSave = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    externalIdAsAccountNumber = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    counterType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hasAssistant = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hasCurator = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hasVisitAssistant = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    canHavePayableActions = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isRequiredCoordination = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isOrgStructurePriority = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isTakenTissue = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isSetContractNumFromCounter = Column(TINYINT(4))
    sex = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    age = Column(String(220), nullable=False)
    isOnJobPayedFilter = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    permitAnyActionDate = Column(TINYINT(1), nullable=False)
    prefix = Column(String(8))
    exposeGrouped = Column(SMALLINT(6), nullable=False, server_default=alchemy_text("0"))
    showLittleStranger = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    uniqueExternalId = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    uniqueExternalIdInThisYear = Column(TINYINT(1), server_default=alchemy_text("0"))
    defaultOrder = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    inheritDiagnosis = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    diagnosisSetDateVisible = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    isResetSetDate = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isAvailInFastCreateMode = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    caseCast_id = Column(ForeignKey('rbCaseCast.id', onupdate='CASCADE'))
    defaultEndTime = Column(Time)
    isCheck_KSG = Column(TINYINT(1))
    weekdays = Column(TINYINT(1), nullable=False, server_default=alchemy_text("5"))
    exposeConfirmation = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    needMesPerformPercent = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    showZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    purposeFilter = Column(TINYINT(1), server_default=alchemy_text("0"))
    goalFilter = Column(TINYINT(1), server_default=alchemy_text("0"))
    setFilterStandard = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    inheritResult = Column(TINYINT(1), server_default=alchemy_text("1"))
    eventKind_id = Column(ForeignKey('rbEventKind.id'))
    inheritCheckupResult = Column(TINYINT(1), server_default=alchemy_text("1"))
    payerAutoFilling = Column(TINYINT(1), server_default=alchemy_text("0"))
    dispByMobileTeam = Column(TINYINT(1), server_default=alchemy_text("0"))
    filterPosts = Column(TINYINT(1), server_default=alchemy_text("0"))
    filterSpecialities = Column(TINYINT(1), server_default=alchemy_text("0"))
    compulsoryServiceStopIgnore = Column(TINYINT(1), server_default=alchemy_text("0"))
    voluntaryServiceStopIgnore = Column(TINYINT(1), server_default=alchemy_text("0"))
    inheritGoal = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    MSE = Column(TINYINT(1), server_default=alchemy_text("0"))
    netrica_Code = Column(String(65))
    reqDN = Column(TINYINT(1))
    reqHealthGroup = Column(TINYINT(1))
    isAddTreatmentToDeath = Column(TINYINT(1), nullable=False)
    needReferal = Column(TINYINT(1), server_default=alchemy_text("0"))
    referalDateActualityDays = Column(INTEGER(11), server_default=alchemy_text("0"))
    eventGoal = Column(INTEGER(11))
    result = Column(INTEGER(11))
    MKB = Column(String(8))
    postfix = Column(String(200))
    limitAnalysesActionsInput = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isAutoPrint = Column(TINYINT(1), server_default=alchemy_text("1"))
    chk_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkMKB_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkReason_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkstady_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkstady_T_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkstady_N_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkstady_M_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkDate_ZNO = Column(TINYINT(1), server_default=alchemy_text("0"))
    isKSGCriterion = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkConsiliumData = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkSurgeryCure = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkPillsTherapy = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkRadiationTherapy = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkChemyTherapy = Column(TINYINT(1), server_default=alchemy_text("0"))
    chk_SendInIEMK = Column(TINYINT(1), server_default=alchemy_text("0"))
    isSeveralEvents = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkTransf = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    transfId = Column(INTEGER(11))
    IEMKSend = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isKslpShow = Column(TINYINT(1), server_default=alchemy_text("0"))
    isFilterKSLP = Column(TINYINT(1), server_default=alchemy_text("0"))
    availableForExternal = Column(TINYINT(1), server_default=alchemy_text("0"))
    isCheckSocStatus = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    visit_circumstances = Column(String(10))
    chkCheckMedicalSpecialtyServices = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isDnChoiceConstraint = Column(TINYINT(1), server_default=alchemy_text("1"))
    defaultNosologyTypeId = Column(ForeignKey('rbDiagnosisNosologyType.id', ondelete='SET NULL', onupdate='CASCADE'))
    defaultRationaleId = Column(ForeignKey('rbDiagnosisRationale.id', ondelete='SET NULL', onupdate='CASCADE'))
    chkMorphDiag = Column(TINYINT(1), server_default=alchemy_text("0"))
    chkTumorTopography = Column(TINYINT(1), server_default=alchemy_text("0"))
    filterOrgstructure = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    filterPersons = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    caseCast = relationship('RbCaseCast')
    counter = relationship('RbCounter')
    createPerson = relationship('Person', primaryjoin='EventType.createPerson_id == Person.id')
    rbDiagnosisNosologyType = relationship('RbDiagnosisNosologyType')
    rbDiagnosisRationale = relationship('RbDiagnosisRationale')
    eventKind = relationship('RbEventKind')
    eventProfile = relationship('RbEventProfile')
    finance = relationship('RbFinance')
    medicalAidKind = relationship('RbMedicalAidKind')
    medicalAidType = relationship('RbMedicalAidType')
    modifyPerson = relationship('Person', primaryjoin='EventType.modifyPerson_id == Person.id')
    purpose = relationship('RbEventTypePurpose')
    scene = relationship('RbScene')
    service = relationship('RbService')


class EventFeed(Base):
    __tablename__ = 'Event_Feed'
    __table_args__ = {'comment': 'Питание'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    diet_id = Column(ForeignKey('rbDiet.id'))
    courtingDiet_id = Column(ForeignKey('rbDiet.id'))

    courtingDiet = relationship('RbDiet', primaryjoin='EventFeed.courtingDiet_id == RbDiet.id')
    createPerson = relationship('Person', primaryjoin='EventFeed.createPerson_id == Person.id')
    diet = relationship('RbDiet', primaryjoin='EventFeed.diet_id == RbDiet.id')
    event = relationship('Event')
    modifyPerson = relationship('Person', primaryjoin='EventFeed.modifyPerson_id == Person.id')


class EventHospitalBedsLocationCard(Base):
    __tablename__ = 'Event_HospitalBedsLocationCard'
    __table_args__ = {'comment': 'Место нахождения амбулаторной карты'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    event_id = Column(ForeignKey('Event.id'), nullable=False)
    locationCardType_id = Column(ForeignKey('rbHospitalBedsLocationCardType.id'), nullable=False)
    moveDate = Column(Date)
    returnDate = Column(Date)

    event = relationship('Event')
    locationCardType = relationship('RbHospitalBedsLocationCardType')


class EventPayment(Base):
    __tablename__ = 'Event_Payment'
    __table_args__ = {'comment': 'Оплата за платные услуги'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(ForeignKey('Event.id', ondelete='CASCADE'), nullable=False)
    date = Column(Date, nullable=False)
    cashOperation_id = Column(ForeignKey('rbCashOperation.id'))
    sum = Column(Float(asdecimal=True), nullable=False)
    typePayment = Column(TINYINT(1), nullable=False)
    settlementAccount = Column(String(64))
    bank_id = Column(ForeignKey('Bank.id'))
    numberCreditCard = Column(String(64))
    cashBox = Column(String(32), nullable=False)
    cheque = Column(String(64))

    bank = relationship('Bank')
    cashOperation = relationship('RbCashOperation')
    createPerson = relationship('Person', primaryjoin='EventPayment.createPerson_id == Person.id')
    master = relationship('Event')
    modifyPerson = relationship('Person', primaryjoin='EventPayment.modifyPerson_id == Person.id')


class InformerMessageReadMark(Base):
    __tablename__ = 'InformerMessage_readMark'
    __table_args__ = {'comment': 'Отметка прочтения сообщения информатора'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('InformerMessage.id', ondelete='CASCADE'), nullable=False)
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))

    master = relationship('InformerMessage')
    person = relationship('Person')


class LicenceService(Base):
    __tablename__ = 'Licence_Service'
    __table_args__ = {'comment': 'Сервисы в лицензии'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('Licence.id'), nullable=False)
    service_id = Column(ForeignKey('rbService.id'), nullable=False)

    master = relationship('Licence')
    service = relationship('RbService')


class OrgStructureAddres(Base):
    __tablename__ = 'OrgStructure_Address'
    __table_args__ = {'comment': 'Адрес, принадлежащий подразделению'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    house_id = Column(ForeignKey('AddressHouse.id', onupdate='CASCADE'), nullable=False)
    firstFlat = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    lastFlat = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))

    house = relationship('AddressHouse')
    master = relationship('OrgStructure')


class OrgStructureDisabledAttendance(Base):
    __tablename__ = 'OrgStructure_DisabledAttendance'
    __table_args__ = {'comment': 'Запрет обслуживания'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    attachType_id = Column(ForeignKey('rbAttachType.id', ondelete='CASCADE', onupdate='CASCADE'))
    disabledType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    attachType = relationship('RbAttachType')
    master = relationship('OrgStructure')


class OrgStructureEquipment(Base):
    __tablename__ = 'OrgStructure_Equipment'
    __table_args__ = {'comment': 'Оборудование прикрепленное к подразделению'}

    id = Column(INTEGER(11), primary_key=True)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'), nullable=False)
    equipment_id = Column(INTEGER(11), nullable=False)

    master = relationship('OrgStructure')


class OrgStructureGap(Base):
    __tablename__ = 'OrgStructure_Gap'
    __table_args__ = {'comment': 'Расписание перерывов в работе подразделений с учетом специал'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    begTime = Column(Time, nullable=False)
    endTime = Column(Time, nullable=False)
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='CASCADE'))
    person_id = Column(ForeignKey('Person.id'))

    master = relationship('OrgStructure')
    person = relationship('Person')
    speciality = relationship('RbSpeciality')


class OrgStructureHospitalBed(Base):
    __tablename__ = 'OrgStructure_HospitalBed'
    __table_args__ = {'comment': 'Койки в подразделениях'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    code = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    isPermanent = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    type_id = Column(ForeignKey('rbHospitalBedType.id'))
    profile_id = Column(ForeignKey('rbHospitalBedProfile.id'))
    relief = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    schedule_id = Column(ForeignKey('rbHospitalBedShedule.id'))
    begDate = Column(Date)
    endDate = Column(Date)
    sex = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    age = Column(String(9), nullable=False)
    involution = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    begDateInvolute = Column(Date)
    endDateInvolute = Column(Date)
    ward = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    quota = Column(INTEGER(3), server_default=alchemy_text("0"))
    paidFlag = Column(TINYINT(1), server_default=alchemy_text("0"))

    master = relationship('OrgStructure')
    profile = relationship('RbHospitalBedProfile')
    schedule = relationship('RbHospitalBedShedule')
    type = relationship('RbHospitalBedType')


class OrgStructureJob(Base):
    __tablename__ = 'OrgStructure_Job'
    __table_args__ = {'comment': 'Предоставляемые подразделениями ресурсы, и умолчания для гра'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    jobType_id = Column(ForeignKey('rbJobType.id', ondelete='CASCADE'))
    begTime = Column(Time, nullable=False)
    endTime = Column(Time, nullable=False)
    quantity = Column(INTEGER(11), nullable=False)
    lastAccessibleDate = Column(Date, nullable=False)
    isVisibleInDR = Column(TINYINT(4), server_default=alchemy_text("1"))
    person_id = Column(INTEGER(11))

    jobType = relationship('RbJobType')
    master = relationship('OrgStructure')


class OrgStructureProfile(Base):
    __tablename__ = 'OrgStructure_Profile'
    __table_args__ = {'comment': 'Профиль Подразделений'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'), nullable=False)
    medicalAidProfile_id = Column(INTEGER(11))
    referralType_id = Column(INTEGER(11), nullable=False)

    master = relationship('OrgStructure')


class OrgStructureStock(Base):
    __tablename__ = 'OrgStructure_Stock'
    __table_args__ = {'comment': 'Планируемые запасы ЛСиИМН на складе подразделения'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    nomenclature_id = Column(ForeignKey('rbNomenclature.id', onupdate='CASCADE'))
    finance_id = Column(ForeignKey('rbFinance.id', onupdate='CASCADE'))
    constrainedQnt = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    orderQnt = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))

    finance = relationship('RbFinance')
    master = relationship('OrgStructure')
    nomenclature = relationship('RbNomenclature')


class OrganisationAccount(Base):
    __tablename__ = 'Organisation_Account'
    __table_args__ = {'comment': 'Расчетный счет'}

    id = Column(INTEGER(11), primary_key=True)
    organisation_id = Column(INTEGER(11), nullable=False)
    bankName = Column(String(128), nullable=False)
    name = Column(String(20), nullable=False)
    notes = Column(TINYTEXT, nullable=False)
    bank_id = Column(ForeignKey('Bank.id'), nullable=False)
    cash = Column(TINYINT(1), nullable=False)
    personalAccount = Column(String(20), nullable=False)

    bank = relationship('Bank')


class OrganisationPolicySerial(Base):
    __tablename__ = 'Organisation_PolicySerial'
    __table_args__ = {'comment': 'Серии полисов страховых компаний'}

    id = Column(INTEGER(11), primary_key=True)
    organisation_id = Column(ForeignKey('Organisation.id', ondelete='CASCADE'), nullable=False)
    serial = Column(String(16), nullable=False)
    policyType_id = Column(ForeignKey('rbPolicyType.id', ondelete='SET NULL'))

    organisation = relationship('Organisation')
    policyType = relationship('RbPolicyType')


class PaymentScheme(Base):
    __tablename__ = 'PaymentScheme'
    __table_args__ = {'comment': 'Схема оплаты'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    type = Column(TINYINT(1), nullable=False)
    number = Column(String(9))
    OKPF_id = Column(ForeignKey('rbOKPF.id'))
    org_id = Column(ForeignKey('Organisation.id'))
    orgStructure_id = Column(INTEGER(11))
    status = Column(TINYINT(1))
    numberProtocol = Column(String(64))
    nameProtocol = Column(String(255))
    person_id = Column(ForeignKey('Person.id'))
    begDate = Column(Date)
    endDate = Column(Date)
    subjectContract = Column(String(255))
    postAddress = Column(String(1024))
    total = Column(DECIMAL(10, 2), nullable=False, server_default=alchemy_text("0.00"))
    enrollment = Column(TINYINT(1), nullable=False)

    OKPF = relationship('RbOKPF')
    org = relationship('Organisation')
    person = relationship('Person')


class PersonAttach(Base):
    __tablename__ = 'PersonAttach'
    __table_args__ = {'comment': '"Работа на участке". Периоды работы сотрудников на определённом участке'}

    id = Column(INTEGER(11), primary_key=True)
    orgStructure_id = Column(ForeignKey('OrgStructure.id'), nullable=False)
    begDate = Column(Date, nullable=False)
    endDate = Column(Date)
    salary = Column(String(64), nullable=False)
    master_id = Column(INTEGER(11), nullable=False)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    sentToTFOMS = Column(TINYINT(1), nullable=False)
    errorCode = Column(String(256))

    orgStructure = relationship('OrgStructure')


class PersonIdentification(Base):
    __tablename__ = 'PersonIdentification'
    __table_args__ = {'comment': 'Таблица для хранения id сотрудников во внешней системе'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    modifyDatetime = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    person_id = Column(ForeignKey('Person.id'), nullable=False)
    accountingSystem_id = Column(ForeignKey('rbAccountingSystem.id'), nullable=False)
    identifier = Column(String(36))

    accountingSystem = relationship('RbAccountingSystem')
    person = relationship('Person')


class PersonPrerecordQuota(Base):
    __tablename__ = 'PersonPrerecordQuota'
    __table_args__ = {'comment': 'Значения квот предварительной записи для каждого работника'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE'), nullable=False)
    quotaType_id = Column(ForeignKey('rbPrerecordQuotaType.id', ondelete='CASCADE'), nullable=False)
    value = Column(SMALLINT(4), nullable=False)

    person = relationship('Person')
    quotaType = relationship('RbPrerecordQuotaType')


class PersonActivity(Base):
    __tablename__ = 'Person_Activity'
    __table_args__ = {'comment': 'Обзор: Виды деятельности сотрудников'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Person.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    activity_id = Column(ForeignKey('rbActivity.id', ondelete='CASCADE'))

    activity = relationship('RbActivity')
    createPerson = relationship('Person', primaryjoin='PersonActivity.createPerson_id == Person.id')
    master = relationship('Person', primaryjoin='PersonActivity.master_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='PersonActivity.modifyPerson_id == Person.id')


class PersonEducation(Base):
    __tablename__ = 'Person_Education'
    __table_args__ = {'comment': 'Сведения о квалификации сотрудников'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(INTEGER(11), nullable=False)
    documentType_id = Column(INTEGER(11))
    serial = Column(String(8), nullable=False)
    number = Column(String(16), nullable=False)
    date = Column(Date, nullable=False)
    origin = Column(String(64), nullable=False)
    status = Column(String(64), nullable=False)
    validFromDate = Column(Date)
    validToDate = Column(Date)
    speciality_id = Column(INTEGER(11))
    org_id = Column(ForeignKey('Organisation.id'))
    educationType = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    cycle = Column(String(80), nullable=False, server_default=alchemy_text("''"))
    hours = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    category_id = Column(ForeignKey('rbPersonCategory.id'))

    category = relationship('RbPersonCategory')
    org = relationship('Organisation')


class PersonJobType(Base):
    __tablename__ = 'Person_JobType'
    __table_args__ = {'comment': 'Типы работ разрешенные для назначения сотрудником'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('Person.id', ondelete='CASCADE'), nullable=False)
    jobType_id = Column(ForeignKey('rbJobType.id', ondelete='SET NULL'))

    jobType = relationship('RbJobType')
    master = relationship('Person')


class QueueControlEvent(Base):
    __tablename__ = 'QueueControlEvents'
    __table_args__ = {'comment': 'Управление очередями (сервис нетрики)'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    medicalProfile_id = Column(ForeignKey('rbMedicalAidProfile.id'), nullable=False)
    begDate = Column(Date)
    endDate = Column(Date)
    contacts = Column(String(60))
    notes = Column(String(120))
    closedDate = Column(Date)
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'))
    maxWeight = Column(String(10))
    qType = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person')
    medicalProfile = relationship('RbMedicalAidProfile')
    orgStructure = relationship('OrgStructure')


class StockMotionItem(Base):
    __tablename__ = 'StockMotion_Item'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('StockMotion.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    nomenclature_id = Column(ForeignKey('rbNomenclature.id', onupdate='CASCADE'))
    seria = Column(TINYTEXT)
    unit_id = Column(INTEGER(11))
    qnt = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))

    master = relationship('StockMotion')
    nomenclature = relationship('RbNomenclature')


class TreatmentPlanItem(Base):
    __tablename__ = 'TreatmentPlan_Item'
    __table_args__ = {'comment': 'Сущность "Элемент плана лечения"'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    treatmentPlan_id = Column(ForeignKey('TreatmentPlan.id'))
    actionType_id = Column(INTEGER(11), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    isExposedToEvent = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isPrepaymentItem = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    status = Column(TINYINT(4), nullable=False)
    count = Column(INTEGER(11), nullable=False, server_default=alchemy_text("1"))
    total = Column(DECIMAL(10, 2))

    createPerson = relationship('Person', primaryjoin='TreatmentPlanItem.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='TreatmentPlanItem.modifyPerson_id == Person.id')
    treatmentPlan = relationship('TreatmentPlan')


class RbActionSheduleItem(Base):
    __tablename__ = 'rbActionShedule_Item'
    __table_args__ = {'comment': 'Элемент графика выполнения действия'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbActionShedule.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    offset = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    time = Column(Time, nullable=False, server_default=alchemy_text("'00:00:00'"))

    createPerson = relationship('Person', primaryjoin='RbActionSheduleItem.createPerson_id == Person.id')
    master = relationship('RbActionShedule')
    modifyPerson = relationship('Person', primaryjoin='RbActionSheduleItem.modifyPerson_id == Person.id')


class RbAssignedContract(Base):
    __tablename__ = 'rbAssignedContracts'
    __table_args__ = {'comment': 'Справочник по индивидуальным договорам'}

    id = Column(INTEGER(11), primary_key=True)
    type = Column(INTEGER(11), nullable=False)
    code = Column(String(9), nullable=False)
    OKPF_id = Column(ForeignKey('rbOKPF.id'))
    org_id = Column(ForeignKey('Organisation.id'))
    contractNumber = Column(String(30))
    contractDate = Column(Date, nullable=False)
    contractEndDate = Column(Date)
    contractSum = Column(String(15))

    OKPF = relationship('RbOKPF')
    org = relationship('Organisation')


class RbBlankTempInvalid(Base):
    __tablename__ = 'rbBlankTempInvalids'
    __table_args__ = {'comment': 'Бланки для ВУТ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    doctype_id = Column(ForeignKey('rbTempInvalidDocument.id'), nullable=False)
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    checkingSerial = Column(TINYINT(3), nullable=False)
    checkingNumber = Column(TINYINT(3), nullable=False)
    checkingAmount = Column(TINYINT(2), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbBlankTempInvalid.createPerson_id == Person.id')
    doctype = relationship('RbTempInvalidDocument')
    modifyPerson = relationship('Person', primaryjoin='RbBlankTempInvalid.modifyPerson_id == Person.id')


class RbContainerType(Base):
    __tablename__ = 'rbContainerType'
    __table_args__ = {'comment': 'Типы контейнеров'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(24), nullable=False)
    name = Column(String(32), nullable=False)
    color = Column(String(7))
    amount = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    unit_id = Column(ForeignKey('rbUnit.id', ondelete='SET NULL'))
    netrica_Code = Column(CHAR(1))

    createPerson = relationship('Person', primaryjoin='RbContainerType.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbContainerType.modifyPerson_id == Person.id')
    unit = relationship('RbUnit')


class RbDetachmentReason(Base):
    __tablename__ = 'rbDetachmentReason'
    __table_args__ = {'comment': 'Справочник причин открепления'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    attachType_id = Column(ForeignKey('rbAttachType.id'))

    attachType = relationship('RbAttachType')
    createPerson = relationship('Person', primaryjoin='RbDetachmentReason.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDetachmentReason.modifyPerson_id == Person.id')


class RbDocumentType(Base):
    __tablename__ = 'rbDocumentType'
    __table_args__ = {'comment': 'Тип документа (паспорт и пр.)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    regionalCode = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    group_id = Column(ForeignKey('rbDocumentTypeGroup.id'), nullable=False)
    serial_format = Column(INTEGER(11), nullable=False)
    number_format = Column(INTEGER(11), nullable=False)
    federalCode = Column(String(16), nullable=False)
    usedIndex = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    isDefault = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isForeigner = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    netrica_Code = Column(String(255))
    autoCloseDate = Column(TINYINT(4), server_default=alchemy_text("0"))
    EGIZ_code = Column(INTEGER(11))
    seriesLenSign = Column(String(2))
    seriesLen = Column(INTEGER(11))
    numberLenSign = Column(String(2))
    numberLen = Column(INTEGER(11))
    EGIZ_name = Column(Text)

    createPerson = relationship('Person', primaryjoin='RbDocumentType.createPerson_id == Person.id')
    group = relationship('RbDocumentTypeGroup')
    modifyPerson = relationship('Person', primaryjoin='RbDocumentType.modifyPerson_id == Person.id')


class RbDrugNomenclature(Base):
    __tablename__ = 'rbDrugNomenclature'
    __table_args__ = {'comment': 'Номенклатурна ЛС. (Формальное описание лекарственных средств)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    code = Column(String(128))
    name = Column(String(255))
    baseUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    primaryContainerUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    storageUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    conventration = Column(Float(asdecimal=True), nullable=False)
    concentrationUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    RLS_code = Column(INTEGER(11))
    RLS_tradeName = Column(String(255), nullable=False)
    RLS_latinTradeName = Column(String(255), nullable=False)
    RLS_manufacturer = Column(String(128), nullable=False)
    RLS_manufacturerCountry = Column(String(64), nullable=False)
    RLS_formName = Column(String(64), nullable=False)
    RLS_packing = Column(String(64), nullable=False)
    RLS_filling = Column(String(64), nullable=False)
    RLS_isRegistered = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    MNN_name = Column(String(255), nullable=False)
    latinMNN_name = Column(String(255), nullable=False)

    baseUnit = relationship('RbUnit', primaryjoin='RbDrugNomenclature.baseUnit_id == RbUnit.id')
    concentrationUnit = relationship('RbUnit', primaryjoin='RbDrugNomenclature.concentrationUnit_id == RbUnit.id')
    createPerson = relationship('Person', primaryjoin='RbDrugNomenclature.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbDrugNomenclature.modifyPerson_id == Person.id')
    primaryContainerUnit = relationship('RbUnit', primaryjoin='RbDrugNomenclature.primaryContainerUnit_id == RbUnit.id')
    storageUnit = relationship('RbUnit', primaryjoin='RbDrugNomenclature.storageUnit_id == RbUnit.id')


class RbEQGatewayConfig(Base):
    __tablename__ = 'rbEQGatewayConfig'
    __table_args__ = {'comment': 'Конфигурация шлюза(моста EPort) для табло электронной очереди.'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(32), nullable=False)
    name = Column(String(128), nullable=False)
    host = Column(String(40), nullable=False, server_default=alchemy_text("'192.168.0.222'"))
    port = Column(INTEGER(11), nullable=False, server_default=alchemy_text("5000"))
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='SET NULL'))
    type = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbEQGatewayConfig.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEQGatewayConfig.modifyPerson_id == Person.id')
    orgStructure = relationship('OrgStructure')


class RbEQueueType(Base):
    __tablename__ = 'rbEQueueType'
    __table_args__ = {'comment': 'Тип очереди'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(64))
    name = Column(String(128))
    ticketPrefix = Column(String(4), nullable=False)
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    isImmediatelyReady = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))

    orgStructure = relationship('OrgStructure')


class RbEpicrisisSectionsRbEpicrisisProperty(Base):
    __tablename__ = 'rbEpicrisisSections_rbEpicrisisProperty'
    __table_args__ = {'comment': 'Ссылки на свойства в шаблонах разделов эпикризов.'}

    id = Column(INTEGER(11), primary_key=True)
    id_rbEpicrisisSections = Column(ForeignKey('rbEpicrisisSections.id', ondelete='CASCADE'), nullable=False)
    id_rbEpicrisisProperty = Column(ForeignKey('rbEpicrisisProperty.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(10))
    htmlTemplate = Column(String(500), server_default=alchemy_text("'<p style=''font-size: 11pt; text-align:left; margin-bottom: 0.5em; margin-top: 0.5em;''>\n <b>{name}: </b>{value}\n</p>'"))
    orgStruct = Column(String(120))
    isRequired = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isEditable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))

    rbEpicrisisProperty = relationship('RbEpicrisisProperty')
    rbEpicrisisSection = relationship('RbEpicrisisSection')


class RbEpicrisisStoredProperty(Base):
    __tablename__ = 'rbEpicrisisStoredProperties'
    __table_args__ = {'comment': 'Шаблонные фразы эпикризов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    rbEpicrisisProperty_id = Column(ForeignKey('rbEpicrisisProperty.id'), nullable=False)
    StoredValue = Column(Text, nullable=False)
    orgStructure_id = Column(ForeignKey('OrgStructure.id'), server_default=alchemy_text("39"))
    readOnly = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))

    createPerson = relationship('Person', primaryjoin='RbEpicrisisStoredProperty.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbEpicrisisStoredProperty.modifyPerson_id == Person.id')
    orgStructure = relationship('OrgStructure')
    rbEpicrisisProperty = relationship('RbEpicrisisProperty')


class RbEpicrisisTemplatesRbEpicrisisSection(Base):
    __tablename__ = 'rbEpicrisisTemplates_rbEpicrisisSections'
    __table_args__ = {'comment': 'Ссылки на шаблоны разделов в эпикризе.'}

    id = Column(INTEGER(11), primary_key=True)
    id_rbEpicrisisTemplates = Column(ForeignKey('rbEpicrisisTemplates.id', ondelete='CASCADE'), nullable=False)
    id_rbEpicrisisSections = Column(ForeignKey('rbEpicrisisSections.id', ondelete='CASCADE'), ForeignKey('rbEpicrisisSections.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(10))
    htmlTemplate = Column(String(512), server_default=alchemy_text("'<div style=''font-size: 14pt; text-align:center; margin-bottom: 0.25em; margin-top: 0.25em; border-bottom:1px solid black; border-top:1px solid black;''>\n <b>{name} </b> \n</div>\n{value}'"))
    isRequired = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isEditable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))

    rbEpicrisisSection = relationship('RbEpicrisisSection', primaryjoin='RbEpicrisisTemplatesRbEpicrisisSection.id_rbEpicrisisSections == RbEpicrisisSection.id')
    rbEpicrisisTemplate = relationship('RbEpicrisisTemplate')


class RbEquipment(Base):
    __tablename__ = 'rbEquipment'
    __table_args__ = {'comment': 'Оборудование'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    equipmentType_id = Column(ForeignKey('rbEquipmentType.id', ondelete='SET NULL'))
    inventoryNumber = Column(String(32), nullable=False)
    model = Column(String(16), nullable=False)
    releaseDate = Column(DateTime)
    startupDate = Column(DateTime, nullable=False)
    status = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    employmentTerm = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    warrantyTerm = Column(TINYINT(2))
    maintenancePeriod = Column(TINYINT(4), nullable=False)
    maintenanceSingleInPeriod = Column(TINYINT(4), nullable=False)
    tripod = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    tripodCapacity = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    manufacturer = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    protocol = Column(INTEGER(11), nullable=False, server_default=alchemy_text("1"))
    address = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    ownName = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    labName = Column(String(128), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbEquipment.createPerson_id == Person.id')
    equipmentType = relationship('RbEquipmentType')
    modifyPerson = relationship('Person', primaryjoin='RbEquipment.modifyPerson_id == Person.id')


class RbHighTechCureMethod(Base):
    __tablename__ = 'rbHighTechCureMethod'
    __table_args__ = {'comment': 'Методы высокотехнологичной помощи'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(9), nullable=False)
    name = Column(String(400), nullable=False)
    regionalCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    federalCode = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    cureKind_id = Column(ForeignKey('rbHighTechCureKind.id', ondelete='CASCADE'), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbHighTechCureMethod.createPerson_id == Person.id')
    cureKind = relationship('RbHighTechCureKind')
    modifyPerson = relationship('Person', primaryjoin='RbHighTechCureMethod.modifyPerson_id == Person.id')


class RbJobTypeQuota(Base):
    __tablename__ = 'rbJobType_Quota'
    __table_args__ = {'comment': 'Квотирование номерков'}

    id = Column(INTEGER(11), primary_key=True)
    count = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='SET NULL', onupdate='CASCADE'))
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='SET NULL', onupdate='CASCADE'))
    post_id = Column(ForeignKey('rbPost.id', ondelete='SET NULL', onupdate='CASCADE'))
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    master_id = Column(ForeignKey('rbJobType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    master = relationship('RbJobType')
    orgStructure = relationship('OrgStructure')
    person = relationship('Person')
    post = relationship('RbPost')
    speciality = relationship('RbSpeciality')


class RbJobTypeSmartQuota(Base):
    __tablename__ = 'rbJobType_SmartQuota'
    __table_args__ = {'comment': 'Smart-график на номерки для типа работ'}

    jobType_id = Column(ForeignKey('rbJobType.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    day = Column(TINYINT(3), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    available = Column(TINYINT(3), nullable=False, server_default=alchemy_text("0"))

    jobType = relationship('RbJobType')


class RbMKBSubclassItem(Base):
    __tablename__ = 'rbMKBSubclass_Item'
    __table_args__ = {'comment': 'элемент субклассификации МКБ по 5 знаку'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbMKBSubclass.id', ondelete='CASCADE'), nullable=False)
    code = Column(String(8), nullable=False)
    name = Column(String(128), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbMKBSubclassItem.createPerson_id == Person.id')
    master = relationship('RbMKBSubclas')
    modifyPerson = relationship('Person', primaryjoin='RbMKBSubclassItem.modifyPerson_id == Person.id')


class RbMedicine(Base):
    __tablename__ = 'rbMedicines'
    __table_args__ = {'comment': 'Справочник формулярных наименований ЛС (кэш лекарств из 1с)'}

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(50), nullable=False)
    name = Column(String(300), nullable=False)
    unit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    group_id = Column(INTEGER(11), server_default=alchemy_text("0"))
    mnn = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    latinMnn = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    tradeName = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    issueForm = Column(String(128), nullable=False)
    latinIssueForm = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    concentration = Column(String(50), nullable=False)
    isDrugs = Column(TINYINT(1), nullable=False)
    baseUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    minIndivisibleUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    packingUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)
    baseUnitsInMinIndivisibleUnit = Column(Float(asdecimal=True), nullable=False)
    minIndivisibleUnitsInPackingUnit = Column(Float(asdecimal=True), nullable=False)
    assignUnit_id = Column(INTEGER(11))

    baseUnit = relationship('RbUnit', primaryjoin='RbMedicine.baseUnit_id == RbUnit.id')
    minIndivisibleUnit = relationship('RbUnit', primaryjoin='RbMedicine.minIndivisibleUnit_id == RbUnit.id')
    packingUnit = relationship('RbUnit', primaryjoin='RbMedicine.packingUnit_id == RbUnit.id')
    unit = relationship('RbUnit', primaryjoin='RbMedicine.unit_id == RbUnit.id')


class RbMenu(Base):
    __tablename__ = 'rbMenu'
    __table_args__ = {'comment': 'Справочник Шаблон питания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    diet_id = Column(ForeignKey('rbDiet.id'))
    courtingDiet_id = Column(ForeignKey('rbDiet.id'))

    courtingDiet = relationship('RbDiet', primaryjoin='RbMenu.courtingDiet_id == RbDiet.id')
    createPerson = relationship('Person', primaryjoin='RbMenu.createPerson_id == Person.id')
    diet = relationship('RbDiet', primaryjoin='RbMenu.diet_id == RbDiet.id')
    modifyPerson = relationship('Person', primaryjoin='RbMenu.modifyPerson_id == Person.id')


class RbNomenclatureKind(Base):
    __tablename__ = 'rbNomenclatureKind'
    __table_args__ = {'comment': 'Виды номенклатуры ЛСиИМН'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    class_id = Column(ForeignKey('rbNomenclatureClass.id', ondelete='SET NULL', onupdate='CASCADE'))
    code = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(128), nullable=False, server_default=alchemy_text("''"))

    _class = relationship('RbNomenclatureClas')
    createPerson = relationship('Person', primaryjoin='RbNomenclatureKind.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbNomenclatureKind.modifyPerson_id == Person.id')


class RbPatientModelItem(Base):
    __tablename__ = 'rbPatientModel_Item'
    __table_args__ = {'comment': 'Справочник Методы видов лечения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    cureType_id = Column(ForeignKey('rbCureType.id', ondelete='SET NULL'))
    cureMethod_id = Column(ForeignKey('rbCureMethod.id', ondelete='SET NULL'))
    master_id = Column(ForeignKey('rbPatientModel.id', ondelete='CASCADE'), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbPatientModelItem.createPerson_id == Person.id')
    cureMethod = relationship('RbCureMethod')
    cureType = relationship('RbCureType')
    master = relationship('RbPatientModel')
    modifyPerson = relationship('Person', primaryjoin='RbPatientModelItem.modifyPerson_id == Person.id')


class RbPrintTemplate(Base):
    __tablename__ = 'rbPrintTemplate'
    __table_args__ = {'comment': 'Шаблоны печати'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    context = Column(String(64), nullable=False)
    fileName = Column(String(128), nullable=False)
    default = Column(LONGTEXT)
    dpdAgreement = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    type = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    banUnkeptDate = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    counter_id = Column(ForeignKey('rbCounter.id'))
    deleted = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    isPatientAgreed = Column(TINYINT(1), server_default=alchemy_text("0"))
    groupName = Column(String(20))
    hideParam = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    documentType_id = Column(ForeignKey('rbIEMKDocument.id'))
    isEditableInWeb = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    chkProfiles = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    chkPersons = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    counter = relationship('RbCounter')
    createPerson = relationship('Person', primaryjoin='RbPrintTemplate.createPerson_id == Person.id')
    documentType = relationship('RbIEMKDocument')
    modifyPerson = relationship('Person', primaryjoin='RbPrintTemplate.modifyPerson_id == Person.id')


class RbResult(Base):
    __tablename__ = 'rbResult'
    __table_args__ = {'comment': 'Результат обращения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    eventPurpose_id = Column(ForeignKey('rbEventTypePurpose.id'), nullable=False)
    code = Column(String(8), nullable=False)
    name = Column(String(255), nullable=False)
    continued = Column(TINYINT(1), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    federalCode = Column(String(8), nullable=False)
    notAccount = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    counter_id = Column(ForeignKey('rbCounter.id'))
    begDate = Column(Date, nullable=False, server_default=alchemy_text("'1900-01-01'"))
    endDate = Column(Date, nullable=False, server_default=alchemy_text("'2999-12-31'"))
    netrica_Code = Column(String(65))
    attachType = Column(INTEGER(11))
    socStatusClass = Column(INTEGER(11))
    socStatusType = Column(INTEGER(11))
    isDeath = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    caseCast_id = Column(INTEGER(11))

    counter = relationship('RbCounter')
    createPerson = relationship('Person', primaryjoin='RbResult.createPerson_id == Person.id')
    eventPurpose = relationship('RbEventTypePurpose')
    modifyPerson = relationship('Person', primaryjoin='RbResult.modifyPerson_id == Person.id')


class RbServiceGoal(Base):
    __tablename__ = 'rbService_Goal'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('rbService.id', onupdate='CASCADE'), nullable=False)
    goal_id = Column(ForeignKey('rbEventGoal.id', onupdate='CASCADE'), nullable=False)

    goal = relationship('RbEventGoal')
    master = relationship('RbService')


class RbServiceProfile(Base):
    __tablename__ = 'rbService_Profile'
    __table_args__ = {'comment': 'Профили мед.помощи, применяемые в зависимости от обстоятельс'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('rbService.id', ondelete='CASCADE'), nullable=False)
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='SET NULL'))
    sex = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    age = Column(String(255), nullable=False, server_default=alchemy_text("''''''"))
    mkbRegExp = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    medicalAidProfile_id = Column(ForeignKey('rbMedicalAidProfile.id', ondelete='SET NULL'))
    medicalAidKind_id = Column(ForeignKey('rbMedicalAidKind.id', ondelete='SET NULL'))
    medicalAidType_id = Column(ForeignKey('rbMedicalAidType.id', ondelete='SET NULL'))
    eventProfile_id = Column(ForeignKey('rbEventProfile.id'))

    createPerson = relationship('Person', primaryjoin='RbServiceProfile.createPerson_id == Person.id')
    eventProfile = relationship('RbEventProfile')
    master = relationship('RbService')
    medicalAidKind = relationship('RbMedicalAidKind')
    medicalAidProfile = relationship('RbMedicalAidProfile')
    medicalAidType = relationship('RbMedicalAidType')
    modifyPerson = relationship('Person', primaryjoin='RbServiceProfile.modifyPerson_id == Person.id')
    speciality = relationship('RbSpeciality')


class RbServicePurpose(Base):
    __tablename__ = 'rbService_Purpose'
    __table_args__ = {'comment': '[OBSOLETE] Связь услуг и цели обращения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('rbService.id', onupdate='CASCADE'), nullable=False)
    purpose_id = Column(ForeignKey('rbEventTypePurpose.id', onupdate='CASCADE'), nullable=False)

    master = relationship('RbService')
    purpose = relationship('RbEventTypePurpose')


class RbStockRecipeItem(Base):
    __tablename__ = 'rbStockRecipe_Item'
    __table_args__ = {'comment': 'Элемент рецепта для производства ЛСиИМН'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbStockRecipe.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    nomenclature_id = Column(ForeignKey('rbNomenclature.id', onupdate='CASCADE'))
    qnt = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    isOut = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='RbStockRecipeItem.createPerson_id == Person.id')
    master = relationship('RbStockRecipe')
    modifyPerson = relationship('Person', primaryjoin='RbStockRecipeItem.modifyPerson_id == Person.id')
    nomenclature = relationship('RbNomenclature')


class RbTempInvalidRegime(Base):
    __tablename__ = 'rbTempInvalidRegime'
    __table_args__ = {'comment': 'Режим периода ВУТ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    type = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    doctype_id = Column(ForeignKey('rbTempInvalidDocument.id', ondelete='SET NULL'))
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbTempInvalidRegime.createPerson_id == Person.id')
    doctype = relationship('RbTempInvalidDocument')
    modifyPerson = relationship('Person', primaryjoin='RbTempInvalidRegime.modifyPerson_id == Person.id')


class RbTest(Base):
    __tablename__ = 'rbTest'
    __table_args__ = {'comment': 'Показатели исследований'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    testGroup_id = Column(ForeignKey('rbTestGroup.id', ondelete='SET NULL'))
    code = Column(String(16), nullable=False)
    name = Column(String(128), nullable=False)
    position = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    lis_id = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='RbTest.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='RbTest.modifyPerson_id == Person.id')
    testGroup = relationship('RbTestGroup')


class RbUserProfileRight(Base):
    __tablename__ = 'rbUserProfile_Right'
    __table_args__ = {'comment': 'Профили пользователей'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbUserProfile.id', ondelete='CASCADE'), nullable=False)
    userRight_id = Column(ForeignKey('rbUserRight.id', ondelete='CASCADE'), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbUserProfileRight.createPerson_id == Person.id')
    master = relationship('RbUserProfile')
    modifyPerson = relationship('Person', primaryjoin='RbUserProfileRight.modifyPerson_id == Person.id')
    userRight = relationship('RbUserRight')


class RcParamValue(Base):
    __tablename__ = 'rcParam_Value'
    __table_args__ = {'comment': 'Значения для пользовательских параметров для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    title = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    master_id = Column(ForeignKey('rcParam.id', ondelete='SET NULL', onupdate='CASCADE'))
    number = Column(INTEGER(5), nullable=False, server_default=alchemy_text("0"))

    master = relationship('RcParam')


class RcQueryCol(Base):
    __tablename__ = 'rcQuery_Cols'
    __table_args__ = {'comment': 'Поля для запросов в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    number = Column(INTEGER(5), nullable=False, server_default=alchemy_text("0"))
    field = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    alias = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    master_id = Column(ForeignKey('rcQuery.id', ondelete='SET NULL', onupdate='CASCADE'))
    description = Column(Text)
    visible = Column(TINYINT(1), server_default=alchemy_text("1"))
    extended = Column(TINYINT(1), server_default=alchemy_text("0"))

    master = relationship('RcQuery')


class RcQueryCondition(Base):
    __tablename__ = 'rcQuery_Conditions'
    __table_args__ = {'comment': 'Условия для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    field = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    conditionType_id = Column(ForeignKey('rcConditionType.id', ondelete='SET NULL', onupdate='CASCADE'))
    value = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    valueType_id = Column(ForeignKey('rcValueType.id', ondelete='SET NULL', onupdate='CASCADE'))
    defaultValue = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    parentCondition_id = Column(ForeignKey('rcQuery_Conditions.id', ondelete='SET NULL', onupdate='CASCADE'))
    master_id = Column(ForeignKey('rcQuery.id', ondelete='SET NULL', onupdate='CASCADE'))

    conditionType = relationship('RcConditionType')
    master = relationship('RcQuery')
    parentCondition = relationship('RcQueryCondition', remote_side=[id])
    valueType = relationship('RcValueType')


class RcQueryGroup(Base):
    __tablename__ = 'rcQuery_Group'
    __table_args__ = {'comment': 'Группировки для запросов в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    number = Column(INTEGER(5), nullable=False, server_default=alchemy_text("0"))
    field = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    master_id = Column(ForeignKey('rcQuery.id', ondelete='SET NULL', onupdate='CASCADE'))
    extended = Column(TINYINT(1), server_default=alchemy_text("0"))

    master = relationship('RcQuery')


class RcQueryOrder(Base):
    __tablename__ = 'rcQuery_Order'
    __table_args__ = {'comment': 'Порядок сортировки для запросов в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    number = Column(INTEGER(5), nullable=False, server_default=alchemy_text("0"))
    field = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    master_id = Column(ForeignKey('rcQuery.id', ondelete='SET NULL', onupdate='CASCADE'))
    extended = Column(TINYINT(1), server_default=alchemy_text("0"))

    master = relationship('RcQuery')


class RcReport(Base):
    __tablename__ = 'rcReport'
    __table_args__ = {'comment': 'Отчёт'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    name = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    description = Column(Text)
    editionMode = Column(TINYINT(1), server_default=alchemy_text("0"))
    query_id = Column(ForeignKey('rcQuery.id', ondelete='SET NULL', onupdate='CASCADE'))
    sql = Column(Text)

    query = relationship('RcQuery')


t_smpPerson = Table(
    'smpPerson', metadata,
    Column('person_id', ForeignKey('Person.id'), primary_key=True),
    Column('type_id', ForeignKey('smpPersonType.id')),
    comment='список сотрудников CМП'
)


class ActionPropertyType(Base):
    __tablename__ = 'ActionPropertyType'
    __table_args__ = {'comment': 'Описание свойства типа действия'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actionType_id = Column(ForeignKey('ActionType.id'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    template_id = Column(INTEGER(11))
    name = Column(String(500))
    shortName = Column(String(64))
    descr = Column(String(128), nullable=False)
    unit_id = Column(ForeignKey('rbUnit.id'))
    typeName = Column(String(64), nullable=False)
    valueDomain = Column(Text, nullable=False)
    defaultValue = Column(LONGTEXT)
    isVector = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    norm = Column(String(64), nullable=False)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    penalty = Column(INTEGER(3), nullable=False, server_default=alchemy_text("0"))
    penaltyUserProfile = Column(Text)
    penaltyDiagnosis = Column(Text)
    visibleInJobTicket = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    visibleInTableRedactor = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isAssignable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    test_id = Column(ForeignKey('rbTest.id', ondelete='SET NULL'))
    defaultEvaluation = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    canChangeOnlyOwner = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isActionNameSpecifier = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    laboratoryCalculator = Column(String(3))
    inActionsSelectionTable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    redactorSizeFactor = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isFrozen = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    typeEditable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    visibleInDR = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    userProfile_id = Column(ForeignKey('rbUserProfile.id', ondelete='SET NULL', onupdate='CASCADE'))
    userProfileBehaviour = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    copyModifier = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    isVitalParam = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    vitalParamId = Column(INTEGER(11))
    isODIIParam = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    customSelect = Column(Text)
    autoFieldUserProfile = Column(Text)
    formulaAlias = Column(String(10))
    ticketsNeeded = Column(TINYINT(4))
    incrementOnSave = Column(TINYINT(4), server_default=alchemy_text("0"))
    parent_id = Column(INTEGER(11))
    orientation = Column(Enum('v', 'h'), nullable=False, server_default=alchemy_text("'v'"))

    actionType = relationship('ActionType')
    test = relationship('RbTest')
    unit = relationship('RbUnit')
    userProfile = relationship('RbUserProfile')


class ActionTypeMedicament(Base):
    __tablename__ = 'ActionType_Medicament'
    __table_args__ = {'comment': 'Медикаменты относящиеся к типу действия'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    finance_id = Column(ForeignKey('rbFinance.id', ondelete='CASCADE'))
    medicament_id = Column(ForeignKey('rbService.id', ondelete='CASCADE'))

    finance = relationship('RbFinance')
    master = relationship('ActionType')
    medicament = relationship('RbService')


class ActionTypePersonPost(Base):
    __tablename__ = 'ActionType_PersonPost'
    __table_args__ = {'comment': 'Фильтр типов действий по должности'}

    id = Column(INTEGER(11), primary_key=True)
    actionType_id = Column(ForeignKey('ActionType.id'), nullable=False)
    post_id = Column(ForeignKey('rbPost.id'), nullable=False)

    actionType = relationship('ActionType')
    post = relationship('RbPost')


class ActionTypePersonSpeciality(Base):
    __tablename__ = 'ActionType_PersonSpeciality'
    __table_args__ = {'comment': 'Фильтр типов действий по специальности'}

    id = Column(INTEGER(11), primary_key=True)
    actionType_id = Column(ForeignKey('ActionType.id'), nullable=False)
    speciality_id = Column(ForeignKey('rbSpeciality.id'), nullable=False)

    actionType = relationship('ActionType')
    speciality = relationship('RbSpeciality')


class ActionTypeQuotaType(Base):
    __tablename__ = 'ActionType_QuotaType'
    __table_args__ = {'comment': 'Вид квотирования в произведённом действии'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    quotaClass = Column(TINYINT(1))
    finance_id = Column(ForeignKey('rbFinance.id', ondelete='CASCADE'))
    quotaType_id = Column(ForeignKey('QuotaType.id', ondelete='CASCADE'))

    finance = relationship('RbFinance')
    master = relationship('ActionType')
    quotaType = relationship('QuotaType')


class ActionTypeService(Base):
    __tablename__ = 'ActionType_Service'
    __table_args__ = {'comment': 'Выставляемая в счёте услуга за произведённое действие в зави'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    finance_id = Column(ForeignKey('rbFinance.id', ondelete='CASCADE'))
    service_id = Column(ForeignKey('rbService.id', ondelete='CASCADE'))

    finance = relationship('RbFinance')
    master = relationship('ActionType')
    service = relationship('RbService')


class ActionTypeSpeciality(Base):
    __tablename__ = 'ActionType_Speciality'
    __table_args__ = {'comment': 'Допустимые для типа действия специальности'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ActionType.id'), nullable=False)
    speciality_id = Column(ForeignKey('rbSpeciality.id'), nullable=False)

    master = relationship('ActionType')
    speciality = relationship('RbSpeciality')


class ActionTypeTissueType(Base):
    __tablename__ = 'ActionType_TissueType'
    __table_args__ = {'comment': 'Заборы ткани применяемые в типах действий'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    tissueType_id = Column(ForeignKey('rbTissueType.id', ondelete='SET NULL'))
    amount = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    unit_id = Column(ForeignKey('rbUnit.id', ondelete='SET NULL'))
    containerType_id = Column(ForeignKey('rbContainerType.id', ondelete='SET NULL'))
    parent_id = Column(INTEGER(11))
    isActiveGroup = Column(TINYINT(1), nullable=False)

    containerType = relationship('RbContainerType')
    master = relationship('ActionType')
    tissueType = relationship('RbTissueType')
    unit = relationship('RbUnit')


class AssignmentsTemplateItem(Base):
    __tablename__ = 'AssignmentsTemplate_Item'
    __table_args__ = {'comment': 'Шаблоны элементов назначения'}

    id = Column(INTEGER(11), primary_key=True)
    actionType_id = Column(ForeignKey('ActionType.id', onupdate='CASCADE'), nullable=False)
    assignmentsTemplate_id = Column(ForeignKey('AssignmentsTemplate.id', onupdate='CASCADE'), nullable=False)

    actionType = relationship('ActionType')
    assignmentsTemplate = relationship('AssignmentsTemplate')


class BlankTempInvalidParty(Base):
    __tablename__ = 'BlankTempInvalid_Party'
    __table_args__ = {'comment': 'Случай ВУТ, инвалидности или ограничения жизнедеятельности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    date = Column(Date, nullable=False)
    doctype_id = Column(ForeignKey('rbBlankTempInvalids.id'), nullable=False)
    person_id = Column(ForeignKey('Person.id'))
    serial = Column(String(8), nullable=False)
    numberFrom = Column(String(16), nullable=False)
    numberTo = Column(String(16), nullable=False)
    amount = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    extradited = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    returnBlank = Column(INTEGER(11), nullable=False)
    balance = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    used = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    writing = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    is_ELN = Column(TINYINT(1), server_default=alchemy_text("0"))
    issuedOrgStructureId = Column(INTEGER(11))

    createPerson = relationship('Person', primaryjoin='BlankTempInvalidParty.createPerson_id == Person.id')
    doctype = relationship('RbBlankTempInvalid')
    modifyPerson = relationship('Person', primaryjoin='BlankTempInvalidParty.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='BlankTempInvalidParty.person_id == Person.id')


class ClientAddres(Base):
    __tablename__ = 'ClientAddress'
    __table_args__ = {'comment': 'Адрес пациента'}

    id = Column(INTEGER(11), primary_key=True, nullable=False)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    type = Column(TINYINT(4), nullable=False)
    address_id = Column(ForeignKey('Address.id'))
    freeInput = Column(String(200), primary_key=True, nullable=False)
    freeInput_p = Column(String(200), nullable=False)
    district_id = Column(ForeignKey('rbDistrict.id', ondelete='SET NULL', onupdate='CASCADE'))
    isVillager = Column(TINYINT(1), nullable=False)

    address = relationship('Addres')
    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientAddres.createPerson_id == Person.id')
    district = relationship('RbDistrict')
    modifyPerson = relationship('Person', primaryjoin='ClientAddres.modifyPerson_id == Person.id')


class ClientAllergy(Base):
    __tablename__ = 'ClientAllergy'
    __table_args__ = {'comment': 'Аллергическая непереносимость'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.createPerson_id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.modifyPerson_id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    nameSubstance = Column(String(128), nullable=False)
    power = Column(INTEGER(11), nullable=False)
    createDate = Column(Date)
    notes = Column(TINYTEXT, nullable=False)
    reactionCode_id = Column(INTEGER(11))
    reactionType_id = Column(INTEGER(11))

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientAllergy.createPerson_id == Person.createPerson_id')
    modifyPerson = relationship('Person', primaryjoin='ClientAllergy.modifyPerson_id == Person.modifyPerson_id')


class ClientAnthropometric(Base):
    __tablename__ = 'ClientAnthropometric'
    __table_args__ = {'comment': 'Антропометрические данные пациента'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    date = Column(Date, nullable=False)
    height = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    weight = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    waist = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    bust = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    bodyType = Column(String(20))
    dailyVolume = Column(INTEGER(11))
    bodyType_id = Column(INTEGER(11))
    hips = Column(Float(asdecimal=True), nullable=False)

    client = relationship('Client')


class ClientAttachRequest(Base):
    __tablename__ = 'ClientAttachRequest'

    id = Column(INTEGER(11), primary_key=True)
    dateTime = Column(DateTime)
    canceledDateTime = Column(DateTime)
    type = Column(INTEGER(1))
    person_id = Column(ForeignKey('Person.id'))
    orgStructure_id = Column(INTEGER(11))
    client_id = Column(ForeignKey('Client.id'))
    related_id = Column(INTEGER(11))
    status = Column(String(255))
    rejectionReason = Column(ForeignKey('rbReasonsForRefusal.id'))
    note = Column(String(255))
    external_id = Column(String(255))
    attach_id = Column(INTEGER(11))
    deketed = Column(TINYINT(1), server_default=alchemy_text("0"))
    home = Column(String(255))
    authoredDate = Column(DateTime)

    client = relationship('Client')
    person = relationship('Person')
    rbReasonsForRefusal = relationship('RbReasonsForRefusal')


class ClientCompulsoryTreatment(Base):
    __tablename__ = 'ClientCompulsoryTreatment'
    __table_args__ = {'comment': 'Принудительное лечение'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False)
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    setKind_id = Column(ForeignKey('rbCompulsoryTreatmentKind.id'), nullable=False)
    newKind_id = Column(ForeignKey('rbCompulsoryTreatmentKind.id'))
    begDate = Column(Date, nullable=False)
    extensionDate = Column(Date)
    endDate = Column(String(255), nullable=False)
    note = Column(TINYTEXT)

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientCompulsoryTreatment.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientCompulsoryTreatment.modifyPerson_id == Person.id')
    newKind = relationship('RbCompulsoryTreatmentKind', primaryjoin='ClientCompulsoryTreatment.newKind_id == RbCompulsoryTreatmentKind.id')
    setKind = relationship('RbCompulsoryTreatmentKind', primaryjoin='ClientCompulsoryTreatment.setKind_id == RbCompulsoryTreatmentKind.id')


class ClientContact(Base):
    __tablename__ = 'ClientContact'
    __table_args__ = {'comment': 'Способы связи с пациентом'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    contactType_id = Column(ForeignKey('rbContactType.id'), nullable=False)
    isPrimary = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    contact = Column(String(32), nullable=False)
    notes = Column(String(64), nullable=False)

    client = relationship('Client')
    contactType = relationship('RbContactType')
    createPerson = relationship('Person', primaryjoin='ClientContact.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientContact.modifyPerson_id == Person.id')


class ClientDocument(Base):
    __tablename__ = 'ClientDocument'
    __table_args__ = {'comment': 'Документы пациентов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    documentType_id = Column(ForeignKey('rbDocumentType.id'), nullable=False)
    serial = Column(String(10), nullable=False)
    number = Column(String(16), nullable=False)
    date = Column(DateTime, nullable=False)
    origin = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    endDate = Column(DateTime)
    hasEndDate = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientDocument.createPerson_id == Person.id')
    documentType = relationship('RbDocumentType')
    modifyPerson = relationship('Person', primaryjoin='ClientDocument.modifyPerson_id == Person.id')


class ClientExaminationPlan(Base):
    __tablename__ = 'ClientExaminationPlan'
    __table_args__ = {'comment': 'Диспансеризация и профилактические осмотры'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    event_id = Column(INTEGER(11))
    year = Column(SMALLINT(4), nullable=False)
    month = Column(TINYINT(4), nullable=False)
    kind = Column(TINYINT(1), nullable=False)
    category = Column(INTEGER(4))
    step = Column(SMALLINT(4))
    orgCode = Column(String(8))
    date = Column(DateTime)
    status = Column(TINYINT(3), nullable=False, server_default=alchemy_text("0"))
    sendDate = Column(DateTime)
    stepStatus = Column(TINYINT(3), nullable=False, server_default=alchemy_text("0"))
    infoDate = Column(DateTime)
    infoMethod = Column(TINYINT(1))
    infostep = Column(INTEGER(4))
    error = Column(Text, nullable=False)
    deleteStatus = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    infoRslt = Column(INTEGER(4))
    mkbx = Column(String(8))
    mkbxdate = Column(Date)
    mkbxstts = Column(TINYINT(4))
    mkbxmeth = Column(TINYINT(4))
    doc_ss = Column(CHAR(11))

    client = relationship('Client')


class ClientFakeSNIL(Base):
    __tablename__ = 'ClientFakeSNILS'
    __table_args__ = {'comment': 'Информация о фиктивных СНИЛСах'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'))
    fakeSNILS = Column(CHAR(11))

    client = relationship('Client')


class ClientFile(Base):
    __tablename__ = 'ClientFile'
    __table_args__ = {'comment': 'Файлы, относящиеся к пациенту'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(String(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    name = Column(String(80), nullable=False)
    file = Column(MEDIUMBLOB, nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    client = relationship('Client')


class ClientIdentification(Base):
    __tablename__ = 'ClientIdentification'
    __table_args__ = {'comment': 'Учётные номера в различный системах'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    accountingSystem_id = Column(ForeignKey('rbAccountingSystem.id'), nullable=False)
    identifier = Column(String(36))
    checkDate = Column(Date)

    accountingSystem = relationship('RbAccountingSystem')
    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientIdentification.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientIdentification.modifyPerson_id == Person.id')


class ClientIdentificationLDE(Base):
    __tablename__ = 'ClientIdentificationLDES'
    __table_args__ = {'comment': 'Идентификаторы пациентов в сервисе ОДЛИ (Нетрика)'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    orgCode = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    patientId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    versionId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    version = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    datetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))

    client = relationship('Client')


class ClientIdentificationODII(Base):
    __tablename__ = 'ClientIdentificationODII'
    __table_args__ = {'comment': 'Идентификаторы пациентов в сервисе ОДИИ (Нетрика)'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    orgCode = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    patientId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    versionId = Column(String(36), nullable=False, server_default=alchemy_text("''"))
    version = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    datetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))

    client = relationship('Client')


class ClientInfoSource(Base):
    __tablename__ = 'ClientInfoSource'
    __table_args__ = {'comment': 'Таблица для фиксации источника информации пациента о ЛПУ (для НИИ Онкологии)'}

    id = Column(INTEGER(11), primary_key=True)
    createDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    modifyDateTime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyPerson_id = Column(ForeignKey('Person.id'))
    client_id = Column(ForeignKey('Client.id'))
    rbInfoSource_id = Column(ForeignKey('rbInfoSource.id', ondelete='SET NULL'))
    infoSourceDate = Column(Date)
    docDoc = Column(TINYINT(1))
    onMend = Column(TINYINT(1))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientInfoSource.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientInfoSource.modifyPerson_id == Person.id')
    rbInfoSource = relationship('RbInfoSource')


class ClientIntoleranceMedicament(Base):
    __tablename__ = 'ClientIntoleranceMedicament'
    __table_args__ = {'comment': 'Медикаментозная непереносимость'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.createPerson_id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.modifyPerson_id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    nameMedicament = Column(String(128), nullable=False)
    power = Column(INTEGER(11), nullable=False)
    createDate = Column(Date)
    notes = Column(TINYTEXT, nullable=False)
    reactionCode_id = Column(INTEGER(11))
    allergyDrug_id = Column(INTEGER(11))

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientIntoleranceMedicament.createPerson_id == Person.createPerson_id')
    modifyPerson = relationship('Person', primaryjoin='ClientIntoleranceMedicament.modifyPerson_id == Person.modifyPerson_id')


class ClientMisdemeanor(Base):
    __tablename__ = 'ClientMisdemeanor'
    __table_args__ = {'comment': 'Правонарушения пациента'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    crimeDate = Column(Date, nullable=False)
    criminalRule = Column(String(32), nullable=False)
    court = Column(String(128), nullable=False)
    caseNumber = Column(String(64), nullable=False)
    writ = Column(String(128), nullable=False)
    writDate = Column(Date)
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    nextRecourceDate = Column(Date)
    note = Column(String(255))

    client = relationship('Client')
    person = relationship('Person')


class ClientPolicy(Base):
    __tablename__ = 'ClientPolicy'
    __table_args__ = {'comment': 'Полисы пациентов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    insurer_id = Column(INTEGER(11))
    policyType_id = Column(ForeignKey('rbPolicyType.id'))
    policyKind_id = Column(ForeignKey('rbPolicyKind.id', ondelete='SET NULL', onupdate='CASCADE'))
    serial = Column(String(16), nullable=False)
    number = Column(String(35), nullable=False)
    begDate = Column(Date, nullable=False)
    endDate = Column(Date)
    dischargeDate = Column(Date)
    name = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    note = Column(String(200), nullable=False, server_default=alchemy_text("''"))
    insuranceArea = Column(String(13), nullable=False)
    isSearchPolicy = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    franchisePercent = Column(Float, server_default=alchemy_text("0"))

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientPolicy.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientPolicy.modifyPerson_id == Person.id')
    policyKind = relationship('RbPolicyKind')
    policyType = relationship('RbPolicyType')


class ClientQueueNumber(Base):
    __tablename__ = 'ClientQueueNumber'
    __table_args__ = {'comment': 'Сквозной номер пациента в очереди для вызова на прием'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    date = Column(Date, nullable=False)
    number = Column(INTEGER(11), nullable=False)

    client = relationship('Client')


class ClientRelation(Base):
    __tablename__ = 'ClientRelation'
    __table_args__ = {'comment': 'Связи пациента'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'))
    relativeType_id = Column(ForeignKey('rbRelationType.id'), ForeignKey('rbRelationType.id'))
    relative_id = Column(ForeignKey('Client.id', ondelete='CASCADE'))
    freeInput = Column(String(80))

    client = relationship('Client', primaryjoin='ClientRelation.client_id == Client.id')
    createPerson = relationship('Person', primaryjoin='ClientRelation.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientRelation.modifyPerson_id == Person.id')
    relativeType = relationship('RbRelationType', primaryjoin='ClientRelation.relativeType_id == RbRelationType.id')
    relative = relationship('Client', primaryjoin='ClientRelation.relative_id == Client.id')


class ClientRemark(Base):
    __tablename__ = 'ClientRemark'
    __table_args__ = {'comment': 'Пометки пациента.'}

    id = Column(INTEGER(11), primary_key=True)
    remarkType_id = Column(ForeignKey('rbClientRemarkType.id'), nullable=False)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    date = Column(Date)
    note = Column(String(255), nullable=False)

    client = relationship('Client')
    remarkType = relationship('RbClientRemarkType')


class ClientVIP(Base):
    __tablename__ = 'ClientVIP'
    __table_args__ = {'comment': 'VIP пациенты'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'), nullable=False)
    createDatetime = Column(DateTime, nullable=False)
    comment = Column(String(255), nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    deletePerson_id = Column(ForeignKey('Person.id'))
    deleteDatetime = Column(DateTime, nullable=False)

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientVIP.createPerson_id == Person.id')
    deletePerson = relationship('Person', primaryjoin='ClientVIP.deletePerson_id == Person.id')


class ClientWork(Base):
    __tablename__ = 'ClientWork'
    __table_args__ = {'comment': 'Место работы/учебы пациента'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    org_id = Column(INTEGER(11))
    freeInput = Column(String(128), nullable=False)
    post = Column(String(64), nullable=False)
    stage = Column(TINYINT(3), nullable=False)
    OKVED = Column(String(10), nullable=False)
    note = Column(String(100), nullable=False, server_default=alchemy_text("''"))

    client = relationship('Client')


class ClientAnalyze(Base):
    __tablename__ = 'Client_Analyzes'

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id'))
    createDateTime = Column(DateTime)
    modifyDateTime = Column(DateTime)
    RW = Column(INTEGER(11))
    F50 = Column(INTEGER(11))
    HbsAg = Column(INTEGER(11))
    Tuberkulez = Column(INTEGER(11))
    Diabet = Column(INTEGER(11))

    client = relationship('Client')


class ClientHospitalBedsLocationCard(Base):
    __tablename__ = 'Client_HospitalBedsLocationCard'
    __table_args__ = {'comment': 'Место нахождения амбулаторной карты по Client_id (DEPRECATED; DELETE_ME?). Заменена на Event_HospitalBedsLocationCard'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(ForeignKey('Client.id'), nullable=False)
    locationCardType_id = Column(ForeignKey('rbHospitalBedsLocationCardType.id'))
    moveDate = Column(Date)
    returnDate = Column(Date)

    locationCardType = relationship('RbHospitalBedsLocationCardType')
    master = relationship('Client')


class ClientLocationCard(Base):
    __tablename__ = 'Client_LocationCard'
    __table_args__ = {'comment': 'Место нахождения амбулаторной карты'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    locationCardType_id = Column(ForeignKey('rbLocationCardType.id'))

    locationCardType = relationship('RbLocationCardType')
    master = relationship('Client')


class ClientPayer(Base):
    __tablename__ = 'Client_Payers'
    __table_args__ = {'comment': 'Платильщики клиента'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    document_id = Column(ForeignKey('rbDocumentType.id', ondelete='CASCADE', onupdate='CASCADE'))
    firstName = Column(String(30))
    lastName = Column(String(30))
    patrName = Column(String(30))
    birthDate = Column(Date)
    serialLeft = Column(String(8))
    serialRight = Column(String(8))
    number = Column(String(16))
    regAddress = Column(String(128))
    issuedBy = Column(String(128))
    phoneNumber = Column(String(16))
    createDate = Column(Date, nullable=False)

    client = relationship('Client')
    document = relationship('RbDocumentType')


class ClientPaymentScheme(Base):
    __tablename__ = 'Client_PaymentScheme'
    __table_args__ = {'comment': 'Набор "обследований пациента"'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'))
    paymentScheme_id = Column(ForeignKey('PaymentScheme.id', ondelete='CASCADE', onupdate='CASCADE'))
    begDate = Column(Date)
    endDate = Column(Date)

    client = relationship('Client')
    paymentScheme = relationship('PaymentScheme')


class ClientStatusObservation(Base):
    __tablename__ = 'Client_StatusObservation'
    __table_args__ = {'comment': 'Статус наблюдения пациента'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    statusObservationType_id = Column(ForeignKey('rbStatusObservationClientType.id'))

    master = relationship('Client')
    statusObservationType = relationship('RbStatusObservationClientType')


class ComplianceTreatment(Base):
    __tablename__ = 'ComplianceTreatment'

    id = Column(INTEGER(11), primary_key=True)
    first_actionType = Column(ForeignKey('ActionType.id'))
    second_actionType = Column(ForeignKey('ActionType.id'))
    treatment_actionType = Column(ForeignKey('ActionType.id'))
    age = Column(String(9), nullable=False, server_default=alchemy_text("''"))

    ActionType = relationship('ActionType', primaryjoin='ComplianceTreatment.first_actionType == ActionType.id')
    ActionType1 = relationship('ActionType', primaryjoin='ComplianceTreatment.second_actionType == ActionType.id')
    ActionType2 = relationship('ActionType', primaryjoin='ComplianceTreatment.treatment_actionType == ActionType.id')


class Contract(Base):
    __tablename__ = 'Contract'
    __table_args__ = {'comment': 'Договор'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    number = Column(String(64), nullable=False)
    date = Column(Date, nullable=False)
    recipient_id = Column(INTEGER(11), nullable=False)
    recipientAccount_id = Column(ForeignKey('Organisation_Account.id'))
    recipientKBK = Column(String(30), nullable=False)
    payer_id = Column(INTEGER(11))
    payerAccount_id = Column(ForeignKey('Organisation_Account.id'))
    payerKBK = Column(String(30), nullable=False)
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    finance_id = Column(ForeignKey('rbFinance.id'), nullable=False)
    grouping = Column(String(64), nullable=False)
    resolution = Column(String(64), nullable=False)
    format_id = Column(ForeignKey('rbAccountExportFormat.id', ondelete='SET NULL'))
    exposeUnfinishedEventVisits = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    exposeUnfinishedEventActions = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    visitExposition = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actionExposition = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    exposeDiscipline = Column(INTEGER(2), nullable=False, server_default=alchemy_text("0"))
    priceList_id = Column(INTEGER(11))
    coefficient = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    coefficientEx = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    coefficientEx2 = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    orgCategory = Column(String(1), nullable=False)
    regionalTariffRegulationFactor = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("1"))
    exposeByMESMaxDuration = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    ignorePayStatusForJobs = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isConsiderFederalPrice = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    assignedClient_id = Column(INTEGER(11))
    assignedBegDate = Column(Date)
    assignedEndDate = Column(Date)
    deposit = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    maxClients = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    counterValue = Column(String(30))
    typeId = Column(INTEGER(11))
    limitationPeriod = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    LPU = Column(INTEGER(11))
    isSumImportableFromEIS = Column(TINYINT(4), server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='Contract.createPerson_id == Person.id')
    finance = relationship('RbFinance')
    format = relationship('RbAccountExportFormat')
    modifyPerson = relationship('Person', primaryjoin='Contract.modifyPerson_id == Person.id')
    payerAccount = relationship('OrganisationAccount', primaryjoin='Contract.payerAccount_id == OrganisationAccount.id')
    recipientAccount = relationship('OrganisationAccount', primaryjoin='Contract.recipientAccount_id == OrganisationAccount.id')


class DNPlan(Base):
    __tablename__ = 'DNPlan'

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    name = Column(String(255), nullable=False)
    mkb_id = Column(INTEGER(11))
    dndiagnosis = Column(ForeignKey('rbDNDiagnoses.id'), nullable=False)
    deleted = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))

    client = relationship('Client')
    rbDNDiagnose = relationship('RbDNDiagnose')


class DentalFormulaTeethSection(Base):
    __tablename__ = 'DentalFormulaTeethSections'
    __table_args__ = {'comment': 'Состояния поверхностей для зубной формулы'}

    id = Column(INTEGER(11), primary_key=True)
    tooth_id = Column(ForeignKey('DentalFormulaTeeth.id'), nullable=False)
    section = Column(String(4), nullable=False)
    state_id = Column(ForeignKey('rbToothSectionState.id'))

    state = relationship('RbToothSectionState')
    tooth = relationship('DentalFormulatooth')


class Diagnosi(Base):
    __tablename__ = 'Diagnosis'
    __table_args__ = {'comment': 'Элемент листа уточнённых диагнозов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    diagnosisType_id = Column(ForeignKey('rbDiagnosisType.id'), nullable=False)
    character_id = Column(ForeignKey('rbDiseaseCharacter.id'))
    MKB = Column(String(8), nullable=False)
    MKBEx = Column(String(8), nullable=False)
    morphologyMKB = Column(String(16), nullable=False)
    TNMS = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    dispanser_id = Column(ForeignKey('rbDispanser.id'))
    traumaType_id = Column(ForeignKey('rbTraumaType.id'))
    setDate = Column(Date)
    endDate = Column(Date, nullable=False)
    mod_id = Column(ForeignKey('Diagnosis.id', ondelete='CASCADE'), ForeignKey('Diagnosis.id'))
    person_id = Column(ForeignKey('Person.id'))
    tempEventId = Column(INTEGER(11))
    note = Column(Text)

    character = relationship('RbDiseaseCharacter')
    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='Diagnosi.createPerson_id == Person.id')
    diagnosisType = relationship('RbDiagnosisType')
    dispanser = relationship('RbDispanser')
    mod = relationship('Diagnosi', remote_side=[id], primaryjoin='Diagnosi.mod_id == Diagnosi.id')
    modifyPerson = relationship('Person', primaryjoin='Diagnosi.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='Diagnosi.person_id == Person.id')
    traumaType = relationship('RbTraumaType')


class DloDrugFormularyItem(Base):
    __tablename__ = 'DloDrugFormulary_Item'
    __table_args__ = {'comment': 'Элементы формуляра лекарственных средств ДЛО'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('DloDrugFormulary.id', onupdate='CASCADE'), nullable=False)
    code = Column(INTEGER(11), nullable=False)
    mnn_id = Column(ForeignKey('dlo_rbMNN.id', onupdate='CASCADE'), nullable=False)
    issueForm_id = Column(ForeignKey('dlo_rbIssueForm.id', onupdate='CASCADE'), nullable=False)
    name = Column(String(250), nullable=False)
    dosageQnt = Column(INTEGER(11), nullable=False)
    dosage_id = Column(INTEGER(11), nullable=False)
    tradeName_id = Column(ForeignKey('dlo_rbTradeName.id', onupdate='CASCADE'), nullable=False)
    qnt = Column(SMALLINT(6), nullable=False)
    producer = Column(String(50))
    isDrugs = Column(TINYINT(4), nullable=False)
    baseUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'))
    limit = Column(Float(asdecimal=True), nullable=False)
    federalCode = Column(INTEGER(11))
    isSprPC = Column(TINYINT(1), server_default=alchemy_text("0"))
    isDevice = Column(TINYINT(1), server_default=alchemy_text("0"))

    baseUnit = relationship('RbUnit')
    issueForm = relationship('DloRbIssueForm')
    master = relationship('DloDrugFormulary')
    mnn = relationship('DloRbMNN')
    tradeName = relationship('DloRbTradeName')


class DnChoiceConstraint(Base):
    __tablename__ = 'DnChoiceConstraint'
    __table_args__ = {'comment': 'Ограничения выбора идентификаторов диспансерного наблюдения'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id'), nullable=False)
    rbDispanser_id = Column(ForeignKey('rbDispanser.id'), nullable=False)

    eventType = relationship('EventType')
    rbDispanser = relationship('RbDispanser')


class DrugFormularyItem(Base):
    __tablename__ = 'DrugFormulary_Item'
    __table_args__ = {'comment': 'Элементы формуляра лекарственных средств'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('DrugFormulary.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    drug_id = Column(ForeignKey('rbDrug.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    limit = Column(Float(asdecimal=True), nullable=False)
    limitUnit_id = Column(ForeignKey('rbUnit.id', onupdate='CASCADE'), nullable=False)

    drug = relationship('RbDrug')
    limitUnit = relationship('RbUnit')
    master = relationship('DrugFormulary')


class DrugNomenclatureUnitConversion(Base):
    __tablename__ = 'DrugNomenclature_UnitConversion'
    __table_args__ = {'comment': 'Коэфициент преобразования единиц измерения друг в друга для номенклатурыных позиций.'}

    drugNomenclature_id = Column(ForeignKey('rbDrugNomenclature.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    sourceUnit_id = Column(ForeignKey('rbUnit.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    targetUnit_id = Column(ForeignKey('rbUnit.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    multiplier = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("1"))

    drugNomenclature = relationship('RbDrugNomenclature')
    sourceUnit = relationship('RbUnit', primaryjoin='DrugNomenclatureUnitConversion.sourceUnit_id == RbUnit.id')
    targetUnit = relationship('RbUnit', primaryjoin='DrugNomenclatureUnitConversion.targetUnit_id == RbUnit.id')


class DrugRecipeR78(Base):
    __tablename__ = 'DrugRecipeR78'
    __table_args__ = {'comment': 'Льготные рецепты (СПб)'}

    id = Column(INTEGER(11), primary_key=True)
    event_id = Column(ForeignKey('Event.id'))
    client_id = Column(ForeignKey('Client.id'))
    person_id = Column(ForeignKey('Person.id'))
    MKB = Column(String(10))
    LP_id = Column(ForeignKey('DrugLPR78.id'))
    pref_cat_c_katl = Column(String(20))
    pref_cat_NPP = Column(String(30))
    pref_cat_finance = Column(String(30))
    is_vk = Column(TINYINT(4))
    set_date = Column(Date, server_default=alchemy_text("current_timestamp()"))
    series = Column(String(20))
    number = Column(String(20))
    bar_code_id = Column(INTEGER(11))
    bar_code_url = Column(Text)

    LP = relationship('DrugLPR78')
    client = relationship('Client')
    event = relationship('Event')
    person = relationship('Person')


class EQHost(Base):
    __tablename__ = 'EQHost'
    __table_args__ = {'comment': 'Узлы функционирования электронной очереди'}

    id = Column(INTEGER(11), primary_key=True)
    type = Column(TINYINT(4), nullable=False)
    code = Column(String(32), nullable=False)
    name = Column(String(128), nullable=False)
    address = Column(String(40), nullable=False)
    port = Column(INTEGER(11), nullable=False)
    eQueueType_id = Column(ForeignKey('rbEQueueType.id', ondelete='SET NULL', onupdate='CASCADE'))
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='SET NULL', onupdate='CASCADE'))

    eQueueType = relationship('RbEQueueType')
    orgStructure = relationship('OrgStructure')


class EQOffice(Base):
    __tablename__ = 'EQOffice'
    __table_args__ = {'comment': 'Кабинеты, у которых есть табло электронной очереди'}

    id = Column(INTEGER(11), primary_key=True)
    office = Column(String(16), nullable=False)
    gateway_id = Column(ForeignKey('rbEQGatewayConfig.id', ondelete='CASCADE'), nullable=False)
    address = Column(INTEGER(11), nullable=False)

    gateway = relationship('RbEQGatewayConfig')


class EQueue(Base):
    __tablename__ = 'EQueue'
    __table_args__ = {'comment': 'Электронная очередь на определенную дату'}

    id = Column(INTEGER(11), primary_key=True)
    eQueueType_id = Column(ForeignKey('rbEQueueType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    date = Column(Date, nullable=False)

    eQueueType = relationship('RbEQueueType')


class EquipmentMaintenanceJournal(Base):
    __tablename__ = 'EquipmentMaintenanceJournal'
    __table_args__ = {'comment': 'Журнал технического обслуживания оборудования'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('rbEquipment.id', ondelete='CASCADE'), nullable=False)
    date = Column(DateTime, nullable=False)
    plannedDate = Column(DateTime)
    fullName = Column(String(128), nullable=False)
    note = Column(String(255))

    master = relationship('RbEquipment')


class EventReferralTypesRelation(Base):
    __tablename__ = 'EventReferralTypesRelation'
    __table_args__ = {'comment': 'Ставит в соответствие тип направления типу события'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('EventType.id', ondelete='CASCADE'))
    slave_id = Column(ForeignKey('rbReferralTypeSPB.id', ondelete='CASCADE'))

    master = relationship('EventType')
    slave = relationship('RbReferralTypeSPB')


class EventTypeAssociation(Base):
    __tablename__ = 'EventTypeAssociations'
    __table_args__ = {'comment': 'Связь между типами событий'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    type = Column(TINYINT(1), nullable=False)

    eventType = relationship('EventType', primaryjoin='EventTypeAssociation.eventType_id == EventType.id')
    master = relationship('EventType', primaryjoin='EventTypeAssociation.master_id == EventType.id')


class EventTypeForm(Base):
    __tablename__ = 'EventTypeForm'
    __table_args__ = {'comment': 'Форма для представления события'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE'), nullable=False)
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    descr = Column(String(64), nullable=False)
    _pass = Column('pass', TINYINT(1), nullable=False)

    eventType = relationship('EventType')


class EventTypeScale(Base):
    __tablename__ = 'EventTypeScales'
    __table_args__ = {'comment': 'Таблица Выбранных Шкал в EvenType'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id'), nullable=False)
    rbScales_id = Column(ForeignKey('rbScales.id'), nullable=False)

    eventType = relationship('EventType')
    rbScales = relationship('RbScale')


class EventTypeScalesCheck(Base):
    __tablename__ = 'EventTypeScalesCheck'
    __table_args__ = {'comment': 'Таблица Чекбоксов Шкалы в EventType'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id'), nullable=False)
    isChecked = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    eventType = relationship('EventType')


class EventTypeAction(Base):
    __tablename__ = 'EventType_Action'
    __table_args__ = {'comment': 'Планируемые действия'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    actionType_id = Column(ForeignKey('ActionType.id'), nullable=False)
    speciality_id = Column(ForeignKey('rbSpeciality.id', ondelete='SET NULL'))
    tissueType_id = Column(ForeignKey('rbTissueType.id', ondelete='SET NULL'))
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(220))
    selectionGroup = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    actuality = Column(TINYINT(4), nullable=False)
    expose = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    payable = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hurtType = Column(Text, nullable=False)
    hurtFactorType = Column(Text, nullable=False)
    defaultOrg_id = Column(ForeignKey('Organisation.id', ondelete='SET NULL'))
    isCompulsory = Column(TINYINT(1), server_default=alchemy_text("0"))

    actionType = relationship('ActionType')
    defaultOrg = relationship('Organisation')
    eventType = relationship('EventType')
    speciality = relationship('RbSpeciality')
    tissueType = relationship('RbTissueType')


class EventTypeAutoPrint(Base):
    __tablename__ = 'EventType_AutoPrint'
    __table_args__ = {'comment': 'Автопечать шаблона печати для типа события'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    printTemplate_id = Column(ForeignKey('rbPrintTemplate.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    triggerType = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    repeatType = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    repeatResetType = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    repeatResetDate = Column(Date)

    eventType = relationship('EventType')
    printTemplate = relationship('RbPrintTemplate')


class EventTypeDiagnostic(Base):
    __tablename__ = 'EventType_Diagnostic'
    __table_args__ = {'comment': 'Планируемые осмотры специалистов'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    speciality_id = Column(ForeignKey('rbSpeciality.id'))
    person_id = Column(ForeignKey('Person.id'))
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(100), nullable=False)
    defaultHealthGroup_id = Column(ForeignKey('rbHealthGroup.id'))
    defaultMKB = Column(String(5), nullable=False)
    defaultDispanser_id = Column(ForeignKey('rbDispanser.id', ondelete='SET NULL'))
    selectionGroup = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    actuality = Column(TINYINT(4), nullable=False)
    visitType_id = Column(INTEGER(11))
    hurtType = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    hurtFactorType = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    defaultGoal_id = Column(ForeignKey('rbEventGoal.id'))
    defaultMedicalGroup_id = Column(ForeignKey('rbMedicalGroup.id'))
    service_id = Column(ForeignKey('rbService.id', ondelete='SET NULL'))

    defaultDispanser = relationship('RbDispanser')
    defaultGoal = relationship('RbEventGoal')
    defaultHealthGroup = relationship('RbHealthGroup')
    defaultMedicalGroup = relationship('RbMedicalGroup')
    eventType = relationship('EventType')
    person = relationship('Person')
    service = relationship('RbService')
    speciality = relationship('RbSpeciality')


class EventTypeKSLP(Base):
    __tablename__ = 'EventType_KSLP'

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id'))
    kslp_id = Column(ForeignKey('rbExtraKSLP.id'))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))

    eventType = relationship('EventType')
    kslp = relationship('RbExtraKSLP')


class EventTypeMKB(Base):
    __tablename__ = 'EventType_MKB'
    __table_args__ = {'comment': 'Диагнозы МКБ для обязательного заполнения ЗНО'}

    id = Column(INTEGER(11), primary_key=True)
    diag_id = Column(String(9), nullable=False)
    master_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))

    master = relationship('EventType')


class EventTypeOrgStructure(Base):
    __tablename__ = 'EventType_OrgStructure'

    id = Column(INTEGER(11), primary_key=True)
    orgStructure_id = Column(ForeignKey('OrgStructure.id'))
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'))
    parent_id = Column(INTEGER(11))

    eventType = relationship('EventType')
    orgStructure = relationship('OrgStructure')


class EventTypePost(Base):
    __tablename__ = 'EventType_Post'
    __table_args__ = {'comment': 'Фильтр типов событий по должности'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id'), nullable=False)
    post_id = Column(ForeignKey('rbPost.id'), nullable=False)

    eventType = relationship('EventType')
    post = relationship('RbPost')


class EventTypeSpeciality(Base):
    __tablename__ = 'EventType_Speciality'
    __table_args__ = {'comment': 'Фильтр типов событий по специальности'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id'), nullable=False)
    speciality_id = Column(ForeignKey('rbSpeciality.id'), nullable=False)

    eventType = relationship('EventType')
    speciality = relationship('RbSpeciality')


class EventTypeZNO(Base):
    __tablename__ = 'EventType_ZNO'
    __table_args__ = {'comment': 'Шаблоны подозрений на ЗНО для типов событий'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    template_code = Column(String(64), nullable=False)
    template_name = Column(String(128), nullable=False)
    relegateOrg_id = Column(INTEGER(11))
    relegateToOrg_id = Column(INTEGER(11))
    dateReferral = Column(INTEGER(11))
    examType = Column(INTEGER(11))
    nmkl = Column(INTEGER(11))
    consilium_code = Column(INTEGER(11))
    consilium_date = Column(INTEGER(11))
    reason = Column(INTEGER(11))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    MKB = Column(String(128))
    createDatetime = Column(DateTime, nullable=False)
    modifyDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))

    createPerson = relationship('Person', primaryjoin='EventTypeZNO.createPerson_id == Person.id')
    eventType = relationship('EventType')
    modifyPerson = relationship('Person', primaryjoin='EventTypeZNO.modifyPerson_id == Person.id')


class EventTypeZNOInfo(Base):
    __tablename__ = 'EventType_ZNOInfo'
    __table_args__ = {'comment': 'Шаблоны сведений о ЗНО для типов событий'}

    id = Column(INTEGER(11), primary_key=True)
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    template_code = Column(String(64), nullable=False)
    template_name = Column(String(128), nullable=False)
    reason = Column(INTEGER(11))
    reason_fill = Column(INTEGER(11))
    stady = Column(INTEGER(11))
    stady_T = Column(INTEGER(11))
    stady_N = Column(INTEGER(11))
    stady_M = Column(INTEGER(11))
    consilium_code = Column(INTEGER(11))
    consilium_date = Column(INTEGER(11))
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    createDatetime = Column(DateTime, nullable=False)
    modifyDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))

    createPerson = relationship('Person', primaryjoin='EventTypeZNOInfo.createPerson_id == Person.id')
    eventType = relationship('EventType')
    modifyPerson = relationship('Person', primaryjoin='EventTypeZNOInfo.modifyPerson_id == Person.id')


class EventFeedMeal(Base):
    __tablename__ = 'Event_Feed_Meal'
    __table_args__ = {'comment': 'Список блюд для отдельного приема пищи'}

    id = Column(INTEGER(10), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Event_Feed.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    mealTime_id = Column(ForeignKey('rbMealTime.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    meal_id = Column(ForeignKey('rbMeal.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    master = relationship('EventFeed')
    mealTime = relationship('RbMealTime')
    meal = relationship('RbMeal')


class EventLocalContract(Base):
    __tablename__ = 'Event_LocalContract'
    __table_args__ = {'comment': 'Согласование с Договорным отделом ЛПУ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(ForeignKey('Event.id', ondelete='CASCADE'), nullable=False)
    coordDate = Column(DateTime)
    coordAgent = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    coordInspector = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    coordText = Column(TINYTEXT, nullable=False)
    dateContract = Column(Date, nullable=False)
    numberContract = Column(String(64), nullable=False)
    sumLimit = Column(Float(asdecimal=True), nullable=False)
    lastName = Column(String(30), nullable=False)
    firstName = Column(String(30), nullable=False)
    patrName = Column(String(30), nullable=False)
    birthDate = Column(Date, nullable=False)
    documentType_id = Column(ForeignKey('rbDocumentType.id'))
    serialLeft = Column(String(8), nullable=False)
    serialRight = Column(String(8), nullable=False)
    number = Column(String(16), nullable=False)
    regAddress = Column(String(64), nullable=False)
    org_id = Column(ForeignKey('Organisation.id', ondelete='SET NULL'))
    issuedBy = Column(String(128))
    phoneNumber = Column(String(128))

    createPerson = relationship('Person', primaryjoin='EventLocalContract.createPerson_id == Person.id')
    documentType = relationship('RbDocumentType')
    master = relationship('Event')
    modifyPerson = relationship('Person', primaryjoin='EventLocalContract.modifyPerson_id == Person.id')
    org = relationship('Organisation')


class EventPrintTemplateCounter(Base):
    __tablename__ = 'Event_PrintTemplateCounter'
    __table_args__ = {'comment': 'Сопоставление значений счетчиков с шаблонами печати, распечатанными из конкретных обращений'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    template_id = Column(ForeignKey('rbPrintTemplate.id'), nullable=False)
    counterValue = Column(String(32), nullable=False)

    createPerson = relationship('Person', primaryjoin='EventPrintTemplateCounter.createPerson_id == Person.id')
    event = relationship('Event')
    modifyPerson = relationship('Person', primaryjoin='EventPrintTemplateCounter.modifyPerson_id == Person.id')
    template = relationship('RbPrintTemplate')


class ExportStatu(Base):
    __tablename__ = 'ExportStatus'
    __table_args__ = {'comment': 'Статус экспорта записи о пациенте'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE', onupdate='CASCADE'))
    status = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    note = Column(String(128), nullable=False, server_default=alchemy_text("''"))

    client = relationship('Client')
    event = relationship('Event')


class ExternalIEMKDocument(Base):
    __tablename__ = 'ExternalIEMKDocument'
    __table_args__ = {'comment': 'Внешние документы для ИЭМК'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE', onupdate='CASCADE'))
    deleted = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    document_type = Column(ForeignKey('rbIEMKDocument.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    MO_name = Column(String(255))
    file_name = Column(String(255))
    file_id = Column(INTEGER(11), nullable=False)
    doc_date = Column(Date, nullable=False)
    createPersonId = Column(INTEGER(11))

    client = relationship('Client')
    rbIEMKDocument = relationship('RbIEMKDocument')
    event = relationship('Event')


class ForeignHospitalization(Base):
    __tablename__ = 'ForeignHospitalization'
    __table_args__ = {'comment': 'Справочник целей госпитализации'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False)
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    org_id = Column(ForeignKey('Organisation.id'), nullable=False)
    purpose_id = Column(ForeignKey('rbHospitalizationPurpose.id'), nullable=False)
    MKB = Column(String(10), nullable=False)
    clinicDiagnosis = Column(String(128))
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ForeignHospitalization.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ForeignHospitalization.modifyPerson_id == Person.id')
    org = relationship('Organisation')
    purpose = relationship('RbHospitalizationPurpose')


class HospitalBedInvolute(Base):
    __tablename__ = 'HospitalBed_Involute'
    __table_args__ = {'comment': 'Сворачивание для коек'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure_HospitalBed.id', ondelete='CASCADE'), nullable=False)
    involuteType = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    begDateInvolute = Column(Date)
    endDateInvolute = Column(Date)

    master = relationship('OrgStructureHospitalBed')


class Job(Base):
    __tablename__ = 'Job'
    __table_args__ = {'comment': 'Планирование работ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    jobType_id = Column(ForeignKey('rbJobType.id', ondelete='CASCADE'), nullable=False)
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'), nullable=False)
    date = Column(Date, nullable=False)
    begTime = Column(Time, nullable=False)
    endTime = Column(Time, nullable=False)
    quantity = Column(INTEGER(11), nullable=False)
    isOvertime = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    limitSuperviseUnit = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    orgStructureJob_id = Column(ForeignKey('OrgStructure_Job.id', ondelete='CASCADE'))
    personQuota = Column(INTEGER(3), nullable=False, server_default=alchemy_text("100"))
    eQueueType_id = Column(ForeignKey('rbEQueueType.id', ondelete='SET NULL', onupdate='CASCADE'))
    externalSystem = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))

    createPerson = relationship('Person', primaryjoin='Job.createPerson_id == Person.id')
    eQueueType = relationship('RbEQueueType')
    jobType = relationship('RbJobType')
    modifyPerson = relationship('Person', primaryjoin='Job.modifyPerson_id == Person.id')
    orgStructureJob = relationship('OrgStructureJob')
    orgStructure = relationship('OrgStructure')
    person = relationship('Person', primaryjoin='Job.person_id == Person.id')


class LastNameList(Base):
    __tablename__ = 'LastNameList'
    __table_args__ = {'comment': 'История фамилий. Заполняется если включена настройка 80'}

    id = Column(INTEGER(11), primary_key=True)
    create_datetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    lastName = Column(String(64))
    typeLastName = Column(INTEGER(11))
    commentLastName = Column(String(128))
    firstName = Column(String(64))
    typeFirstName = Column(INTEGER(11))
    commentFirstName = Column(String(128))
    patrName = Column(String(64))
    typePatrName = Column(INTEGER(11))
    commentPatrName = Column(String(128))

    client = relationship('Client')


class OrgStructureActionType(Base):
    __tablename__ = 'OrgStructure_ActionType'
    __table_args__ = {'comment': 'Привязка типов действий к подразделениям'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    actionType_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE', onupdate='CASCADE'))

    actionType = relationship('ActionType')
    master = relationship('OrgStructure')


class OrgStructureEventType(Base):
    __tablename__ = 'OrgStructure_EventType'
    __table_args__ = {'comment': 'Привязка типов событий к подразделениям'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'))

    eventType = relationship('EventType')
    master = relationship('OrgStructure')


class PersonFavouriteActionType(Base):
    __tablename__ = 'Person_FavouriteActionTypes'
    __table_args__ = {'comment': 'Избранные услуги'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    actionType_id = Column(ForeignKey('ActionType.id'), nullable=False)

    actionType = relationship('ActionType')
    person = relationship('Person')


class PoliclinicReferral(Base):
    __tablename__ = 'PoliclinicReferrals'
    __table_args__ = {'comment': 'Таблица, направлений от поликлиники.'}

    id = Column(INTEGER(11), primary_key=True)
    number = Column(String(64), nullable=False)
    refDate = Column(Date, nullable=False)
    status = Column(String(64))
    organisation_id = Column(ForeignKey('Organisation.id', onupdate='CASCADE'))
    orgStruct_id = Column(ForeignKey('OrgStructure.id', onupdate='CASCADE'))
    bedProfile_id = Column(INTEGER(11))
    hospDate = Column(Date)
    person_id = Column(ForeignKey('Person.id', onupdate='CASCADE'), nullable=False)
    client_id = Column(ForeignKey('Client.id', onupdate='CASCADE'), nullable=False)
    MKB = Column(String(64), nullable=False)
    note = Column(Text)

    client = relationship('Client')
    orgStruct = relationship('OrgStructure')
    organisation = relationship('Organisation')
    person = relationship('Person')


class ReferralTemplate(Base):
    __tablename__ = 'ReferralTemplate'
    __table_args__ = {'comment': 'Шаблоны направлений'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    code = Column(String(16))
    name = Column(String(64))
    referral_id = Column(ForeignKey('Referral.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    defaultDate = Column(TINYINT(4), server_default=alchemy_text("0"))
    eventType_id = Column(ForeignKey('EventType.id', ondelete='CASCADE', onupdate='CASCADE'))
    eventResult_id = Column(ForeignKey('rbResult.id', ondelete='CASCADE', onupdate='CASCADE'))
    actionType_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE', onupdate='CASCADE'))
    actionStatus = Column(TINYINT(4))
    noActionType_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE', onupdate='CASCADE'))

    actionType = relationship('ActionType', primaryjoin='ReferralTemplate.actionType_id == ActionType.id')
    createPerson = relationship('Person', primaryjoin='ReferralTemplate.createPerson_id == Person.id')
    eventResult = relationship('RbResult')
    eventType = relationship('EventType')
    modifyPerson = relationship('Person', primaryjoin='ReferralTemplate.modifyPerson_id == Person.id')
    noActionType = relationship('ActionType', primaryjoin='ReferralTemplate.noActionType_id == ActionType.id')
    referral = relationship('Referral')


class SignedIEMKDocument(Base):
    __tablename__ = 'SignedIEMKDocument'
    __table_args__ = {'comment': 'Подписанные документы для ИЭМК'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    event_id = Column(INTEGER(11))
    action_id = Column(INTEGER(11))
    person_id = Column(INTEGER(11))
    sign_date = Column(DateTime)
    deleted = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    document_code = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    file_id = Column(INTEGER(11), nullable=False)
    sign_id = Column(INTEGER(11), nullable=False)
    html = Column(Text, nullable=False)
    template_id = Column(INTEGER(11), nullable=False)
    createPersonId = Column(INTEGER(11), nullable=False)
    status = Column(INTEGER(11), nullable=False, server_default=alchemy_text("2"))
    description = Column(Text)
    messageId = Column(String(64))
    doc_date = Column(Date, nullable=False)
    doc_version = Column(INTEGER(11), nullable=False)
    mis_messageId = Column(String(64), nullable=False)
    txt = Column(Text, nullable=False)
    IEMKEventLog_id = Column(INTEGER(11))
    certOwner = Column(String(512))
    certSerial = Column(String(128))
    notValidBefore = Column(DateTime)
    notValidAfter = Column(DateTime)
    ownerOrganisation = Column(String(512))
    file_path = Column(String(512))
    file_name = Column(String(512))
    sign_path = Column(String(512))

    client = relationship('Client')


class StockTran(Base):
    __tablename__ = 'StockTrans'
    __table_args__ = {'comment': 'Фантазия на тему бух. проводки'}

    id = Column(BIGINT(11), primary_key=True)
    stockMotionItem_id = Column(ForeignKey('StockMotion_Item.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    date = Column(DateTime, nullable=False, server_default=alchemy_text("'0000-00-00 00:00:00'"))
    qnt = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    sum = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    debOrgStructure_id = Column(ForeignKey('OrgStructure.id'))
    debNomenclature_id = Column(ForeignKey('rbNomenclature.id'))
    debFinance_id = Column(ForeignKey('rbFinance.id'))
    creOrgStructure_id = Column(ForeignKey('OrgStructure.id'))
    creNomenclature_id = Column(ForeignKey('rbNomenclature.id'))
    creFinance_id = Column(ForeignKey('rbFinance.id'))
    batch = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    shelfTime = Column(Date)

    creFinance = relationship('RbFinance', primaryjoin='StockTran.creFinance_id == RbFinance.id')
    creNomenclature = relationship('RbNomenclature', primaryjoin='StockTran.creNomenclature_id == RbNomenclature.id')
    creOrgStructure = relationship('OrgStructure', primaryjoin='StockTran.creOrgStructure_id == OrgStructure.id')
    debFinance = relationship('RbFinance', primaryjoin='StockTran.debFinance_id == RbFinance.id')
    debNomenclature = relationship('RbNomenclature', primaryjoin='StockTran.debNomenclature_id == RbNomenclature.id')
    debOrgStructure = relationship('OrgStructure', primaryjoin='StockTran.debOrgStructure_id == OrgStructure.id')
    stockMotionItem = relationship('StockMotionItem')


class SuiteReagentTest(Base):
    __tablename__ = 'SuiteReagent_Test'
    __table_args__ = {'comment': 'Связанные с набором реагентов тесты'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('SuiteReagent.id', ondelete='CASCADE'), nullable=False)
    test_id = Column(ForeignKey('rbTest.id', ondelete='SET NULL'))

    master = relationship('SuiteReagent')
    test = relationship('RbTest')


class TakenTissueJournal(Base):
    __tablename__ = 'TakenTissueJournal'
    __table_args__ = {'comment': 'Журнал забора тканей'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='SET NULL'), ForeignKey('Client.id', ondelete='CASCADE'))
    tissueType_id = Column(ForeignKey('rbTissueType.id', ondelete='CASCADE'), ForeignKey('rbTissueType.id', ondelete='SET NULL'))
    externalId = Column(String(30), nullable=False)
    number = Column(String(30), nullable=False)
    amount = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    unit_id = Column(ForeignKey('rbUnit.id', ondelete='SET NULL'))
    datetimeTaken = Column(DateTime, nullable=False)
    execPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    note = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    status = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    client = relationship('Client', primaryjoin='TakenTissueJournal.client_id == Client.id')
    createPerson = relationship('Person', primaryjoin='TakenTissueJournal.createPerson_id == Person.id')
    execPerson = relationship('Person', primaryjoin='TakenTissueJournal.execPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='TakenTissueJournal.modifyPerson_id == Person.id')
    tissueType = relationship('RbTissueType', primaryjoin='TakenTissueJournal.tissueType_id == RbTissueType.id')
    unit = relationship('RbUnit')


class TempInvalid(Base):
    __tablename__ = 'TempInvalid'
    __table_args__ = {'comment': 'Случай ВУТ, инвалидности или ограничения жизнедеятельности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    type = Column(TINYINT(2), nullable=False, server_default=alchemy_text("0"))
    doctype = Column(TINYINT(4), nullable=False)
    doctype_id = Column(INTEGER(11))
    serial = Column(String(8), nullable=False)
    number = Column(String(16), nullable=False)
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    tempInvalidReason_id = Column(ForeignKey('rbTempInvalidReason.id'))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    person_id = Column(ForeignKey('Person.id'))
    diagnosis_id = Column(INTEGER(11))
    sex = Column(TINYINT(1), nullable=False)
    age = Column(TINYINT(3), nullable=False)
    notes = Column(TINYTEXT, nullable=False)
    duration = Column(INTEGER(4), nullable=False)
    closed = Column(TINYINT(1), nullable=False)
    prev_id = Column(INTEGER(11))
    insuranceOfficeMark = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    caseBegDate = Column(Date, nullable=False)
    tempInvalidExtraReason_id = Column(ForeignKey('rbTempInvalidExtraReason.id'))
    busyness = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    placeWork = Column(String(64))
    employmentService = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    mainNumber = Column(String(16))
    state = Column(INTEGER(11), server_default=alchemy_text("0"))
    signedMessage = Column(Text)
    is_ELN = Column(TINYINT(1), server_default=alchemy_text("0"))
    ln_hash = Column(String(32))
    parent_id = Column(INTEGER(11))
    firstRelation = Column(INTEGER(11))
    secondRelation = Column(INTEGER(11))
    issueDate = Column(Date)
    pregnancyTwelveWeeks = Column(TINYINT(1))
    isDuplicate = Column(TINYINT(1), server_default=alchemy_text("0"))
    sanatoriumOGRN = Column(Text)
    regDateInMSE = Column(Date)
    prolongFlag = Column(TINYINT(1), server_default=alchemy_text("0"))
    prev_ln = Column(String(12))

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='TempInvalid.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='TempInvalid.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='TempInvalid.person_id == Person.id')
    tempInvalidExtraReason = relationship('RbTempInvalidExtraReason')
    tempInvalidReason = relationship('RbTempInvalidReason')


class TempInvalidELN(Base):
    __tablename__ = 'TempInvalidELN'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    duplicate = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isImported = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    number = Column(String(16))
    prev_id = Column(INTEGER(11))
    prev_ln = Column(String(16))
    next_id = Column(INTEGER(11))
    next_ln = Column(String(16))
    lnDate = Column(Date)
    lpu_name = Column(String(90))
    lpu_address = Column(Text)
    lpu_ogrn = Column(String(15))
    caseDate = Column(Date)
    parent_id = Column(INTEGER(11))
    parent_ln = Column(String(16))
    client_id = Column(ForeignKey('Client.id'))
    lastName = Column(String(60))
    firstName = Column(String(60))
    patrName = Column(String(60))
    birthDate = Column(Date)
    age = Column(TINYINT(1))
    sex = Column(TINYINT(1))
    SNILS = Column(String(11))
    isStationary = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    hospital_dt1 = Column(Date)
    hospital_dt2 = Column(Date)
    pregn12w_flag = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    reason1_id = Column(ForeignKey('rbTempInvalidReason.id'))
    reason2_id = Column(ForeignKey('rbTempInvalidExtraReason.id'))
    diagnos = Column(String(10))
    mseDate1 = Column(Date)
    mseDate2 = Column(Date)
    mseDate3 = Column(Date)
    mse_invalid_group = Column(TINYINT(1))
    employerFlag = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    employer = Column(String(60))
    voucher_no = Column(String(10))
    voucher_ogrn = Column(String(15))
    date1 = Column(Date)
    date2 = Column(Date)
    serv1_fio = Column(String(100))
    serv1_month = Column(INTEGER(3))
    serv1_age = Column(INTEGER(3))
    serv1_relation_code = Column(TINYINT(1))
    serv2_fio = Column(String(100))
    serv2_month = Column(INTEGER(3))
    serv2_age = Column(INTEGER(3))
    serv2_relation_code = Column(TINYINT(1))
    letswork = Column(Date)
    breach_id = Column(ForeignKey('rbTempInvalidBreak.id'))
    breach_date = Column(Date)
    mse_result = Column(INTEGER(11))
    mse_date = Column(Date)
    begDate = Column(Date)
    endDate = Column(Date)
    duration = Column(INTEGER(4))
    person_id = Column(ForeignKey('Person.id'))
    note = Column(Text)
    closed = Column(TINYINT(1))
    state = Column(TINYINT(1))
    signedMessage = Column(Text)
    ln_hash = Column(String(32))
    reason3_id = Column(String(2))
    version = Column(String(12))
    unconditional = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    idMo = Column(String(60), server_default=alchemy_text("''"))
    previouslyIssuedCode = Column(String(24), server_default=alchemy_text("''"))
    writtenAgreementFlag = Column(TINYINT(1), nullable=False, server_default=alchemy_text("1"))
    intermittenMethodFlag = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    serv1snils = Column(String(12), server_default=alchemy_text("''"))
    isStatServ1 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    serv1birthday = Column(Date)
    serv1reason1 = Column(INTEGER(11))
    serv1diagnos = Column(String(10))
    chkCare1Serv1 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    chkCare2Serv1 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    chkCare3Serv1 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    edtBegCareDate1Serv1 = Column(Date)
    edtEndCareDate1Serv1 = Column(Date)
    edtBegCareDate2Serv1 = Column(Date)
    edtEndCareDate2Serv1 = Column(Date)
    edtBegCareDate3Serv1 = Column(Date)
    edtEndCareDate3Serv1 = Column(Date)
    serv2snils = Column(String(12), server_default=alchemy_text("''"))
    isStatServ2 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    serv2birthday = Column(Date)
    serv2reason1 = Column(INTEGER(11))
    serv2diagnos = Column(String(10))
    chkCare1Serv2 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    chkCare2Serv2 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    chkCare3Serv2 = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    edtBegCareDate1Serv2 = Column(Date)
    edtEndCareDate1Serv2 = Column(Date)
    edtBegCareDate2Serv2 = Column(Date)
    edtEndCareDate2Serv2 = Column(Date)
    edtBegCareDate3Serv2 = Column(Date)
    edtEndCareDate3Serv2 = Column(Date)
    error = Column(Text, server_default=alchemy_text("''"))

    breach = relationship('RbTempInvalidBreak')
    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='TempInvalidELN.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='TempInvalidELN.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='TempInvalidELN.person_id == Person.id')
    reason1 = relationship('RbTempInvalidReason')
    reason2 = relationship('RbTempInvalidExtraReason')


class TreatmentPlanItemsTemplate(Base):
    __tablename__ = 'TreatmentPlanItemsTemplate'
    __table_args__ = {'comment': 'Шаблоны элементов плана лечения'}

    id = Column(INTEGER(11), primary_key=True)
    element_id = Column(ForeignKey('ActionType.id', onupdate='CASCADE'), nullable=False)
    planTemplate_id = Column(ForeignKey('TreatmentPlanTemplate.id', onupdate='CASCADE'), nullable=False)
    count = Column(INTEGER(11), nullable=False)
    isPrepaymentItem = Column(TINYINT(1), nullable=False)

    element = relationship('ActionType')
    planTemplate = relationship('TreatmentPlanTemplate')


class RbBlankAction(Base):
    __tablename__ = 'rbBlankActions'
    __table_args__ = {'comment': 'Бланки на основе Action'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    doctype_id = Column(ForeignKey('ActionType.id'), nullable=False)
    code = Column(String(16), nullable=False)
    name = Column(String(64), nullable=False)
    checkingSerial = Column(TINYINT(3), nullable=False)
    checkingNumber = Column(TINYINT(3), nullable=False)
    checkingAmount = Column(TINYINT(2), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbBlankAction.createPerson_id == Person.id')
    doctype = relationship('ActionType')
    modifyPerson = relationship('Person', primaryjoin='RbBlankAction.modifyPerson_id == Person.id')


class RbDNDiagnosesActionType(Base):
    __tablename__ = 'rbDNDiagnosesActionType'

    id = Column(INTEGER(11), primary_key=True)
    DNDiagnoses_id = Column(ForeignKey('rbDNDiagnoses.id', ondelete='CASCADE'), nullable=False)
    action_type_id = Column(ForeignKey('ActionType.id', ondelete='CASCADE'), nullable=False)

    DNDiagnoses = relationship('RbDNDiagnose')
    action_type = relationship('ActionType')


class RbDiagnosticResult(Base):
    __tablename__ = 'rbDiagnosticResult'
    __table_args__ = {'comment': 'Результат осмотра'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    eventPurpose_id = Column(ForeignKey('rbEventTypePurpose.id'), nullable=False)
    code = Column(String(8), nullable=False)
    name = Column(String(64), nullable=False)
    continued = Column(TINYINT(1), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    federalCode = Column(String(8), nullable=False)
    result_id = Column(ForeignKey('rbResult.id'))
    begDate = Column(Date, nullable=False, server_default=alchemy_text("'1900-01-01'"))
    endDate = Column(Date, nullable=False, server_default=alchemy_text("'2999-12-31'"))
    filterResults = Column(TINYINT(1), server_default=alchemy_text("0"))
    netrica_Code = Column(String(65))

    createPerson = relationship('Person', primaryjoin='RbDiagnosticResult.createPerson_id == Person.id')
    eventPurpose = relationship('RbEventTypePurpose')
    modifyPerson = relationship('Person', primaryjoin='RbDiagnosticResult.modifyPerson_id == Person.id')
    result = relationship('RbResult')
    results = relationship('RbResult', secondary='rbDiagnosticResult_rbResult')


class RbEquipmentTest(Base):
    __tablename__ = 'rbEquipment_Test'
    __table_args__ = {'comment': 'Тесты соответствующего оборудования'}

    id = Column(INTEGER(11), primary_key=True)
    equipment_id = Column(ForeignKey('rbEquipment.id', ondelete='CASCADE'), nullable=False)
    test_id = Column(ForeignKey('rbTest.id', ondelete='SET NULL'))
    hardwareTestCode = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    hardwareTestName = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    hardwareSpecimenCode = Column(String(32), nullable=False, server_default=alchemy_text("''"))
    hardwareSpecimenName = Column(String(128), nullable=False, server_default=alchemy_text("''"))

    equipment = relationship('RbEquipment')
    test = relationship('RbTest')


class RbHighTechCureMethodDiag(Base):
    __tablename__ = 'rbHighTechCureMethodDiag'

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    cureMethod_id = Column(ForeignKey('rbHighTechCureMethod.id'), nullable=False)
    MKB = Column(String(8), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbHighTechCureMethodDiag.createPerson_id == Person.id')
    cureMethod = relationship('RbHighTechCureMethod')
    modifyPerson = relationship('Person', primaryjoin='RbHighTechCureMethodDiag.modifyPerson_id == Person.id')


class RbJobTypeActionType(Base):
    __tablename__ = 'rbJobType_ActionType'
    __table_args__ = {'comment': 'Действия связанные с типом работ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbJobType.id', ondelete='CASCADE'), nullable=False)
    actionType_id = Column(ForeignKey('ActionType.id', ondelete='SET NULL'))
    selectionGroup = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    onDayLimit = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))

    actionType = relationship('ActionType')
    createPerson = relationship('Person', primaryjoin='RbJobTypeActionType.createPerson_id == Person.id')
    master = relationship('RbJobType')
    modifyPerson = relationship('Person', primaryjoin='RbJobTypeActionType.modifyPerson_id == Person.id')


class RbLaboratoryTest(Base):
    __tablename__ = 'rbLaboratory_Test'
    __table_args__ = {'comment': 'Уточнение унифицированного справочника для конкретной ЛИС'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('rbLaboratory.id', ondelete='CASCADE'), nullable=False)
    test_id = Column(ForeignKey('rbTest.id', ondelete='CASCADE'), nullable=False)
    book = Column(String(64), nullable=False)
    code = Column(String(64), nullable=False)

    master = relationship('RbLaboratory')
    test = relationship('RbTest')


class RbMenuContent(Base):
    __tablename__ = 'rbMenu_Content'
    __table_args__ = {'comment': 'Содержимое справочника Шаблон питания'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbMenu.id'), nullable=False)
    mealTime_id = Column(ForeignKey('rbMealTime.id'), nullable=False)
    meal_id = Column(ForeignKey('rbMeal.id'), nullable=False)

    createPerson = relationship('Person', primaryjoin='RbMenuContent.createPerson_id == Person.id')
    master = relationship('RbMenu')
    mealTime = relationship('RbMealTime')
    meal = relationship('RbMeal')
    modifyPerson = relationship('Person', primaryjoin='RbMenuContent.modifyPerson_id == Person.id')


class RbNomenclatureType(Base):
    __tablename__ = 'rbNomenclatureType'
    __table_args__ = {'comment': 'Типы номенклатуры ЛСиИМН'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    kind_id = Column(ForeignKey('rbNomenclatureKind.id', ondelete='SET NULL', onupdate='CASCADE'))
    code = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    name = Column(String(128), nullable=False, server_default=alchemy_text("''"))

    createPerson = relationship('Person', primaryjoin='RbNomenclatureType.createPerson_id == Person.id')
    kind = relationship('RbNomenclatureKind')
    modifyPerson = relationship('Person', primaryjoin='RbNomenclatureType.modifyPerson_id == Person.id')


class RbPrintTemplatePerson(Base):
    __tablename__ = 'rbPrintTemplate_Persons'
    __table_args__ = {'comment': 'Таблица для хранения данных о доступности пользователям шаблонов печати'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('rbPrintTemplate.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    master = relationship('RbPrintTemplate')
    person = relationship('Person')


class RbPrintTemplateProfile(Base):
    __tablename__ = 'rbPrintTemplate_Profiles'
    __table_args__ = {'comment': 'Таблица для хранения данных о доступности профилям прав шаблонов печати'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('rbPrintTemplate.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    profile_id = Column(ForeignKey('rbUserProfile.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    master = relationship('RbPrintTemplate')
    profile = relationship('RbUserProfile')


class RbSocStatusType(Base):
    __tablename__ = 'rbSocStatusType'
    __table_args__ = {'comment': 'Социальный статус: тип (льготы)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    code = Column(String(8), nullable=False)
    name = Column(String(250), nullable=False)
    regionalCode = Column(String(8), nullable=False)
    documentType_id = Column(ForeignKey('rbDocumentType.id'))
    netrica_Code = Column(String(64))

    createPerson = relationship('Person', primaryjoin='RbSocStatusType.createPerson_id == Person.id')
    documentType = relationship('RbDocumentType')
    modifyPerson = relationship('Person', primaryjoin='RbSocStatusType.modifyPerson_id == Person.id')


class RbTestAnalogTest(Base):
    __tablename__ = 'rbTest_AnalogTest'
    __table_args__ = {'comment': 'Аналоги тестов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    master_id = Column(ForeignKey('rbTest.id', ondelete='CASCADE'), nullable=False)
    analogTest_id = Column(ForeignKey('rbTest.id', ondelete='SET NULL'))

    analogTest = relationship('RbTest', primaryjoin='RbTestAnalogTest.analogTest_id == RbTest.id')
    createPerson = relationship('Person', primaryjoin='RbTestAnalogTest.createPerson_id == Person.id')
    master = relationship('RbTest', primaryjoin='RbTestAnalogTest.master_id == RbTest.id')
    modifyPerson = relationship('Person', primaryjoin='RbTestAnalogTest.modifyPerson_id == Person.id')


class RcReportGroup(Base):
    __tablename__ = 'rcReport_Group'
    __table_args__ = {'comment': 'Группировка для запросов в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    number = Column(INTEGER(5), nullable=False, server_default=alchemy_text("0"))
    field = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    master_id = Column(ForeignKey('rcReport.id', ondelete='SET NULL', onupdate='CASCADE'))

    master = relationship('RcReport')


class RcReportParam(Base):
    __tablename__ = 'rcReport_Params'
    __table_args__ = {'comment': 'Параметры для запроса в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    param_id = Column(ForeignKey('rcParam.id', ondelete='SET NULL', onupdate='CASCADE'))
    master_id = Column(ForeignKey('rcReport.id', ondelete='SET NULL', onupdate='CASCADE'))

    master = relationship('RcReport')
    param = relationship('RcParam')


class RcReportTableCapCell(Base):
    __tablename__ = 'rcReport_TableCapCells'
    __table_args__ = {'comment': 'Ячейки шапки таблицы в конструкторе отчётов'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(256), nullable=False, server_default=alchemy_text("''"))
    row = Column(INTEGER(4), nullable=False)
    column = Column(INTEGER(4), nullable=False)
    rowSpan = Column(INTEGER(4), nullable=False, server_default=alchemy_text("1"))
    columnSpan = Column(INTEGER(4), nullable=False, server_default=alchemy_text("1"))
    master_id = Column(ForeignKey('rcReport.id', ondelete='SET NULL', onupdate='CASCADE'))
    alignment = Column(String(10), server_default=alchemy_text("'left'"))
    bold = Column(TINYINT(1), server_default=alchemy_text("0"))
    type = Column(String(10), server_default=alchemy_text("'cap'"))

    master = relationship('RcReport')


class ReferralMseTimeout(Base):
    __tablename__ = 'referral_mse_timeout'
    __table_args__ = {'comment': 'Таймаут автоматического обновления статусов МСЭ'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False, server_default=alchemy_text("current_timestamp() ON UPDATE current_timestamp()"))

    client = relationship('Client')





class Account(Base):
    __tablename__ = 'Account'
    __table_args__ = {'comment': 'Выставленные счета за оказанные услуги'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isPreliminary = Column(TINYINT(1), server_default=alchemy_text("0"))
    contract_id = Column(ForeignKey('Contract.id'), nullable=False)
    orgStructure_id = Column(INTEGER(11))
    payer_id = Column(INTEGER(11), nullable=False)
    settleDate = Column(Date, nullable=False)
    number = Column(String(64), server_default=alchemy_text("''"))
    date = Column(Date, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    uet = Column(DECIMAL(10, 2), nullable=False)
    sum = Column(DECIMAL(10, 2), nullable=False)
    exposeDate = Column(DateTime)
    payedAmount = Column(DECIMAL(10, 2), nullable=False)
    payedSum = Column(DECIMAL(10, 2), nullable=False)
    refusedAmount = Column(DECIMAL(10, 2), nullable=False)
    refusedSum = Column(DECIMAL(10, 2), nullable=False)
    format_id = Column(ForeignKey('rbAccountExportFormat.id', ondelete='SET NULL'))
    accountType_id = Column(ForeignKey('rbAccountType.id', ondelete='SET NULL', onupdate='CASCADE'))
    exportFileName = Column(String(64))
    acceptNewKSLPForChildWithOnko = Column(TINYINT(1), server_default=alchemy_text("0"))
    acceptNewKSLPForChild = Column(TINYINT(1), server_default=alchemy_text("0"))
    eisImportDate = Column(DateTime)

    accountType = relationship('RbAccountType')
    contract = relationship('Contract')
    createPerson = relationship('Person', primaryjoin='Account.createPerson_id == Person.id')
    format = relationship('RbAccountExportFormat')
    modifyPerson = relationship('Person', primaryjoin='Account.modifyPerson_id == Person.id')


class Action(Base):
    __tablename__ = 'Action'
    __table_args__ = {'comment': 'Описание действия'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    actionType_id = Column(ForeignKey('ActionType.id'), nullable=False)
    specifiedName = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE'))
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    directionDate = Column(DateTime)
    status = Column(TINYINT(4), nullable=False)
    setPerson_id = Column(ForeignKey('Person.id'))
    isUrgent = Column(INTEGER(1), nullable=False, server_default=alchemy_text("0"))
    begDate = Column(DateTime)
    plannedEndDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime)
    note = Column(Text, nullable=False)
    person_id = Column(ForeignKey('Person.id'))
    office = Column(String(16), nullable=False)
    amount = Column(Float(asdecimal=True), nullable=False)
    uet = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    expose = Column(INTEGER(1), nullable=False, server_default=alchemy_text("1"))
    payStatus = Column(INTEGER(11), nullable=False)
    account = Column(TINYINT(1), nullable=False)
    MKB = Column(String(8), nullable=False)
    morphologyMKB = Column(String(16), nullable=False)
    finance_id = Column(ForeignKey('rbFinance.id', ondelete='SET NULL'))
    contract_id = Column(ForeignKey('Contract.id', ondelete='SET NULL'))
    prescription_id = Column(ForeignKey('Action.id', ondelete='SET NULL', onupdate='CASCADE'))
    takenTissueJournal_id = Column(ForeignKey('TakenTissueJournal.id', ondelete='SET NULL'))
    org_id = Column(ForeignKey('Organisation.id', ondelete='SET NULL'))
    coordDate = Column(DateTime)
    coordAgent = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    coordInspector = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    coordText = Column(TINYTEXT, nullable=False)
    assistant_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    preliminaryResult = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    duration = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    periodicity = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    aliquoticity = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    assistant2_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    assistant3_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    packPurchasePrice = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    doseRatePrice = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    MES_id = Column(INTEGER(11))
    hmpKind_id = Column(ForeignKey('rbHighTechCureKind.id'))
    hmpMethod_id = Column(ForeignKey('rbHighTechCureMethod.id'))
    counterValue = Column(String(30))
    customSum = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    parent_id = Column(ForeignKey('Action.id', ondelete='SET NULL', onupdate='CASCADE'))
    isVerified = Column(TINYINT(1), server_default=alchemy_text("0"))
    importDate = Column(DateTime)
    signature = Column(INTEGER(11), server_default=alchemy_text("0"))

    actionType = relationship('ActionType')
    assistant2 = relationship('Person', primaryjoin='Action.assistant2_id == Person.id')
    assistant3 = relationship('Person', primaryjoin='Action.assistant3_id == Person.id')
    assistant = relationship('Person', primaryjoin='Action.assistant_id == Person.id')
    contract = relationship('Contract')
    createPerson = relationship('Person', primaryjoin='Action.createPerson_id == Person.id')
    event = relationship('Event')
    finance = relationship('RbFinance')
    hmpKind = relationship('RbHighTechCureKind')
    hmpMethod = relationship('RbHighTechCureMethod')
    modifyPerson = relationship('Person', primaryjoin='Action.modifyPerson_id == Person.id')
    org = relationship('Organisation')
    parent = relationship('Action', remote_side=[id], primaryjoin='Action.parent_id == Action.id')
    person = relationship('Person', primaryjoin='Action.person_id == Person.id')
    prescription = relationship('Action', remote_side=[id], primaryjoin='Action.prescription_id == Action.id')
    setPerson = relationship('Person', primaryjoin='Action.setPerson_id == Person.id')
    takenTissueJournal = relationship('TakenTissueJournal')


class ActionPropertyActivateCondition(Base):
    __tablename__ = 'ActionPropertyActivateCondition'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ActionPropertyType.id'))
    affectProperty = Column(ForeignKey('ActionPropertyType.id'))
    sign = Column(String(20))
    status = Column(String(20))
    value = Column(Text)

    ActionPropertyType = relationship('ActionPropertyType', primaryjoin='ActionPropertyActivateCondition.affectProperty == ActionPropertyType.id')
    master = relationship('ActionPropertyType', primaryjoin='ActionPropertyActivateCondition.master_id == ActionPropertyType.id')


class BlankActionsParty(Base):
    __tablename__ = 'BlankActions_Party'
    __table_args__ = {'comment': 'Случай ВУТ, инвалидности или ограничения жизнедеятельности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    date = Column(Date, nullable=False)
    doctype_id = Column(ForeignKey('rbBlankActions.id'), nullable=False)
    person_id = Column(ForeignKey('Person.id'))
    serial = Column(String(8), nullable=False)
    numberFrom = Column(String(16), nullable=False)
    numberTo = Column(String(16), nullable=False)
    amount = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    extradited = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    returnBlank = Column(INTEGER(11), nullable=False)
    balance = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    used = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    writing = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))

    createPerson = relationship('Person', primaryjoin='BlankActionsParty.createPerson_id == Person.id')
    doctype = relationship('RbBlankAction')
    modifyPerson = relationship('Person', primaryjoin='BlankActionsParty.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='BlankActionsParty.person_id == Person.id')


class BlankTempInvalidMoving(Base):
    __tablename__ = 'BlankTempInvalid_Moving'
    __table_args__ = {'comment': 'Случай ВУТ, инвалидности или ограничения жизнедеятельности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    date = Column(Date, nullable=False)
    blankParty_id = Column(ForeignKey('BlankTempInvalid_Party.id'), nullable=False)
    numberFrom = Column(String(16), nullable=False)
    numberTo = Column(String(16), nullable=False)
    orgStructure_id = Column(ForeignKey('OrgStructure.id'))
    person_id = Column(ForeignKey('Person.id'))
    received = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    used = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    returnDate = Column(Date)
    returnAmount = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))

    blankParty = relationship('BlankTempInvalidParty')
    createPerson = relationship('Person', primaryjoin='BlankTempInvalidMoving.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='BlankTempInvalidMoving.modifyPerson_id == Person.id')
    orgStructure = relationship('OrgStructure')
    person = relationship('Person', primaryjoin='BlankTempInvalidMoving.person_id == Person.id')


class ClientAttach(Base):
    __tablename__ = 'ClientAttach'
    __table_args__ = {'comment': 'Прикрепление пациентов'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    attachType_id = Column(ForeignKey('rbAttachType.id'), nullable=False)
    LPU_id = Column(INTEGER(11), nullable=False)
    netType = Column(INTEGER(11))
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='SET NULL'))
    begDate = Column(Date, nullable=False)
    endDate = Column(Date)
    document_id = Column(ForeignKey('ClientDocument.id'))
    detachment_id = Column(ForeignKey('rbDetachmentReason.id', ondelete='SET NULL', onupdate='CASCADE'))
    sentToTFOMS = Column(TINYINT(1), nullable=False)
    errorCode = Column(String(256))
    reason = Column(TINYINT(4), server_default=alchemy_text("0"))

    attachType = relationship('RbAttachType')
    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientAttach.createPerson_id == Person.id')
    detachment = relationship('RbDetachmentReason')
    document = relationship('ClientDocument')
    modifyPerson = relationship('Person', primaryjoin='ClientAttach.modifyPerson_id == Person.id')
    orgStructure = relationship('OrgStructure')


class ClientDisability(Base):
    __tablename__ = 'ClientDisability'
    __table_args__ = {'comment': 'Инвалидность пациента'}

    id = Column(INTEGER(11), primary_key=True)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    setDate = Column(Date, nullable=False)
    groupNumber = Column(INTEGER(11))
    recertificationDate = Column(Date)
    work_id = Column(ForeignKey('ClientWork.id', ondelete='SET NULL', onupdate='SET NULL'))
    degree = Column(INTEGER(11))
    note = Column(String(256), nullable=False)
    isPrimary = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    isSomatic = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isStationary = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isTermless = Column(TINYINT(1), server_default=alchemy_text("0"))

    client = relationship('Client')
    work = relationship('ClientWork')


class ClientExaminationPlanSPB(Base):
    __tablename__ = 'ClientExaminationPlan_SPB'
    __table_args__ = {'comment': 'Диспансеризация и профилактические осмотры для Санкт-Петербурга'}

    id = Column(INTEGER(11), primary_key=True)
    datcreup = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    tfoms_client_id = Column(INTEGER(11))
    event_id = Column(INTEGER(11))
    clientExaminationPlan_TFOMS_SPB_id = Column(INTEGER(11))
    kind = Column(INTEGER(11), nullable=False)
    category = Column(INTEGER(4))
    year = Column(SMALLINT(4), nullable=False)
    month = Column(TINYINT(4), nullable=False)
    orgCode = Column(CHAR(16))
    status = Column(TINYINT(3), nullable=False, server_default=alchemy_text("0"))
    step = Column(SMALLINT(4))
    stepStatus = Column(TINYINT(3), nullable=False, server_default=alchemy_text("0"))
    date = Column(DateTime)
    sendDate = Column(DateTime)
    idSmo = Column(INTEGER(11), nullable=False)
    idLpu = Column(INTEGER(11), nullable=False)
    lpuFedCode = Column(String(16))
    includeDate = Column(Date, nullable=False)
    eliminationDate = Column(Date)
    eliminationReason = Column(String(20))
    mkbx = Column(String(8))
    mkbxdate = Column(Date)
    mkbxstts = Column(TINYINT(4))
    mkbxmeth = Column(TINYINT(4))
    master_id = Column(ForeignKey('DNPlan.id', ondelete='SET NULL', onupdate='CASCADE'))
    event_id_stage1 = Column(INTEGER(11))
    event_id_stage2 = Column(INTEGER(11))

    client = relationship('Client')
    master = relationship('DNPlan')


class ClientExaminationPlanTFOM(Base):
    __tablename__ = 'ClientExaminationPlan_TFOMS'
    __table_args__ = {'comment': 'Загруженные из ТФОМС списки лиц, подлежащих проф. мероприятиям'}

    id = Column(INTEGER(11), primary_key=True)
    rid = Column(INTEGER(11))
    year = Column(SMALLINT(4))
    month = Column(TINYINT(4))
    kind = Column(TINYINT(1))
    category = Column(INTEGER(4))
    orgCode = Column(CHAR(16))
    sectionCode = Column(CHAR(16))
    lastName = Column(String(30), nullable=False, server_default=alchemy_text("''"))
    firstName = Column(String(30), nullable=False, server_default=alchemy_text("''"))
    patrName = Column(String(30), nullable=False, server_default=alchemy_text("''"))
    birthDate = Column(Date)
    sex = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    SNILS = Column(CHAR(11), nullable=False, server_default=alchemy_text("''"))
    contacts = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    docType = Column(TINYINT(1))
    docSerial = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    docNumber = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    policyType = Column(TINYINT(1))
    policySerial = Column(String(16), nullable=False, server_default=alchemy_text("''"))
    policyNumber = Column(String(35), nullable=False, server_default=alchemy_text("''"))
    insurerCode = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    insuranceArea = Column(String(8), nullable=False, server_default=alchemy_text("''"))
    ENP = Column(String(35), nullable=False, server_default=alchemy_text("''"))
    syncStatus = Column(TINYINT(1), server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='SET NULL', onupdate='CASCADE'))
    plan_id = Column(ForeignKey('ClientExaminationPlan.id', ondelete='SET NULL', onupdate='CASCADE'))
    mkbx = Column(String(8))
    mkbxdate = Column(Date)
    mkbxstts = Column(TINYINT(4))
    mkbxmeth = Column(TINYINT(4))
    doc_ss = Column(CHAR(11))

    client = relationship('Client')
    plan = relationship('ClientExaminationPlan')


class ClientPolicyIdentification(Base):
    __tablename__ = 'ClientPolicyIdentification'
    __table_args__ = {'comment': 'Таблица для хранения id полисов во внешней системе'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    modifyDatetime = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    clientPolicy_id = Column(ForeignKey('ClientPolicy.id'), nullable=False)
    accountingSystem_id = Column(ForeignKey('rbAccountingSystem.id'), nullable=False)
    identifier = Column(String(36))

    accountingSystem = relationship('RbAccountingSystem')
    clientPolicy = relationship('ClientPolicy')


class ClientSocStatu(Base):
    __tablename__ = 'ClientSocStatus'
    __table_args__ = {'comment': 'Социальный статус пациента'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    socStatusClass_id = Column(INTEGER(11))
    socStatusType_id = Column(ForeignKey('rbSocStatusType.id'), nullable=False)
    begDate = Column(Date, nullable=False)
    endDate = Column(Date)
    document_id = Column(INTEGER(11))
    notes = Column(TINYTEXT)

    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='ClientSocStatu.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ClientSocStatu.modifyPerson_id == Person.id')
    socStatusType = relationship('RbSocStatusType')


class ClientWorkHurt(Base):
    __tablename__ = 'ClientWork_Hurt'
    __table_args__ = {'comment': 'Вредность работы пациента'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ClientWork.id', ondelete='CASCADE'), nullable=False)
    hurtType_id = Column(ForeignKey('rbHurtType.id'), nullable=False)
    stage = Column(TINYINT(3), nullable=False)

    hurtType = relationship('RbHurtType')
    master = relationship('ClientWork')


class ClientWorkHurtFactor(Base):
    __tablename__ = 'ClientWork_Hurt_Factor'
    __table_args__ = {'comment': 'Вредные факторы работы пациента'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('ClientWork.id', ondelete='CASCADE'))
    factorType_id = Column(ForeignKey('rbHurtFactorType.id'), nullable=False)

    factorType = relationship('RbHurtFactorType')
    master = relationship('ClientWork')


class ContractContingent(Base):
    __tablename__ = 'Contract_Contingent'
    __table_args__ = {'comment': 'Контингент договора'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Contract.id', ondelete='CASCADE'), nullable=False)
    client_id = Column(ForeignKey('Client.id'))
    attachType_id = Column(ForeignKey('rbAttachType.id'))
    org_id = Column(INTEGER(11))
    socStatusType_id = Column(ForeignKey('rbSocStatusType.id'))
    insurer_id = Column(ForeignKey('Organisation.id'))
    policyType_id = Column(ForeignKey('rbPolicyType.id'))
    serviceArea = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)

    attachType = relationship('RbAttachType')
    client = relationship('Client')
    insurer = relationship('Organisation')
    master = relationship('Contract')
    policyType = relationship('RbPolicyType')
    socStatusType = relationship('RbSocStatusType')


class ContractContragent(Base):
    __tablename__ = 'Contract_Contragent'
    __table_args__ = {'comment': 'Контрагенты договора'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Contract.id', ondelete='CASCADE'), nullable=False)
    insurer_id = Column(INTEGER(11), nullable=False)
    payer_id = Column(INTEGER(11), nullable=False)
    payerAccount_id = Column(INTEGER(11), nullable=False)
    payerKBK = Column(String(30), nullable=False)
    begDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)

    master = relationship('Contract')


class ContractSpecification(Base):
    __tablename__ = 'Contract_Specification'
    __table_args__ = {'comment': 'Спецификация договора'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Contract.id', ondelete='CASCADE'), nullable=False)
    eventType_id = Column(ForeignKey('EventType.id'), nullable=False)

    eventType = relationship('EventType')
    master = relationship('Contract')


class ContractTariff(Base):
    __tablename__ = 'Contract_Tariff'
    __table_args__ = {'comment': 'Тариф договора'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    master_id = Column(ForeignKey('Contract.id', ondelete='CASCADE'), nullable=False)
    eventType_id = Column(ForeignKey('EventType.id'))
    tariffType = Column(TINYINT(1), nullable=False)
    service_id = Column(ForeignKey('rbService.id'))
    tariffCategory_id = Column(ForeignKey('rbTariffCategory.id', ondelete='SET NULL'))
    begDate = Column(Date)
    endDate = Column(Date)
    sex = Column(TINYINT(4), nullable=False)
    age = Column(String(9), nullable=False)
    attachType_id = Column(ForeignKey('rbAttachType.id', ondelete='SET NULL'))
    attachLPU_id = Column(ForeignKey('Organisation.id', ondelete='SET NULL'))
    unit_id = Column(ForeignKey('rbMedicalAidUnit.id'))
    amount = Column(Float(asdecimal=True), nullable=False)
    uet = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    price = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag1Start = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag1Sum = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag1Price = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag2Start = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag2Sum = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    frag2Price = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    limitationExceedMode = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    limitation = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    priceEx = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    limitation2ExceedMode = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    limitation2 = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    priceEx2 = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    MKB = Column(String(64), nullable=False)
    federalPrice = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    federalLimitation = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))
    speciality_id = Column(INTEGER(11))
    vat = Column(DECIMAL(3, 2), nullable=False, server_default=alchemy_text("0.00"))
    createPerson_id = Column(ForeignKey('Person.id'))
    createDatetime = Column(DateTime)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime)
    caseCast_id = Column(INTEGER(11))

    attachLPU = relationship('Organisation')
    attachType = relationship('RbAttachType')
    createPerson = relationship('Person', primaryjoin='ContractTariff.createPerson_id == Person.id')
    eventType = relationship('EventType')
    master = relationship('Contract')
    modifyPerson = relationship('Person', primaryjoin='ContractTariff.modifyPerson_id == Person.id')
    service = relationship('RbService')
    tariffCategory = relationship('RbTariffCategory')
    unit = relationship('RbMedicalAidUnit')


class DiagnosisChangeReason(Base):
    __tablename__ = 'DiagnosisChangeReason'
    __table_args__ = {'comment': 'Причины изменения диагноза'}

    id = Column(INTEGER(11), primary_key=True)
    person_id = Column(ForeignKey('Person.id'))
    createDate = Column(DateTime, server_default=alchemy_text("current_timestamp()"))
    diagnosis_id = Column(ForeignKey('Diagnosis.id'), nullable=False)
    event_id = Column(ForeignKey('Event.id'), nullable=False)
    reason = Column(String(255), nullable=False)
    new_MKB = Column(String(10))
    old_MKB = Column(String(10))
    status = Column(INTEGER(11))
    reason_rb = Column(INTEGER(11))

    diagnosis = relationship('Diagnosi')
    event = relationship('Event')
    person = relationship('Person')


class Diagnostic(Base):
    __tablename__ = 'Diagnostic'
    __table_args__ = {'comment': 'Диагностика (ввод диагнозов)'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE'), nullable=False)
    diagnosis_id = Column(ForeignKey('Diagnosis.id', ondelete='SET NULL'))
    TNMS = Column(String(512))
    diagnosisType_id = Column(ForeignKey('rbDiagnosisType.id'), nullable=False)
    character_id = Column(ForeignKey('rbDiseaseCharacter.id'))
    stage_id = Column(ForeignKey('rbDiseaseStage.id'))
    phase_id = Column(ForeignKey('rbDiseasePhases.id'))
    dispanser_id = Column(ForeignKey('rbDispanser.id'))
    sanatorium = Column(TINYINT(1), nullable=False)
    hospital = Column(TINYINT(1), nullable=False)
    traumaType_id = Column(ForeignKey('rbTraumaType.id'))
    speciality_id = Column(ForeignKey('rbSpeciality.id'), nullable=False)
    person_id = Column(ForeignKey('Person.id'))
    healthGroup_id = Column(ForeignKey('rbHealthGroup.id'))
    result_id = Column(ForeignKey('rbDiagnosticResult.id'), ForeignKey('rbDiagnosticResult.id'))
    setDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime)
    notes = Column(TINYTEXT, nullable=False)
    assistant_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    medicalGroup_id = Column(ForeignKey('rbMedicalGroup.id'))
    status = Column(TINYINT(4))
    org_id = Column(INTEGER(11))
    diagnosisRationale_id = Column(ForeignKey('rbDiagnosisRationale.id'))
    diagnosisNosologyType_id = Column(ForeignKey('rbDiagnosisNosologyType.id'))
    diagnosisPrimaryPluralTumor_id = Column(ForeignKey('rbDiagnosisPrimaryPluralTumor.id'))
    diagnosisTumorTopography_id = Column(ForeignKey('rbDiagnosisTumorTopography.id'))
    diagnosisAffectedSide_id = Column(ForeignKey('rbDiagnosisAffectedSide.id'))
    diagnosisMetastasesLocalization_id = Column(ForeignKey('rbDiagnosisMetastasesLocalization.id'))
    diagnosisTumorIndexNumber = Column(INTEGER(11))
    date_registration = Column(Date)

    assistant = relationship('Person', primaryjoin='Diagnostic.assistant_id == Person.id')
    character = relationship('RbDiseaseCharacter')
    createPerson = relationship('Person', primaryjoin='Diagnostic.createPerson_id == Person.id')
    diagnosisAffectedSide = relationship('RbDiagnosisAffectedSide')
    diagnosisMetastasesLocalization = relationship('RbDiagnosisMetastasesLocalization')
    diagnosisNosologyType = relationship('RbDiagnosisNosologyType')
    diagnosisPrimaryPluralTumor = relationship('RbDiagnosisPrimaryPluralTumor')
    diagnosisRationale = relationship('RbDiagnosisRationale')
    diagnosisTumorTopography = relationship('RbDiagnosisTumorTopography')
    diagnosisType = relationship('RbDiagnosisType')
    diagnosis = relationship('Diagnosi')
    dispanser = relationship('RbDispanser')
    event = relationship('Event')
    healthGroup = relationship('RbHealthGroup')
    medicalGroup = relationship('RbMedicalGroup')
    modifyPerson = relationship('Person', primaryjoin='Diagnostic.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='Diagnostic.person_id == Person.id')
    phase = relationship('RbDiseasePhase')
    result = relationship('RbDiagnosticResult', primaryjoin='Diagnostic.result_id == RbDiagnosticResult.id')
    speciality = relationship('RbSpeciality')
    stage = relationship('RbDiseaseStage')
    traumaType = relationship('RbTraumaType')


class DrugRecipe(Base):
    __tablename__ = 'DrugRecipe'
    __table_args__ = {'comment': 'Лекарственные рецепты'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', onupdate='CASCADE'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', onupdate='CASCADE'))
    event_id = Column(ForeignKey('Event.id', onupdate='CASCADE'))
    dateTime = Column(DateTime, nullable=False)
    number = Column(String(50), nullable=False)
    socCode = Column(String(50), nullable=False)
    pregCard = Column(INTEGER(11))
    finance_id = Column(ForeignKey('rbFinance.id', onupdate='CASCADE'), nullable=False, server_default=alchemy_text("0"))
    percentage = Column(INTEGER(11), nullable=False, server_default=alchemy_text("100"))
    mkb = Column(String(10), nullable=False)
    formularyItem_id = Column(ForeignKey('DloDrugFormulary_Item.id', onupdate='CASCADE'), nullable=False)
    dosage = Column(String(50), nullable=False)
    qnt = Column(INTEGER(11), nullable=False)
    duration = Column(INTEGER(11), nullable=False)
    numPerDay = Column(INTEGER(11), nullable=False)
    signa = Column(String(100), nullable=False)
    isVk = Column(TINYINT(4), nullable=False)
    term = Column(TINYINT(4), nullable=False)
    status = Column(TINYINT(4), nullable=False)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    sentToMiac = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    errorCode = Column(String(500))
    printMnn = Column(TINYINT(1), server_default=alchemy_text("1"))

    createPerson = relationship('Person', primaryjoin='DrugRecipe.createPerson_id == Person.id')
    event = relationship('Event')
    finance = relationship('RbFinance')
    formularyItem = relationship('DloDrugFormularyItem')
    modifyPerson = relationship('Person', primaryjoin='DrugRecipe.modifyPerson_id == Person.id')


class EQPersonPreference(Base):
    __tablename__ = 'EQPersonPreference'
    __table_args__ = {'comment': 'Пользовательские настройки табло электройнной очереди'}

    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE'), nullable=False)
    eqOffice_id = Column(ForeignKey('EQOffice.id', ondelete='SET NULL', onupdate='SET NULL'))
    isControlEnabled = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    dateControl = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    personControl = Column(TINYINT(4), nullable=False, server_default=alchemy_text("1"))
    id = Column(INTEGER(11), primary_key=True)

    eqOffice = relationship('EQOffice')
    person = relationship('Person')


class EQueueTicket(Base):
    __tablename__ = 'EQueueTicket'
    __table_args__ = {'comment': 'Талон/номерок электронной очереди.'}

    id = Column(INTEGER(11), primary_key=True)
    queue_id = Column(ForeignKey('EQueue.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    status = Column(TINYINT(4), nullable=False)
    idx = Column(INTEGER(11), nullable=False)
    value = Column(String(16), nullable=False)
    summonDatetime = Column(DateTime)
    orgStructure_id = Column(ForeignKey('OrgStructure.id', ondelete='SET NULL', onupdate='CASCADE'))

    orgStructure = relationship('OrgStructure')
    queue = relationship('EQueue')


class EventTypeAutoPrintRepeat(Base):
    __tablename__ = 'EventType_AutoPrint_Repeat'
    __table_args__ = {'comment': 'Отслеживание уже совершенной автопечати для реализации ее повторов'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('EventType_AutoPrint.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    checkData = Column(String(64), nullable=False)
    expiredDate = Column(Date)

    master = relationship('EventTypeAutoPrint')


class EventTypeZNOInfoMKB(Base):
    __tablename__ = 'EventType_ZNOInfo_MKB'
    __table_args__ = {'comment': 'Диагнозы МКБ шаблонов сведений ЗНО для типов событий'}

    id = Column(INTEGER(11), primary_key=True)
    diag_id = Column(String(9), nullable=False)
    master_id = Column(ForeignKey('EventType_ZNOInfo.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))

    master = relationship('EventTypeZNOInfo')


class EventTypeZNOMKB(Base):
    __tablename__ = 'EventType_ZNO_MKB'
    __table_args__ = {'comment': 'Диагнозы МКБ шаблонов подозрений на ЗНО для типов событий'}

    id = Column(INTEGER(11), primary_key=True)
    diag_id = Column(String(9), nullable=False)
    master_id = Column(ForeignKey('EventType_ZNO.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))

    master = relationship('EventTypeZNO')


class PaymentSchemeItem(Base):
    __tablename__ = 'PaymentSchemeItem'
    __table_args__ = {'comment': 'Этапы конкретного исследования/конкретной схемы оплаты'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    idx = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    name = Column(String(255))
    type = Column(TINYINT(1), nullable=False)
    paymentScheme_id = Column(ForeignKey('PaymentScheme.id', ondelete='CASCADE', onupdate='CASCADE'))
    contract_id = Column(ForeignKey('Contract.id'))

    contract = relationship('Contract')
    paymentScheme = relationship('PaymentScheme')


class Probe(Base):
    __tablename__ = 'Probe'
    __table_args__ = {'comment': 'Пробы'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    externalId = Column(String(30), nullable=False)
    equipment_id = Column(ForeignKey('rbEquipment.id', ondelete='SET NULL'))
    status = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    suiteReagent_id = Column(ForeignKey('SuiteReagent.id', ondelete='SET NULL'))
    test_id = Column(ForeignKey('rbTest.id', ondelete='SET NULL'))
    workTest_id = Column(ForeignKey('rbTest.id', ondelete='SET NULL'))
    takenTissueJournal_id = Column(ForeignKey('TakenTissueJournal.id', ondelete='CASCADE'), nullable=False)
    result1 = Column(String(128), nullable=False)
    result2 = Column(String(128), nullable=False)
    result3 = Column(String(128), nullable=False)
    typeName = Column(String(64), nullable=False)
    norm = Column(String(64), nullable=False)
    unit_id = Column(ForeignKey('rbUnit.id', ondelete='SET NULL'))
    resultIndex = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    isUrgent = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    containerType_id = Column(ForeignKey('rbContainerType.id', ondelete='SET NULL'))
    tripodNumber = Column(SMALLINT(2))
    placeInTripod = Column(SMALLINT(2))

    containerType = relationship('RbContainerType')
    createPerson = relationship('Person', primaryjoin='Probe.createPerson_id == Person.id')
    equipment = relationship('RbEquipment')
    modifyPerson = relationship('Person', primaryjoin='Probe.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='Probe.person_id == Person.id')
    suiteReagent = relationship('SuiteReagent')
    takenTissueJournal = relationship('TakenTissueJournal')
    test = relationship('RbTest', primaryjoin='Probe.test_id == RbTest.id')
    unit = relationship('RbUnit')
    workTest = relationship('RbTest', primaryjoin='Probe.workTest_id == RbTest.id')


class SocStatu(Base):
    __tablename__ = 'SocStatus'
    __table_args__ = {'comment': 'Описание социального статуса'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    socStatusClass_id = Column(ForeignKey('rbSocStatusClass.id'), nullable=False)
    socStatusType_id = Column(ForeignKey('rbSocStatusType.id'), nullable=False)

    createPerson = relationship('Person', primaryjoin='SocStatu.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='SocStatu.modifyPerson_id == Person.id')
    socStatusClass = relationship('RbSocStatusClas')
    socStatusType = relationship('RbSocStatusType')


class TempInvalidDuplicate(Base):
    __tablename__ = 'TempInvalidDuplicate'
    __table_args__ = {'comment': 'Дубликат документа ВУТ'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    deleted = Column(TINYINT(1), nullable=False)
    tempInvalid_id = Column(ForeignKey('TempInvalid.id', ondelete='CASCADE'), nullable=False)
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL'))
    date = Column(Date, nullable=False)
    serial = Column(String(8), nullable=False)
    number = Column(String(16), nullable=False)
    destination = Column(String(128), nullable=False)
    reason_id = Column(ForeignKey('rbTempInvalidDuplicateReason.id'))
    note = Column(TINYTEXT, nullable=False)
    insuranceOfficeMark = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    placeWork = Column(String(64))
    expert_id = Column(ForeignKey('Person.id'))

    createPerson = relationship('Person', primaryjoin='TempInvalidDuplicate.createPerson_id == Person.id')
    expert = relationship('Person', primaryjoin='TempInvalidDuplicate.expert_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='TempInvalidDuplicate.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='TempInvalidDuplicate.person_id == Person.id')
    reason = relationship('RbTempInvalidDuplicateReason')
    tempInvalid = relationship('TempInvalid')


class TempInvalidELNPeriod(Base):
    __tablename__ = 'TempInvalidELN_Period'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('TempInvalidELN.id'), nullable=False)
    begDate = Column(Date)
    endDate = Column(Date)
    doctor = Column(ForeignKey('Person.id'))
    doctor_role = Column(String(300))
    doctor_name = Column(String(90))
    chairman = Column(ForeignKey('Person.id'))
    chairman_role = Column(String(300))
    chairman_name = Column(String(90))
    toTherapist = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    state = Column(TINYINT(1), server_default=alchemy_text("0"))
    isUP = Column(TINYINT(4), server_default=alchemy_text("0"))

    Person = relationship('Person', primaryjoin='TempInvalidELNPeriod.chairman == Person.id')
    master = relationship('TempInvalidELN')


class TempInvalidImported(Base):
    __tablename__ = 'TempInvalid_Imported'

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('TempInvalid.id'), nullable=False)
    firstName = Column(String(30))
    lastName = Column(String(30))
    patrName = Column(String(30))
    lpuName = Column(Text)
    lpuAddress = Column(Text)
    lpuOgrn = Column(INTEGER(14))
    birthday = Column(Date)
    chairmanRole = Column(String(30))
    chairman = Column(String(30))
    SERV1_AGE = Column(INTEGER(5))
    SERV1_MM = Column(INTEGER(5))
    SERV1_RELATION_CODE = Column(String(5))
    SERV2_AGE = Column(INTEGER(5))
    SERV2_MM = Column(INTEGER(5))
    SERV2_RELATION_CODE = Column(String(5))
    firstRelation = Column(String(60))
    secondRelation = Column(String(60))

    master = relationship('TempInvalid')


class TempInvalidPeriod(Base):
    __tablename__ = 'TempInvalid_Period'
    __table_args__ = {'comment': 'Период листка временной нетрудоспособности'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('TempInvalid.id', ondelete='CASCADE'), nullable=False)
    diagnosis_id = Column(ForeignKey('Diagnosis.id'))
    begPerson_id = Column(ForeignKey('Person.id'))
    begDate = Column(Date, nullable=False)
    endPerson_id = Column(ForeignKey('Person.id'))
    endDate = Column(Date, nullable=False)
    isExternal = Column(TINYINT(1), nullable=False)
    regime_id = Column(ForeignKey('rbTempInvalidRegime.id'))
    break_id = Column(ForeignKey('rbTempInvalidBreak.id'))
    result_id = Column(ForeignKey('rbTempInvalidResult.id'))
    note = Column(String(256), nullable=False)
    numberPermit = Column(String(64))
    begDatePermit = Column(Date)
    endDatePermit = Column(Date)
    disability_id = Column(ForeignKey('rbTempInvalidRegime.id'))
    directDateOnKAK = Column(Date)
    expert_id = Column(ForeignKey('Person.id'))
    dateKAK = Column(Date)
    begDateHospital = Column(Date)
    endDateHospital = Column(Date)
    breakDate = Column(Date)
    anotherDoc = Column(String(128))
    anotherVk = Column(String(128))
    resultDate = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))

    begPerson = relationship('Person', primaryjoin='TempInvalidPeriod.begPerson_id == Person.id')
    _break = relationship('RbTempInvalidBreak')
    diagnosis = relationship('Diagnosi')
    disability = relationship('RbTempInvalidRegime', primaryjoin='TempInvalidPeriod.disability_id == RbTempInvalidRegime.id')
    endPerson = relationship('Person', primaryjoin='TempInvalidPeriod.endPerson_id == Person.id')
    expert = relationship('Person', primaryjoin='TempInvalidPeriod.expert_id == Person.id')
    master = relationship('TempInvalid')
    regime = relationship('RbTempInvalidRegime', primaryjoin='TempInvalidPeriod.regime_id == RbTempInvalidRegime.id')
    result = relationship('RbTempInvalidResult')


t_rbDiagnosticResult_rbResult = Table(
    'rbDiagnosticResult_rbResult', metadata,
    Column('diagnosticResult_id', ForeignKey('rbDiagnosticResult.id')),
    Column('result_id', ForeignKey('rbResult.id')),
    comment='Допустимые {rbResult} для {rbDiagnosticResult} (i3552)'
)


class RbSocStatusClassTypeAssoc(Base):
    __tablename__ = 'rbSocStatusClassTypeAssoc'
    __table_args__ = {'comment': 'Ассоциация классов и типов соц.статуса'}

    id = Column(INTEGER(11), primary_key=True)
    class_id = Column(ForeignKey('rbSocStatusClass.id', ondelete='CASCADE'), nullable=False)
    type_id = Column(ForeignKey('rbSocStatusType.id', ondelete='CASCADE'), nullable=False)
    isDefault = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    _class = relationship('RbSocStatusClas')
    type = relationship('RbSocStatusType')


class ActionProperty(Base):
    __tablename__ = 'ActionProperty'
    __table_args__ = {'comment': 'Описание свойства действия'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    action_id = Column(ForeignKey('Action.id', ondelete='CASCADE'), nullable=False)
    type_id = Column(ForeignKey('ActionPropertyType.id', ondelete='CASCADE'), nullable=False)
    unit_id = Column(ForeignKey('rbUnit.id'))
    norm = Column(String(64), nullable=False)
    isAssigned = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    evaluation = Column(TINYINT(1))
    isAutoFillCancelled = Column(TINYINT(1), server_default=alchemy_text("0"))

    action = relationship('Action')
    createPerson = relationship('Person', primaryjoin='ActionProperty.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ActionProperty.modifyPerson_id == Person.id')
    type = relationship('ActionPropertyType')
    unit = relationship('RbUnit')


class ActionAssistant(Base):
    __tablename__ = 'Action_Assistant'
    __table_args__ = {'comment': 'Ассистенты действия'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    action_id = Column(ForeignKey('Action.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    assistantType_id = Column(ForeignKey('rbActionAssistantType.id'), nullable=False)
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'))
    freeInput = Column(String(128), nullable=False)

    action = relationship('Action')
    assistantType = relationship('RbActionAssistantType')
    createPerson = relationship('Person', primaryjoin='ActionAssistant.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='ActionAssistant.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='ActionAssistant.person_id == Person.id')


class ActionExecutionPlan(Base):
    __tablename__ = 'Action_ExecutionPlan'
    __table_args__ = {'comment': 'План выполнения назначения'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False)
    master_id = Column(ForeignKey('Action.id', ondelete='CASCADE'), nullable=False)
    execDate = Column(DateTime, nullable=False)

    master = relationship('Action')


class BlankActionsMoving(Base):
    __tablename__ = 'BlankActions_Moving'
    __table_args__ = {'comment': 'Случай ВУТ, инвалидности или ограничения жизнедеятельности'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    date = Column(Date, nullable=False)
    blankParty_id = Column(ForeignKey('BlankActions_Party.id'), nullable=False)
    numberFrom = Column(String(16), nullable=False)
    numberTo = Column(String(16), nullable=False)
    orgStructure_id = Column(ForeignKey('OrgStructure.id'))
    person_id = Column(ForeignKey('Person.id'))
    received = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    used = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))
    returnDate = Column(Date)
    returnAmount = Column(INTEGER(4), nullable=False, server_default=alchemy_text("0"))

    blankParty = relationship('BlankActionsParty')
    createPerson = relationship('Person', primaryjoin='BlankActionsMoving.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='BlankActionsMoving.modifyPerson_id == Person.id')
    orgStructure = relationship('OrgStructure')
    person = relationship('Person', primaryjoin='BlankActionsMoving.person_id == Person.id')


class CashBoxExportInfo(Base):
    __tablename__ = 'CashBoxExportInfo'

    id = Column(INTEGER(11), primary_key=True)
    summ = Column(DECIMAL(20, 2), server_default=alchemy_text("0.00"))
    total_paid = Column(DECIMAL(20, 2), server_default=alchemy_text("0.00"))
    payment_date = Column(DateTime)
    client_id = Column(ForeignKey('Client.id'))
    event_id = Column(ForeignKey('Event.id'))
    account_id = Column(ForeignKey('Account.id'))
    payment_type = Column(String(256))
    payment_method = Column(ForeignKey('rbPaymentMethod.id'))
    person_id = Column(String(255))
    isReturn = Column(INTEGER(11))

    account = relationship('Account')
    client = relationship('Client')
    event = relationship('Event')
    rbPaymentMethod = relationship('RbPaymentMethod')


class ContractCompositionExpense(Base):
    __tablename__ = 'Contract_CompositionExpense'
    __table_args__ = {'comment': 'Состав затрат'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('Contract_Tariff.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    rbTable_id = Column(ForeignKey('rbExpenseServiceItem.id', onupdate='CASCADE'), nullable=False)
    percent = Column(Float(asdecimal=True), nullable=False, server_default=alchemy_text("0"))

    master = relationship('ContractTariff')
    rbTable = relationship('RbExpenseServiceItem')


class DeferredQueue(Base):
    __tablename__ = 'DeferredQueue'
    __table_args__ = {'comment': 'Журнал отложенного спроса'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(String(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    client_id = Column(ForeignKey('Client.id'), nullable=False)
    orgStructure_id = Column(ForeignKey('OrgStructure.id'))
    speciality_id = Column(ForeignKey('rbSpeciality.id'), nullable=False)
    person_id = Column(INTEGER(11))
    maxDate = Column(DateTime)
    status_id = Column(ForeignKey('rbDeferredQueueStatus.id'), nullable=False)
    action_id = Column(ForeignKey('Action.id'))
    comment = Column(Text)
    contact = Column(String(128))
    netrica_Code = Column(String(128))

    action = relationship('Action')
    client = relationship('Client')
    orgStructure = relationship('OrgStructure')
    speciality = relationship('RbSpeciality')
    status = relationship('RbDeferredQueueStatu')


class DrugDestinationSchedule(Base):
    __tablename__ = 'DrugDestinationSchedule'
    __table_args__ = {'comment': 'График выполнения лекарственных назначений (Процедурный лист)'}

    id = Column(INTEGER(11), primary_key=True)
    takeDatetime = Column(DateTime, nullable=False)
    action_id = Column(ForeignKey('Action.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    takeDose = Column(Float(asdecimal=True), nullable=False)
    takeDuration = Column(String(255), nullable=False)
    status = Column(TINYINT(4), nullable=False)
    execPerson_id = Column(ForeignKey('Person.id'))
    note = Column(String(255), nullable=False)
    cancel_reason = Column(String(255), nullable=False, server_default=alchemy_text("''"))
    nomenclature_id = Column(ForeignKey('rbStockNomenclature.id', onupdate='CASCADE'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))

    action = relationship('Action')
    execPerson = relationship('Person')
    nomenclature = relationship('RbStockNomenclature')


class HomeCallQueue(Base):
    __tablename__ = 'HomeCallQueue'
    __table_args__ = {'comment': 'Журнал вызова врача на дом'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime)
    modifyDatetime = Column(DateTime)
    createPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    modifyPerson_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    status_id = Column(ForeignKey('rbHomeCallQueueStatus.id', ondelete='SET NULL', onupdate='CASCADE'))
    action_id = Column(ForeignKey('Action.id', ondelete='SET NULL', onupdate='CASCADE'))
    sentStatus = Column(TINYINT(4), server_default=alchemy_text("0"))
    client_id = Column(ForeignKey('Client.id', ondelete='SET NULL', onupdate='CASCADE'))
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    session_id = Column(String(36))
    slot_id = Column(String(36))
    slot_datetime = Column(DateTime)
    slot_duration = Column(TINYINT(4))
    phone_number = Column(String(20))
    address = Column(String(160))
    kladr_code = Column(String(18))
    idHomeCallRequest = Column(String(36))
    reason = Column(String(120))
    comment = Column(String(120))

    action = relationship('Action')
    client = relationship('Client')
    createPerson = relationship('Person', primaryjoin='HomeCallQueue.createPerson_id == Person.id')
    modifyPerson = relationship('Person', primaryjoin='HomeCallQueue.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='HomeCallQueue.person_id == Person.id')
    status = relationship('RbHomeCallQueueStatu')


class HomeRequest(Base):
    __tablename__ = 'HomeRequest'

    id = Column(INTEGER(11), primary_key=True)
    create_date = Column(Date)
    create_time = Column(Time)
    claim = Column(Text)
    client_id = Column(ForeignKey('Client.id', ondelete='CASCADE'), nullable=False)
    type_id = Column(ForeignKey('HomeRequestType.id'), nullable=False)
    action_id = Column(ForeignKey('Action.id'))
    reason_of_cancel = Column(Text)
    operator_id = Column(ForeignKey('Person.id'))
    org_structure_id = Column(ForeignKey('OrgStructure.id'))
    note = Column(Text, server_default=alchemy_text("''"))
    datetime_of_transfer_to_osmp = Column(DateTime)
    datetime_of_brigade_appointed = Column(DateTime)
    datetime_of_brigade_came = Column(DateTime)
    datetime_of_brigade_end = Column(DateTime)
    emergencyBrigade_id = Column(ForeignKey('EmergencyBrigade.id'))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE', onupdate='CASCADE'))
    emergencyCallReason_id = Column(ForeignKey('EmergencyCallReason.id', ondelete='CASCADE', onupdate='CASCADE'))
    front_door = Column(INTEGER(11))
    floor = Column(INTEGER(11))
    intercom = Column(String(30))
    person_id = Column(INTEGER(11))
    cardNumber = Column(INTEGER(11))
    whoCalls = Column(String(250))

    action = relationship('Action')
    client = relationship('Client')
    emergencyBrigade = relationship('EmergencyBrigade')
    emergencyCallReason = relationship('EmergencyCallReason')
    event = relationship('Event')
    operator = relationship('Person')
    org_structure = relationship('OrgStructure')
    type = relationship('HomeRequestType')


class JobTicket(Base):
    __tablename__ = 'Job_Ticket'
    __table_args__ = {'comment': 'Талон на выполнение работ'}

    id = Column(INTEGER(11), primary_key=True)
    master_id = Column(ForeignKey('Job.id', ondelete='CASCADE'), nullable=False)
    idx = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    datetime = Column(DateTime, nullable=False)
    resTimestamp = Column(TIMESTAMP)
    resConnectionId = Column(INTEGER(11))
    jobTicketType_id = Column(ForeignKey('rbJobTicketType.id'))
    status = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    begDateTime = Column(DateTime)
    endDateTime = Column(DateTime)
    label = Column(String(64), nullable=False, server_default=alchemy_text("''"))
    note = Column(String(128), nullable=False, server_default=alchemy_text("''"))
    eQueueTicket_id = Column(ForeignKey('EQueueTicket.id', ondelete='SET NULL', onupdate='CASCADE'))
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    quota_id = Column(ForeignKey('rbJobType_Quota.id', ondelete='SET NULL', onupdate='CASCADE'))

    eQueueTicket = relationship('EQueueTicket')
    jobTicketType = relationship('RbJobTicketType')
    master = relationship('Job')
    person = relationship('Person')
    quota = relationship('RbJobTypeQuota')


class Recommendation(Base):
    __tablename__ = 'Recommendation'
    __table_args__ = {'comment': 'Направления'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(INTEGER(11))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(INTEGER(11))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    person_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    actionType_id = Column(ForeignKey('ActionType.id'), nullable=False)
    amount = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    price = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    setDate = Column(Date, nullable=False)
    expireDate = Column(Date, nullable=False)
    execDate = Column(Date)
    setEvent_id = Column(ForeignKey('Event.id', ondelete='SET NULL', onupdate='CASCADE'))
    execAction_id = Column(ForeignKey('Action.id', ondelete='SET NULL', onupdate='CASCADE'))
    amount_left = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    person2_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))

    actionType = relationship('ActionType')
    execAction = relationship('Action')
    person2 = relationship('Person', primaryjoin='Recommendation.person2_id == Person.id')
    person = relationship('Person', primaryjoin='Recommendation.person_id == Person.id')
    setEvent = relationship('Event')


class Visit(Base):
    __tablename__ = 'Visit'
    __table_args__ = {'comment': 'Посещение ЛПУ в рамках события'}

    id = Column(INTEGER(11), primary_key=True)
    createDatetime = Column(DateTime, nullable=False)
    createPerson_id = Column(ForeignKey('Person.id'))
    modifyDatetime = Column(DateTime, nullable=False)
    modifyPerson_id = Column(ForeignKey('Person.id'))
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    event_id = Column(ForeignKey('Event.id', ondelete='CASCADE'), nullable=False)
    scene_id = Column(ForeignKey('rbScene.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    visitType_id = Column(ForeignKey('rbVisitType.id'), nullable=False)
    person_id = Column(ForeignKey('Person.id'), nullable=False)
    isPrimary = Column(TINYINT(1), nullable=False)
    finance_id = Column(ForeignKey('rbFinance.id'), nullable=False)
    service_id = Column(ForeignKey('rbService.id'))
    payStatus = Column(INTEGER(11), nullable=False)
    assistant_id = Column(ForeignKey('Person.id', ondelete='SET NULL', onupdate='CASCADE'))
    MKB = Column(String(8))
    diagnostic_id = Column(ForeignKey('Diagnostic.id', ondelete='CASCADE'))

    assistant = relationship('Person', primaryjoin='Visit.assistant_id == Person.id')
    createPerson = relationship('Person', primaryjoin='Visit.createPerson_id == Person.id')
    diagnostic = relationship('Diagnostic')
    event = relationship('Event')
    finance = relationship('RbFinance')
    modifyPerson = relationship('Person', primaryjoin='Visit.modifyPerson_id == Person.id')
    person = relationship('Person', primaryjoin='Visit.person_id == Person.id')
    scene = relationship('RbScene')
    service = relationship('RbService')
    visitType = relationship('RbVisitType')


class AccountItem(Base):
    __tablename__ = 'Account_Item'
    __table_args__ = {'comment': 'Реестр счета'}

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), nullable=False, server_default=alchemy_text("0"))
    sourceAccountItem_id = Column(ForeignKey('Account_Item.id', ondelete='CASCADE'))
    master_id = Column(ForeignKey('Account.id', ondelete='CASCADE'), nullable=False)
    RKEY = Column(String(50))
    serviceDate = Column(Date, server_default=alchemy_text("'0000-00-00'"))
    event_id = Column(ForeignKey('Event.id'))
    visit_id = Column(ForeignKey('Visit.id'))
    action_id = Column(ForeignKey('Action.id'))
    price = Column(DECIMAL(10, 2), nullable=False)
    unit_id = Column(ForeignKey('rbMedicalAidUnit.id'))
    amount = Column(DECIMAL(10, 2), nullable=False)
    uet = Column(DECIMAL(10, 2), nullable=False)
    sum = Column(DECIMAL(10, 2), nullable=False)
    date = Column(Date)
    number = Column(String(48), nullable=False)
    refuseType_id = Column(ForeignKey('rbPayRefuseType.id'))
    reexposeItem_id = Column(ForeignKey('Account_Item.id', ondelete='SET NULL'))
    note = Column(String(256), nullable=False)
    tariff_id = Column(ForeignKey('Contract_Tariff.id', ondelete='SET NULL'))
    service_id = Column(INTEGER(11))
    kslp_coefficient = Column(Float(asdecimal=True))
    eisCase = Column(String(50))
    eisServ = Column(String(50))

    action = relationship('Action')
    event = relationship('Event')
    master = relationship('Account')
    reexposeItem = relationship('AccountItem', remote_side=[id], primaryjoin='AccountItem.reexposeItem_id == AccountItem.id')
    refuseType = relationship('RbPayRefuseType')
    sourceAccountItem = relationship('AccountItem', remote_side=[id], primaryjoin='AccountItem.sourceAccountItem_id == AccountItem.id')
    tariff = relationship('ContractTariff')
    unit = relationship('RbMedicalAidUnit')
    visit = relationship('Visit')


class ActionPropertyAction(Base):
    __tablename__ = 'ActionProperty_Action'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('Action.id', ondelete='CASCADE', onupdate='CASCADE'))
    egiszId = Column(INTEGER(11))

    ActionProperty = relationship('ActionProperty')
    Action = relationship('Action')


class ActionPropertyArterialPressure(Base):
    __tablename__ = 'ActionProperty_ArterialPressure'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(String(32))

    ActionProperty = relationship('ActionProperty')


class ActionPropertyBlankNumber(Base):
    __tablename__ = 'ActionProperty_BlankNumber'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(String(32))

    ActionProperty = relationship('ActionProperty')


class ActionPropertyBlankSerial(Base):
    __tablename__ = 'ActionProperty_BlankSerial'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(String(32))

    ActionProperty = relationship('ActionProperty')


class ActionPropertyClientQuoting(Base):
    __tablename__ = 'ActionProperty_Client_Quoting'
    __table_args__ = {'comment': 'Значение свойства действия типа Квота'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('Client_Quoting.id', ondelete='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    Client_Quoting = relationship('ClientQuoting')


class ActionPropertyDate(Base):
    __tablename__ = 'ActionProperty_Date'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(Date)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyDateTime(Base):
    __tablename__ = 'ActionProperty_DateTime'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(DateTime)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyDouble(Base):
    __tablename__ = 'ActionProperty_Double'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(Float(asdecimal=True), nullable=False)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyFile(Base):
    __tablename__ = 'ActionProperty_File'
    __table_args__ = {'comment': 'Значение свойства действия типа "File"'}

    id = Column(INTEGER(11), primary_key=True)
    index = Column(INTEGER(11), nullable=False, server_default=alchemy_text("0"))
    actionProperty_id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    value = Column(LONGBLOB)
    name = Column(String(254))

    actionProperty = relationship('ActionProperty')


class ActionPropertyHospitalBed(Base):
    __tablename__ = 'ActionProperty_HospitalBed'
    __table_args__ = {'comment': 'Значение свойства действия типа "Койка"'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('OrgStructure_HospitalBed.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    OrgStructure_HospitalBed = relationship('OrgStructureHospitalBed')


class ActionPropertyImage(Base):
    __tablename__ = 'ActionProperty_Image'
    __table_args__ = {'comment': 'Значение свойства действия типа "Image"'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(MEDIUMBLOB)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyInteger(Base):
    __tablename__ = 'ActionProperty_Integer'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(INTEGER(11), nullable=False)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyJobTicket(Base):
    __tablename__ = 'ActionProperty_Job_Ticket'
    __table_args__ = {'comment': 'Значение свойства действия типа Задание на работу'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('Job_Ticket.id', ondelete='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    Job_Ticket = relationship('JobTicket')


class ActionPropertyOrgStructure(Base):
    __tablename__ = 'ActionProperty_OrgStructure'
    __table_args__ = {'comment': 'Значение свойства действия типа Подразделение'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('OrgStructure.id', ondelete='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    OrgStructure = relationship('OrgStructure')


class ActionPropertyOrganisation(Base):
    __tablename__ = 'ActionProperty_Organisation'
    __table_args__ = {'comment': 'Значение свойства действия типа "Организация"'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('Organisation.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    Organisation = relationship('Organisation')


class ActionPropertyPerson(Base):
    __tablename__ = 'ActionProperty_Person'
    __table_args__ = {'comment': 'Значение свойства действия типа "Персона"'}

    id = Column(ForeignKey('ActionProperty.id', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    Person = relationship('Person')


class ActionPropertyPill(Base):
    __tablename__ = 'ActionProperty_Pills'
    __table_args__ = {'comment': 'Значение свойства действия "Примененные медикоменты в процессе оказания мед. помощи"'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(INTEGER(11))
    form_id = Column(INTEGER(11))
    amount = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    note = Column(Text, nullable=False)
    date = Column(Date)
    delivery_route = Column(INTEGER(11))
    pills_form = Column(INTEGER(11))
    day_amount = Column(Float(asdecimal=True))
    day_form_id = Column(INTEGER(11))
    day_count = Column(INTEGER(11))
    recipe_number = Column(String(255))
    recipe_serial = Column(String(255))
    assigned = Column(TINYINT(1), server_default=alchemy_text("0"))
    one_time_form_id = Column(INTEGER(11))
    one_time_amount = Column(Float(asdecimal=True))
    pills_way = Column(INTEGER(11))
    reject_reason = Column(INTEGER(11))

    ActionProperty = relationship('ActionProperty')


class ActionPropertyPulse(Base):
    __tablename__ = 'ActionProperty_Pulse'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(String(32))

    ActionProperty = relationship('ActionProperty')


class ActionPropertyQuotaType(Base):
    __tablename__ = 'ActionProperty_QuotaType'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('QuotaType.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    QuotaType = relationship('QuotaType')


class ActionPropertyRL(Base):
    __tablename__ = 'ActionProperty_RLS'
    __table_args__ = {'comment': 'Значение свойства действия "Расширенный РЛС"'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(INTEGER(11))
    form_id = Column(INTEGER(11))
    amount = Column(Float(asdecimal=True), server_default=alchemy_text("0"))
    note = Column(Text, nullable=False)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyString(Base):
    __tablename__ = 'ActionProperty_String'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(Text, nullable=False)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyTemperature(Base):
    __tablename__ = 'ActionProperty_Temperature'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(String(32))

    ActionProperty = relationship('ActionProperty')


class ActionPropertyTime(Base):
    __tablename__ = 'ActionProperty_Time'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(Time, nullable=False)

    ActionProperty = relationship('ActionProperty')


class ActionPropertyRbDistrict(Base):
    __tablename__ = 'ActionProperty_rbDistrict'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('rbDistrict.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    rbDistrict = relationship('RbDistrict')


class ActionPropertyRbFinance(Base):
    __tablename__ = 'ActionProperty_rbFinance'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('rbFinance.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    rbFinance = relationship('RbFinance')


class ActionPropertyRbHospitalBedProfile(Base):
    __tablename__ = 'ActionProperty_rbHospitalBedProfile'
    __table_args__ = {'comment': 'Значение свойства действия типа "Профиль койки"'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('rbHospitalBedProfile.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    rbHospitalBedProfile = relationship('RbHospitalBedProfile')


class ActionPropertyRbReasonOfAbsence(Base):
    __tablename__ = 'ActionProperty_rbReasonOfAbsence'
    __table_args__ = {'comment': 'Значение свойства действия'}

    id = Column(ForeignKey('ActionProperty.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    index = Column(INTEGER(11), primary_key=True, nullable=False, server_default=alchemy_text("0"))
    value = Column(ForeignKey('rbReasonOfAbsence.id', ondelete='CASCADE', onupdate='CASCADE'))

    ActionProperty = relationship('ActionProperty')
    rbReasonOfAbsence = relationship('RbReasonOfAbsence')


class JobTicketSignedDocument(Base):
    __tablename__ = 'JobTicketSignedDocument'
    __table_args__ = {'comment': 'Подписанные документы для номерка на работу'}

    id = Column(INTEGER(11), primary_key=True)
    jobTicket_id = Column(ForeignKey('Job_Ticket.id', ondelete='CASCADE'), ForeignKey('Job_Ticket.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    template_id = Column(ForeignKey('rbPrintTemplate.id', ondelete='CASCADE', onupdate='CASCADE'), ForeignKey('rbPrintTemplate.id', ondelete='CASCADE'), nullable=False)
    person_id = Column(ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'), ForeignKey('Person.id', ondelete='CASCADE'), nullable=False)
    datetime = Column(DateTime, nullable=False, server_default=alchemy_text("current_timestamp()"))
    exchange_type = Column(TINYINT(4))
    status = Column(TINYINT(4), nullable=False, server_default=alchemy_text("0"))
    html_content = Column(Text)
    file_path = Column(String(1023))
    sign_path = Column(String(1023))
    org_sign_path = Column(String(1023))
    file_type = Column(TINYINT(1), server_default=alchemy_text("0"))
    action_id = Column(ForeignKey('Action.id', ondelete='CASCADE', onupdate='CASCADE'))

    action = relationship('Action')
    jobTicket = relationship('JobTicket', primaryjoin='JobTicketSignedDocument.jobTicket_id == JobTicket.id')
    person = relationship('Person', primaryjoin='JobTicketSignedDocument.person_id == Person.id')
    template = relationship('RbPrintTemplate', primaryjoin='JobTicketSignedDocument.template_id == RbPrintTemplate.id')


class AccountItemKSLP(Base):
    __tablename__ = 'Account_Item_KSLP'

    id = Column(INTEGER(11), primary_key=True)
    deleted = Column(TINYINT(1), server_default=alchemy_text("0"))
    account_item_id = Column(ForeignKey('Account_Item.id'))
    kslp_coeff = Column(Float(asdecimal=True))
    kslp_id = Column(ForeignKey('rbExtraKSLP.id'))

    account_item = relationship('AccountItem')
    kslp = relationship('RbExtraKSLP')


class AccountRefus(Base):
    __tablename__ = 'Account_Refuses'
    __table_args__ = {'comment': 'Отказы счетов'}

    id = Column(INTEGER(11), primary_key=True)
    account_id = Column(ForeignKey('Account.id'), nullable=False)
    account_item_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    event_id = Column(ForeignKey('Event.id'), nullable=False)
    refuseType_id = Column(ForeignKey('rbPayRefuseType.id'), nullable=False)
    refuse_date = Column(Date)

    account = relationship('Account')
    account_item = relationship('AccountItem')
    event = relationship('Event')
    refuseType = relationship('RbPayRefuseType')


class CashBoxItem(Base):
    __tablename__ = 'CashBoxItems'

    id = Column(INTEGER(11), primary_key=True)
    check_id = Column(INTEGER(11))
    account_item_id = Column(ForeignKey('Account_Item.id'))
    service_name = Column(String(256))
    person_id = Column(ForeignKey('Person.id'))
    execPerson_id = Column(INTEGER(11))
    setPerson_id = Column(INTEGER(11))

    account_item = relationship('AccountItem')
    person = relationship('Person')


class ExportFileC(Base):
    __tablename__ = 'ExportFileC'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `C` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    CID = Column(INTEGER(14))
    CODE_MO = Column(String(5))
    NS = Column(INTEGER(5))
    SN = Column(INTEGER(12))
    OID = Column(INTEGER(14))
    PROT = Column(String(2))
    D_PROT = Column(Date)
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')


class ExportFileD(Base):
    __tablename__ = 'ExportFileD'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `D` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    CODE_MO = Column(String(5))
    SNILS = Column(String(14))
    FIO = Column(String(30))
    IMA = Column(String(20))
    OTCH = Column(String(30))
    POL = Column(String(1))
    DATR = Column(Date)
    DATN = Column(Date)
    DATO = Column(Date)
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')


class ExportFileI(Base):
    __tablename__ = 'ExportFileI'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `I` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    IID = Column(INTEGER(14))
    CODE_MO = Column(String(5))
    NS = Column(INTEGER(5))
    SN = Column(INTEGER(12))
    UID = Column(INTEGER(14))
    DIAG_D = Column(Date)
    DIAG_TIP = Column(String(1))
    DIAG_CODE = Column(String(3))
    DIAG_RSLT = Column(String(3))
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')


class ExportFileN(Base):
    __tablename__ = 'ExportFileN'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `N` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    CODE_MO = Column(String(5))
    NS = Column(INTEGER(5))
    NAPR_N = Column(String(15))
    NAPR_MO = Column(String(5))
    NAPR_D = Column(Date)
    DOC_SS = Column(String(14))
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')


class ExportFileO(Base):
    __tablename__ = 'ExportFileO'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `O` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    OID = Column(INTEGER(14))
    CODE_MO = Column(String(5))
    NS = Column(INTEGER(5))
    SN = Column(INTEGER(12))
    UID = Column(INTEGER(14))
    DS1_T = Column(String(2))
    PR_CONS = Column(String(1))
    D_CONS = Column(Date)
    STAD = Column(String(3))
    ONK_T = Column(String(4))
    ONK_N = Column(String(4))
    ONK_M = Column(String(4))
    MTSTZ = Column(String(1))
    SOD = Column(DECIMAL(6, 2))
    LEK_PR = Column(String(40))
    DATE_INJ = Column(Date)
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')


class ExportFileP(Base):
    __tablename__ = 'ExportFileP'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `P` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    NS = Column(DECIMAL(5, 0))
    VS = Column(String(1))
    DATS = Column(Date)
    SN = Column(DECIMAL(12, 0))
    DATPS = Column(Date)
    CODE_MO = Column(String(5))
    PL_OGRN = Column(String(15))
    FIO = Column(String(30))
    IMA = Column(String(25))
    OTCH = Column(String(30))
    POL = Column(String(1))
    DATR = Column(Date)
    KAT = Column(String(1))
    SNILS = Column(String(14))
    OKATO_OMS = Column(String(5))
    SPV = Column(INTEGER(1))
    SPS = Column(String(10))
    SPN = Column(String(20))
    INV = Column(String(1))
    MSE = Column(String(1))
    Q_G = Column(String(10))
    NOVOR = Column(String(9))
    VNOV_D = Column(DECIMAL(10, 0))
    FAMP = Column(String(30))
    IMP = Column(String(20))
    OTP = Column(String(30))
    POLP = Column(String(1))
    DATRP = Column(Date)
    C_DOC = Column(DECIMAL(2, 0))
    S_DOC = Column(String(10))
    N_DOC = Column(String(15))
    NAPR_MO = Column(String(6))
    NAPR_N = Column(String(15))
    NAPR_D = Column(Date)
    NAPR_DP = Column(Date)
    TAL_N = Column(String(18))
    TAL_D = Column(Date)
    PR_D_N = Column(String(1))
    PR_DS_N = Column(String(1))
    DATN = Column(Date)
    DATO = Column(Date)
    ISHL = Column(String(3))
    ISHOB = Column(String(3))
    MP = Column(String(1))
    DOC_SS = Column(String(14))
    SPEC = Column(String(9))
    PROFIL = Column(String(3))
    MKBX = Column(String(6))
    MKBXS = Column(String(6))
    DS_ONK = Column(String(1))
    MKBX_PR = Column(String(1))
    VMP = Column(String(2))
    KSO = Column(String(2))
    P_CEL = Column(String(4))
    VB_P = Column(String(1))
    PV = Column(String(40))
    DVOZVRAT = Column(Date)
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')


class ExportFileR(Base):
    __tablename__ = 'ExportFileR'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `R` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    RID = Column(INTEGER(14))
    CODE_MO = Column(String(5))
    NS = Column(INTEGER(5))
    SN = Column(INTEGER(12))
    UID = Column(INTEGER(14))
    NAZR_D = Column(Date)
    NAPR_MO = Column(String(6))
    NAZR = Column(String(2))
    SPEC = Column(String(9))
    VID_OBS = Column(String(2))
    PROFIL = Column(String(3))
    KPK = Column(String(3))
    NAPR_USL = Column(String(15))
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')


class ExportFileU(Base):
    __tablename__ = 'ExportFileU'
    __table_args__ = {'comment': 'Таблица для файла выгрузки `U` (КК)'}

    id = Column(INTEGER(11), primary_key=True)
    accountItem_id = Column(ForeignKey('Account_Item.id'), nullable=False)
    UID = Column(INTEGER(14))
    CODE_MO = Column(String(5))
    NS = Column(DECIMAL(5, 0))
    SN = Column(DECIMAL(12, 0))
    ISTI = Column(String(10))
    P_PER = Column(String(1))
    KOTD = Column(String(4))
    KPK = Column(String(2))
    MKBX = Column(String(6))
    MKBXS = Column(String(6))
    MKBXS_PR = Column(String(1))
    PR_MS_N = Column(String(1))
    MKBXO = Column(String(6))
    VP = Column(String(3))
    KRIT = Column(String(9))
    KRIT2 = Column(String(9))
    KSLP = Column(String(40))
    KSLP_IT = Column(DECIMAL(4, 2))
    KUSL = Column(String(15))
    KOLU = Column(DECIMAL(3, 0))
    KD = Column(DECIMAL(3, 0))
    DATN = Column(Date)
    DATO = Column(Date)
    TARU = Column(DECIMAL(10, 2))
    SUMM = Column(DECIMAL(14, 2))
    IS_OUT = Column(DECIMAL(1, 0))
    OUT_MO = Column(String(5))
    DOC_SS = Column(String(14))
    SPEC = Column(String(9))
    PROFIL = Column(String(3))
    VMP = Column(String(2))
    COMMENT = Column(String(10))
    DS_ONK = Column(String(1))
    USL_TIP = Column(String(1))
    HIR_TIP = Column(String(2))
    LEK_TIPL = Column(String(2))
    LEK_TIPV = Column(String(2))
    LUCH_TIP = Column(String(2))
    RKEY = Column(String(50))

    accountItem = relationship('AccountItem')
