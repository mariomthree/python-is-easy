import json
import pymongo
import csv, os
import env

client = pymongo.MongoClient(env.DB_HOST)
database = client[env.DATABASE_NAME]

hospitalCollection = database['hospitals']
doctorCollection  = database['doctors']
patientCollection  = database['patients']

def insertHospitals(hospitals):
    print(hospitalCollection)
    docs = hospitalCollection.insert_many(hospitals)
    return docs.inserted_ids

def insertDoctors(doctors):
    docs = doctorCollection.insert_many(doctors)
    return docs.inserted_ids

def insertPatients(patients):
    docs = patientCollection.insert_many(patients)
    return docs.inserted_ids

def getDataOfHospital(): 
    return hospitalCollection.find()

def getDataOfDoctors(): 
    return doctorCollection.find()

def getDataOfPatients(): 
    return patientCollection.find()

def showRecords(records):
    print(*records, sep='\n')

# file manipulation
def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

def readCSVFile(fileName):
    records = []
    with open(fileName, 'r') as fileReader:
        csvFile = csv.DictReader(fileReader)
        [records.append(record) for record in csvFile]
        return records
   
hospitals = readCSVFile(getCurrentDirname()+'/hospital.csv')
doctors = readCSVFile(getCurrentDirname()+'/doctor.csv')
patients = readCSVFile(getCurrentDirname()+'/patient.csv')

# insertHospitals(hospitals)
# insertDoctors(doctors)
# insertPatients(patients)

print("======= Hospital  ========")
hospitals = getDataOfHospital()
showRecords(hospitals)

print("\n======= DOCTORS  ========")
doctors = getDataOfDoctors()
showRecords(doctors)

print("\n======= PATIENTS  ========")
patients = getDataOfPatients()
showRecords(patients)