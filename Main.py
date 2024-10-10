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

@app.route('/AddDados', methods=['POST'])
def AddDados():
    nome_usuario = request.form.get('UsuarioUsu')
    email_usuario = request.form.get('EmailUsu')
    senha_usuario = request.form.get('SenhaUsu')

    print(nome_usuario)
    print(email_usuario)
    print(senha_usuario)

    conexao = DbConect()
    cursor = conexao.cursor()
    comando = f'INSERT INTO usuarios(usuario, email, senha) VALUES ("{nome_usuario}","{email_usuario}","{senha_usuario}");'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    return redirect(url_for('homepage'))


if __name__ in "__main__":
    app.run(debug=True)