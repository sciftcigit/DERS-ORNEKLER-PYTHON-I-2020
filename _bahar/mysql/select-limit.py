import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers Limit 5,5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

