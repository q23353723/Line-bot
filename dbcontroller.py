import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a chihuahua-line-bot').read()[:-1]

conn = psycopg2.connect(database="d257c3vevk7b15",user="uvvzexnmjjixeq",password="f7fbeb5e4ec298b1bfa40c0b5020808ad6418ef2ac88b755c102e9a5611346ce",host="ec2-52-202-22-140.compute-1.amazonaws.com",port=5432)

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()

def addVocabulary(k, r):
    cursor.execute("INSERT INTO vocabulary (keyword, response) VALUES (k, r)")

def searchVocabulary(k):
    postgres_select_query = f"""SELECT * FROM vocabulary;"""
    for i in message:
        if (i[0] == k):
            return i[1]
    return "聽不懂"


conn.commit()

cursor.close()
conn.close()