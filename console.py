#!/usr/bin/python3
"""This defines the Airbnb console using cmd serving as frontend
    (for interaction)
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """This defines the Airbnb console inherited from the base class
        cmd.Cmd
    """
    prompt = '(hbnb) '
    __cls_names = ('BaseModel', 'User')

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to signal end of file
        """
        print()
        return True

    def do_create(self, cls):
        """Creates a new instance of `BaseModel` saves it and prints
            the `id`

        Args:
            cls(obj): The class name
        """
        if not cls:
            print("** class name missing **")
        elif cls not in self.__cls_names:
            print("** class doesn't exist **")
        else:
            new_model = eval(f'{cls}')()
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
            if cls not in self.__cls_names:
                print("** class doesn't exit **")
            elif not obj_id:
                print("** instance id missing **")
            else:
                key = f'{cls}.{obj_id}'
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
            if cls not in self.__cls_names:
                print("** class doesn't exit **")
            elif not obj_id:
                print("** instance id missing **")
            else:
                key = f'{cls}.{obj_id}'
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

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
            the class name
        """
        all_list = []
        if not arg:
            for key, obj in storage.all().items():
                all_list.append(str(obj))
            print(all_list)
        elif arg in self.__cls_names:
            for key, obj in storage.all().items():
                if key.split('.')[0] == arg:
                    all_list.append(str(obj))
            print(all_list)
        else:
            print("** class doesn't exit **")

    def help_all(self):
        """help text for <all> command
        """
        print("Usage:\n\tall <class name> or all\n"
              "Description:\n\tPrints all string representation of all"
              "instances based or not on the class name.\n"
              "e.g: (hbnb) all BaseModel or (hbnb) all\n")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file)
        """
        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
        elif arg_list[0] not in self.__cls_names:
            print("** class doesn't exit **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif f'{arg_list[0]}.{arg_list[1]}' not in storage.all().keys():
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            cls = arg_list[0]
            obj_id = arg_list[1]
            attr_name = arg_list[2]
            attr_val = arg_list[3].strip('\"')  # Remove the double quote
            obj = storage.all()[f'{cls}.{obj_id}']
            my_model = eval(f'{cls}')(**obj.to_dict())  # Creates new instance
            setattr(my_model, f'{attr_name}', attr_val)
            storage.new(my_model)
            my_model.save()

    def help_update(self):
        """help text for <update> command
        """
        print("Usage:\n\tupdate <class name> <id> <attribute name> \"<attribut"
              "e value>\"\nDescription:\n\tUpdates an instance based on the"
              "class name and id by adding or updating attribute (save the"
              " change into the JSON file).\n\nNote: Only one attribute can be"
              " updated at the time\n"
              "e.g: (hbnb) update BaseModel 1234-1234-1234 email "
              "\"aibnb@mail.com\"\n")

    def emptyline(self):
        """Execute nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
