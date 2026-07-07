# Cadastro de Carro

Sistema de cadastro de veículos para uma concessionária, desenvolvido em **Python** com persistência em **MySQL**. A aplicação roda em modo console (menu interativo) e implementa o CRUD completo de três entidades relacionadas: **Marca**, **Modelo** e **Carro**.

## Entidades

- **Marca** — ex.: Toyota, Honda
- **Modelo** — pertence a uma marca (ex.: Corolla, Civic)
- **Carro** — pertence a um modelo, com renavam, placa, valor e ano

Relacionamento: `marca (1) → (N) modelo (1) → (N) carro`

## Funcionalidades (CRUD completo)

| Entidade | Cadastrar | Listar | Atualizar | Excluir |
|----------|:---------:|:------:|:---------:|:-------:|
| Marca    | ✅ | ✅ | ✅ | ✅ |
| Modelo   | ✅ | ✅ | ✅ | ✅ |
| Carro    | ✅ | ✅ | ✅ | ✅ |

Todas as operações realizam persistência completa no banco de dados.

## Pré-requisitos

- Python 3
- MySQL Server
- Driver Python: `pip install mysql-connector-python`

## Como executar

1. Crie o banco de dados e as tabelas:

   ```bash
   mysql -u root -p < sql/dump.sql
   ```

2. Ajuste as credenciais em `src/database.py` (host, user, password) conforme a sua instalação do MySQL.

3. Execute a aplicação:

   ```bash
   cd src
   python main.py
   ```

## Estrutura do projeto

```
cadastro-carro/
├── sql/
│   └── dump.sql        # criação do banco e das tabelas
└── src/
    ├── database.py     # conexão com o MySQL
    ├── main.py         # menu principal e interface de console
    ├── marca.py        # CRUD de marcas
    ├── modelo.py       # CRUD de modelos
    └── carro.py        # CRUD de carros
```
