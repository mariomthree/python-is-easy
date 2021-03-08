# Python

## Python File Processing & Pickling

`Python` file handling also referred to as File Input and Output I/O.
It is a requirement to work with files for either writing to a file or read data from a file.

In Python, file processing takes place in the following order.
-   Open a file that returns a filehandle.
-   Use the handle to perform read or write action.
-   Close the filehandle.

### Open a file in Python

To read or write to a file, we need to open it first.
To open a file in Python, we use its built-in `open()` function. This function returns a file object, i.e., a handle. 

There are four different methods (modes) for opening a file:

-   "r" - Read - Default value. Opens a file for reading, error if the file does not exist
-   "a" - Append - Opens a file for appending, creates the file if it does not exist
-   "w" - Write - Opens a file for writing, creates the file if it does not exist
-   "x" - Create - Creates the specified file, returns an error if the file exists

In addition we can specify if the file should be handled as binary or text mode

-   "t" - Text - Default value. Text mode
-   "b" - Binary - Binary mode (e.g. images)

## Operations on a File in Python

The operations performed on a file are called the file operation or processing. Following is the list of operations that can be applied on a file in python.

1.	Opening or Creating a File
2.	Writing to a File
3.	Reading from a File
4.	Closing a File
5.	Renaming a File
6.	Deleting a File

## Files Types in Python

The in-built methods in Python can handle two major types of files. The types are text files(`.txt`) and binary files(`.bin`).

-   `Text files` are used to store human readable information.
-   `Binary files` contain computer readable information that are written using binary digits 0s and 1s.

The file processing in python is done by two different types of approaches. 

a) One is processing the content in the file. 
b) Two is processing the directory. 

The first one can be done by the built in functions. The second one can be processed by the `os` module methods.

## Opening or Creating a New File in Python

The method open() is used to open an existing file or create a new file. If the complete directory is not given then the file will be created in the directory in which the Python file is stored.

Syntax: 
```
file_object = open( file_name, "Access Mode", Buffering )
```

Below are the parameter details.

<access_mode> - The file opening mode, e.g., read, write, append, etc. It’s an optional parameter. By default, it is set to read-only <r>. 

<buffering> - The default value is 0, which means buffering won’t happen. If the value is 1, then line buffering will take place while accessing the file. If it’s higher than 1, then the buffering action will run as per the buffer size. In the case of a negative value, the default behavior is considered.

<file_name> - The name of the file you want to access.

## File Open Modes

<r>	    It opens a file in read-only mode while the file offset stays at the root.
<rb>	It opens a file in (binary + read-only) modes. And the offset remains at the root level.
<r+>	It opens the file in both (read + write) modes while the file offset is again at the root level.
<rb+>	It opens the file in (read + write + binary) modes. The file offset is again at the root level.
<w>	    If the file already exists, then it’ll get overwritten. It’ll create a new file if the same doesn’t exist.
<wb>	Use it to open a file for writing in binary format.
<w+>	It opens a file in both (read + write) modes. 
<wb+>	It opens a file in (read + write + binary) modes.
<a>	    It opens the file in append mode.
<ab>	It opens a file in (append + binary) modes. 
<a+>	It opens a file in (append + read) modes. 
<ab+>	It opens a file in (append + read + binary) modes. 

`examples:`
```
fileText = open("app.txt", "w")
fileText.write("Hello World")
fileText.close

fileText = open('app.txt', 'r')
fileContent = fileText.read()
print(fileContent) # Hello World
fileText.close()

   
fileObject = open("app2.log", "wb")
fileObject.name()
fileObject.mode()
fileObject.closed()

try:
   fileObject = open('app.log', encoding = 'utf-8')
   #do operations
finally:
   fileObject.close()
```
Another way to close a file is by using the WITH clause. It ensures that the file gets closed when the block inside the WITH clause executes.

`example:`
```
with open('/content/presidentsOfMozambique.txt', 'w') as w:
    w.write("Samora Machel")
    w.write("Joaquim Chissano")

with open('/content/presidentsOfMozambique.txt', 'r') as r:
    print(r.read())
```

## Pickle Module in Python

The purpose of pickling is to translate data into a format that can be transferred from RAM to disk. The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

`Warning`: The pickle module is not secure. Only unpickle data you trust. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Never unpickle data that could have come from an untrusted source, or that could have been tampered with.

### Storing data with pickle

You can pickle objects with the following data types:
-   Booleans
-	Integers
-	Floats
-	Complex numbers
-	(normal and Unicode) Strings
-	Tuples
-	Lists
-	Sets
-	Dictionaries

## Pickling files

To use pickle, start by importing it in Python.

`import pickle`

Example pickling a simple dictionary. 

```
pets_dict = { 'Bob': 3, 'Jimmy': 2, 'Laika': 3, 'Jimmy': 10, 'Jack': 3, 'Stella': 3, 'Nzinga': 7 }
```

To pickle this dictionary, you first need to specify the name of the file you will write it to, which is pets in this case.
Note that the file does not have an extension.
To open the file for writing, simply we use the open() function. The first argument should be the name of our file. The second argument is 'wb'. The w means that we'll be writing to the file, and b refers to binary mode. This means that the data will be written in the form of byte objects.

```
filename = 'pets'
outfile = open(filename, 'wb')
```

Once the file is opened for writing, we can use pickle.dump(), which takes two arguments: the object we want to pickle and the file to which the object has to be saved. In this case, the former will be pets_dict, while the latter will be outfile.

```
pickle.dump(pets_dict, outfile)
outfile.close()
```
### Unpickling files

We'll be reading a binary file. Assign this to infile. Next, we use pickle.load(), with infile as argument, and assign it to new_dict. The contents of the file are now assigned to this new variable. Again, we'll need to close the file at the end of the process.

```
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
```

### Compressing pickle files

If we’re saving a large dataset and our pickled file takes up a lot of space, we may want to compress it. This can be done using bzip2 or gzip. They both compress files, but bzip2 is a bit slower. gzip, however, produces files about twice as large as bzip2. We'll be using bzip2 in this lesson.

```
import bz2
import pickle

serialized_file = bz2.BZ2File('smallerfile', 'w')
pickle.dump(pets_dict, serialized_file)
```

### Unpickling Python 2 objects in Python 3

We may sometimes come across objects that were pickled in Python 2 while running Python 3. This can be a hassle to unpickle.
We could either unpickle it by running Python 2, or do it in Python 3 with encoding='latin1' in the load() function.

```
infile = open(filename,'rb')
new_dict = pickle.load(infile, encoding='latin1')
```

This will not work if your objects contain NumPy arrays. In that case, you could also try using encoding='bytes':

```
infile = open(filename,'rb')
new_dict = pickle.load(infile, encoding='bytes')
```
```
import pickle

pets_dict = { 'Bob': 3, 'Jimmy': 2, 'Laika': 3, 'Tobi': 10, 'Jack': 3, 'Stella': 3, 'Nzinga': 7 }
#Below code will save the pickle file for us, now we need to cover how to access the pickled file:
pickle_output = open("dict.pickle","wb")
pickle.dump(pets_dict, pickle_output)
pickle_output.close()

#Open the pickle file
#Use pickle.load() to load it to a var.
pickle_input = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)
#This shows that we've retained the dict data-type.
print(example_dict)
print(example_dict[‘Laika’])
```