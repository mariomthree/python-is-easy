# Mongo Exercise

## Description of the exercise

Using MongoDB and python create two `hospital` and` doctor` tables with the following structure.

`hospital`                  
-   hospital_id             
-   hospital_name
-   bed_count 
-   address

`doctor` 
-   doctor_id
-   doctor_name
-   hospital_id
-   date_joined
-   speciality
-   salary REAL
-   experience

Create two documents with `hospital.csv` and` doctor.csv` records and insert them in the database.

## Structure of CSV documents
### hospital.csv

|  hospital_name| bed_count | address |
| ------------- | ------------- | ------------- |
| Hospital Central Maputo | 12000 | "Costa do Sol, 321" |
| Hospital Central Beira | 1200 | "Beira, 321" |
| Hospital Central Nampula | 6200 | "Nacala Porto, 221" |
| Hospital Central Zambezia | 4000 | "Mocuba, 121" |

<br>

### doctor.csv

| doctor_name | hospital_id | date_joined | speciality | salary | experience |
| ----------- | ----------- | ----------- | ---------- | ------ | ---------- |
| Mario|2|2000-01-21|AC|2000|2|
| Jonh|1|2002-01-21|AO|3000|3 |
| Ana|3|1990-01-21|AL|1200|4 |

<br>
<br>

# Exercise Resolution

## Prerequisites
- Python (https://www.python.org/downloads/)
- Python interpreter

There are other alternatives you can use `VS Code`,` Sublime Text` but you must install the extension or the package to program in `Python`.

## File `env.example` and `env.py`

To create the connection, create a new env.py file, copy the entire contents of env.example and place env.py.

<br>

## Description of the methods
Description of the methods of the `Main.py` file

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

## How to run the project for the first time
First, it is necessary to have the files `hospital.csv` and` doctor.csv`, and finally follow the code below.

```py

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
