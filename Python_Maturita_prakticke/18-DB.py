import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "Admin",
    password = "Admin123",
    database = "uzivatele"
)


cur = mydb.cursor()

# --- INSERT ---
cur.execute("INSERT INTO users (ID, jmeno, rok) VALUES (%s, %s, %s)", ("Null", "Jakub", "2015-09-15"))
mydb.commit()

# --- SELECT ---
cur.execute("SELECT ID, jmeno, rok FROM users")
print(cur.fetchall())

# --- UPDATE ---
cur.execute("UPDATE users SET jmeno = %s WHERE ID = %s", ("Petr", 1))
mydb.commit()

# --- DELETE ---
cur.execute("DELETE FROM users WHERE ID = %s", (1,))
mydb.commit()

