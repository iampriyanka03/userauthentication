from flask import g
import sqlite3

def connect_to_database():
    sql = sqlite3.connect('C:/Users/deept/OneDrive/Desktop/userauthentication/userauth.db')
    sql.row_factory = sqlite3.Row

    return sql


def get_database():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_to_database()

    return g.sqlite_db
