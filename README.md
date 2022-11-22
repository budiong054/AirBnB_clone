# AIRBNB CONSOLE
---
<img src="/images/console.png" border="0">
This project is the first step towards building a full web application: the AirBnB clone.

The console or command interpreter create the data model and allows create, update, destroy, store and persist objects to a file (JSON file). This console will be a tool to validate this storage engine.

## Table of Contents
---
* Objetives
* Requeriments
* Installation and execution
* Console commands
* Tests
* Development environment
* Authors

## Objectives
---
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Requeriments 📋
---
Airbnb was built and tested in Ubuntu 14.04 LTS via Vagrant in VirtualBox. Programming languaje python3

## Installation and execution 🔧
---
* Clone the repository
> $ git clone https://github.com/budiong054/AirBnB_clone.git
* Move in to the directory
> $ cd AirBnB_clone
* Execute the console file
> /AirBnB_clone$ ./console.py


## Console commands
---
The commands available for this command interpreter are:

| Name       | Description   |
| ---------- | ------------- |
|**create*| Creates a new instance of the class passed by argument.|
|*show*| Prints the string representation of an instance.                                        |
|**destroy*| Deletes an instance that was already created.                                           |
|*all*| Prints string representation of all instances or of all instances of a specified class. |
|**update*| Updates an instance attribute if exists otherwise create it.                            |
|*help*| Show all commands or display information about a specific command.|
|*quit*| Exit the console.|
|*EOF*| Exit the console.|

**create, destroy and update commands save changes into a JSON file.*

### Commands usage: 


| *Command*  | *Usage* |
| -------- | -------- |
|*create*  | ***create*** <class_name>|
|*show*    | ***show*** <class_name> <object_id> **;** <class_name>.***show***(<object_id>)()|
|*destroy* | ***destroy*** <class_name> <object_id **;** <class_name>.***destroy***(<object_id>)()|
| *all*    | **all** <class_name> **;** <class_name>.**all**()|
| *update* | ***update*** <class_name> <object_id> <attribute name> "<attribute value>" **;** <class name>.***update***(<object_id>, <attribute name>, <attribute value>) **;** <class name>.***update***(<object_id>, <dictionary representation>)|
| *help*   | ***help*** **;** ***help*** <command_name>|
| *quit*   | ***quit*** |
| *EOF*    | ***EOF*** **;** (ctrl + d)|

## Tests ⚙️
---

### Interactive Mode ⌨️

#### Example 1: Using create, count and all commands
```
solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$ ./console.py 
(hbnb) all
[]
(hbnb) create Place
492f60f3-ff1e-43c7-bb11-f8407b04dd59
(hbnb) create BaseModel
99f01e9a-99c0-42af-8c10-c35cadee1d8f
(hbnb) BaseModel.count()
1
(hbnb) all
["[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530)}", "[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236)}"]
(hbnb)
```

#### Example 2: Using basic update with an Id and show command

```
(hbnb) update BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f first_name "Betty"
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Betty'}
(hbnb) Place.update("492f60f3-ff1e-43c7-bb11-f8407b04dd59", "first_name", "John")
(hbnb) show Place 492f60f3-ff1e-43c7-bb11-f8407b04dd59
[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}
```

#### Example 3: Using update with a dictionary

```
(hbnb) BaseModel.update("99f01e9a-99c0-42af-8c10-c35cadee1d8f", {'first_name': "Petter", "age": 45})
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Petter', 'age': '45'}
```
#### Example 4: Using destroy and count command
```
(hbnb) BaseModel.destroy("99f01e9a-99c0-42af-8c10-c35cadee1d8f")
(hbnb) all
["[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}"]
(hbnb) BaseModel.count()
0
(hbnb) quit
solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$
```

### Non - Interactive Mode ⌨️
```
solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$ echo "create User" | ./console.py
(hbnb) 55b76419-6009-4b36-b88a-7c2930283f4a
solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$ echo "show User 55b76419-6009-4b36-b88a-7c2930283f4a" | ./console.py
(hbnb) [User] (55b76419-6009-4b36-b88a-7c2930283f4a) {'id': '55b76419-6009-4b36-b88a-7c2930283f4a', 'created_at': datetime.datetime(2020, 7, 1, 12, 37, 15, 575191), 'updated_at': datetime.datetime(2020, 7, 1, 12, 37, 15, 575237)}
```

## Development environment 🛠️
This project has been tested on Ubuntu 14.06.6 LTS

* Programming languaje Python
* The tests are carried out in virtualBox
* Development environment manager vagrant
* Style guidelines: PEP 8 (version 1.7) || Google Style Python Docstrings

## AUTHORS✒️
---

* [Blessing Udiong](https://github.com/budiong054) Software Engineering student at [ALX Africa](https://www.alxafrica.com/)
* [Muyiwa Fatunsin](https://github.com/phatlines) - Software Engineering student at [ALX Africa](https://www.alxafrica.com/)
