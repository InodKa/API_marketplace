# API_marketplace

```
API_marketplace
├─ .gitignore
├─ LICENSE
├─ README.md
├─ databases
│  ├─ mongoDB
│  └─ postgres
│     ├─ README.md
│     └─ scripts
│        └─ create_tables.sql
├─ docker
│  ├─ docker-compose.yml
│  ├─ postgres
│  │  └─ Dockerfile
│  └─ web_api
│     └─ Dockerfile
└─ web_api
   └─ src
      ├─ __init__.py
      ├─ dao
      │  ├─ __init__.py
      │  ├─ crud.py
      │  ├─ database.py
      │  └─ models.py
      ├─ main.py
      ├─ routers
      │  ├─ __init__.py
      │  └─ users.py
      └─ schemas
         ├─ __init__.py
         └─ user.py

```