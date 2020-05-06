import logging


class Log(object):
    def __init__(self, debug=False,
                 info=False, warning=False,
                 error=False, critical=False, message=None):
        if not debug and \
                info and \
                warning and \
                error and \
                critical and message is None:
            logging.basicConfig(level=logging.INFO)
            # logging.info("Hypotenuse of {a}, {b} is {c}".format(a=3, b=4, c=hypotenuse(a, b)))
            logging.info("not specify type of log")

        if debug and message is not None:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug(message)
        elif info and message is not None:
            logging.basicConfig(level=logging.INFO)
            logging.info(message)
        elif warning and message is not None:
            logging.basicConfig(level=logging.WARNING)
            logging.warning(message)
        elif error and message is not None:
            logging.basicConfig(level=logging.ERROR)
            logging.error(message)
        elif critical and message is not None:
            logging.basicConfig(level=logging.CRITICAL)
            logging.critical(message)


def logger(message, debug=False,
           info=False, warning=False,
           error=False, critical=False):
    return Log(message, debug=False,
           info=False, warning=False,
           error=False, critical=False)
