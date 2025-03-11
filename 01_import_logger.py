import logging
import logging.config

from logger import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger(__name__)


def main():
    log.debug("It's DEBUG message")
    log.info("It's INFO message")
    log.warning("It's WARNING message")


if __name__ == "__main__":
    log.debug("Start")
    main()
    log.debug("Finish")
