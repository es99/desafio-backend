# Desafio Back-end

## Objetivo: Criação de uma API Restfull que visa retorna dados de uma lista de tarefas, bem como inserir novas tarefas nesta lista.
- Tecnologias/Linguagens utilizadas:
  - Python
  - Framework Flask
  - TinyDB (persistir os dados em formato json) no database.json
  - flask_pydantic_spec (criação da documentação e listagem de endpoints)

## Como executar a aplicação
- Executar o comando no terminal:
  -  source ./setar_variaveis_ambiente
- O arquivo "setar_variaveis_ambiente" contém as variváveis FLASK_APP e FLASK_DEBUG que são setadas no ambiente, 
  respectivamente como, caminho do arquivo de aplicação flasky.py e modo debug ativo 1.
- flask run
  
## Endpoints da API
- Retornar toda a lista - GET
    - localhost:5000/api/v1/lista/
- Retornar apenas um elemento da lista, baseado em seu Id - GET
    - localhost:5000/api/v1/lista/{id}
      - Ex: localhost:5000/api/v1/lista/1
- Inserir uma nova tarefa na lista - POST
    formato json: {"id": 0, "tarefa": string}

- Para verificar a documentação e os endpoints acessar: http://localhost:5000/apidoc/swagger