# Description
-----
This clone of AirBnB is an application which use JSON to storage, and a back-end in Python.
In this app is used to save information that is displayed in the following points.
At the momment its only a back-end console
## Attributes
---
The Clone use the following attributes in the classes:
| Principal Classes | BaseModel | FileStorage|
|---|------|----|
|**Public Instance Attributes**|`id` `created_at` `update_at`||
|**Public Instance Methods**|`save` `to_dict`|`all` `new` `save` `reload`|

And after the class `BaseModel` exist another more clases which inherit from it

|Inherit from BaseModel| User | State | City | Amenity | Place | Review|
|---|---|---|---|---|---|---|
|**Public Class Attributes**| `email` `password` `first_name` `last_name` |`name`| `state_id` `name`|`name`|`city_id` `user_id` `name` `description` `number_rooms` `number_bathrooms` `max_guest` `price_by_night` `latitude` `longitude` `amenity_ids`| `place_id` `user_id` `text`|

# Console
---
The console is a command line interpreter that allows managing the back-end of the clone. It can be used to handle the classes and attributes of the app.

## Start using the console

the console has the following commands for handling information, once we run the `console.py` file.
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
```
First of all the command `exit` and `EOF` is the way to exit the console
```
$ ./console.py
(hbnb) quit 
$
```
`EOF` is the signal to exit the console (ctrl-D)
```
$ ./console.py
(hbnb) EOF

$
```
The `create` command create a new instance of a the class we pass to the prompt, once created the ID of the instance is saved in the file `file.json`
- usage: `create <class>`
```
$ ./console.py
(hbnb)create BaseModel
381c3fcb-3abd-435f-9cb4-f550a81bd600
(hbnb)quit
$cat file.json
{"BaseModel.381c3fcb-3abd-435f-9cb4-f550a81bd600": {"id": "381c3fcb-3abd-435f-9cb4-f550a81bd600", "created_at": "2021-02-16T14:17:47.130618", "update_at": "2021-02-16T14:17:47.130645", "__class__": "BaseModel"}}
```
with `show` command, the class and the instance `id`, the console will print the string representation of the instance.
- Usage: `show <class> <id>`
```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
`destroy` is to delete the class instance of the file based on the given `id`
-  Usage: `destroy <class> <id>`
```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```
with the command `all` the console will prints the string representation of all instance of the given class. If the class is not in the command line, the prompt will print all instance of all class
```
(hbnb)create BaseModel
974775a1-a5bd-4340-8696-f8618da1ae67
(hbnb)create BaseModel
1164624f-80a4-405b-9473-384d42cbd630
(hbnb)create BaseModel
81b08608-9aac-4d46-bb5b-2d1fe09cbe61
(hbnb)all BaseModel
["BaseModel] (974775a1-a5bd-4340-8696-f8618da1ae67) ({'id': '974775a1-a5bd-4340-8696-f8618da1ae67', 'created_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451911), 'update_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451918)})", "[BaseModel] (1164624f-80a4-405b-9473-384d42cbd630) ({'id': '1164624f-80a4-405b-9473-384d42cbd630', 'created_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451927), 'update_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451934)})", "[BaseModel] (81b08608-9aac-4d46-bb5b-2d1fe09cbe61) ({'id': '81b08608-9aac-4d46-bb5b-2d1fe09cbe61', 'created_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451942), 'update_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451947)})"]
(hbnb)create User
54b38608-3bac-3e56-ca7b-2d1fe09cbe61
(hbnb)all
["BaseModel] (974775a1-a5bd-4340-8696-f8618da1ae67) ({'id': '974775a1-a5bd-4340-8696-f8618da1ae67', 'created_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451911), 'update_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451918)})", "[BaseModel] (1164624f-80a4-405b-9473-384d42cbd630) ({'id': '1164624f-80a4-405b-9473-384d42cbd630', 'created_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451927), 'update_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451934)})", "[BaseModel] (81b08608-9aac-4d46-bb5b-2d1fe09cbe61) ({'id': '81b08608-9aac-4d46-bb5b-2d1fe09cbe61', 'created_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451942), 'update_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451947)})", "[User] (54b38608-3bac-3e56-ca7b-2d1fe09cbe61) ({'id': '54b38608-3bac-3e56-ca7b-2d1fe09cbe61', 'created_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451911), 'update_at': datetime.datetime(2021, 2, 16, 14, 32, 24, 451918)})"]
```
The command `update` updates the attributes passed of a class instances based in the given `id`.
- Usage: `update <class> <id> <attribute name> "<attribute value>"`
```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
