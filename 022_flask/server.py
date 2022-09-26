from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'helloworld'
app.permanent_session_lifetime = timedelta(minutes=10)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:####@localhost/flask_tester'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))
    password = db.Column('password', db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        user_name = request.form["nm"]
        user_password = request.form["password"]
        user_in_db = Users.query.filter_by(name=user_name).first()
        if user_in_db:
            session['user_name'] = user_name
            session['email'] = user_in_db.email
            flash('Logged in')
            return redirect(url_for('user'))
        else:
            new_user = Users(user_name, '', user_password)
            db.session.add(new_user)
            db.session.commit()
            session['user_name'] = user_name
            session['user_password'] = user_password
            session['email'] = ''
            flash('Logged in')
            return redirect(url_for('user'))
    else:
        if 'user_name' in session:
            flash('Already logged in')
            return redirect(url_for('user'))
        else:
            return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    flash('Logged out')
    return redirect(url_for('login'))


@app.route('/user', methods=['POST', 'GET'])
def user():
    if "user_name" in session:
        user_name = session['user_name']
        if request.method == 'POST':
            email = request.form['em']
            session['email'] = email
            user_in_db = Users.query.filter_by(name=user_name).first()
            user_in_db.email = email
            db.session.commit()
            flash('Email saved')
        else:
            if 'email' in session:
                email = session['email']
            else:
                email = ''
        return render_template('user.html', user_name=user_name, email=email)
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
