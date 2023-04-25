#!/usr/bin/python3
""" This is a module of a class of students that defines students by their
first_name, last_name, age. """

# if __name__ == "__main__":
#    class_to_json = __import__('8-class_to_json').class_to_json

class Student():
    """
    This class defines a student by first_name, last_name, age.
    """

    def __init__(self, first_name, last_name, age):
        """initializez a new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance.
        """
        return {
                'first_name' : self.first_name,
                'last_name' : self.last_name,
                'age' : self.age
                }


