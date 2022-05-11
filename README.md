# 🙉 What's all the CUST?

Cross-platform users script toolkit - this is CMS, containing scripts, developed over time, to automation of routine tasks, assembled on:

* Infrastructure: Docker-compose
* Web servers: Nginx
* Web apps: Django Channels (JSON RPC API)
* Frontend: HTML5 Bootstrap, jQuery
* Databases: PostgreSQL, Redis

The GitHub repository houses the components needed to build cust as a container. Images are will be built regularly using the code in that repository and are pushed to Docker Hub.

## ⚡ Fast implementation

**Step 1:** If not installed, download and install docker and docker-compose:
* Get Docker - https://docs.docker.com/get-docker/ (see the **Dependencies** section)

**Step 2:** Cloning the project:
```bash
    git clone -b release https://github.com/pvenv/cust-docker.git
```

**Step 3:** Creating **.env** files (see the **Env examples** section):

**Step 4:** Running and usage the project:
```bash
    cd cust-docker
    docker-compose up -d
```

The whole application will be available after a few minutes. Open the URL http://127.0.0.1/ in a web-browser.
The default credentials are:
* login: admin
* password: admin


## 🎉 Env examples

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

## Dependencies

This project relies only on *Docker* and *docker-compose* meeting these requirements:

* The *Docker version* must be at least `19.03`.
* The *docker-compose version* must be at least `1.28.0`.

To check the version installed on your system run `docker --version` and `docker-compose --version`.

## Updating
...

## Recreating containers with data removal
```bash
    docker-compose up --build --remove-orphans
```

## Demo
...

## Screenshots
...
