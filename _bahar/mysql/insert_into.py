import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
degerler = ("Serdar ", "Aydın/Efeler")
mycursor.execute(sql, degerler)

mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")


