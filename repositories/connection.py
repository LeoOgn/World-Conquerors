import pymysql, os
from dotenv import load_dotenv


load_dotenv(override=True)
connection = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME"),
    cursorclass=pymysql.cursors.DictCursor
)