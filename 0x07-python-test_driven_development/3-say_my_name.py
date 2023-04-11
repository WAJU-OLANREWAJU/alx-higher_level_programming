#!/usr/bin/python3
'''This function simply prints the names passed to the argument as first and last name '''

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        ''' checks if the first_name is a string '''
        raise TypeError("first_name must be a string$")
    elif not isinstance(last_name, str):
        ''' checks if the last_name is a string '''
        raise TypeError("last_name must be a string$")
    print("My name is {} " " {}$".format(first_name, last_name))
