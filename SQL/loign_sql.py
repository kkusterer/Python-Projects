from cs50 import SQL

db = SQL("sqlite:///data.db")

username = input("Username: ")
password = input("Password: ")

rows = db.execute("SELECT * FROM data_table WHERE username = ? AND password = ?", username, password)

if len(rows) == 1:
    print(f"Welcome, {rows[0]['name']}!")
else:
    print("Invalid username or password.")
