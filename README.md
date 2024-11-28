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
│        ├─ create_tables.sql
│        └─ seed_data.sql
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
      │  │  ├─ pickup_points.py
      │  │  ├─ statuses.py
      │  │  ├─ users.py
      │  │  └─ warehouses.py
      │  ├─ database.py
      │  └─ models.py
      ├─ main.py
      ├─ routers
      │  ├─ pickup_points.py
      │  ├─ statuses.py
      │  ├─ users.py
      │  └─ warehouses.py
      └─ schemas
         ├─ pickup_point.py
         ├─ status.py
         ├─ user.py
         └─ warehouse.py

```