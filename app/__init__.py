from flask import Flask, render_template, request
app = Flask(__name__) #instanciando a classe Flask

#endereço do site
@app.route('/') #abrir o que for definido aqui
@app.route('/index') #abrir o que for definido aqui ROTA ALTERNATIVA
def index(): #função que retorna mensagem
    #return "Hello World!"
    nome = "Jean Dias"
    dados = {"profissao": "SRE", "formacao": "GTI/Pós Data Science"}
    #return render_template('index.html')
    return render_template('index.html',nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar')
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return "usuario:{} e senha:{}".format(usuario, senha)



app.run()