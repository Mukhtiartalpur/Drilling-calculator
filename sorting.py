import random
# def generate_random_numbers(count, start, end, msg):
#   random_numbers = random.sample(range(start, end + 1), count)
#   print(msg)
#   return random_numbers
# unsorted_list = generate_random_numbers(25, 1, 50, 'Unsorted list:')
# unsorted_list

# my_list = ['red', 'green', 'blue', 'yellow',]
# random_colours = random.sample(my_list,2)
# print(random_colours)

def random_numbers(count, start, end, msg):
    num = random.sample(range(start , end+1),count)
    print(msg)
    return num
numbers = random_numbers(4,1,20,'unsorted list: ')
print(numbers)

