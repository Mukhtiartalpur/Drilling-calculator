# guessing a number

# correct_num = 9
# guess = 0
# while guess != correct_num:
#     guess = int(input("Guess a number: "))
#     if guess != correct_num:
#         print(f'wrong try again')
#     else:
#         print(f'you guessed right')

# i = 10
# while i>= 1:
#     print(i)
#     i -= 1

# num = [1,2,3,4,5,6,7,8,9,]
# for i in num:
#     print(i**2)


#================================================================
# clues = [
#     "Pine Tree", "Oak Tree", "River", "Mountain", "Valley", "Cave",
#     "Waterfall", "Lake", "Forest", "Desert", "Fountain", "Statue",
#     "Bridge", "Tunnel", "Castle", "Moat", "Tower", "Garden", "Park", "Temple"
# ]
# treasure_clue = 12

# for i in range(len(clues)):  
#     print(f"Checking clue {i + 1}: {clues[i]}")  
#     if i + 1 == treasure_clue:  
#         print(f"🎉 You found the treasure at clue {i + 1}: {clues[i]}!")
#         break  



clues = [
    "Pine Tree", "Oak Tree", "River", "Mountain", "Valley", "Cave",
    "Waterfall", "Lake", "Forest", "Desert", "Fountain", "Statue",
    "Bridge", "Tunnel", "Castle", "Moat", "Tower", "Garden", "Park", "Temple"
]
treasure_clue = 10
for i in range(len(clues)):
    print(f'checking clue number: {i+1} : {clues[i]}')
    if i+1 == treasure_clue:
        print(f'you have found the treasure: {treasure_clue}')
        break