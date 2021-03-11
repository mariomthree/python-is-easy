# MySQL Exercise

## Description of the exercise

Using MySQL and python create 3 tables `College`, `Student` and `Professor` with the following structure.

`College`                  
- College_id
- College_Name
- College_Address
- College_city
- College_country
    

`Professor` 
- teacher_id
- Teacher_Name
- teacher_Email
- College_id
- Date_joined
- Speciality
- Salary
- Experience

`Student` 
- Student_id
- Student_Name
- Student_Email
- College_id
- Date_joined
- Major_taken
- College_Level

Creates `csv` para` College` documents,` `Aluno` Professor` and performs reads and inserts in the database.


# Exercise Resolution

## Prerequisites
- Python (https://www.python.org/downloads/)
- Python interpreter

There are other alternatives you can use `VS Code`,` Sublime Text` but you must install the extension or the package to program in `Python`.
- MySQL (https://www.mysql.com/downloads/)

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

## How to run the project for the first time
First, it is necessary to have the files `hospital.csv` and` doctor.csv`, and finally follow the code below.

```py
# create database and table
createDatabase()
createTable()

# read csv files
colleges = readCSVFile(getCurrentDirname()+'\college.csv')
students = readCSVFile(getCurrentDirname()+'\student.csv')
teachers = readCSVFile(getCurrentDirname()+'\\teacher.csv')

# insert in database
insertCollege(colleges)
insertStudent(students)
insertTeacher(teachers)

# read and show data
print("======== Colleges =========")
showRecords(getDataOfColleges())
print("======== Teachers =========")
showRecords(getDataOfTeachers())
print("======== Students =========")
showRecords(getDataOfStudents())
```
