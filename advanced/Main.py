import sqlite3

databaseFile = 'students.db'
databaseName = 'STUDENTS'
query = ''

# connect to sqlite database
connectation = sqlite3.connect(databaseFile)

# start cursor
cursor = connectation.cursor()

# drop table if exists
query = f'DROP TABLE IF EXISTS {databaseName}'
cursor.execute(query)

# create table
query = f'''
        CREATE TABLE {databaseName}(
            id INT PRIMARY KEYNOT NULL,
            name CHAR(20) NOT NULL,
            roll CHAR(20),
            address CHAR(50),
            class CHAR(20)
        )'''
cursor.execute(query)

# commit and close
connectation.commit()
connectation.close()