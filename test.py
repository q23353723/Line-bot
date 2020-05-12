import os
import psycopg2
import psycopg2.extras

#DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a chihuahua-line-bot').read()[:-1]

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

conn = psycopg2.connect(database="d257c3vevk7b15",user="uvvzexnmjjixeq",password="f7fbeb5e4ec298b1bfa40c0b5020808ad6418ef2ac88b755c102e9a5611346ce",host="ec2-52-202-22-140.compute-1.amazonaws.com",port=5432)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

SQL_order = '''CREATE TABLE vocabulary(
   keyword TEXT NOT NULL,
   response TEXT NOT NULL
);'''
#cursor.execute(SQL_order)


#cursor.execute("SELECT keyword, response FROM vocabulary")
#cursor.execute("SELECT keyword, response FROM information_schema.columns WHERE table_name = 'vocabulary'")
#cursor.execute("INSERT INTO vocabulary (keyword, response) VALUES ('卑鄙', '卑鄙源之助')")
#key = "台北"
#res = "暴徒"
#cursor.execute("INSERT INTO vocabulary (keyword, response) VALUES(%s, %s)",[key, res])

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
#raw = cursor.fetchall()
message = []
#message.append(cursor.fetchall())
dataRow = cursor.fetchall()

if len(dataRow):
    print("\t\t".join(list(dataRow[0].keys())))
    for row in dataRow:
        print("\t\t".join(row))
"""
for i in raw:
    print(raw)
    message.append((i[0], i[1]))
    
for i in message:
    print(i[0])
"""
conn.commit()

cursor.close()
conn.close()