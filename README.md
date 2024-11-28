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
   ├─ README.md
   └─ src
      ├─ dao
      │  ├─ crud
      │  │  ├─ statuses.py
      │  │  └─ users.py
      │  ├─ database.py
      │  └─ models.py
      ├─ main.py
      ├─ routers
      │  ├─ statuses.py
      │  └─ users.py
      └─ schemas
         ├─ status.py
         └─ user.py

```