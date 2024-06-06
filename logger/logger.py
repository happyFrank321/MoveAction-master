import logging
from logging.handlers import RotatingFileHandler
from logging import Logger as DefaultLogger
from urllib.error import HTTPError
from sqlalchemy.exc import OperationalError
from suds import WebFault
from suds.transport import TransportError

try:
    from config import logFileName, VERBOSE_LOG
except ImportError:
    try:
        from config_example import logFileName, VERBOSE_LOG
    except ImportError:
        logFileName = 'var/log/pyEgisz/log.log'
        VERBOSE_LOG = False


class Logger:
    _logger: DefaultLogger

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger') or cls._logger is None:
            # # Отключаем логгер sqlalchemy
            # sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
            # sqlalchemy_logger.root.manager.disable = logging.CRITICAL

            cls._logger = logging.getLogger(__name__)
            cls._logger.propagate = False

            formatter = logging.Formatter('%(levelname)s %(asctime)s %(funcName)s %(message)s')

            file_handler = RotatingFileHandler(
                logFileName,
                mode='a',
                # 10 Мегабайт
                maxBytes=1000 * 1000 * 10,
                encoding='utf8',
                backupCount=1
            )
            file_handler.setFormatter(formatter)
            cls._logger.addHandler(file_handler)

            cls._logger.setLevel(logging.DEBUG if VERBOSE_LOG else logging.INFO)

        return cls._logger


def methods_handler(logger):
    def wrap(method):
        def wrapper(*args, **kwargs):
            try:
                logger.info(f'Начало работы метода {method.__name__} {f"с параметрами: {kwargs}" if kwargs else ""}')
                result = method(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f'Ошибка в методе {method.__name__}')
                # Ошибка в модуле suds (при отправке soap-запроса)
                if isinstance(e, WebFault):
                    if hasattr(e.fault, 'detail'):
                        logger.error(f'Описание ошибки: {e.fault.detail}')
                    else:
                        logger.error(f'Описание ошибки: {e.fault}')
                # Ошибка при подключении к сервису
                elif isinstance(e, HTTPError | TransportError):
                    logger.error(f'Проблемы с подключением и/или неверно указан token в config.py')
                # Ошибка при выполнении запроса sqlalchemy
                elif isinstance(e, OperationalError):
                    logger.error(f'Описание ошибки: {e.args[0]}')
                    logger.error(f'Запрос: {e.statement}')
                # Другой тип ошибки
                else:
                    logger.error(f'Ошибка: {e}')
            finally:
                logger.info(f'Конец работы метода {method.__name__}\n')

        return wrapper

    return wrap
