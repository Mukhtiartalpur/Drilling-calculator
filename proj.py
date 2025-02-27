#Guess the Number Game Python Project (computer)

# import random
# def game(x):
#     random_number = random.randint(0,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input('Guess a number: '))
#         if guess < random_number:
#             print(f'your guess is too low..!')
#         elif guess > random_number:
#             print(f'your guess is too high..!')
#         else:
#             print(f'Perferct guess: {random_number}')
# game(8)

#========================================================================================================
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

# Guess the Number Game Python Project (user)

# import random

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low,high)
#         else:
#             guess = low
#         feedback = input(f'is {guess} too high {h}, too low {l} or correct {c}....?')
#         if feedback == 'h':
#             high = guess - 1
#         elif guess == 'l':
#             low = guess + 1
#     print(f'computer guessed your number {guess} correctly.')
# computer_guess(10)

#===========================================================

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low  # could also be high b/c low = high
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1

#     print(f'Yay! The computer guessed your number, {guess}, correctly!')


#computer_guess(10)

#==================================================================================

# import random 
# def play():
#     user = input(" whats your choice 'r' for rock, 'p' for paper and 's' for scissor: ")
#     computer = random.choice(['r', 'p', 's'])
#     if user == computer:
#         return 'tie'
#     if is_win(user, computer):
#          return 'you won'
#     return  'you lost' 
# def is_win(player, opponent):
#     if (player == 'r' and opponent == 's') or  (player == 's' and opponent == 'p') \
#     or (player == 'p' and opponent == 'r'):
#         return True
# print(play())

# import random
# def play():
#     user = input(f's=sscissor\nr= rock\np=paper')
#     computer = random.choice(['r','s','p'])
#     if user == computer:
#         return 'tie'
#     elif is_win(user , computer):
#         return 'you won'
#     else:
#         return 'you lost'
# def is_win(player,opponent):
#     if (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's') \
#     or (player == 's' and opponent == 'p'):
#         return True
# print(play())
    
#=========================================================================================

# import random 
# def is_win(player, opponent):  
#     if (player == 'r' and opponent == 's') or \
#        (player == 's' and opponent == 'p') or \
#        (player == 'p' and opponent == 'r'):
#         return True
#     return False
# def play():
#     user = input("What's your choice? Type 'r' for Rock, 'p' for Paper, and 's' for Scissors: ")
#     computer = random.choice(['r', 'p', 's'])
#     if user == computer:
#         return "It's a Tie!"
#     if is_win(user, computer):  
#         return "You Won!"
#     return "You Lost!"
# print(play())

# import random
# def game(player , opponent):
#     if (player == 's' and opponent == 'p') or \
#        (player == 'p' and opponent == 'r') or \
#        (player == 'r' and opponent == 's') :
#        return True
#     return False
# def play(user , computer):
#     user = input('Enter s for scissors r for rocks p for paper:  ')
#     computer = random.choice(['p','r','s'])
#     if user == computer:
#         return 'tie'
#     if game(user, computer):
#         return 'you won'
#     return 'you lost'
# print(play()) 




# import random
# def game(player, opponent):
#     if (player == 's' and opponent == 'p') or \
#        (player == 'p' and opponent == 'r') or \
#        (player == 'r' and opponent == 's'):
#        return True
#     return False
# def play():
#     user = input("Enter 's' for scissors, 'r' for rock, 'p' for paper: ")  
#     computer = random.choice(['p', 'r', 's'])  
#     print(f"Computer chose: {computer}")  
#     if user == computer:
#         return "It's a tie!"
#     if game(user, computer):
#         return "You won!"
#     return "You lost!"
# print(play())

#=============================================================================
# import random
# words = ["PYTHON", "DEVELOPER", "COMPUTER", "PROGRAMMING", "LANGUAGE", "ALGORITHM"]
# lives_visual_dict = {
#     7: """
#         +---+
#         |   |
#             |
#             |
#             |
#             |
#       =========
#     """,
#     6: """
#         +---+
#         |   |
#         O   |
#             |
#             |
#             |
#       =========
#     """,
#     5: """
#         +---+
#         |   |
#         O   |
#         |   |
#             |
#             |
#       =========
#     """,
#     4: """
#         +---+
#         |   |
#         O   |
#        /|   |
#             |
#             |
#       =========
#     """,
#     3: """
#         +---+
#         |   |
#         O   |
#        /|\\  |
#             |
#             |
#       =========
#     """,
#     2: """
#         +---+
#         |   |
#         O   |
#        /|\\  |
#        /    |
#             |
#       =========
#     """,
#     1: """
#         +---+
#         |   |
#         O   |
#        /|\\  |
#        / \\  |
#             |
#       =========
#     """,
#     0: """
#         +---+
#         |   |
#         O   |
#        /|\\  |
#        / \\  |
#       =========
#       GAME OVER
#     """
# }

# import string
# def get_valid_word(words):
#     word = random.choice(words)  # randomly chooses something from the list
#     while '-' in word or ' ' in word:
#         word = random.choice(words)

#     return word.upper()


# def hangman():
#     word = get_valid_word(words)
#     word_letters = set(word)  # letters in the word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()  # what the user has guessed

#     lives = 7

#     # getting user input
#     while len(word_letters) > 0 and lives > 0:
#         # letters used
#         # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
#         print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

#         # what current word is (ie W - R D)
#         word_list = [letter if letter in used_letters else '-' for letter in word]
#         print(lives_visual_dict[lives])
#         print('Current word: ', ' '.join(word_list))

#         user_letter = input('Guess a letter: ').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#                 print('')

#             else:
#                 lives = lives - 1  # takes away a life if wrong
#                 print('\nYour letter,', user_letter, 'is not in the word.')

#         elif user_letter in used_letters:
#             print('\nYou have already used that letter. Guess another letter.')

#         else:
#             print('\nThat is not a valid letter.')

#     # gets here when len(word_letters) == 0 OR when lives == 0
#     if lives == 0:
#         print(lives_visual_dict[lives])
#         print('You died, sorry. The word was', word)
#     else:
#         print('YAY! You guessed the word', word, '!!')


# if __name__ == '__main__':
#     hangman()

#=========================================================

# import time
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
#     print('Timer completed!')
# t = input('Enter the time in seconds: ')
# countdown(int(t))  

#=======================================================================

# import time
# def countdown(t):
#     while t>0:
#         mins, secs = divmod(t, 60)
#         timer = f'{mins:02d}:{secs:02d}'
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
#     print('Timer completed!')
# t = input('Enter the time in seconds: ')
# countdown(int(t))

#=================================================


#import time

# def count(t):
#     while t > 0 :
#         min , sec = divmod(t, 60)
#         timer = f'{min: 02d}:{sec:02d}'
#         print(timer ,end = '\r' )
#         time.sleep(1)
#         t -= 1
# t = int(input('enter time: '))
# count(t)



#====================================================

# import random
# print('welcome to your password generator')
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW/=@#123456789'
# number = int(input('Enter the amount of password to generate: '))
# length = int(input('enter the length of the password:'))
# print('here are your passwords')
# for pwd in range(number):
#     passwords = ''
#     for c in range(length):
#         passwords += random.choice(chars)
#     print(passwords)

#=========================================================


import streamlit as st
import pandas as pd
st.title('BMI calculator')
height = st.slider('Enter your height in cm', min_value=100, max_value=250, value=170)
weight = st.slider('Enter your weight in kg', min_value=40, max_value=200, value=70)
bmi = weight / ((height/100))**2
st.write(f'your BMI is {bmi:.2f}')
st.write('###  BMI categories ###')
st.write('-underweight: BMI less than 18.5')
st.write('-normal: BMI between 18.5 and 24.9')
st.write('-overweight: BMI between 25 and 29.9')
st.write('-obesity: BMI 30 or greater')

