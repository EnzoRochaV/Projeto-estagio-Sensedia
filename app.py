import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

con = sqlite3.connect("sistema.db")
cursor = con.cursor()

# tabela de usuario SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    data_nascimento TEXT,
    CONSTRAINT usuario_unico UNIQUE (nome, telefone, data_nascimento)
)
""")

# tabela de projeto SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS projeto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_projeto TEXT,
    data_inicio TEXT,
    data_fim TEXT,
    usuario_id INTEGER,
    CONSTRAINT projeto_unico UNIQUE (nome_projeto),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
)
""")

con.commit()
con.close()

#função para verificar se existe ususario
def existe_usuario():
    con = sqlite3.connect("sistema.db")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuario")
    total = cursor.fetchone()[0]
    con.close()
    return total > 0

# rota homepage
@app.route("/")
def home():
    con = sqlite3.connect("sistema.db")
    cursor = con.cursor()

    cursor.execute("""
        SELECT
            p.nome_projeto,
            p.data_inicio,
            p.data_fim,
            u.nome,
            u.telefone
        FROM projeto p
        JOIN usuario u ON p.usuario_id = u.id
        ORDER BY p.id DESC
    """)
    projetos = cursor.fetchall()

    cursor.execute("""
        SELECT nome, telefone, data_nascimento
        FROM usuario
        ORDER BY id DESC
    """)
    usuarios = cursor.fetchall()

    con.close()

    msg = request.args.get("msg")
    return render_template("index.html", projetos=projetos, usuarios=usuarios, msg=msg)

#rota de cadastro de usuario
@app.route("/usuarios", methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        nome = request.form.get("nome")
        data = request.form.get("data_nascimento")
        telefone = request.form.get("telefone")
        termo = request.form.get("termo")

        if not termo:
            return redirect(url_for("cadastro_usuario", msg="termo_obrigatorio"))

        con = sqlite3.connect("sistema.db")
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuario (nome, telefone, data_nascimento) VALUES (?, ?, ?)",
                (nome, telefone, data)
            )
            con.commit()
            con.close()
            return redirect(url_for("home", msg="usuario_ok"))

        except sqlite3.IntegrityError:
            con.close()
            return redirect(url_for("cadastro_usuario", msg="usuario_duplicado"))

    msg = request.args.get("msg")
    return render_template("cadastro_usuario.html", msg=msg)

#rota de cadastro de projeto
@app.route("/projetos", methods=["GET", "POST"])
def cadastro_projeto():
    if not existe_usuario():
        return redirect(url_for("home", msg="precisa_usuario"))

    con = sqlite3.connect("sistema.db")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome FROM usuario")
    usuarios = cursor.fetchall()
    con.close()

    if request.method == "POST":
        nome_projeto = request.form.get("nome_projeto")
        data_inicial = request.form.get("data_inicio")
        data_final = request.form.get("data_final")
        usuario_id = request.form.get("usuario_id")

        if data_final <= data_inicial:
            return redirect(url_for("cadastro_projeto", msg="data_invalida"))

        con = sqlite3.connect("sistema.db")
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO projeto (nome_projeto, data_inicio, data_fim, usuario_id) VALUES (?, ?, ?, ?)",
                (nome_projeto, data_inicial, data_final, usuario_id)
            )
            con.commit()
            con.close()
            return redirect(url_for("home", msg="projeto_ok"))

        except sqlite3.IntegrityError:
            con.close()
            return redirect(url_for("cadastro_projeto", msg="projeto_duplicado"))

    msg = request.args.get("msg")
    return render_template("cadastro_projeto.html", usuarios=usuarios, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
