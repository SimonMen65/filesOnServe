# filesOnServe

### Environment
Need to install flask, flask-mysql
```
pip3 install flask, flask-mysql
```

### Database
Create a database named "FilesAnubis", and insert three columns id, name and file. If you are using MySQL:
```
Create Database FilesAnubis;
Create Table Files(
    id int,
    name varchar(255),
    file mediumblob
);
```