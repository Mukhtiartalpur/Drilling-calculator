import random
# random : no parameters, between 0 and 1 any float and 1 is not included
# randint: integar , inlcude intial and final both
# randrange: intial and final. if given one argument it will be the final, steps

# print(random.random())
# print(random.randint(1,4))
#print(random.randint(1,4)+10)
#print(random.randrange(1,10,2))

# list = ['karachi','hyderabad','sukkur','jamshoro']
# for i in range(1,10):
#     x = random.randint(0,3)
#     print(list[x])

# def game(x):
#     random_number = random.randint(1 , x)
#     guess = 0
#     while guess != random_number:
#           guess = int(input(f'Guess a number between 1 and {x}: '))
#           if guess < random_number:
#                print(f'sorry you were too low  try again')
#           elif guess > random_number:
#                print(f'sorry you were too high  try again')
#     print(f'Congratulations you have perfectlly guessed the correct number: {random_number}')
# game(10)


def game(x):
     random_n = random.randint(1, x)
     guess = 0 
     while guess != random_n:
          guess = int(input(f'guess a number between 1 and {x}: '))
          if guess < random_n:
               print(f'try again, ')
          elif guess > random_n:
               print(f'try Again, ')
          else:
               print(f'congratulations')
game(10)