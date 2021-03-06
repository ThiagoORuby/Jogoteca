from flask import Flask, render_template, request, redirect, session, flash

#iniciando app em flask
app = Flask(__name__)
app.secret_key = 'pytorch'

class Jogo:

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console,

lista = [Jogo('Tetris', 'Puzzle','Arcade'), Jogo('God of War', 'Hack and Slash', 'PS2'), Jogo('Pokemon Ruby', 'Adventure', 'GameBoy Advance')]

@app.route('/')
def ola():
    print(lista[1].console)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')

def novo():
    return render_template('novo.html', titulo='Adicionar novo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome, categoria, console)
    lista.append(novo_jogo)
    return redirect('/')

#Rota de login
@app.route('/login')
def login():
    return render_template('login.html', titulo='Faça seu login')

#Rota de autenticação
@app.route('/autenticar', methods=['POST',])
def autenticar():
    senha = request.form['senha']
    if senha=='familhao':
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso')
        return redirect('/')
    else:
        flash('Usuario não logado')
        return redirect('/login')

#Recebe parametros host="0.0.0.0" e port=5000
app.run(debug=True)

