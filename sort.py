# numbers = [5, 3]
# if numbers[0] > numbers[1]:
#     # Swap the elements if they are in the wrong order
#     numbers[0], numbers[1] = numbers[1], numbers[0]
# print("Sorted list:", numbers)

num = [4,2,5,3]
if num[0] > num[1]:
    num[0], num[1] = num[1], num[0]
if num[1] > num[2]:
    num[1], num[2] = num[2], num[1]
if num[2] > num[3]:
    num[2], num[3] = num[3], num[2]
print(num)