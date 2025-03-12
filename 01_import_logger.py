import logging
from logging.config import dictConfig

from logger import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
log = logging.getLogger(__name__)


def another_function(message: str):
    log.debug("Another DEBUG %s", message)
    log.info("Another INFO %s", message)
    log.warning("Another WARNING %s", message)


def main():
    log.debug("It's DEBUG message")
    log.info("It's INFO message")
    log.warning("It's WARNING message")
    another_function("message")


if __name__ == "__main__":
    log.debug("Start")
    main()
    log.debug("Finish")
