import mysql.connector
from pythonjsonlogger import jsonlogger
import logging
import os

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


def _connect_db():
    try:
        cnx = mysql.connector.connect(
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASS", "password"),
            host=os.environ.get("DB_HOST", "localhost"),
            database=os.environ.get("DB_NAME", "billmanager"),
        )
        logger.info("connect DB")
        return cnx
    except Exception as e:
        logger.error("failed to connect DB: %s", e)
        os.exit(1)


def _make_yyyymmdd(day, yyyymm):
    if int(day) >= 10:
        return '"' + yyyymm + day + '"'
    else:
        return '"' + yyyymm + "0" + day + '"'


def insert_auelect(data, yyyymm):
    cnx = _connect_db()
    cursor = cnx.cursor()
    add_data = (
        "INSERT IGNORE INTO elect_consumption"
        "(record_date, total_consumption, day_consumption, night_consumption) "
        "VALUES ({}, {}, {}, {})"
    )

    for d in data:
        sql = add_data.format(
            _make_yyyymmdd(d[0], yyyymm), int(float(d[1]) * 1000), 0, 0
        )
        cursor.execute(sql)

    cnx.commit()
    cursor.close()
    logger.info("insert commited")
    cnx.close()
