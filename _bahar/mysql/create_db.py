import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

sql = "CREATE DATABASE IF NOT EXISTS deneme"
mycursor.execute(sql)
