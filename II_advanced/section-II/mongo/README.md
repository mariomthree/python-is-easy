# Mongo

MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. 

You can download a free MongoDB database at https://www.mongodb.com.
Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.


## Install Mongo Driver

Python needs a MongoDB driver to access the MongoDB database.
We recommend that you use PIP to install "PyMongo".

```sh
$ python -m pip install pymongo
```

## Create Database

```py
import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

# check if exists
databases = mongoClient.list_database_names()
print(*databases, sep='\n')
```

## Python MongoDB Create Collection

`Note:` A collection in MongoDB is the same as a table in SQL databases.

## Creating a Collection
To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
MongoDB will create the collection if it does not exist.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]
```

## Python MongoDB Insert Document

`Note:` A document in MongoDB is the same as a record in SQL databases.

## Insert Into Collection
To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]
studentDict = { "name": "Mario", "address": "Costa do Sol 37" }

studentDoc = studentCollection.insert_one(studentDict)
print(studentDoc.inserted_id)
```

### Insert Multiple Documents

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]
studentList = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"}
]

studentDoc = studentCollection.insert_many(studentList)
print(studentDoc.inserted_ids)
```
### Insert Multiple Documents, with Specified IDs

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]
studentList = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"}
]

studentDoc = studentCollection.insert_many(studentList)
print(studentDoc.inserted_ids)
```

## Python MongoDB Find

`Note:` In MongoDB we use the find and findOne methods to find data in a collection.<br>
Just like the SELECT statement is used to find data in a table in a MySQL database.

### Find One

The find_one() method returns the first occurrence in the selection.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]
studentDoc = studentCollection.find_one()
print(studentDoc)
```

### Find All

The find() method returns all occurrences in the selection.

The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]
studentsDoc = studentCollection.find()
print(*studentsDoc, sep='\n')
```

### Return Only Some Fields

The second parameter of the find() method is an object describing which fields to include in the result.
This parameter is optional, and if omitted, all fields will be included in the result.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]

studentsDoc = studentCollection.find({},{ "_id": 0, "name": 1, "address": 1 })
#studentsDoc = studentCollection.find({},{"address": 0 })
#studentsDoc = studentCollection.find({},{"name": 1, "address": 0 })

print(*studentsDoc, sep='\n')
```

## Python MongoDB Query

### Filter the Result

When finding documents in a collection, you can filter the result by using a query object.
The first argument of the find() method is a query object, and is used to limit the search.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]

#Find document(s) with the address "Park Lane 38":
studentsDoc = studentCollection.find({"address": "Park Lane 38"})

print(*studentsDoc, sep='\n')
```
### Advanced Query

To make advanced queries you can use modifiers as values in the query object.
E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]

#Find document(s) with the address "Park Lane 38":
studentsDoc = studentCollection.find( { "address": { "$gt":"S" } } )

print(*studentsDoc, sep='\n')
```
## Python MongoDB Sort

Use the sort() method to sort the result in ascending or descending order.
The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]

#Sort the result alphabetically by name:
studentsDoc = studentCollection.find().sort("name") #ascending
studentsDoc = studentCollection.find().sort("name",1) #ascending
studentsDoc = studentCollection.find().sort("name",-1) #descending

print(*studentsDoc, sep='\n')
```

## Python MongoDB Delete Document

### Delete Document

To delete one document, we use the delete_one() method.
The first parameter of the delete_one() method is a query object defining which document to delete.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

studentCollection = database["students"]
studentsDoc = studentCollection.delete_one({ "address": "Mountain 21" }) 

print(*studentsDoc, sep='\n')
```

### Delete Many Documents

To delete more than one document, use the delete_many() method.
The first parameter of the delete_many() method is a query object defining which documents to delete.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

# delete all documents were the address starts with the letter S
studentCollection = database["students"]
studentsDoc = studentCollection.delete_many({ "name": {"$regex": "^S"} }) 

print(studentsDoc.deleted_count)
```

### Delete All Documents in a Collection

To delete all documents in a collection, pass an empty query object to the delete_many() method:

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

# Delete all documents in the "students" collection:
studentCollection = database["students"]
studentsDoc = studentCollection.delete_many({}) 

print(studentsDoc.deleted_count)
```
## Python MongoDB Drop Collection

### Delete Collection

You can delete a table, or collection as it is called in MongoDB, by using the drop() method.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

Delete the "customers" collection:
studentCollection = database["students"]
studentCollection.drop()
```
## Python MongoDB Update

### Update Collection

You can update a record, or document as it is called in MongoDB, by using the update_one() method.
The first parameter of the update_one() method is a query object defining which document to update.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

Delete the "customers" collection:
studentCollection = database["students"]

query = { "address": "Valley 345" }
newValues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(query, newValues)

studentsDoc = studentCollection.find()
print(*studentsDoc, sep='\n')
```

## Python MongoDB Limit

### Limit the Result

To limit the result in MongoDB, we use the limit() method.
The limit() method takes one parameter, a number defining how many documents to return.

```py
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongoClient["school"]

Delete the "customers" collection:
studentCollection = database["students"]

studentsDoc = studentCollection.find().limit(5)
print(*studentsDoc, sep='\n')
```

## Credits

w3schools
- <a href="https://www.w3schools.com/python/default.asp" target="_blank">Python Tutorial</a>
- <a href="https://www.w3schools.com/python/python_mongodb_getstarted.asp" target="_blank">Mongo Database</a>