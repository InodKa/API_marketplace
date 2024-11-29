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
├─ requirements.txt
└─ web_api
   ├─ README.md
   └─ src
      ├─ dao
      │  ├─ crud
      │  │  ├─ categories.py
      │  │  ├─ inventories.py
      │  │  ├─ order_items.py
      │  │  ├─ orders.py
      │  │  ├─ pickup_points.py
      │  │  ├─ products.py
      │  │  ├─ statuses.py
      │  │  ├─ transfers.py
      │  │  ├─ users.py
      │  │  └─ warehouses.py
      │  ├─ database.py
      │  └─ models.py
      ├─ main.py
      ├─ routers
      │  ├─ categories.py
      │  ├─ inventories.py
      │  ├─ order_items.py
      │  ├─ orders.py
      │  ├─ pickup_points.py
      │  ├─ products.py
      │  ├─ statuses.py
      │  ├─ transfers.py
      │  ├─ users.py
      │  └─ warehouses.py
      └─ schemas
         ├─ category.py
         ├─ inventory.py
         ├─ order.py
         ├─ order_item.py
         ├─ pickup_point.py
         ├─ product.py
         ├─ status.py
         ├─ transfer.py
         ├─ user.py
         └─ warehouse.py

```