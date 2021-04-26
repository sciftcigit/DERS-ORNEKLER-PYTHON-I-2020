import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
degerler  = ("Michelle", "Blue Village")

mycursor.execute(sql, degerler)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)


