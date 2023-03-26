from pythonjsonlogger import jsonlogger
import logging
import glob
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler()
h.setLevel(logging.DEBUG)
json_fmt = jsonlogger.JsonFormatter(fmt='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s', json_ensure_ascii=False)
h.setFormatter(json_fmt)
logger.addHandler(h)

def _proc_file(f):
    logger.info("proc file {}".format(f))
    html = open(f, 'r')

    mat = []  # 保存先の行列
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.findAll("table")[0]
    rows = table.findAll("tr")
    for row in rows:
        ts = row.findAll("td")
        if ts == []:
            continue
        day_text = ts[0].get_text() # ex. "    11 (土)"
        consume_text = ts[1].get_text() # ex. "8.50 kWh"
        price_text = ts[2].get_text() # ex. "   111 円"
        day, consume, price = [day_text.split(' ')[-2], consume_text.split(' ')[0], price_text.split(' ')[-2]]
        print(day)
        print("---------------")
        print(consume)
        print("---------------")
        print(price)
        print("===============")
    return 0


def auelect_main():
    logger.info("auelect start")

    files = glob.glob("/data/*")
    for f in files:
        _proc_file(f)

    logger.info("auelect end")
    return 0
