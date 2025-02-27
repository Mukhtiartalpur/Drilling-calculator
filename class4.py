# project

# is_hungry = False
# burger_lover = True
# if  is_hungry and burger_lover:
#     print('lets order the food')
# else:
#     print('ok dear lets work')



# is_hungry = True
# burger_lover = True
# if  is_hungry and burger_lover:
#     print('lets order the food')
# else:
#     print('ok dear lets work')


# is_hungry = True
# burger_lover = True
# pizza_lover = False

# if  (is_hungry and (burger_lover or pizza_lover)):
#     print('lets order the food')
# elif (is_hungry):
#     print('ok dear lets sleep')
# else:
#     print('not hungry')

#================================================================

# list

#shoppin list

# item_1: str = 'Cake'
# item_2: str = 'Eggs'
# item_3: str = 'Juice'
# item_4: str = 'chips'
# item_5: str = 'Bread'
# shopping_items : list[str] = ['Cake','Eggs','Juice','Chips','Bread']
# tasks : list[str] = ['Teach a class' , 'Finish project' , 'Dinner','Sleep']
# print(shopping_items[1])
# print(tasks[1])

shopping_items : list[str] = ['Cake','Eggs','Juice','Chips','Bread','Oil']
print(len(shopping_items))
print(shopping_items[0:6])
print('Oil' in shopping_items)
shopping_items.append('Flour')
print(shopping_items)
shopping_items.remove('Cake')
print(shopping_items)
shopping_items.insert(0,'Cofee')
print(shopping_items)
shopping_items.pop(1)
print(shopping_items)