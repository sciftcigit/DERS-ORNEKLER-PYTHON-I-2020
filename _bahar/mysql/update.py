import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()


sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Ankara-Ulus", "Apple st 652")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
