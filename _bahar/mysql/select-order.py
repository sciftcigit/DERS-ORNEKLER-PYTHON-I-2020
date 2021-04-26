import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers ORDER BY name DESC")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

