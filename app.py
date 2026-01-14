import sqlite3

con = sqlite3.connect("sistema.db")

cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS usuario(nome varchar(50), data int, telefone int)')

nome = input('Qual o seu nome?' )
data = input('Qual sua data de aniversario?')
telefone = input('Qual seu numero de telefone?')

verif = cursor.execute('SELECT nome FROM usuario')

usuarios = verif.fetchall()

nomes_lp = [i[0] for i in usuarios] 

if nome in nomes_lp :
    print('Usuario ja cadastrado')

else : 
    cursor.execute('INSERT INTO usuario VALUES (?,?,?)',(nome,data,telefone))
    print('Cadastro executado com sucesso')
    

con.commit()