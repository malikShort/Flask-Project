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
tempusers = cur.fetchall()

print(tempusers)
users = []
for i in tempusers:
    users.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
print(users)
conn.close()
cur.close()

@app.Route("/login/<error> = ''")
def loginPath(error = ''):
    return render_template('login.html',error = error)

@app.Route("/login",methods=['POST', 'GET'])
def loginFunc():
    if request.method == 'POST':
        usr = request.form['nm']
        upswrd = request.form['pw']
        for i in users:
            if i[3] == usr and i[4] == upswrd:
                print(i[3],i[4])
                return redirect(url_for('main'),id = i[0])
            return redirect(url_for('login'),error = 'Incorrect username or password')

    else:
        usr = request.args.get('nm')
        uspswrd = request.args.get('pw')
        for i in users:
            if i[3] == usr and i[4] == upswrd:
                print(i[3],i[4])
                return redirect(url_for('main'),id = i[0])
            return redirect(url_for('login'),error = 'Incorrect username or password')
        
    
