# Order Management System

## Installation
Make sure to have [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/linux/) installed on your system.

## Building and Running
Create a `.env` file at the root of the project and fill in these variables with appropriate values.

```python
SECRET_KEY="SECRET_KEY"
DEBUG=False
ALLOWED_HOSTS=*

DATABASE_NAME=database_name
DATABASE_USER=username
DATABASE_PASSWORD=password
DATABASE_HOST=database # must be the same as the name of the database service in docker-compose.yml
DATABASE_PORT=5432
```

Simply run this command to bring the services up.

```shell
docker compose up -d --build
```

Depending on your installation, the *compose* command might be like this:

```shell
docker-compose up -d --build
```

## Documentation
You can view the Swagger UI at http://127.0.0.1/api/v1/docs.
