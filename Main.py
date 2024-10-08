from flask import Flask, redirect, render_template, request, url_for, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'

def DbConect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='16012008',
        database='estudodoflask'
    )

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/AddDados', methods=['post'])
def AddDados():

    return redirect(url_for('homepage'))


if __name__ in "__main__":
    app.run(debug=True)