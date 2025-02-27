# homework make a calculator

#functions
# saves repition
# organize the code

# syntax
# def function_name(parameters):
#     # code block
#     return value

# def greet():
#     # block of code
#     print('hello person')
    
# # calling the funtion
# greet()

# def greet(name):

#     print(f'hi how are you {name}')
# greet('ali')
# greet('raza')
# greet('ahmed')

# def add_two(a, b):
#     c = a+b
#     return(c)
# add_two(10,30)
# print(add_two(10,30))




# def greet(name = 'ali'):
#     print(f'hi {name} how are you')

# greet('ahmed')
# greet()

# def add(a=10 , b = 20):
#     c = a + b
#     print(c)
# add()
# add(36,46)

# def tea():
#     print('Add some milk')
#     print('Add some tea')
#     print('Add some sugar')
#     print('apply heat')
#     return ('Tea is ready')
#     print('wash the cups') # function will end after return
# tea()
# print(tea())


# def tea():
#     print('Add some milk')
#     print('Add some tea')
#     print('Add some sugar')
#     print('apply heat')
    
# tea()
# print(tea())

import random

def roll_dice():
    return random.randint(1,6)
result = roll_dice()
print(result)