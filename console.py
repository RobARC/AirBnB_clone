#!/usr/bin/python3
import cmd
import re
from models import storage
from models.base_model import BaseModel

if __name__ == "__main__":
    class HBNBCommand(cmd.Cmd):
        prompt = "(hbnb)"
        __classes = {
                "BaseModel"
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
            if len(arg) == 0:
                print("** class name missing **")
            elif arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(arg1) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg1[0], arg1[1]) not in obje:
                print("** no instance found **")
            else:
                print(obje["{}.{}".format(arg1[0], arg1[1])])

        def do_destroy(self, arg):
            """destroy an instance"""
            arg1 = arg.split()
            obje = storage.all()
            if len(arg1) == 0:
                print("** class name missing **")
            elif arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(arg1) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg1[0], arg1[1]) not in obje.keys():
                print("** no instance found **")
            else:
                del obje["{}.{}".format(arg1[0], arg1[1])]
                storage.save()

        def do_all(self, arg):
            """print all string representation of all instances based or not on the class name"""
            arg1 = arg.split()
            if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                objlist = []
                for obj in storage.all().values():
                    if len(arg1) > 0 and arg[0] == obj.__class__.__name__:
                        objlist.append(obj.__str__())
                    elif len(arg1) == 0:
                        objlist.append(obj.__str__())
                print(objlist)

        def do_update(self, arg):
            """update class"""
            arg1 = arg.split()
            obj = storage.all()
            #print(type(obj))
            new = obj.copy()

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
                    type(eval(arg1[2]+" = "+arg1[3])) != dict
                    #eval('"arg1[1].arg1[2] = lambda: None"')
                    #setattr(arg1[1], arg1[2], arg1[3])
                    #print(arg1[2])
                    #for key, value in obj.items():
                    #    if arg1[0]+"."+arg1[1] == key:
                    #        print(eval("{}.id".format(arg1[1])))

                    
                except NameError:
                    print("** value missing **")
                    return False



    HBNBCommand().cmdloop()
