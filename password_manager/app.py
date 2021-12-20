from sqlite3.dbapi2 import connect
from pandas.core.frame import DataFrame
from werkzeug.security import check_password_hash, generate_password_hash
import os
import pandas as pd
import sqlite3
from cryptography.fernet import Fernet

def connect_db(cursor, conn):
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([site] TEXT PRIMARY KEY, [password] TEXT)
          ''')
    conn.commit()
    conn.close()
    
def get_db_cursor():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    return c, conn

def encrypt(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    passw = f.encrypt(password.encode())
    return passw



def insert_on_db():
    site = input('Enter site: ')
    password = input('Enter password: ')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    password = encrypt(password)
    c.execute("INSERT OR REPLACE INTO products VALUES (?, ?)", (site, password))
    a = c.execute("SELECT * FROM products")
    print(a)
    conn.commit()
    conn.close()


class PasswordManager():
    def __init__(self):
        self.cursor = get_db_cursor()
        connect_db(self.cursor[0], self.cursor[1])
        self.password = os.getenv('pass')
        self.password_check = input('Password: ')

    def options(self):
        option = input(
            'What do you want to do? \n 1 - Insert a new password \n 2 - Get an old password \n 3 - List all passwords \n')
        return option

    def check_password(self):
        return check_password_hash(generate_password_hash(self.password), self.password_check)
    
    def insert_password(self):
        insert_on_db()
        

p = PasswordManager()
if p.check_password():
    print('Password correct')
    p.insert_password()