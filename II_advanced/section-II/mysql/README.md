# MySQL

MySQL is an open-source relational database management system (RDBMS). 
A relational database organizes data into one or more data tables in which data types may be related to each other; these relations help structure the data. 

## Prerequisite
- MySQL (https://www.mysql.com/downloads/)

## Install MySQL Driver

Python needs a MySQL driver to access the MySQL database.
We recommend that you use PIP to install "MySQL Connector".

```sh
$ python -m pip install mysql-connector-python
```

## Create Connection
Start by creating a connection to the database.
Use the username and password from your MySQL database.

```PY
import mysql.connector

connection = mysql.connector.connect(
    host="hostname",
    user="yourusername",
    password="password"
)

# test connection
print(connection)
```

## Create Database
To create a database in MySQL, use the `CREATE DATABASE database_name`.

```py
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE college")
```

## Creating a Table

To create a table in MySQL, use the "CREATE TABLE" statement.
Make sure you define the name of the database when you create the connection.

```py
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="college"
)

cursor = connection.cursor()
cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
```
## Insert Into Table
To fill a table in MySQL, use the "INSERT INTO" statement.
```py
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="college"
)

cursor = connection.cursor()

query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = ("Mario", "Maputo, Costal do Sol")
cursor.execute(query, values)

connection.commit()
```