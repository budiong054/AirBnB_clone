#!/usr/bin/python3
"""This defines the Airbnb console using cmd serving as frontend
    (for interaction)
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This defines the Airbnb console inherited from the base class
        cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to signal end of file
        """
        return True

    def do_create(self, cls):
        """Creates a new instance of `BaseModel` saves it and prints
            the `id`

        Args:
            cls(obj:BaseModel): The class name
        """
        if not cls:
            print("** class name missing **")
        elif cls != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def help_create(self):
        """help text for the <create> command
        """
        print("Usage:\n\tcreate <class name>\n"
              "Description:\n\tCreates a new instance of BaseModel,"
              "saves it (to the JSON file) and prints the id\n"
              "e.g: (hbnb) create BaseModel\n")

    def do_show(self, args):
        """Prints the string representation of an instance based on the
            class name and id

        Args:
            cls(obj:BaseModel): The class name
            obj_id: The id of the instance
        """
        if args:
            line = self.parseline(args)
            cls = line[0]
            obj_id = line[1]
            if cls != 'BaseModel':
                print("** class doesn't exit **")
            elif not obj_id:
                print("** instance id missing **")
            else:
                key = f'BaseModel.{obj_id}'
                all_obj = storage.all()
                if key in all_obj.keys():
                    print(all_obj[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_show(self):
        """help text for <show> command
        """
        print("Usage:\n\tshow <class name> <id>\n"
              "Description:\n\tPrints the string representation of an"
              "instance based on the class name and id\n"
              "e.g: (hbnb) show BaseModel 1234-1234-1234\n")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the
            the change into the JSON file)

        Args:
            cls(obj:BaseModel): The class name
            obj_id: The id of the instance
        """
        if args:
            line = self.parseline(args)
            cls = line[0]
            obj_id = line[1]
            if cls != 'BaseModel':
                print("** class doesn't exit **")
            elif not obj_id:
                print("** instance id missing **")
            else:
                key = f'BaseModel.{obj_id}'
                all_obj = storage.all()
                if key in all_obj.keys():
                    del all_obj[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """help text for <destroy> command
        """
        print("Usage:\n\tdestroy <class name> <id>\n"
              "Description:\n\tDeletes an instance based on the class"
              "name and id (save the change into the JSON file).\n"
              "e.g: (hbnb) destroy BaseModel 1234-1234-1234\n")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on
            the class name
        """
        if not args or args == 'BaseModel':
            for key in storage.all().keys():
                print(storage.all()[key])
        else:
            print("** class doesn't exit **")

    def help_all(self):
        """help text for <all> command
        """
        print("Usage:\n\tall <class name> or all\n"
              "Description:\n\tPrints all string representation of all"
              "instances based or not on the class name.\n"
              "e.g: (hbnb) all BaseModel or (hbnb) all\n")

    def emptyline(self):
        """Execute nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
