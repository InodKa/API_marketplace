FROM postgres:14

ENV POSTGRES_USER=pguser
ENV POSTGRES_PASSWORD=pgpassword
ENV POSTGRES_DB=marketplace_db

COPY databases/postgres/scripts/ /docker-entrypoint-initdb.d/
