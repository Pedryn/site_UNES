from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'Faculdade'


@app.route("/")
def home():
    titulo = "Home"
    return render_template ("home.html", title = titulo)

@app.route("/home")
def home2():
    titulo = "Home"
    return render_template ("home.html", title = titulo)

@app.route("/quemsomos")
def quemsomos():
    titulo = "Quem Somos"
    return render_template ("quemsomos.html", title = titulo)

@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method =='POST':
        email = request.form['email']
        assunto = request.form['email']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)",(email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'sucesso'
    return render_template("contato.html")

#@app.route("/contato")
#def contato():
#    titulo = "Contato"
#    return render_template ("contato.html", title = titulo)

# rota usuários para listar todos os usuários no banco de dados

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contato")
     if users > 0:
        userDetails = cur.fetchall()

        return_template("user.html", userDetails=userDetails)

#testa ve se é aqui mesmo ou em cima do comentado acima

if __name__ == '__main__':
    app.run()