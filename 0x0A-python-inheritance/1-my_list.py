#!/usr/bin/python3
"""This module inherits from the list class"""

class MyList(list):
    ''' My list class that inherits from the base list '''
    
    def print_sorted(self):
        ''' This sorts the list in ascending order '''
        sorted_list = sorted(self)
        print(sorted_list)
