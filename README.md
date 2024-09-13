
## Init

##### Destroy docker containers and volumes
```bash
docker system prune -a
docker volume prune
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```

##### Docker (dev)
```bash
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py createsuperuser
docker-compose up
```

##### .env file
```bash
DB_NAME=postgres
DB_USER=postgres
DB_HOST=db
SECRET_KEY=django-insecure-rpt591+wff3e&(q&zp=m^0kd1&)@d55e-1uv1=s9kztc4mu3b+
```


### tests
```bash
docker-compose run web python3 manage.py test project.user.tests
docker-compose run web python3 manage.py test project.main.tests
```


### Swagger
http://localhost/swagger/