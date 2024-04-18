import logging


def setup_logging(level):
    """
    Sets up logging level via command line

    :param level: Passed via command line
    """
    logging_level = logging.DEBUG
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="./dev/events.log", encoding="utf-8", level=logging_level)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
