#!/usr/bin/python3

class MyList(list):
    ''' My list class that inherits from the base list '''
    
    def print_sorted(self):
        ''' This sorts the list in ascending order '''
        sorted_list = sorted(self)
        print(sorted_list)
