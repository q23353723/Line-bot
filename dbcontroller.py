import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a chihuahua-line-bot').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()

def addVocabulary(k, r):
    cursor.execute("INSERT INTO vocabulary (keyword, response) VALUES (k, r)")

def searchVocabulary(k):
    postgres_select_query = f"""SELECT * FROM vocabulary;"""
    for i in message:
        if (i[0] == k):
            return i[1]
    return False


conn.commit()

cursor.close()
conn.close()