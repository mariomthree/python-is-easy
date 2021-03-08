import sqlite3

databaseFile = 'students.db'
databaseTableName = 'STUDENTS'
query = ''

connectation = sqlite3.connect(databaseFile)

query = f'DELETE FROM {databaseTableName} WHERE id = 1'
connectation.execute(query)
connectation.commit()

query = f'SELECT * FROM {databaseTableName}'
cursor = connectation.execute(query)
students = cursor.fetchall()
print(students)

connectation.close()