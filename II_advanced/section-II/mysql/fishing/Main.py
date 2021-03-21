import mysql.connector
import os
import csv

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_DATABASE = 'fishing'

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
        "CREATE TABLE IF NOT EXISTS boat(\
            boat_id INT AUTO_INCREMENT PRIMARY KEY,\
            boat_name VARCHAR(50),\
            boat_size INT,\
            boat_lenght INT,\
            station_id INT,\
            boat_capacity INT,\
            fishing TINYINT(1))"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Fisher(\
            fisherman_id INT AUTO_INCREMENT PRIMARY KEY,\
            fisher_name VARCHAR(50),\
            boat_id INT,\
            phone_number DOUBLE,\
            email VARCHAR(50),\
            age INT,\
            UNIQUE KEY unique_email (email))"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Owner(\
            owner_id INT AUTO_INCREMENT PRIMARY KEY,\
            owner_name VARCHAR(255),\
            boat_id INT,\
            phone_number INT,\
            email VARCHAR(100),\
            UNIQUE KEY unique_email (email))"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS station(\
            station_id INT AUTO_INCREMENT PRIMARY KEY,\
            station_name VARCHAR(100),\
            address VARCHAR(200))"
        )

def insertBoat(boats):
    connection = getInstance()
    cursor = connection.cursor()
    for boat in boats:
        query = "INSERT INTO boat(boat_name,boat_size,boat_lenght,station_id,boat_capacity,fishing) VALUES (%s,%s,%s,%s,%s,%s);"
        params =  (
            boat[0],
            boat[1],
            boat[2],
            boat[3],
            boat[4],
            boat[5],
        )
        cursor.execute(query,params)
    connection.commit()
    connection.close()
           
def insertFisher(fishers):
    connection = getInstance()
    cursor = connection.cursor()
    for fisher in fishers:
        query = "INSERT INTO Fisher(fisher_name, boat_id, phone_number, email, age)\
        VALUES (%s,%s,%s,%s,%s);"
        params =  (
            fisher[0],
            fisher[1],
            fisher[2],
            fisher[3],
            fisher[4],
        )
        cursor.execute(query,params)
    connection.commit()
    connection.close()

def insertOwner(owners):
    connection = getInstance()
    cursor = connection.cursor()
    for owner in owners:
        query = "INSERT INTO Owner(owner_name,boat_id,phone_number,email)\
        VALUES (%s,%s,%s,%s);"
        params =  (
            owner[0],
            owner[1],
            owner[2],
            owner[3],
        )        
    cursor.execute(query,params)
    connection.commit()
    connection.close()

def insertStation(stations):
    connection = getInstance()
    cursor = connection.cursor()
    for station in stations:
        query = "INSERT INTO station(station_name,address)\
        VALUES (%s,%s);"
        params =  (
            station[0],
            station[1],
        )        
    cursor.execute(query,params)
    connection.commit()
    connection.close()

def getDataOfStation():
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM station')
    records = cursor.fetchall()
    connection.close()
    return records

def getDataOfBoat():
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT b.boat_name,s.station_name\
         FROM boat b INNER JOIN station s ON b.station_id = s.station_id')
    records = cursor.fetchall()
    connection.close()
    return records

def getDataOfFisher():
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT f.fisher_name, b.boat_name\
         FROM fisher f INNER JOIN boat b ON  f.boat_id = b.boat_id')
    records = cursor.fetchall()
    connection.close()
    return records

def getDataOfOwner():
    connection = getInstance()
    cursor = connection.cursor()
    cursor.execute('SELECT o.owner_name, b.boat_name\
         FROM owner o INNER JOIN boat b ON  o.boat_id = b.boat_id')
    records = cursor.fetchall()
    connection.close()
    return records


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

def showRecords(records):
    for record in records:
        print(record)

def main():
    createDatabase()
    createTable()

    stations = readCSVFile(getCurrentDirname()+'\\station.csv')
    boats = readCSVFile(getCurrentDirname()+'\\boat.csv')
    owners = readCSVFile(getCurrentDirname()+'\\owner.csv')
    fishers = readCSVFile(getCurrentDirname()+'\\fisher.csv')

    insertStation(stations)
    insertBoat(boats)
    insertFisher(fishers)
    insertOwner(owners)

    print("======== Boat =========")
    showRecords(getDataOfBoat())
    print("======== Fisher =========")
    showRecords(getDataOfFisher())
    print("======== Owner =========")
    showRecords(getDataOfOwner())
    print("======== Station =========")
    showRecords(getDataOfStation())
main()

