import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

con = sqlite3.connect("sistema.db")
cursor = con.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    data_nascimento TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS projeto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_do_projeto TEXT,
    data_inicio TEXT,
    data_fim TEXT,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
)
""")

con.commit()
con.close()

#função para verificar a existencia de usuarios antes do cadastro de projetos
def existe_usuario():
    con = sqlite3.connect("sistema.db")
    cursor = con.cursor()

    cursor.execute("SELECT COUNT(*) FROM usuario")
    total = cursor.fetchone()[0]

    con.close()

    return total > 0

#rota flask para homepage
@app.route("/")
def home():
    return render_template("index.html")


#rota flask para cadastro de ususarios
@app.route("/usuarios", methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        nome = request.form.get("nome")
        data = request.form.get("data_nascimento")
        telefone = request.form.get("telefone")
        termo = request.form.get("termo")

        if not termo:
            return "É necessario aceitar os termos de uso"

        con = sqlite3.connect("sistema.db")
        cursor = con.cursor()

        cursor.execute(
            "INSERT INTO usuario (nome, telefone, data_nascimento) VALUES (?, ?, ?)",
            (nome, data, telefone)
        )

        con.commit()
        con.close()

        return "Usuario cadastrado com sucesso"

    
    return render_template("cadastro_usuario.html")


#rota flask para cadastro de projeto
@app.route("/projetos", methods=["GET", "POST"])
def cadastro_projeto():

    if not existe_usuario():
        return "Para cadastrar um projeto, é necessário cadastrar um usuário primeiro."

    con = sqlite3.connect("sistema.db")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome FROM usuario")
    usuarios = cursor.fetchall()
    con.close()

    if request.method == "POST":
        nome = request.form.get("nome_do_projeto")
        data_inicial = request.form.get("data_inicio")
        data_final = request.form.get("data_final")
        usuario_id = request.form.get("usuario_id")

        if data_final <= data_inicial:
            return "A data final do projeto não pode ser menor que a data inicial"

        con = sqlite3.connect("sistema.db")
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO projeto (nome_do_projeto, data_inicio, data_fim, usuario_id) VALUES (?, ?, ?, ?)",
            (nome, data_inicial, data_final, usuario_id)
        )
        con.commit()
        con.close()

        return "Projeto cadastrado com sucesso"

    return render_template("cadastro_projeto.html", usuarios=usuarios)







if __name__ == "__main__":
    app.run(debug=True)

