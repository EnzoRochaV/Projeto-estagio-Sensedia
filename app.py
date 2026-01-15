import sqlite3

con = sqlite3.connect("sistema.db")

cursor = con.cursor()


#criação das tabelas para o banco de dados, somente se elas já não foram criadas
cursor.execute('CREATE TABLE IF NOT EXISTS usuario (nome TEXT, data_nascimento TEXT, telefone TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS projeto (nome_do_projeto TEXT, data_de_inicio TEXT, data_de_finalização TEXT)')

#função para o inicio do processo de cadastro do usuario, usando a validação do termo de usuario
def iniciar_cadastro_usuario():
    print('\nInsira os dados abaixo para iniciar o cadastro')

    nome = input('\nQual o seu nome? ' ).lower()
    data = input('\nQual sua data de nascimento (DD-MM-YYYY): ')
    telefone = input('\nQual seu numero de telefone? ')

    print('\nPara prosseguir com o cadastro, você deve aceitar os termos de uso.')

    termo = input('\nVocê aceita os termos de uso? (s/n): ').lower()

    if termo != 's':
        print('\nCadastro não concluído. É necessário aceitar os termos de uso.')
        con.close()
        exit()


    verif = cursor.execute('SELECT nome FROM usuario')

    usuarios = verif.fetchall()

    nomes_lp = [i[0] for i in usuarios] 

    if nome in nomes_lp :
        print('\nUsuario ja cadastrado')
        recomeco = input('\nDeseja recomeçar o cadastro? (s/n)').lower()  
            
        if recomeco == 's':
            
            iniciar_cadastro_usuario()
            
        else:
            
            print('\nCadastro encerrado.')   
            con.close()
            exit()


    else : 
    
        cursor.execute('INSERT INTO usuario VALUES (?,?,?)',(nome,data,telefone))
        print('\nCadastro executado com sucesso')
    
iniciar_cadastro_usuario()

def iniciar_cadastro_projeto():  

    cursor.execute('SELECT nome FROM usuario')
    usuarios = cursor.fetchall()

    if not usuarios:
        print('\nNão é possível cadastrar projeto sem usuários cadastrados.')
        return

    print('\nInsira os dados do projeto')

    nome_projeto = input('\nNome do projeto: ').lower()
    data_inicio = input('Data de início (DD-MM-YYYY): ')
    data_fim = input('Data de fim (DD-MM-YYYY): ')

    if data_fim < data_inicio:
        print('\nErro: a data de fim não pode ser menor que a data de início.')
        return


    cursor.execute(
        'INSERT INTO projeto VALUES (?,?,?)',
        (nome_projeto, data_inicio, data_fim)
    )

    print('\nProjeto cadastrado com sucesso!')

iniciar_cadastro_projeto()       


#print('\nSelecione o responsável pelo projeto:')
#    for i, usuario in enumerate(usuarios, start=1):
#        print(f'{i} - {usuario[0]}')
#
#    escolha = int(input('Digite o número do responsável: '))
#    responsavel = usuarios[escolha - 1][0]






con.commit()
con.close() 