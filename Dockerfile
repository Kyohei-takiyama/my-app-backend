# Base stage for shared environment setup
# ref:Gunicornによる公式Dockerイメージ - Uvicorn
# ref:https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker?tab=readme-ov-file#tiangolouvicorn-gunicorn-fastapi
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim AS base
WORKDIR /app

# Install environment dependencies
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
    openssl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Builder stage for installing Python dependencies
FROM base AS builder
COPY ./requirements.lock .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.lock

# Copy installed packages to a clean Python slim image
FROM base AS app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . /app

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/app/gunicorn.conf.py", "app.main:app"]

EXPOSE 8080