##  SQLite with Python

SQLite is a C library that provides a lightweight disk-based database that
doesn’t require a separate server process and allows accessing the database
using a nonstandard variant of the SQL query language.

SQLite3 can be integrated with Python using the sqlite3 module, which was written by
Gerhard Haring. It provides an SQL interface compliant with the DB-API 2.0
specification described by PEP 249.

To use the sqlite3 module, you must first create a connection object that represents the
database and then optionally you can create a cursor object, which will help you in
executing all the SQL statements.

Some applications can use SQLite for internal data storage. It’s also possible
to prototype an application using SQLite and then port the code to a larger
database such as PostgreSQL, MySQL or Oracle.

To use the module, you must first create a Connection object that represents the
database. Here the data will be stored in the example.db file:

To use the module, you must first create a Connection object that represents the
database. Here the data will be stored in the example.db file:

```py
import sqlite3

# open connectation
connectation = sqlite3.connect('example.db')
```
You can also supply the special name :memory: to create a database in RAM.
Once you have a Connection , you can create a Cursor object and call its execute()
method to perform SQL commands:

```py
cursor = connectation.cursor()

# create table
cursor.execute('''CREATE TABLE animal (name text, height real, weight real)''')

# insert a row of data
cursor.execute("INSERT INTO animal VALUES ('Dog',1.23,60)")

# Save the changes
connectation.commit()

# close the connection
connectation.close()
```
## Create, Read, Update and Delete(CRUD)

### Create 
Inserting or creating a new record within the table. 

```py
import sqlite3

databaseFile = 'students.db'
databaseName = 'STUDENTS'
query = ''

# connect to sqlite database
connectation = sqlite3.connect(databaseFile)

# start cursor
cursor = connectation.cursor()

# drop table if exists
query = f'DROP TABLE IF EXISTS STUDENTS'
cursor.execute(query)

# create table
query = f'''
        CREATE TABLE STUDENTS(
            id INT PRIMARY KEYNOT NULL,
            name CHAR(20) NOT NULL,
            roll CHAR(20),
            address CHAR(50),
            class CHAR(20)
        )'''
cursor.execute(query)

# commit and closen
connectation.commit()
connectation.close()
```

### Insert

```py
import sqlite3

databaseFile = 'students.db'
databaseName = 'STUDENTS'
query = ''

connectation = connect.sqlite3('students.db')
cursor = connectation.cursor()

cursor.execute(f"INSERT INTO {databaseName} (id, name, roll, address, class) VALUES(1, 'Mario', '001, 'pizzam' '10th')")

cursor.commit()
cursor.close()

#OR

cursor = connectation.cursor()

query = (f"INSERT INTO {databaseName} (id, name, roll, address, class)'
          'VALUES(:id, :name, :roll, :address, :class);")
params = {
    'id':2,
    'name':'Manuel',
    'roll':'002',
    'address':'Moz',
    'class':'12th'
}

cursor.execute(query, params)
cursor.commit()
cursor.close()
```

