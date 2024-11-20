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
            return False, "** class doesn't exist **"

        # Checks for missing id
        if len(args) < 2:
            return False, "** instance id missing **"

        # Construct the key and get all objects
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()

        if key not in all_objs:
            return False, "** no instance found **"

        return True, key

    def do_update(self, arg):
        """
        Updates an instance by adding or updating an attribute
        Usage: update <class name> <id> <attribute name> '<attribute value>'
        """
        args = arg.split()

        # Validate class name and id
        is_valid, result = self.validate_class_and_id(args)

        if not is_valid:
            print(result)
            return

        # Check for missing attribute name
        if len(args) < 3:
            print("** attribute name missing **")
            return

        # Check for missing attribute value
        if len(args) < 4:
            print("** value missing **")
            return

        all_objs = storage.all()
        key = result
        instance = all_objs[key]
        protected_attr = ["id", "created_at", "updated_at"]

        attr_name, attr_value = args[2], args[3].strip('"')

        if attr_name in protected_attr:
            return

        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif attr_value.replace('.', '').isdigit() and attr_value.count('.') == 1:
                attr_value = float(attr_value)
        except ValueError:
            pass

        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_all(self, arg):
        """
        Prints string representation of all instances
        Usage: all [ClassName]
        """
        args = arg.split()
        all_objs = storage.all()
        obj_str_list = []

        if len(args) == 0:
            for obj in all_objs.values():
                obj_str_list.append(str(obj))
        else:
            if arg != "BaseModel":
                print("** class doesn't exist **")
                return

            for key, obj in all_objs.items():
                if key.startswith(f"{arg}."):
                    obj_str_list.append(str(obj))

        print(obj_str_list)
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Usage: destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        is_valid, result = self.validate_class_and_id(args)
        
        if not is_valid:
            print(result)
            return

        all_objs = storage.all()
        del all_objs[result]
        storage.save()

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()

        is_valid, result = self.validate_class_and_id(args)

        if not is_valid:
            print(result)
            return

        all_objs = storage.all()
        print(all_objs[result])

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
