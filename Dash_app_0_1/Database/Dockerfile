FROM postgres:15rc1-bullseye

ENV POSTGRES_PASSWORD: ${DB_ADMIN_PASSWORD}

COPY Schema_definitions/ /docker-entrypoint-initdb.d/