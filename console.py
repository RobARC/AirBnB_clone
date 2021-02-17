#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import json
import re
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class for the command interpreter"""

    prompt = '(hbnb) '

    __classes = {
       "BaseModel",
       "User",
       "State",
       "City",
       "Amenity",
       "Place",
       "Review",
       ""
       }

    def emptyline(self):
        """Do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit from prompt"""

        return True

    def do_EOF(self, arg):
        """EOF is a signal to exit the program"""

        print("")
        return True

    def do_create(self, arg):
        """create a new instance"""

        arg1 = arg.split()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, arg):
        """show name class"""

        arg1 = arg.split()
        obje = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        else:
            if arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                if len(arg1) == 1:
                    print("** instance id missing **")
        if len(arg1) == 2:
            if "{}.{}".format(arg1[0], arg1[1]) not in obje:
                print("** no instance found **")
            else:
                print(obje["{}.{}".format(arg1[0], arg1[1])])

    def do_destroy(self, arg):
        """destroy an instance"""

        arg1 = arg.split()
        obje = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        else:
            if arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                if len(arg1) == 1:
                    print("** instance id missing **")
        if len(arg1) == 2:
            if "{}.{}".format(arg1[0], arg1[1]) not in obje.keys():
                print("** no instance found **")
            else:
                del obje["{}.{}".format(arg1[0], arg1[1])]
                storage.save()

    def do_all(self, arg):
        """print all string representation of all instances
        based or not on the class name
        """
        arg1 = arg.split()
        if arg == "" or arg1[0] in HBNBCommand.__classes:
            obj = storage.all()
            objlist = []
            for k, v in obj.items():
                if arg in k:
                    objlist.append(v.__str__())
            print(objlist)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update class"""

        arg1 = arg.split()
        obj = storage.all()
        new = None

        if len(arg1) == 0:
            print("** class name missing **")
            return False
        if arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg1) == 1:
            print("** instance id missing**")
            return False
        if "{}.{}".format(arg1[0], arg1[1]) not in obj.keys():
            print("** no instance found **")
            return False
        if len(arg1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg1) >= 3:
            try:
                search = arg1[0]+"."+arg1[1]
                for key, value in obj.items():
                    if search == key:
                        new = value
                setattr(new, arg1[2], arg1[3])
                new.save()

            except NameError:
                print("** value missing **")
                return False

if __name__ == "__main__":
    """Mai Function"""
HBNBCommand().cmdloop()
