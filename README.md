# Fast API template

### Aim - speed ​​up development with help of a simple and well-designed template

Tech stack: FastAPI + SQLAlchemy + Alembic + Postgres + DockerCompose 

### How to build and run
```
1 Сreate .env file in project root
POSTGRES_USER=user123
POSTGRES_PASSWORD=pass123
POSTGRES_DB=dbname
DB_HOST=db (or 127.0.0.1 for local development)
PGPORT=5432

2 Build and run containers
docker-compose up --build -d
```


### How to create and apply database migrations
```
docker exec -ti  fastapi_template_backend-api_1 bash
alembic revision --autogenerate -m "migration name"
alembic upgrade head
```


### How to run tests
```
pytest tests/api/v1/test_users.py
```     