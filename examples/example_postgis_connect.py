import psycopg2
import psycopg2.extras
import geocoder
import logging
import time

conn = psycopg2.connect("host=kingston.cbn8rngmikzu.us-west-2.rds.amazonaws.com port=5432 dbname=mydb user=addxy password=Denis44C")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

sql_search = """
SELECT * FROM geocoder
LIMIT 1"""

cur.execute(sql_search)
print cur.fetchone()