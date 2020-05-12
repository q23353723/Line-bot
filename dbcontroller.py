import os
import psycopg2

def getConnect():
    conn = psycopg2.connect(database="d257c3vevk7b15",user="uvvzexnmjjixeq",password="f7fbeb5e4ec298b1bfa40c0b5020808ad6418ef2ac88b755c102e9a5611346ce",host="ec2-52-202-22-140.compute-1.amazonaws.com",port=5432)
    conn.autocommit = True
    return conn

postgres_select_query = f"""SELECT * FROM vocabulary;"""

conn = getConnect()
cursor = conn.cursor()
cursor.execute(postgres_select_query)
raw = cursor.fetchmany(int(99999))
message = []

for i in raw:
    message.append((i[0], i[1]))

def addVocabulary(k, r):
    conn = getConnect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vocabulary (keyword, response) VALUES(%s, %s)",[k, r])
    conn.close()

def searchVocabulary(k):
    conn = getConnect()
    cursor = conn.cursor()
    postgres_select_query = f"""SELECT * FROM vocabulary;"""
    for i in message:
        if (i[0] == k):
            conn.close()
            return i[1]
    conn.close()
    return "聽不懂"

def existVocabulary(k):
    conn = getConnect()
    cursor = conn.cursor()
    postgres_select_query = f"""SELECT * FROM vocabulary;"""
    for i in message:
        if (i[0] == k):
            conn.close()
            return True
    conn.close()
    return False
