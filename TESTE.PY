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


#print('\nSelecione o responsável pelo projeto:')
#    for i, usuario in enumerate(usuarios, start=1):
#        print(f'{i} - {usuario[0]}')
#
#    escolha = int(input('Digite o número do responsável: '))
#    responsavel = usuarios[escolha - 1][0]