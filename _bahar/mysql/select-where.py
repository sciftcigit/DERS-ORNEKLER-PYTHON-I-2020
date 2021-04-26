import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers WHERE name like 'S%' ")

myresult = mycursor.fetchall()


for x in myresult:
  print(x)

if mycursor.rowcount <1 :
    print("bu kriterde hic kayit yok")
