# sqlachemy-sandbox
Try SQLAlchemy and Alembic


## Setup
```
$ git clone git@github.com:tayutaedomo/sqlachemy-sandbox.git
$ cd sqlachemy-sandbox
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```


## mysql with docker-compose
```
$ docker-compose build
$ docker-compose up -d
$ docker exec -it sqlachemy-sandbox_mysql_1 bash -p

$ mysql -u root -p -h 127.0.0.1
# Password is MYSQL_ROOT_PASSWORD in docker-compose.yaml

mysql> create database mydb;
mysql> show create database mysql;
```


## Scripts
```
$ cd sqlachemy-sandbox
$ source venv/bin/activate

$ python scripts/connect_db.py
```


## DB Migration with 
Create a new migration file.
```
$ alembic revision --autogenerate -m "create books table" --rev-id=001
```

Execute upgrade or downgrade.
```
$ alembic upgrade head
$ alembic downgrade base
```
