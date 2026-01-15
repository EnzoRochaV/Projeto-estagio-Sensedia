import sqlite3

con = sqlite3.connect("sistema.db")

cursor = con.cursor()

nome = input('Qual o seu nome?' )


teste = cursor.execute('SELECT nome FROM usuario')

nomes = teste.fetchall()

nomes_lp = [i[0] for i in nomes] 

if nome in nomes_lp :
    print('Usuario ja cadastrado')

else : 
    print('Cadastro executado com sucesso')


print(nomes_lp)


#teste