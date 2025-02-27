
#=================  f string / doc string =================

# print("""my name is mukhtiar ali 
# i am working as assistant professor 
# and i am residing in hyderabad""")

# print(f'my name is mukhtiar ali \ni am working as assistant professor \nand i am residing in hyderabad')

#================================================================

# Task print and email withh dynamic name and dynamic signature

# name = 'mukhtiar'
# sender = 'jack'
# print(f'hi {name}\nyou have got an free coupen\nwith kind regards\n{sender}')

#================================================================

# ARITHEMATIIC

# x = 5
# y = 3
# print(f'Addition: {x + y}')
# print(f'Subtraction: {x - y}')
# print(f'Multiplication: {x * y}')
# print(f'Division: {x / y}')
# print(f'modulus: {x % y}')
# print(f'powers: {x**y}')

#================================================

# example

faculty_members = 12
admnistrative_staff = 4 
students = 100 
absent = 15
per_person_serving = 250 

attendees = faculty_members + admnistrative_staff+ students - absent


serving_gm = attendees * per_person_serving
serving_kg = (serving_gm) / 1000

print(f'Total attendees: {attendees}\nTotal serving in gms: {serving_gm}\nTotal serving in kg: {serving_kg}')
