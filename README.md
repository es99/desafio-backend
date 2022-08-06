# Desafio Back-end

## Objetivo: Criação de uma API Restful que visa retornar dados de uma lista de tarefas, bem como inserir novas tarefas nesta lista.
- Tecnologias/Linguagens utilizadas:
  - Python
  - Framework Flask
  - TinyDB (persistir os dados em formato json) no database.json
  - flask_pydantic_spec (criação da documentação e listagem de endpoints)
  - shell script

## Como executar a aplicação - Contexto da Aplicação Restful rodando em LOCALHOST
- Executar o comando no terminal:
  -  rodar o script iniciar.sh; será setada as variáveis de ambiente necessárias e iniciar o servidor FLASK (flask run)
     -  source ./iniciar.sh

## Verificando endpoints/documentação da aplicação
    - http://localhost:5000/apidoc/swagger

### OBS - Testes:
- Poderás utilizar o HTTPie para testes; pip install httpie
- Exemplos:
  - GET (retorna todos os itens da lista)
    - http GET :5000/lista
  - GET (retorna apenas um item baseado no id) - Caso o id do item não exista é retornado código 404 not found, tratado com try except
    - http GET :5000/lista/{id}
  - POST (insere um item na lista, basta passar apenas a tarefa)
    - http POST :5000/lista tarefa="Ir ao supermercado"
  - PUT (modifica um item da lista passa o id e a tarefa)
    - http PUT :5000/lista/{id} tarefa="Trocar os lençois de cama"
  - DELETE (deleta um item da lista baseado no id)
    - http DELETE :5000/lista/{id}