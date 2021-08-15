# MySQL Exercise

## Description of the exercise

Using MySQL and python create 4 tables `Fisher`, `Boat`, `Owner` and `Station` with the following structure.

`Boat`
- boat_Id (Unique)
- boat_Name
- boat_size in tonnes
- boat_length
- station_id
- boat_capacity in number of people 
- fishing (Yes/No)

`Fisher`
- fisher_id (Unique)
- fisher_names
- boat_id 
- phone_number
- email_address
- Age

`Owner`
- owner_id (Unique)
- owner_name
- boat_id 
- phone_number
- owner_email

`Station`
- station_id (Unique)
- station_name
- Address

Create `csv file` for the `fisher`, `boat`, `owner`  and `station` insert the records of the documents in the database.


# Exercise Resolution

## Prerequisites
- Python (https://www.python.org/downloads/)
- Python interpreter
    - PyCharm (https://www.jetbrains.com/pycharm/download/)
    - Anaconda (https://www.anaconda.com/)
    - Jupyter (https://jupyter.org/install)

  There are other alternatives you can use `VS Code`,` Sublime Text` but you must install the extension or the package to program in `Python`.
- MySQL (https://www.mysql.com/downloads/)

<br>

## Description of the methods
Description of the methods of the `Main.py` file

### getInstance() 
- Creates a new connection in the database
### createTable() 
- Creates the hospital and doctor tables
### insertStation() 
- Insert records in the station table
### insertFisher()
- Insert records in the fisher table
### insertBoat()
- Insert records in the boat table
### insertOwner()
- Insert records in the owner table
### getDataOfStation() 
- returns records from the station table
### getDataOfFisher() 
- returns records from the fisher table
### getDataOfBoat() 
- returns records from the boat table
### getDataOfOwner() 
- returns records from the owner table
### showRecords() 
- shows registers using the for cycle
### getCurrentDirname() 
- returns the user's current directory
### readCSVFile() 
- reads a csv file

<br>

## How to run the project for the first time
First, it is necessary to have the files `college`, `Student` and `Teacher`, and finally follow the code below.

```py

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
```
