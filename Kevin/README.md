# 0x00 AirBnB Clone
## Description of the Project
The AirBnB clone project is simply to create a replica of the AirBnB website on a server. The projects covers the fundamental concepts of the ALx higher level programmming track. In this first part the aim is to achieve the following learning objectives:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

The complete web application would be composed by:
- A Command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Description of the Command interpreter
The Command interpreter is a custom shell console. In our case, we want to be able to manage the objects of the project. This means:
- Being able to create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object
   
### How to start it
In order to start running this project for testing or development purposes a good idea would be to clone this git repository from Github.

### How to use it
The console can be used in interactive mode like this:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
The console can also be used in non-interactive mode like this:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
### Examples