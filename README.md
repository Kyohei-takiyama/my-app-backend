# How to development

- clone repogitory
- create feature branch from main branch

```mermaid
gitGraph
   commit
   branch feature_1
   branch feature_2
   checkout feature_1
   commit
   commit
   checkout feature_2
   commit
   checkout main
   merge feature_1 tag: "v1.0"
   checkout feature_2
   commit
   checkout main
   merge feature_2 tag: "v2.0"
```

# Create Environment Variables

- Copy /app/core/envs/exampe.env -> .env.local

```
app
 ┗core
  ┗envs
   ┗env.local
```

# Docker

```
docker-compose build
docker-compose up
```

# API Documents

**precondition**

- docker running

```
http://localhos:8000/docs
or
http://localhost:8000/redoc
```

# Database

### Migration

**precondition**

- docker running

**run command**

- into docker container

  ```
  docker-compose exec db sh
  ```

- change derectory app derectory

  ```
  cd app
  ```

- make migration file

  ```
  alembic revision --autogenerate -m "{xxxxxxxxxxxx}"
  ```

- migration

  ```
  alembic upgrade head
  ```
