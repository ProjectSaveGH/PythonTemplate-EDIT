from lib.gui.login import open_login
from lib.gui.register import open_register
import sqlite3

def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', ('laura', 'laura'))
    
    conn.commit()
    conn.close()

create_database()

open_register(
    "My App", 
    "300x300", 
    "users.db", 
    #bg_image="/home/Alexander/Downloads/bg.webp"
    )

open_login(
    "My App", 
    "300x300", 
    "users.db", 
    #bg_image="/home/Alexander/Downloads/bg.webp"
    )