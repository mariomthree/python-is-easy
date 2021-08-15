import mysql.connector
import os
import csv

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_DATABASE = 'school'

def createDatabase():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute(f"DROP DATABASE {DB_DATABASE}")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_DATABASE}")

def getInstance():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
    )
    return connection

def createTable():
    connection = getInstance()
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS college(\
            college_id INT AUTO_INCREMENT PRIMARY KEY,\
            college_name VARCHAR(255),\
            college_address VARCHAR(255),\
            college_city VARCHAR(255),\
            college_country VARCHAR(255))"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS teacher(\
            teacher_id INT AUTO_INCREMENT PRIMARY KEY,\
            teacher_name VARCHAR(255),\
            teacher_email VARCHAR(255),\
            college_id INT,\
            date_joined DATE,\
            speciality VARCHAR(255),\
            salary double,\
            experience VARCHAR(255),\
            UNIQUE KEY unique_email (teacher_email))"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS student(\
            student_id INT AUTO_INCREMENT PRIMARY KEY,\
            student_name VARCHAR(255),\
            student_email VARCHAR(255),\
            college_id INT,\
            date_joined DATE,\
            major_taken VARCHAR(255),\
            college_Level VARCHAR(255),\
            UNIQUE KEY unique_email (student_email))"
    )

def insertCollege(colleges):
    connection = getInstance()
    cursor = connection.cursor()
    for college in colleges:
        query = "INSERT INTO college(college_name,college_address,college_city,college_country) VALUES (%s,%s,%s,%s);"
        params =  (
            college[0],
            college[1],
            college[2],
            college[3],
        )
        cursor.execute(query,params)
    connection.commit()
    connection.close()

def insertStudent(students):
    connection = getInstance()
    cursor = connection.cursor()
    for student in students:
        query = "INSERT INTO student(student_name, student_email,college_id, date_joined, major_taken, college_Level)\
        VALUES (%s,%s,%s,%s,%s,%s);"
        params =  (
            student[0],
            student[1],
            student[2],
            student[3],
            student[4],
            student[5],
        )
        cursor.execute(query,params)
    connection.commit()
    connection.close()

def insertTeacher(teachers):
    connection = getInstance()
    cursor = connection.cursor()
    for teacher in teachers:
        query = "INSERT INTO teacher(teacher_name,teacher_email,college_id,date_joined,speciality,salary,experience)\
        VALUES (%s,%s,%s,%s,%s,%s,%s);"
        params =  (
            teacher[0],
            teacher[1],
            teacher[2],
            teacher[3],
            teacher[4],
            teacher[5],
            teacher[6]
        )
        cursor.execute(query,params)
    connection.commit()
    connection.close()

def getDataOfColleges(): 
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM college')
    colleges = cursor.fetchall()
    connection.close()
    return colleges

def getDataOfStudents(): 
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT s.student_name, s.student_email,c.college_name, s.date_joined, s.major_taken, s.college_Level\
         FROM student s INNER JOIN college c ON s.college_id = c.college_id')
    students = cursor.fetchall()
    connection.close()
    return students

def getDataOfTeachers(): 
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT t.teacher_name, t.teacher_email,c.college_name,\
         t.date_joined, t.speciality, t.salary, t.experience\
         FROM teacher t INNER JOIN college c ON t.college_id = c.college_id')
    teachers = cursor.fetchall()
    connection.close()
    return teachers

# file manipulation
def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

def readCSVFile(fileName):
    records = []
    with open(fileName, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            records.append(row)
    return records

def showRecords(records):
    for record in records:
        print(record)

def main():
    createDatabase()
    createTable()

    colleges = readCSVFile(getCurrentDirname()+'\college.csv')
    students = readCSVFile(getCurrentDirname()+'\student.csv')
    teachers = readCSVFile(getCurrentDirname()+'\\teacher.csv')

    insertCollege(colleges)
    insertStudent(students)
    insertTeacher(teachers)

    # print("======== Colleges =========")
    # showRecords(getDataOfColleges())
    # print("======== Teachers =========")
    # showRecords(getDataOfTeachers())
    # print("======== Students =========")
    # showRecords(getDataOfStudents())

main()

