from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # chave secreta para sessão

# Usuários simulados — em produção troque isso por banco de dados
users = {
    "usuario@exemplo.com": "senha123",
    "brenolimac17@gmail.com": "123456"
}

@app.route('/')
def index():
    # Se usuário autenticado, mostra a página principal
    if 'user' in session:
        return render_template('index2.html', username=session['user'])
    # senão, redireciona pro login
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('index'))
    erro = None
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email in users and users[email] == senha:
            session['user'] = email
            return redirect(url_for('index'))
        else:
            erro = "E-mail ou senha incorretos"
    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)