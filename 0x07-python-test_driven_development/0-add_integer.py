#!/usr/bin/python3

def add_integer(a, b=98):
    ''' This a function that accepts two arguments and sum them '''

    if isinstance (a, float) or isinstance (b, float):
        ''' This casts floats into integers '''
        a = int(a)
        b = int(b)
    
    if not isinstance (a, int):
        ''' This checks and accepts only integers as arguments '''
        raise TypeError ("a must be an integer")
    elif not isinstance (b, int):
        raise TypeError ("b must be an integer")
    
    return a + b
    ''' Returns the sum of a and b '''
