import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("IP_POSTGRE"),
    database=os.getenv("POSTGRE_DB"),
    user=os.getenv("POSTGRE_USER"),
    password=os.getenv("POSTGRE_PASSWORD"),
    port=5432
)

conn.autocommit = True
cur = conn.cursor()


def query(user_query):
    try:
        cur.execute(user_query)
    except psycopg2.Error as e:
        print("Database error:", e)
        conn.rollback()

def query_select(user_query):
    query(user_query)
    rows = cur.fetchall()
    return rows
    # return rows[0]

def print_db_resp(user_query):
    query(user_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)