# import random
# def guess_num(x):
#     random_num = random.randint(1,x)
#     guess = 0
#     while guess!= random_num:
#         guess = int(input('Guess a number: '))
#         if guess < random_num:
#             print('You are too low')
#         elif guess > random_num:
#             print('you are too high')
#         else:
#             print('perfect guess')
# guess_num(10)

#================================================================

# Write a Python program where the computer randomly selects a word 
# from a given list, and the user has to guess the word. The program should give hints:
# If the guessed word comes alphabetically before the correct word, print "Your guess
#  is too early in the dictionary!"
# If the guessed word comes alphabetically after the correct word, print "Your guess 
# is too late in the dictionary!"
# If the guess is correct, print "Congratulations! You guessed it right."
# Use the following word list:
# ["apple", "banana", "cherry", "grape", "mango", "orange", "strawberry"]


# import random

# def guess_num(x):
#     num = random.randint(1,x)
#     guess = 0
#     while guess != num:
#         guess = int(input('enter a number: '))
#         if guess < num:
#             print('your guess is too early')
#         elif guess > num:
#             print('your guess is too late')
#         else:
#             print('congratulations! you guessed it right')
# guess_num(10)

# import random

# def guess_names():
#     names = ['muktiar','hajesh','sohail','nisar','parvez']
#     name = random.choice(names)
#     guess = ''
#     while guess != name:
#         guess = input('write a name from :[mukhtiar,hajesh,sohail,nisar,parvez]\nhere: ')
#         if guess < name:
#             print('your guess is early')
#         elif guess > name:
#             print('your guess is late')
#         else:
#             print('congratulations! you guessed it right')
# guess_names()

#=======================================================================

import time

Time = time.time()
correct_Time = time.ctime(Time)
print(Time)
print(correct_Time)
