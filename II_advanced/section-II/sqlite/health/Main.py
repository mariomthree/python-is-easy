import sqlite3
import csv, os
from pathlib import Path


# database manipulation
DATABASE = 'school.db'

def getInstance():
    return sqlite3.connect(DATABASE)

def createTable():
    connection = getInstance()
    cursor = connection.cursor()

    # create table hospital
    cursor.execute('DROP TABLE IF EXISTS hospital')
    cursor.execute('''
        CREATE TABLE hospital (
            hospital_id INTEGER PRIMARY KEY NOT NULL,
            hospital_name char(30),
            bed_count int)''')
    connection.commit()

    # create table doctor
    cursor.execute('DROP TABLE IF EXISTS doctor')
    cursor.execute('''
        CREATE TABLE doctor (
            doctor_id INTEGER PRIMARY KEY,
            doctor_name TEXT,
            hospital_id int,
            date_joined TEXT,
            speciality TEXT,
            salary REAL,
            experience TEXT,
            FOREIGN KEY(hospital_id) REFERENCES hospital(hospital_id))''')
    connection.commit()
    connection.close()

def insertHospitals(hospitals):
    connection = getInstance()
    cursor = connection.cursor()
    for hospital_name, bed_count in hospitals:
        query = "INSERT INTO hospital(hospital_name, bed_count) VALUES( ?, ?);"
        params =  (hospital_name, bed_count)
        cursor.execute(query,params)
    connection.commit()
    connection.close()

def insertDoctors(doctors):
    connection = getInstance()
    cursor = connection.cursor()
    for doctor_name, hospital_id, date_joined, speciality, salary, experience in doctors:
        query = "INSERT INTO doctor(doctor_name, hospital_id, date_joined, speciality, salary, experience) VALUES(?,?,?,?,?,?);"
        params =  (doctor_name, hospital_id, date_joined, speciality, salary, experience)
        cursor.execute(query,params)
    connection.commit()
    connection.close()

def getDataOfHospital(): 
    connection = getInstance()
    cursor = connection.execute('SELECT * FROM hospital')
    hospitals = cursor.fetchall()
    connection.close()
    return hospitals

def getDataOfDoctors():
    connection = getInstance()
    cursor = connection.execute('SELECT d.doctor_name, h.hospital_name, d.date_joined, d.speciality, d.salary, d.experience  FROM doctor d INNER JOIN hospital h ON h.hospital_id = d.hospital_id')
    doctors = cursor.fetchall()
    connection.close()
    return doctors

def showRecords(records):
    for record in records:
        print(record)

# file manipulation
def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

def readCSVFile(fileName):
    records = []
    with open(fileName, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                records.append(row)
    return records


createTable()

hospitals = readCSVFile(getCurrentDirname()+'\hospital.csv')
doctors = readCSVFile(getCurrentDirname()+'\doctor.csv')

insertHospitals(hospitals)
insertDoctors(doctors)

print("======= Hospital  ========")
hospitals = getDataOfHospital()
showRecords(hospitals)

print("\n======= DOCTORS  ========")
doctors = getDataOfDoctors()
showRecords(doctors)
