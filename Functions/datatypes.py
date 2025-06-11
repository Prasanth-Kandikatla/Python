# Functions

print('Functions Module imported successfully')
list = ['a', 'ab', 'abc', 'abcd']
tp = (1, 2, 4, 5, 7) #Tuples are Immutable
dt = {'tall': 'Ajay', 'average': 'Prasanth', 'short': 'Ravi'} #Dictionaries are key value pairs

def loop_numbers():
    for i in enumerate(dt):
        print(i)

str = 'Functions String Imported'
loop_numbers()

import os

print(os.getcwd())