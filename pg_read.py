import psycopg2
conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres')

cur = conn.cursor()

cur.execute("select * from employee")

for row in cur.fetchall():
    print(row[1])

cur.close()
conn.close()