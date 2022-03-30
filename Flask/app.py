from flask import Flask, render_template, request, url_for, flash, redirect
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

@app.Route('/main/<id>')
def main():
    return render_template('')

@app.Route("/login/<error> = ''")
def loginPath(error = ''):
    return render_template('login.html',error = error)

@app.Route("/login",methods=['POST', 'GET'])
def loginFunc():

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
        upswrd = request.args.get('pw')
        for i in users:
            if i[3] == usr and i[4] == upswrd:
                print(i[3],i[4])
                return redirect(url_for('main'),id = i[0])
            return redirect(url_for('login'),error = 'Incorrect username or password')
        
@app.Route('/register/<error> = ''')
def register(error):
    return render_template('RegistrationPage.html',error = error)
@app.Route('/register')
def register():

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


    if request.method == 'POST':
        eml = request.form['eml']
        nme = request.form['nme']
        usr = request.form['nm']
        upswrd = request.form['pw']
        for i in users:
            if i[3] == usr and i[4] == upswrd:
                print(i[3],i[4])
                return redirect(url_for('register'),error = 'User already Exists')

        conn = connect()
        cur = conn.cursor()
        cur.execute(f'INSERT INTO str_usrs () (name,email,usernm,password) VALUES ("{nme}","{eml}."{usr}","{upswrd}") ')
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('main'),id = i[0])
        

    else:
        eml = request.args.get('eml')
        nme = request.args.get('nme')
        usr = request.args.get('nm')
        upswrd = request.args.get('pw')
        for i in users:
            if i[3] == usr and i[4] == upswrd:
                print(i[3],i[4])
                return redirect(url_for('register'),error = 'User Already Exists')
        conn = connect()
        cur = conn.cursor()
        cur.execute(f'INSERT INTO str_usrs () (name,email,usernm,password) VALUES ("{nme}","{eml}."{usr}","{upswrd}") ')
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('main'),id = i[0])
