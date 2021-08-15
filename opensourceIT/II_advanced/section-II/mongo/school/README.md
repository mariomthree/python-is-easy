# Mongo Exercise

## Description of the exercise

Using MongoDB and python read the document `data.csv` and display in html.

## Structure of CSV documents

| county|school_type|employment_body|teachers|centroid|year
| ---------------|-------|-------|----|----------|------------|---------------------
| Baringo        |Public |TSC    |1172|"(0.669252, 35.946465)"|12/31/2014 12:00:00 AM
| Bomet          |Public |TSC    |1379|"(-0.726295, 35.298598)"|12/31/2014 12:00:00 AM
| Bungoma        |Public |TSC    |2946|"(0.749285, 34.640461)"|12/31/2014 12:00:00 AM
| Busia          |Public |TSC    |1182|"(0.387444, 34.193631)"|12/31/2014 12:00:00 AM
| Elgeyo Marakwet|Public |TSC    |1087|"(0.802219, 35.536563)"|12/31/2014 12:00:00 AM
| Embu           |Public |TSC    |1491|"(-0.603974, 37.626501)"|12/31/2014 12:00:00 AM
| Garissa        |Public |TSC    |347|"(-0.48891, 40.199279)"|12/31/2014 12:00:

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

### insertSchools() 
- Insert records in the school collection
### getDataOfSchool() 
- returns records from the schooll collection
### getCurrentDirname() 
- returns the user's current directory
### listToStr() 
- Convert list to string
### createHtmlContents()
- create all html contents
### createHtmlFile()
- create the html file


<br>

## How to run the project for the first time
```py

# read csv file and convert to dictonary
dataframe = pandas.read_csv(getCurrentDirname()+'/data.csv')
schools = dataframe.to_dict(orient='records')

# insert all records of school in collection 
insertSchools(schools)

# read the collection
schools =  getDataOfSchool()

# create file and contents for page
filename = 'index.html'
contents = createHtmlContents(schools)
createHtmlFile(contents, filename)    

# open html file in your browser 
webbrowser.open(filename)
```

## Demo
<img src="demo.gif">
