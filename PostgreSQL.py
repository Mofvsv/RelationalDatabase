import sqlite3

pg = psycopg2.connect("dbname=bears")

cursor = pg.cursor()

cursor.execute("select host_key from cookies limit 10")
pg.commit()
results = cursor.fetchall()

print results

conn.close()