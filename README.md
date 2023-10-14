# The AirBnB Clone Project

![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Project Description

The focus of this initial phase is to develop the backend of our Airbnb clone by using Python objects and a JSON file, then integrating it with a console application by using Python's cmd module.

## Description of the command interpreter:

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## How to Start:

To launch the command interpreter, simply run the main script of our project. This will initiate the console interface, ready for user input.

## How to Use:

The command interpreter employs a straightforward syntax. Users can enter commands along with any necessary arguments to execute specific actions. The interpreter will then process the input and carry out the requested operation.

## Execution:

Your console should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (almost like the Shell project in C)

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)


Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```

## Examples:

Some of the commands available are:

```
### - create (e.g. creating a new user):
> create User name="Alice" age=30
User created with ID 1
### - get (Retrieving data)
> get User 1
User ID: 1
Name: Alice
Age: 30
### - count (Count the number of objects of a specified type.)
> count User
Total Users: 3
### - update (updating attributes of an existing object.)
> update Place 2 name="New Place Name"
Place 2 attributes updated successfully.
### - destroy (Delete an object.)
> destroy User 3
User 3 has been deleted.
```
