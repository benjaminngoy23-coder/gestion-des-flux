FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000 \
    DATA_DIR=/app/data \
    DB_FILE=fundflow_stable.db

COPY app.py main.py start.sh ./

RUN mkdir -p /app/data \
    && python -m py_compile /app/app.py /app/main.py

EXPOSE 8000

# Pas de HEALTHCHECK Docker ici : Dokploy peut le configurer lui-même après
# que le premier déploiement a réussi.
CMD ["sh", "/app/start.sh"]
