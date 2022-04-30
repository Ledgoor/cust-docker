# cust-docker

This is a collection of custom scripts developed over time to automation of routine tasks, assembled on:

* Infrastructure: Docker-compose
* Web servers: Nginx
* Databases: PostgreSQL, Redis

The GitHub repository houses the components needed to build cust as a container. Images are will be built regularly using the code in that repository and are pushed to Docker Hub.

## Quickstart

Example env/cust.env file:
```bash
    #BASE
    LOCAL_IP='127.0.0.1'
    SECRET_KEY='secret_key'
    TIME_ZONE='Asia/Yekaterinburg'

    #DATABASE
    DB_HOST='db_host'
    DB_NAME='db_name'
    DB_USER='db_username'
    DB_PASSWORD='db_password'
```

Example env/postgres.env file:
```bash
    POSTGRES_DB='db_name'
    POSTGRES_USER='db_username'
    POSTGRES_PASSWORD='db_passwrod'
```

Installation:
```bash
    git clone -b release https://github.com/pvenv/cust-docker.git
    cd cust-docker
    docker-compose up -d
```

The whole application will be available after a few minutes. Open the URL http://127.0.0.1/ in a web-browser.
The default credentials are:
* login: admin
* password: admin

## Dependencies

This project relies only on *Docker* and *docker-compose* meeting these requirements:

* The *Docker version* must be at least `19.03`.
* The *docker-compose version* must be at least `1.28.0`.

To check the version installed on your system run `docker --version` and `docker-compose --version`.

## Updating
...

## Full data reset
```bash
    docker-compose up --build --remove-orphans
```

## Demo
...
