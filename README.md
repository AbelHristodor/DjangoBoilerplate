# Django Boilerplate

This is an *example* of a simple boilerplate of a dockerized django project using celery and rabbitmq for managing tasks. It also uses pipenv.



# Installation Guide:
Firstly install docker and docker compose. Check https://docs.docker.com/compose/install/ for docker-compose and https://docs.docker.com/install/ for docker.

Git clone the project in a folder and then create a .env file and paste the following inside:

```
# Database credentials

DATABASE_HOST=postgres
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres

# Memcached host
MEMCACHED_HOST=memcached
```

Then go to the base directory and run:  
    ```docker-compose up --build```

Once finished, while the app is running, open another terminal and migrate the app using:    
    ```docker-compose run --rm web scripts/migrate_loaddata.sh```

The app will be running at: http://localhost:8000/

If you can't run those command without sudo see: [Docker-docs-for-linux](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user) or [Stackoverflow-fix](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue)
