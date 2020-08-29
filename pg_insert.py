import psycopg2
conn = psycopg2.connect( dbname='postgres', user='postgres', password='postgres')
cur = conn.cursor()

query = "insert into employee (empid, name, dob, gender) values (%s, %s, %s, %s)"
data = (1004, 'Amal', '30-06-1980', 'M')

cur.execute(query, data)
if cur.rowcount > 0:
    print("Insertion Success!")

conn.commit()
cur.close()
conn.close()