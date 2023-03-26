from pythonjsonlogger import jsonlogger
import logging
import sys
import os
import auelect

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler()
h.setLevel(logging.DEBUG)
json_fmt = jsonlogger.JsonFormatter(fmt='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s', json_ensure_ascii=False)
h.setFormatter(json_fmt)
logger.addHandler(h)

if __name__ == "__main__":
    logger.info("register start")
    args = sys.argv
    if len(args) == 0:
        logger.error("required command argument")
        os.exit(1)

    if args[1] == "auelect":
        auelect.auelect_main()
    else:
        logger.error("unknown command argument")
        os.exit(1)

    logger.info("register end")
