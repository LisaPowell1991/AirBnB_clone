#!/usr/bin/env python3
"""
Module for Console interaction
"""
import cmd  # type:ignore
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that implements command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command
        """
        raise SystemExit

    def do_EOF(self, line):
        """
        Quit command
        """
        raise SystemExit

    def do_help(self, line):
        """
        Help command
        """
        cmd.Cmd.do_help(self, line)

    def create_instance(self, class_name):
        """
        Create instance of class
        """
        try:
           cls = getattr(BaseModel, class_name)
           nw_inst = cls()
           nw_inst.save()
           print("{}".format(nw_inst.id))
        except AttributeError:
           print("** class doesn't exist **")

    def do_create(self, line):
        """
        Create command
        """
        if len(line.split()) < 1:
           print("** class name missing **")
        else:
           cls_name = line.split()[1]
           self.create_instance(cls_name)

    def show_instance(self, class_name, instance_id):
        """
        Show instance of class
        """
        try:
           cls = getattr(BaseModel, class_name)
           key = "{}.{}".format(class_name, instance_id)
           if key in storage.all():
              print(storage.all()[key])
           else:
              print("** no instance found **")
        except AttributeError:
           print("** class doesn't exist **")

    def do_show(self, line):
        """
        Show command
        """
        if len(line.split()) < 1:
           print("** class name missing **")
        else:
           class_name = line.split()[1]
           if len(line.split()) < 2:
              print("** instance id missing **")
           else:
              inst_id = line.split()[2]
              self.show_instance(class_name, inst_id)

    def del_instances(self, class_name, instance_id):
        """
        Delete instance of class
        """
        try:
           cls = getattr(BaseModel, class_name)
           key = "{}.{}".format(class_name, instance_id)
           if key in storage.all():
              del storage.all()[key]
              storage.save()
           else:
              print("** no instance found **")
        except AttributeError:
           print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Destroy command
        """
        if len(line.split()) < 1:
           print("** class name missing **")
        else:
           class_name = line.split()[1]
           if len(line.split()) < 2:
              print("** instance id missing **")
           else:
              inst_id = line.split()[2]
              self.del_instances(class_name, inst_id)

    def all_instances(self, class_name):
        """
        Show all instances of class
        """
        try:
           if not class_name:
              print([str(obj) for obj in storage.all().values()])
           else:
              cls = getattr(BaseModel, class_name)
              print(
                [str(obj) for key, obj in storage.all().items() if key.split(".")[0] == class_name]
              )
        except AttributeError:
           print("** class doesn't exist **")

    def do_all(self, line):
        """
        All command
        """
        args = line.split()
        if len(args) < 1:
           self.all_instances("")
        else:
           cls_name = args[1]
           self.all_instances(cls_name)

    def update_instance(self, class_name, id, attribute_name, attribute_value):
        """
        Update instance of class
        """
        try:
           cls = getattr(BaseModel, class_name)
           key = "{}.{}".format(class_name, id)
           if key in storage.all():
              instance = storage.all()[key]
              setattr(instance, attribute_name, attribute_value)
              instance.save()
           else:
              print("** no instance found **")
        except AttributeError:
           print("** class doesn't exist **")

    def do_update(self, line):
        """
        Update command
        """
        args = line.split()
        if len(args) < 1:
           print("** class name missing **")
        else:
           class_name = args[1]
           if len(args) < 2:
              print("** instance id missing **")
           elif len(args) < 3:
              print("** attribute name missing **")
           elif len(args) < 4:
              print("** value missing")
           else:
              instance_id = args[1]
              attribute_name = args[2]
              attribute_value = args[3]
              self.update_instance(
                class_name, instance_id, attribute_name, attribute_value)
             

    def emptyline(self):
        """
        Empty line instance
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()