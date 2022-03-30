from flask import *
import psycopg2

app = Flask(__name__)
from operator import itemgetter

print('connecting to database')

def connect():
    
    conn = psycopg2.connect(
            database = 'flask_db',
            user = 'postgres',
            password = 'gabe1972',
            host = 'localhost'
        )
    print('connected to database')
    return conn
conn = connect()
cur = conn.cursor()
cur.execute('SELECT * FROM str_usrs')
users = cur.fetchall()

print(users)