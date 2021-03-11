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
# Or
cursor.execute("CREATE DATABASE IF NOT EXISTS college")

# check if exists
cursor.execute("SHOW DATABASES")
print(*cursor, sep='\n')
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

# check if exists
cursor.execute("SHOW TABLES")
print(*cursor, sep='\n')

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

query = "INSERT INTO students (name, address) VALUES (%s, %s)"
values = ("Mario", "Maputo, Costal do Sol")
cursor.execute(query, values)

connection.commit()
```

## Select From a Table

To select from a table in MySQL, use the "SELECT" statement.
```py
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="college"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM students")

students = mycursor.fetchall()
for student in students:
  print(student)
```
## Delete Record
You can delete records from an existing table by using the "DELETE FROM" statement.

```py
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="college"
)

cursor = connection.cursor()

query = "DELETE FROM customers WHERE id = %s"
values = (1, )
cursor.execute(query, values)
connection.commit()
```

## Update Table
You can update existing records in a table by using the "UPDATE" statement.

```py
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="college"
)

cursor = connection.cursor()

query ="UPDATE customers SET address = %s WHERE id = %s"
values = ("Maputo, Costa do Sol - Triunfo", 1)
cursor.execute(query, values)
connection.commit()
```

## Credits

w3schools
- <a href="https://www.w3schools.com/python/default.asp" target="_blank">Python Tutorial</a>
- <a href="https://www.w3schools.com/python/python_mysql_getstarted.asp" target="_blank">Python MySQL</a>