# README - Task Tracker

## Descrição do Projeto

O **Task Tracker** é uma ferramenta de linha de comando desenvolvida em Python 3.13 para gerenciamento de tarefas. Ele permite criar, atualizar, listar, deletar e alterar o status das tarefas de maneira eficiente diretamente pelo terminal.

Esse projeto foi feito baseado no ROADMAP de Python, confira o escopo do projeto [nesse link](https://roadmap.sh/projects/task-tracker)
## Instalação

Siga os passos abaixo para instalar e configurar o projeto:

1. Certifique-se de ter o Python 3.13 instalado em sua máquina. Você pode fazer o download [aqui](https://www.python.org/downloads/).

2. Clone o repositório do projeto:

3. Acesse o diretório do projeto

4. (Opcional) Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

## Execução

Para executar o Task Tracker, utilize o terminal e siga as instruções abaixo:

1. Execute o arquivo principal:
   ```bash
   python main.py <comando> [opções]
   ```

2. Comandos disponíveis:

   - **add**: Adiciona uma nova tarefa.
     ```bash
     python main.py add "Descrição da tarefa"
     ```
   - **delete**: Deleta uma tarefa pelo ID.
     ```bash
     python main.py delete <id>
     ```
   - **update**: Atualiza a descrição de uma tarefa.
     ```bash
     python main.py update <id> "Nova descrição"
     ```
   - **list**: Lista todas as tarefas (caso o status venha em branco) ou filtra por status (opcional: `todo`, `in-progress`, `done`).
     ```bash
     python main.py list [status]
     ```
   - **mark-in-progress**: Marca uma tarefa como "IN PROGRESS".
     ```bash
     python main.py mark-in-progress <id>
     ```
   - **mark-done**: Marca uma tarefa como "DONE".
     ```bash
     python main.py mark-done <id>
     ```

## Estrutura do Projeto

O projeto é organizado em três arquivos principais:

1. **main.py**: Contém a lógica principal e a integração entre os módulos.
2. **cli.py**: Responsável por configurar os argumentos de linha de comando.
3. **classes.py**: Inclui as classes necessárias para gerenciamento de tarefas e persistência de dados.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
