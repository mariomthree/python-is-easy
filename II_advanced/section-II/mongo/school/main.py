import pandas
import os
import pymongo
import webbrowser
import env

client = pymongo.MongoClient(env.DB_HOST)

database = client[env.DATABASE_NAME]
schoolCollection = database['school']

def insertSchools(schools):
    docs = schoolCollection.insert_many(schools)
    return docs.inserted_ids

def getDataOfSchool(): 
    return schoolCollection.find()

def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

def  listToStr(elements):
    elementsStr = ' '.join([str(elem) for elem in elements])
    return elementsStr

def createHtmlContents(schools):

    tableBody= []
    for school in schools:
        tableData = f"<tr><td>{school['county']}</td><td>{school['school_type']}</td>\
                <td>{school['employment_body']}</td><td>{school['teachers']}</td>\
                <td>{school['centroid']}</td><td>{school['year']}</td>"
        tableBody.append(tableData)

    linkStyle = getCurrentDirname()+'/style.css'
    linkJs = getCurrentDirname()+'/main.js'
    

    contents = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>School</title>
        <meta charset="utf-8" />
        
        <link rel="stylesheet" href="{}">
        <link rel="stylesheet" href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">
        <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>
        <script src="{}"></script>
    </head>
        <body>
            <table id="table">
                <thead>
                    <tr>
                        <th>County</th><th>School Type</th><th>Employment Body</th>
                        <th>No. Of Teachers</th><th>County (centroid)</th><th>Year</th>
                    </tr>
                </thead>
                <tbody>
                    {}
                </tbody>
            </table>
        </body>
    </html>
    """.format(linkStyle,linkJs, listToStr(tableBody))
    return contents
    

def createHtmlFile(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

dataframe = pandas.read_csv(getCurrentDirname()+'/data.csv')
schools = dataframe.to_dict(orient='records')
insertSchools(schools)
schools =  getDataOfSchool()


filename = 'index.html'
contents = createHtmlContents(schools)
createHtmlFile(contents, filename)    

webbrowser.open(filename)

