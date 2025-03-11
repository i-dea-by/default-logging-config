import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d | %(levelname)-7s | %(module)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def main():
    log.debug("It's DEBUG message")
    log.info("It's INFO message")
    log.warning("It's WARNING message")


if __name__ == "__main__":
    log.debug("Start")
    main()
    log.debug("Finish")
