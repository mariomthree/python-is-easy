import pandas as pd
import numpy as np
import os
import re
import mysql.connector
import sys

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_DATABASE = 'company'

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
        "CREATE TABLE IF NOT EXISTS employees(\
            emp_id INT PRIMARY KEY,\
            name_prefix VARCHAR(255),\
            first_name VARCHAR(255),\
            middle_initial CHAR,\
            last_name VARCHAR(255),\
            gender CHAR,\
            e_mail VARCHAR(255),\
            father_name VARCHAR(255),\
            mother_name VARCHAR(255),\
            mother_maiden_name VARCHAR(255),\
            date_of_birth DATE,\
            time_of_birth TIME,\
            age_in_yrs FLOAT,\
            weight_in_kgs FLOAT,\
            date_of_joining DATE,\
            quarter_of_joining VARCHAR(255),\
            half_of_joining VARCHAR(255),\
            year_of_joining INT,\
            month_of_joining INT,\
            month_name_of_joining VARCHAR(255),\
            short_month VARCHAR(255),\
            day_of_joining INT,\
            short_dow VARCHAR(255),\
            age_in_company FLOAT,\
            salary FLOAT,\
            ssn VARCHAR(255),\
            phone_no VARCHAR(255),\
            place_name VARCHAR(255),\
            county VARCHAR(255),\
            city VARCHAR(255),\
            state VARCHAR(255),\
            zip INT,\
            region VARCHAR(255)\
        )"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(\
            user_id INT AUTO_INCREMENT PRIMARY KEY,\
            emp_id INT,\
            user_name VARCHAR(50),\
            password VARCHAR(255)\
        )"
    )

def insertUsers(users):
    connection = getInstance()
    cursor = connection.cursor()
    for user in users.values.tolist():
        query = "INSERT INTO users(emp_id,user_name,password) VALUES (%s,%s,%s);"
        params =  (
            user[0],
            user[1],
            user[2],
        )
        cursor.execute(query,params)
    connection.commit()
    connection.close()

def insertEmployees(employees):
    connection = getInstance()
    cursor = connection.cursor()
    for employee in employees.values.tolist():
        query = "INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(query, tuple(employee))
    connection.commit()
    connection.close()

def getDataOfUsers(): 
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    connection.close()
    return users

def getDataOfEmployees(): 
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    connection.close()
    return employees

def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

def normalizeColumns(records):
    columns = []
    for column in records.columns:
        column = column.lower()
        column = column.replace("\'s",'')
        column = column.replace(".",'')
        column = column.replace("%",'')
        column = column.replace(' (years)','')
        column = column.replace('  ','_')
        column = column.replace(' ','_')
        columns.append(column)
    records.columns  = columns
    return records

def showRecords(records):
    for record in records:
        print(record)

records = pd.read_csv(getCurrentDirname()+'/records.csv') 
records =  normalizeColumns(records)

employees = records.drop(columns=['user_name','password', 'last_hike'])
users = records[
    ['emp_id',"user_name", "password"]
]
# createDatabase()
# createTable()
# insertUsers(users=users)
insertEmployees(employees=employees)
#showRecords(getDataOfUsers())
showRecords(getDataOfEmployees())
