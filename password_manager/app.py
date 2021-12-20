from sqlite3.dbapi2 import connect
from pandas.core.frame import DataFrame
from werkzeug.security import check_password_hash, generate_password_hash
import os
import pandas as pd
import sqlite3
from cryptography.fernet import Fernet


def load_key():
    return open("key.key", "rb").read()

f = Fernet(load_key())

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
    passw = f.encrypt(password.encode())
    return passw

def decrypt(password):
    passw = f.decrypt(password)
    return passw

def insert_on_db():
    site = input('Enter site: ')
    password = input('Enter password: ')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    password = encrypt(password)
    c.execute("INSERT OR REPLACE INTO products VALUES (?, ?)", (site, password))
    conn.commit()
    conn.close()


class PasswordManager():
    def __init__(self):
        self.cursor = get_db_cursor()
        connect_db(self.cursor[0], self.cursor[1])
        self.password = os.getenv('pass')
        self.password_check = input('Password: ')

    def display_all(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        passwords = c.fetchall()
        for password in passwords:
            print(password[0], ": ", decrypt(password[1]).decode())

    def options(self):
        option = input(
            'What do you want to do? \n 1 - Insert a new password \n 2 - Get an old password \n 3 - List all passwords \n 4 - Exit \n')
        return option

    def check_password(self):
        return check_password_hash(generate_password_hash(self.password), self.password_check)
    
    def insert_password(self):
        insert_on_db()
        print("Password inserted successfully\n")
        
    def get_password(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        site = input("From which site do you want to get the password? ")
        password = c.execute("SELECT * FROM products WHERE site = ?", (site,))
        return password.fetchone()[1]

    def display_password(self, encrpyted_password):
        password = decrypt(encrpyted_password).decode()
        print(password)

p = PasswordManager()
if p.check_password():
    print('Password correct')
    opt = p.options()
    if opt == '1':
        p.insert_password()
    elif opt == '2':
        password_encrypted = p.get_password()
        p.display_password(password_encrypted)
    
    elif opt == '3':
        p.display_all()

    elif opt == '4':
        exit()


