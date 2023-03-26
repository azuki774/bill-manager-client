from pythonjsonlogger import jsonlogger
import logging
import glob
from bs4 import BeautifulSoup
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, "JST")
now = datetime.datetime.now(JST)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler()
h.setLevel(logging.DEBUG)
json_fmt = jsonlogger.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s",
    json_ensure_ascii=False,
)
h.setFormatter(json_fmt)
logger.addHandler(h)


def _extract_html(f):
    html = open(f, "r")

    ret = []
    soup = BeautifulSoup(html, "html.parser")

    table = soup.findAll("table")[0]
    rows = table.findAll("tr")
    for row in rows:
        ts = row.findAll("td")
        if ts == []:
            continue
        day_text = ts[0].get_text()  # ex. "    11 (土)"
        consume_text = ts[1].get_text()  # ex. "8.50 kWh"
        price_text = ts[2].get_text()  # ex. "   111 円"
        day, consume, price = [
            day_text.split(" ")[-2],
            consume_text.split(" ")[0],
            price_text.split(" ")[-2],
        ]
        ret.append([day, consume, price])  # # ex. [11, 8.50, 111]

    logger.info("extract html data complete: %s", f)
    return ret


def _proc_file(file):
    logger.info("proc file: %s", file)
    _extract_html(file)

    yyyymm = now.strftime("%Y%m")
    return 0


def auelect_main():
    """
    auelect コマンドの main
    """

    logger.info("auelect start")

    files = glob.glob("/data/*")
    for f in files:
        _proc_file(f)

    logger.info("auelect end")
    return 0
