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

    conexao = DbConect()
    cursor = conexao.cursor()
    comando = f'INSERT INTO usuarios(usuario, email, senha) VALUES ("{nome_usuario}","{email_usuario}","{senha_usuario}");'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    return redirect(url_for('homepage'))

@app.route('/LerDados')
def Read():
    conexao = DbConect()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios;')
    usuariosBD = cursor.fetchall()
    conexao.close()
    return render_template('Read.html', usuariosBD=usuariosBD)

@app.route('/EditarDados')
def Update():
    conexao = DbConect()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios;')
    usuariosBD = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('Update.html', usuariosBD=usuariosBD)

@app.route('/EditarNome')
def EditarNome():
    return render_template('editarn.html')


@app.route('/PegarDadosDoNovoNome', methods=['POST'])
def PegarDados():
    nomea = request.form.get('NomeAtual')
    nomen = request.form.get('NomeNovo')
    
    conexao = DbConect()
    cursor = conexao.cursor()
    comando = f'UPDATE usuarios SET usuario = "{nomen}" WHERE usuario = "{nomea}";'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    return render_template('editarn.html')


@app.route('/EditarEmail')
def EditarEmail():

    return render_template('editare.html')


@app.route('/PegarDadosNovoEmail', methods=['POST'])
def PegarDadosEmail():
    emaila = request.form.get('EmailAtual')
    emailn = request.form.get('EmailNovo')

    print(emaila)
    print(emailn)

    conexao = DbConect()
    cursor = conexao.cursor()
    comando = f'UPDATE usuarios SET email = "{emailn}" WHERE email = "{emaila}";'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    return render_template('editare.html')

@app.route('/Delete')
def deletar():
    return render_template('Delete.html')


@app.route('/PegarDadosDelete', methods=['POST'])
def PegarDadosDelete():
    usuario = request.form.get('UsuarioDeletar')
    print(usuario)

    conexao = DbConect()
    cursor = conexao.cursor()

    comando = f'DELETE FROM usuarios WHERE usuario = "{usuario}";'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    return render_template('Delete.html')


if __name__ in "__main__":
    app.run(debug=True)