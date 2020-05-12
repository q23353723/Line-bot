import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a chihuahua-line-bot').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()

SQL_order = '''CREATE TABLE vocabulary(
   keyword TEXT NOT NULL,
   response TEXT NOT NULL
);'''
#cursor.execute(SQL_order)


#cursor.execute("SELECT keyword, response FROM vocabulary")
#cursor.execute("SELECT keyword, response FROM information_schema.columns WHERE table_name = 'vocabulary'")
#cursor.execute("INSERT INTO vocabulary (keyword, response) VALUES ('卑鄙', '卑鄙源之助')")

data = []
'''while True:
    temp = cursor.fetchone()
    if temp:
         data.append(temp)
    else:
        break
'''
#data.append(cursor.fetchall())
#print(data[0][0][0])

postgres_select_query = f"""SELECT * FROM vocabulary;"""
    
cursor.execute(postgres_select_query)
raw = cursor.fetchmany(int(2))
message = []

for i in raw:
    message.append((i[0], i[1]))
    
for i in message:
    print(i[0])

conn.commit()

cursor.close()
conn.close()