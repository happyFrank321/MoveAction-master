from database.database import Database

# Интервал отправки данных о направлениях
interval = 120

URLS_KK = {
    # Настройки сервиса "Терминология" для работы со справочниками
    'termUrl': 'http://10.0.1.179/nsi/fhir/term/',
    # Адрес сервиса ЗПВ (Запись на прием к врачу)
    'url_ZPV': 'http://10.0.1.179/Hub25/HubService.svc?wsdl',
    'url_ZPV_v2': 'http://10.0.1.81/Hub25/HubService.svc?wsdl',
    # Токен авторизации ЗПВ
    'token_ZPV': '09D4AB57-EBB9-4202-BBA4-1DAF27E0A084',
    # Адрес сервиса УО (Управление очередями)
    'url_UO': 'http://10.0.1.179/MQService/MqService.svc?wsdl',
    # Токен авторизации УО
    'token_UO': '74e23bac-ad30-4d52-a917-1182a78a7723'
}

URLS_SPB = {
    # Настройки сервиса "Терминология" для работы со справочниками
    'termUrl': 'http://10.128.66.207:2226/nsi/fhir/term/',
    # Адрес сервиса ЗПВ (Запись на прием к врачу)
    'url_ZPV': 'http://10.128.66.207:2226/Hub25/HubService.svc?wsdl',
    # Токен авторизации ЗПВ
    'token_ZPV': '624CB462-AD1C-4EE2-AC99-0117AA5C84CD',
    # Адрес сервиса УО (Управление очередями)
    'url_UO': 'http://regiz.gorzdrav.spb.ru/queues/MqService.svc?wsdl',
    # Токен авторизации УО
    'token_UO': 'ae315ebc-99e5-42bd-adda-1d8fe11d863f'
}

LPU_CONFIGS = {
    "dkkb": {
        "DB": {
            'host': 'dkkb',
            'port': 33006,
            'user': 'your user',
            'password': 'your password',
            'database': 's11',
        },
        "CREDENTIALS": {
            "org_ZPV": "459",
            "orgList": ['459', '463'],
            "org_UO": "693d1f74-a15c-472d-bf03-ec5c266494ed",
            "logger_db_name": 'logger'
        }
    },
    "p51vms": {
        "DB": {
            'host': 'p51vms',
            'port': 3306,
            'user': 'dbuser',
            'password': 'dbpassword',
            'database': 's11',
        },
        "CREDENTIALS": {
            "org_ZPV": "115",
            "orgList": ['115', '114', '113'],
            "org_UO": "93d8887c-a9ec-4d25-ad39-8644de1181b0",
            "logger_db_name": 'logger'
        }
    },
    "sochiOD2": {
        "DB": {
            'host': '192.168.1.3',
            'port': 2535,
            'user': 'dbuser',
            'password': 'dbpassword',
            'database': 's11vm',
        },
        "CREDENTIALS": {
            "org_ZPV": "316",
            "orgList": ['316'],
            "org_UO": "bf1c2c86-78be-4f00-ac58-dd07d0501db2",
            "logger_db_name": 'logger'
        }
    },
    "p104": {
        "DB": {
            'host': 'p104',
            'port': 3306,
            'user': 'dbuser',
            'password': 'dbpassword',
            'database': 's11',
        },
        "CREDENTIALS": {
            "org_ZPV": "193",
            "orgList": ['193', '194'],
            "org_UO": "27847e99-a94d-64f1-950d-0b961fe52afb",
            "logger_db_name": 'logger'
        }
    },
    "ptd23": {
        "DB": {
            'host': '192.168.1.3',
            'port': 4901,
            'user': 'dbuser',
            'password': 'dbpassword',
            'database': 'ptd23_main',
        },
        "CREDENTIALS": {
            "org_ZPV": "3205",
            "orgList": ['3205', '3206'],
            "org_UO": "bad20334-8baf-4a58-834a-e79e8eae2835",
            "logger_db_name": 'logger23'
        }
    },
    "armagb": {
        "DB": {
            'host': '192.168.1.3',
            'port': 2064,
            'user': 'vm_pyEgisz',
            'password': 'vm_pyEgisz',
            'database': 's11vm',
        },
        "CREDENTIALS": {
            "org_ZPV": "368",
            "orgList": ['368', '323', '370', '369', '1683', '2962', '2963', '2964', '2965', '3218', '3155'],
            "org_UO": "d478105d-cc71-4c45-be1c-e70e2e12ab71",
            "logger_db_name": 'logger'
        }
    },
    "kavptd4": {
        "DB": {
            'host': 'kavptd4',
            'port': 33306,
            'user': 'dbuser',
            'password': 'dbpassword',
            'database': 's11',
        },
        "CREDENTIALS": {
            "org_ZPV": "3213",
            "orgList": ['3213', '3214'],
            "org_UO": "85421fac-540b-41dc-9962-b12ae1e59efb",
            "logger_db_name": 'logger'
        }
    }
}


def select_lpu_region(lpu: str, region: str):
    """
    :region: KK or SPB
    :lpu: see LPU_CONFIGS
    """

    if region == "SPB":
        urls = URLS_SPB
    else:
        urls = URLS_KK

    lpu_config = LPU_CONFIGS.get(lpu)

    return urls, lpu_config


# ------------------ПРИМЕР ДЛЯ 51-ой------------------
URLS, LPU_CONFIG = select_lpu_region("kavptd4", "KK")
# ------------------ПРИМЕР ДЛЯ 51-ой------------------


termUrl = URLS.get('termUrl')

url_ZPV = URLS.get('url_ZPV')
token_ZPV = URLS.get('token_ZPV')

url_UO = URLS.get('url_UO')
token_UO = URLS.get('token_UO')

# Настройки авторизации в сервисе ЗПВ
org_ZPV = LPU_CONFIG.get("CREDENTIALS").get("org_ZPV")

# Настройки авторизации в сервисе УО
org_UO = LPU_CONFIG.get("CREDENTIALS").get("org_UO")

# Коды точек по которым получать данные
orgList = LPU_CONFIG.get("CREDENTIALS").get("orgList")

DB_BASE_FIELDS = {
    'engine': 'mysql+mysqldb',
    'charset': 'utf8'
}

DB_CONFIG = {**LPU_CONFIG.get("DB"), **DB_BASE_FIELDS}

# =======================
# Настройки подключения к БД
# =======================

db = Database(DB_CONFIG)

LOGGER_CONFIG = {**LPU_CONFIG.get("DB"), **DB_BASE_FIELDS}

# Имя базы логгер
loggerDbName = LPU_CONFIG.get("CREDENTIALS").get("logger_db_name")
LOGGER_CONFIG['database'] = loggerDbName

db_logger = Database(LOGGER_CONFIG)

EGISZ_CONFIG = {**LPU_CONFIG.get("DB"), **DB_BASE_FIELDS}

# Имя базы ЕГИСЗ
egiszDbName = 'egisz'
EGISZ_CONFIG['database'] = egiszDbName

db_egisz = Database(EGISZ_CONFIG)

list_function = {
    'registerPaRequest': True,
    'cancelPARequest': False,
    'getNewPARequests': True,
    'searchMany': True,
    'ChangePlannedResource': True,
    'sendNotificationAboutAppointment': True,
    'sendNotificationAboutAppointmentStatus': True,
    'sendNotificationAboutAppointmentStatusV2': False,
    'HealthCareStart': True,
    'HealthCareEnd': True
}

# Глобальная настройка, включающая обновление информации о клиенте, полученной в методе searchOne:
#  1) Обновление информации о документах клиента (см. InReferralHelper._update_client_docs_info)
#  2) Обновление информации о контактах клиента (см. InReferralHelper._update_client_contact_info)
#  3) Обновление информации об адресах клиента (см. InReferralHelper._update_client_address)
update_client_info = {
    'update_client_docs_info': False,
    'update_client_contact_info': False,
    'update_client_address': False
}

DEVELOPMENT = False

if DEVELOPMENT:
    # Путь до лога на вашем ПК
    logFileName = 'log.log'
else:
    logFileName = 'var/log/pyEgisz/log.log'

VERBOSE_LOG = False
DISABLE_LOGGING = False

# Минуты для отправки записей p21
# minBefore = 30
# minAfter = 3
