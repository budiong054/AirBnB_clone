#!/usr/bin/python3
"""This defines the Airbnb console using cmd serving as frontend
    (for interaction)
"""
import cmd


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

    def emptyline(self):
        """Execute nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
