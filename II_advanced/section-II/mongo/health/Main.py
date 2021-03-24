import json
import pymongo
import csv, os
import env

client = pymongo.MongoClient(env.DB_HOST)
database = client[env.DATABASE_NAME]

hospitalCollection = database['hospitals']
doctorCollection  = database['doctors']

def insertHospitals(hospitals):
    print(hospitalCollection)
    docs = hospitalCollection.insert_many(hospitals)
    return docs.inserted_ids

def insertDoctors(doctors):
    docs = doctorCollection.insert_many(doctors)
    return docs.inserted_ids
    
def getDataOfHospital(): 
    return hospitalCollection.find()

def getDataOfDoctors(): 
    return doctorCollection.find()

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
   
#print(*readCSVFile(getCurrentDirname()+'/doctor.csv'), sep='\n')

hospitals = readCSVFile(getCurrentDirname()+'/hospital.csv')
doctors = readCSVFile(getCurrentDirname()+'/doctor.csv')

# insertHospitals(hospitals)
# insertDoctors(doctors)

print("======= Hospital  ========")
hospitals = getDataOfHospital()
showRecords(hospitals)

print("\n======= DOCTORS  ========")
doctors = getDataOfDoctors()
showRecords(doctors)