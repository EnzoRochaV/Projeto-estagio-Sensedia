import sqlite3

con = sqlite3.connect("sistema.db")
cursor = con.cursor()

#criação das tabelas para o banco de dados, somente se elas já não foram criadas
cursor.execute('CREATE TABLE IF NOT EXISTS usuario (nome TEXT, data_nascimento TEXT, telefone TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS projeto (nome_do_projeto TEXT, data_de_inicio TEXT, data_de_finalização TEXT)')

#função dedicada ao cadastro de usuario com validasção do termo de uso
def iniciar_cadastro_usuario():
    print('\nInsira os dados abaixo para iniciar o cadastro')

    nome = input('\nQual o seu nome? ' ).lower()
    data = input('\nQual sua data de nascimento (DD-MM-YYYY): ')
    telefone = input('\nQual seu numero de telefone? ')

    print('\nPara prosseguir com o cadastro, você deve aceitar os termos de uso.')

    while True : 
    
        termo = input('\nVocê aceita os termos de uso? (s/n): ').lower()

        if termo != 's':
            print('\nCadastro não concluído. É necessário aceitar os termos de uso.')

        else :
            break     


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
            return

    else : 
    
        cursor.execute('INSERT INTO usuario VALUES (?,?,?)',(nome,data,telefone))
        print('\nCadastro executado com sucesso')    
        con.commit()

#função dedicada ao cadastro do projeto
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
    con.commit()

iniciar_cadastro_usuario()

iniciar_cadastro_projeto()       

con.commit()
con.close() 