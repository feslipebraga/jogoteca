from flask import Flask, render_template, request

# Classe para organizar os dados de cada jogo
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# Criando instâncias da classe Jogo
jogo1 = Jogo('Super Mario', 'Aventura', 'Nintendo')
jogo2 = Jogo('Pacman', 'Arcade', 'Multiplataforma')
jogo3 = Jogo('Street Fighter', 'Luta', 'Multiplataforma')
jogo4 = Jogo('Fall Guys', 'Competitivo', 'Multiplataforma')

# Criando a lista com os objetos
jogos = [jogo1, jogo2, jogo3, jogo4]
    
# Instância da aplicação Flask
app = Flask(__name__)

# Definição da rota principal
@app.route('/inicio')
def inicio():
    # Renderiza o template HTML, passando o título e a lista de jogos
    return render_template('inicio.html', titulo='Jogoteca', jogos=jogos)

@app.route('/novo')
def novo():
    # Renderiza o template para adicionar um novo jogo
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    jogo = Jogo(nome, categoria, console) 
    jogos.append(jogo)
    return render_template('inicio.html', titulo='Jogoteca', jogos=jogos)

# Garante que a aplicação só rode se o script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)