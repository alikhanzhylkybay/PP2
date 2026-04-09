import psycopg2

conn = psycopg2.connect(
    dbname="suppliers",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())

cur.close()
conn.close()