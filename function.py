# def my_function():
#     print('hello world')
# my_function()

#================================================================

# def fun(age , name):
#     print( age , name)

# fun(30,'ali')

# ring
#     #function_suite
#     return('expression')
# my_function()
# variable = my_function(argument)
# print(variable)

#================================================================

# PASS BY VALUE PASS BY REFERENCE

# def double(x):
#     x = x * 2
#     print(x)
# double(5)


# def modify_value(x):
#     x = 10
#     print("Within function:", x)
# x = 5
# modify_value(x)
# print("After function:", x)

# def modify(x):
#     x = 5
#     print(f'inside function{x}')
# x = 10 
# print(f'ouside function{x}')
# modify(x)

#================================================================

# def modify_list(lst):
#     lst.append(10)
#     print("Within function:", lst)
# lst = [1,2,3,4,5,6,7,8,9]
# modify_list(lst)
# print(f'outside the function: {lst}')
#================================================================
# def modify_int(x):
#     x = 7
#     print(f'inside function: {x} memory location: {id(x)}')
# x = 10
# modify_int(x)
# print(f'outside function: {x} memory location: {id(x)}')
#================================================================
# def modify_lst(lst):
#     lst.append(10)
#     print(f'inside function: {lst} and memory location: {id(lst)}')
# lst = [1,2,3,4,5,6,7,8,9]
# modify_lst(lst)
# print(f'outside function: {lst} and memory location: {id(lst)}')



# =====================================================================

# Keyword Argument
# def info(name, age , gender , qualification):
#     print(f'Name: {name}\nAge: {age}\nGender: {gender}\nQualification: {qualification}')
# info(qualification = 'Engineering' , gender = 'male', age = 26 , name = 'Mukhtiar')

#=======================================================================
# unfolding list and dict
# def info(name , age):
#     print(name)
#     print(age)
# info('ali' , 18)
# lst = ['ali' , 18] 
# info(lst[0] , lst[1])
# info(*lst)
# dct = {'name': 'ali' , 'age' : 18}
# info(dct['name'] , dct['age'])
# info(**dct)
# def info(name,age):
#     print(f'Name: {name}\nAge: {age}')
# lst = ['ali','20']
# dic = {'name':'ali','age':20}
# info(*lst)
# info(**dic)


#================================================================
# key word arguments

# def add(x:int , y:int = 0)-> float:
#     return x + y
# print(float(add(1,2)))
# print(add(y = 36 , x = 2))
# print(add(x = 4))



#==============================================================

# def add(*nums):
#     return sum(nums)
# print(add(1,2,3,4,5))

# def grocery(**items):
#         print(items)
# grocery(banana= 6,apples = 4,oil=5)

#==============================================================


# def mix(x:int , y:int=0 , *tup , **dic):
#     print(x,y,tup,dic)
# print(mix(2,3,'mangoe','apple','banan' , new = 23 , old = 43))

#==============================================================

# def info(**mukhtiar):
#   print(type(mukhtiar))
#   print(mukhtiar)

#   # for num in nums:
#   #   print("value = ", num)

# info(name="mukhtiar", age=30, phone=55566699, address='hyderabad')

#==============================================================

# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print (f'name: {name} age: {age}')
# printinfo( age=50, name="Arif" )
# printinfo( name="Arif" )


#==============================================================
# positional only argument
# def posFun(x, y, /, z):
#     print(x + y + z)

# print("Evaluating positional-only arguments: ")
# posFun(1, 2, z=3)
#===========================================================

#Keyword-only arguments

# def posFun(*, num1, num2, num3):
#     print(num1 + num2 + num3)
# posFun(num1=6, num2=8, num3=5)
# posFun(num3=6, num1=8, num2=5)

#===========================================================

# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print ("Output is: ")
#    print (arg1)
#    for var in vartuple:
#       print ("*",var)
#    return;

# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50, 70, 90 )

#================================================================

# def add(x,y):
#    z=x+y
#    return z
# a=int(input('enter a number: '))
# b=int(input('enter another number: '))
# result = add(a,b)
# print(result)

#================================================================

# def add_two(x, y):
#   return x + y
# print(add_two(1,2))
#================================================================
# my_lambda = lambda x, y:  x + y

# print(my_lambda(1,2))

#================================================================
# new = lambda x,y : x + y
# print(new(1,2))
#================================================================
# new = lambda x : x**2
# x = int(input('enter a number '))
# print(new(x))
#================================================================

#Write a lambda function that takes a number and returns True if it's even, otherwise

#new = lambda x :

# def even(x):
#     if x % 2 == 0: 
#         return True
#     else: 
#         return False
# x = int(input('Enter number: '))
# result = even(x)
# print(result)

#===========================================================

#Arbitrary or Variable-length Arguments

# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print ("Output is: ")
#    print (arg1)
#    for var in vartuple:
#       print ("*",var)
#    return;
# printinfo( 10 )
# printinfo( 70, 60, 50, 70, 90 )

# def one(x,*vac):
#     print(x)
#     print(vac)
# one(1,235)


# def new(x:int,*VLA:int):
#     print(x)
#     print(VLA)
#     print(x,VLA)
# new(1,10,20,30,40,50,60,70,80,90)

#=======================================================================

# Python Function with Return Value

# def add(x,y):
#    z=x+y
#    return z
# a=10
# b=20
# result = add(a,b)
# print (result)

# #===========================================================
# #The Anonymous Functions

# def add_two(x, y):
#   return x + y
# my_lambda = lambda x, y:  x + y;
# print(my_lambda(1,2))

# my_lambda = lambda x,y : x*y
# print(my_lambda(3,4))

#================================================
#====================  NOT CLEAR =================================================
# my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}

# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# sorted_dict

#======================================================

# sum = lambda arg1, arg2: arg1 + arg2;

# # Now you can call sum as a function
# print ("Value of total : ", sum( 10, 20 ))
# print ("Value of total : ", sum( 50, 20 ))
#============================================================================
# my_lambda = lambda x,y,z, : x*y*z
# print(my_lambda(2,3,4))
#============================================================================
#Global vs. Local variables

# x = 10
# def add(x,y):
#     print(f'inside function local variable: {x+y}')
# add(1,1)
# print(f'outside function global variable: {x}')

#===========================================================================

#Generator function

# def my_gen():
#     print('my_gen')
#     yield 'hello world'
# g = my_gen()
# print(g)
# print(type(g))

# def my_gen():
#     yield 'my name is mukhtiar'
#     yield 'I am a software engineer'
#     yield 'I am from hyderabad'
# g= my_gen()
# print(next(g))
# print(next(g))
# print(next(g))

# def my_gen():
#     yield 'my name is mukhtiar'
#     yield 'I am a software engineer'
#     yield 'I am from hyderabad'
# g= my_gen()
# for ele in g:
#     print(ele)