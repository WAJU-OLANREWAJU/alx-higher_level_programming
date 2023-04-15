#!/usr/bin/python3

'''
class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        self.sort()
        print(self)
        '''
class MyList(list):

    ''' My list class '''

    def print_sorted(self):

        ''' Modification to sort the list '''
        
        original_list = self.copy()  # Create a copy of the original list
        sorted_list = sorted(original_list)  # Sort the copy
        print(original_list)
        print(sorted_list)
        print(self)
