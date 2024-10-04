
from flask import Flask, render_template,url_for, g , request,session,redirect

from database import get_database , connect_to_database

from werkzeug.security import generate_password_hash, check_password_hash

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.teardown_appcontext
def close_database(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()

def get_current_user():
    user_result =None
    if 'user' in session:
        user = session['user']

        # fetch the particular user from the database
        db = get_database()
        user_cur = db.execute('select id,name,password,expert,admin from users where name = ?' ,[user])
        user_result = user_cur.fetchone()
    return user_result


@app.route('/')
def homepage():
    user = get_current_user()
    if 'user' in session:
        user = session['user']
    return render_template('home.html',user=user)

@app.route('/login', methods = ['POST','GET'])
def login():
    user = get_current_user()
    if request.method == "POST":

        db = get_database()
        name = request.form['name']
        password_user_entered = request.form['password']

        user_fetched_from_db = db.execute('select id,name,password from users where name = ? ', [name])
        user_fetched_result =user_fetched_from_db.fetchone()

        if check_password_hash(user_fetched_result['password'],password_user_entered):
            session['user'] = user_fetched_result['name']
            return redirect(url_for('homepage'))
        
        else:
            return '<h1> pwd is incorrect </h1>'

    return render_template('login.html',user = user)

@app.route('/register' , methods = ['POST','GET'])
def register():
    user = get_current_user()
    if request.method == 'POST':
        db = get_database()

        hashed_password = generate_password_hash(request.form['password'], method = 'pbkdf2:sha256')
        db.execute('insert into users(name,password,expert,admin) values(?,?,?,?)',[request.form['name'],hashed_password,'0','0'])
        db.commit()
        session['user'] = request.form['name']
        return redirect(url_for('homepage'))
    return render_template('register.html', user = user)


@app.route('/users')
def users():
    user = get_current_user()
    db = get_database()
    user_cur = db.execute('select id,name,expert from users')
    all_user_result = user_cur.fetchall() 
    return render_template('users.html',user=user, users = all_user_result)


@app.route('/promote/<user_id>')
def promote(user_id):
    # update code needs to be written
    db = get_database()
    db.execute("update users set expert = 1 where id = ?",[user_id])
    db.commit()
    return redirect(url_for('users'))
@app.route('/logout')
def logout():
    session.pop('user',None)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)