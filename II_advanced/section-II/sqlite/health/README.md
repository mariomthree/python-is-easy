# SQLite Exercise

## Description of the exercise

Using SQLite and python create two `hospital` and` doctor` tables with the following structure.

`hospital`                  
-   hospital_id             
-   hospital_name
-   bed_count 

`doctor` 
-   doctor_id
-   doctor_name
-   hospital_id
-   date_joined
-   speciality
-   salary REAL
-   experience

Create two documents with `hospital.csv` and` doctor.csv` records and insert them in the database.

## Estrutura dos documentos csv
### hospital.csv

|  hospital_name| bed_count |
| ------------- | ------------- |
| HCM | 2500 |
| HCZ | 5600  |
| HCT | 2500 |
| HCG | 4500  |

<br>

### doctor.csv

| doctor_name | hospital_id | date_joined | speciality | salary | experience |
| ----------- | ----------- | ----------- | ---------- | ------ | ---------- |
| Mario|2|2000-01-21|AC|2000|BBB|
| Jonh|6|2002-01-21|AO|3000|DDD |
| Ana|4|1990-01-21|AL|1200|BBB |

<br>
<br>

# Exercise Resolution

## Prerequisites
- Python (https://www.python.org/downloads/)
- Python interpreter

There are other alternatives you can use `VS Code`,` Sublime Text` but you must install the extension or the package to program in `Python`.

<br>

## Description of the methods
Description of the methods of the `Main.py` file

### getInstance() 
- Creates a new connection in the database
### createTable() 
- Creates the hospital and doctor tables
### insertHospitals() 
- Insert records in the hospital table
### insertDoctors() 
- Insert records in the doctor table
### getDataOfHospital() 
- returns records from the hospital table
### getDataOfDoctors() 
- returns records from the doctor table
### showRecords() 
- shows registers using the for cycle
### getCurrentDirname() 
- returns the user's current directory
### readCSVFile() 
- reads a csv file

<br>

## Como executar o projecto pela primeira vez
First, it is necessary to have the files `hospital.csv` and` doctor.csv`, and finally follow the code below.

```py
# create all tables requirements
createTable()

# get all records of csv file
hospitals = readCSVFile(getCurrentDirname()+'\hospital.csv')
doctors = readCSVFile(getCurrentDirname()+'\doctor.csv')

# insert in database, first insert hospital and then doctors
insertHospitals(hospitals)
insertDoctors(doctors)

# show records
print("======= Hospital  ========")
hospitals = getDataOfHospital()
showRecords(hospitals)

print("\n======= DOCTORS  ========")
doctors = getDataOfDoctors()
showRecords(doctors)
```

