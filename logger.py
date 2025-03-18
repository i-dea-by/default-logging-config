import logging
from pathlib import Path


LOGS_DIR = Path(__file__).parent / "logs"
LOG_BACKUP_COUNT = 3  # кол-во бэкапов файла логов
LOG_MAXSIZE = 10 * 1024 * 1024  # макс. размер файла лога байт


class FuncNameFilter(logging.Filter):
    def filter(self, record):
        record.expandedFuncName = "%s:%s:%s" % (
            record.module,
            record.funcName,
            record.lineno,
        )
        return True


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "func_name_filter": {
            "()": FuncNameFilter,
        },
    },
    "formatters": {
        "detailed": {
            "format": "[%(asctime)s.%(msecs)03d] %(levelname)-7s %(expandedFuncName)-20s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "console": {
            "format": "[%(asctime)s.%(msecs)03d] %(levelname)-7s %(module)s:%(lineno)d - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "file": {
            "formatter": "detailed",
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGS_DIR / "project.log",
            "backupCount": 3,
            "mode": "a",
            "maxBytes": LOG_MAXSIZE,
            "encoding": "UTF-8",
            "filters": ["func_name_filter"],
        },
        "console": {
            "formatter": "console",
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "filters": ["func_name_filter"],
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        },
    },
}
