#!/usr/bin/python3
"""This module serves as the entry point of the Abnb programme"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the programme"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the programme"""
        return True

    def emptyline(self):
        """Do nothing when an empty is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
