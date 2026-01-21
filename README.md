Sistema de Cadastro de Usuários e Projetos

Esse projeto é um sistema simples para gerenciar usuários e projetos com
Python + Flask + SQL (SQLite).

Ele foi feito como parte do meu desafio de estágio. A ideia era aprender
como construir uma aplicação web do zero usando Python, Flask e banco de
dados. Comecei tentando entender a lógica geral, fazendo um código para rodar diretamente no terminal.
Aos poucos fui aprendendo e introduzindo o Flask para chegar no resultado atual.

---------------------------------------------------------------------------------------------------

Pré-requisitos: 
- Python 3.11.3 
- SQLite 
- Flask 

----------------------------------------------------------------------------------------------------

USANDO O SISTEMA

Página inicial

Exibe o nome do sistema com os botões "Cadastrar Usuário" e "Cadastrar Projeto".
Clique na opção desejada (Só é permitido cadastrar um projeto se já existir um usuário cadastrado).

Mostra tabela de usuários cadastrados com os dados fornecidos pelo usuário:
(Nome, telefone e data de nascimento)

Mostra tabela de projetos com os dados fornecidos pelo usuário:
(Nome do projeto, início do projeto, previsão de conclusão, responsável pelo projeto
e telefone do responsável)

Cadastro de usuário
 
Clique em “Cadastrar Usuário”, preencha os campos e aceite os termos de uso.
Se já existir um usuário igual, um aviso irá aparecer, acusando o erro.
Caso contrário, a mensagem "Usuário cadastrado com sucesso" irá aparecer na tela,
redirecionando o usuário para a página inicial.

Caso tenha clicado "sem querer" na página de cadastro de usuário, existe um botão que 
redireciona o usuário para a página inicial.

Cadastro de projeto:

Só é possível cadastrar um projeto se já existir um usuário criado.
Clique em "Cadastrar Projeto" e preencha os campos.

Atenção na data de início e na data final, pois a data final não 
pode ser menor ou igual à data inicial.

Caso use um nome repetido, um aviso irá aparecer na tela, retornando o usuário
para o cadastro de projeto.

Caso tenha clicado "sem querer" na página de cadastro de projeto, existe um botão que 
redireciona o usuário para a página inicial.

-----------------------------------------------------------------------------------------------------

TECNOLOGIAS UTILIZADAS

- Python 3.11.3  
- Flask  
- SQLite  


-----------------------------------------------------------------------------------------------------

Uso de IA

O ChatGPT foi utilizado como ferramenta de apoio ao aprendizado de Flask,
principalmente para entender conceitos e a lógica por trás do framework,
já que tive meu primeiro contato com a ferramenta durante esta semana do projeto.

A IA não foi utilizada para gerar automaticamente rotas, funções ou tabelas do sistema.
Todo o código foi escrito e estruturado por mim.

Em alguns momentos, o ChatGPT também foi utilizado para auxiliar na identificação
de erros quando o sistema apresentava falhas, servindo apenas como apoio para
localizar o problema e permitir que eu mesmo realizasse a correção.



------------------------------------------------------------------------------------------------------


AUTOR

Enzo Rocha
