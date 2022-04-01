from flask import Flask, render_template, request, url_for, flash, redirect
import psycopg2

app = Flask(__name__)

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

@app.route('/main/<id>')
def main(id):
    return render_template('BicyclePage.html',id = id)

@app.route("/login")
def loginPath():
    return render_template('Login.html')

@app.route("/login/<error> = ''")
def loginErr(error = ''):
    return render_template('Login.html',error = error)

@app.route("/login",methods=['POST', 'GET'])
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
                global userID
                userID = i[0]
                return redirect(url_for('main',id = i[0]))
        return redirect(url_for('login',error = 'Incorrect username or password'))

    else:
        usr = request.args.get('nm')
        upswrd = request.args.get('pw')
        for i in users:
            if i[3] == usr and i[4] == upswrd:
                print(i[3],i[4])
                userID = i[0]
                return redirect(url_for('main',id = i[0]))
        return redirect(url_for('login',error = 'Incorrect username or password'))
        
@app.route('/register')
def register():
    return render_template('RegistrationPage.html')
@app.route('/register/<error>')

def registerErr(error):
    print(error)
    return render_template('RegistrationPage.html',error = error)
@app.route('/register',methods=['POST', 'GET'])
def registering():

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
        usr = request.form['unR']
        upswrd = request.form['pwR']
        for i in users:
            if i[3] == usr:
                print(i[3],i[4])
                return redirect(url_for('register',error = 'User already Exists'))

        conn = connect()
        cur = conn.cursor()
        #cur.execute(f'INSERT INTO str_usrs  (name,email,usernm,password) VALUES ("{nme}","{eml}","{usr}","{upswrd}") ')
        cur.execute('INSERT INTO str_usrs (name,email,usernm,password)'
            'VALUES(%s,%s,%s,%s)',
            (f"{nme}",f"{eml}",f"{usr}",f"{upswrd}"))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('login'))
        

    else:
        eml = request.args.get('eml')
        nme = request.args.get('nme')
        usr = request.args.get('unR')
        upswrd = request.args.get('pwR')
        for i in users:
            if i[3] == usr:
                print(i[3],i[4])
                return redirect(url_for('register',error = 'User Already Exists'))
        conn = connect()
        cur = conn.cursor()
        cur.execute(f'INSERT INTO str_usrs  (name,email,usernm,password) VALUES ("{nme}","{eml}","{usr}","{upswrd}") ')
        conn.commit()
        cur.execute(f'SELECT id FROM str_usrs WHERE name = {nme}')
        id = cur.fetchall()
        print(id)
        cur.close()
        conn.close()
        return redirect(url_for('login'))

@app.route('/bike1Code')
def bike1():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 1')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike2Code')
def bike2():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 2')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike3Code')
def bike3():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 3')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike4Code')
def bike4():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 4')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike5Code')
def bike5():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 5')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike6Code')
def bike6():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 6')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike7Code')
def bike7():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 7')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike8Code')
def bike8():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 8')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike9Code')
def bike9():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 9')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'

@app.route('/bike10Code')
def bike10():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM bikestock WHERE id = 10')
    bike = cur.fetchall()
    bike = bike[0]
    print(bike[1])
    cur.execute("""UPDATE str_usrs 
    SET bcylenmn = %s
    WHERE id = %s""",
    (bike[1],userID))
    print(bike[1],userID)
    cur.execute("UPDATE str_usrs SET bycleprc = %sWHERE id = %s ",
    (bike[2],userID))
    conn.commit()

    cur.execute('SELECT * FROM str_usrs')
    test = cur.fetchall()
    print(test)
    
    cur.close()
    conn.close()
    print(bike)
    print('success1')
    return 'nothing'