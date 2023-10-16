#!/usr/bin/python3
"""
A command-line interpreter for the HBNB project.
"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter. """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of a class.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the str representation of an instance.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        try:
            obj = storage.all()[f"{class_name}.{obj_id}"]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the
        class name and id.

        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        try:
            obj = storage.all()[f"{class_name}.{obj_id}"]
            del storage.all()[f"{class_name}.{obj_id}"]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Display all instances or all instances
        of a specific class.

        Usage: all or all<class_name>
        """
        objects = FileStorage.all(self)
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = arg
                print([str(obj) for obj in objects.value()
                      if obj.__class__.__name__ == class_name])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        Usage: update <class_name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        attr_name = args[2]
        attr_value = args[3]
        try:
            obj = storage.all()[f"{class_name}.{obj_id}"]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except KeyError:
            print("** no instance found **")

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """
        Exit the command interpreter.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the command interpreter at the end of file.
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
