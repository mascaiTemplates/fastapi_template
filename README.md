# Fast API template

### Aim - speed ​​up development with help of a simple and well-designed template


### How to build and run
```
1) Create .env file in project root
POSTGRES_USER=user123
POSTGRES_PASSWORD=pass123
POSTGRES_DB=dbname
DB_HOST=127.0.0.1
DB_PORT=5433

2) Build and run containers
docker-compose up --build -d
```


### How to create and apply database migrations
```
alembic revision --autogenerate -m "migration name"
alembic upgrade head
```