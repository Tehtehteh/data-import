import logging


def setup_logging(debug: bool = False):
    log_level = logging.INFO
    if debug:
        log_level = logging.DEBUG
    logging.basicConfig(format='[%(asctime)s] [ %(filename)8s:%(lineno)4d] %(levelname)8s: %(message)s')
    logging.getLogger().setLevel(log_level)
