import sqlite3

dataBase = sqlite3.connector.connect(
    host="localhost",
    user="root",
    password="1234",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE DOMINATOR")
print("Database created successfully")

#Linux
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

dataBase = sqlite3.connect('DOMINATOR.db')
cursorObject = dataBase.cursor()


cursorObject.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    is_root BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')


root_username = 'root'
root_password = '' 

hashed_password = hash_password(root_password)

try:
    cursorObject.execute('''
    INSERT INTO users (username, password, is_root) 
    VALUES (?, ?, ?)
    ''', (root_username, hashed_password, 1))

    dataBase.commit()
    print("Root user created successfully")

except sqlite3.IntegrityError:
    print("Root user already exists")

finally:
    dataBase.close()
