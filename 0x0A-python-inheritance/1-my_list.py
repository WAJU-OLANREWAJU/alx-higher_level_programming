#!/usr/bin/python3


class MyList(list):
    ''' My list class '''

    def __init__(self, *args, **kwargs):
        ''' Modification that sorts the list '''
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        ''' this sorts '''
        self.sort()
        print(self)
