import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"

)

mycursor = mydatabase.cursor()
mycursor.execute("SELECT * FROM uzivatele")

results = mycursor.fetchall()

for x in results:
    print(x)
    
mydatabase.commit()