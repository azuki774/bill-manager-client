from pythonjsonlogger import jsonlogger
import logging
import glob

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler()
h.setLevel(logging.DEBUG)
json_fmt = jsonlogger.JsonFormatter(fmt='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s', json_ensure_ascii=False)
h.setFormatter(json_fmt)
logger.addHandler(h)

def auelect_main():
    logger.info("auelect start")

    files = glob.glob("/data/*")
    for f in files:
        print(f)

    logger.info("auelect end")
    return 0
