#!/usr/bin/python3
"""This module serves as the entry point of the Abnb programme"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand command interpreter"""

    prompt = "(hbnb) "

    @staticmethod
    def validate_class_and_id(args):
        """
        Validates class name and id for various commands

        Args:
            args (list): List of argumenenst from the command

        Returns:
            tuple: (is_valid, error_message)
            - is_valid: Bolean indicating validation is passed
            - error_message: String Erorr (None if no erro)
        """

        # Checks if class name is provided
        if len(args) == 0:
            return False, "** class name missing **"

        # Checks if class exist
        if args[0] != "BaseModel":
            return False, "** class dosen't exist **"

        # Checks for missing id
        if len(args) != 2:
            return False, "** instance id missing **"

        # Construct the key and get all objects
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()

        if key not in all_objs:
            return False, "** no instance found **"

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()

        is_valid, result = self.validate_class_and_id(args)

        if not is_valid:
            print(result)
            return

        print(all_objs[key])

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return

        new_model = BaseModel()
        new_model.save()
        print(new_model.id)

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
