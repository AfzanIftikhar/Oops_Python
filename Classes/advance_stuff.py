# --------------------- Decorater ---------------------

# A decorator is a function which modifies another function without changing its original code

# It's kinda decorator you can use for anything 

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("The addition of you numbers is ")
#         func(*args, **kwargs)
#         print("Thank you !")
#     return wrapper
    


# @decorator
# def add(a,b,c):
#     print( a + b + c)


# add(12,23,21)


# Args & kwargs
# Args are used for passing a variable number of arguments to a function. It allows you to pass any number of positional arguments to a function, and they will be accessible as a tuple within the function.
# Kwargs are used for passing a variable number of keyword arguments to a function. It allows you to pass any number of keyword arguments to a function, and they will be accessible as a dictionary within the function.

# def adding(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)



# adding(1,5,2,63,21,32,21)

# def person(**kwargs):
#     print(kwargs)



# person(name = "Afzan", age = 20, Skills = "Python")



# List & Dictionary comprehension


# a = 13

# result = "Even" if a % 2 == 0 else "Odd"

# print(result)



# lis = [i for i in range(1,10) if i % 2 == 0 ]

# print(lis)


# dic = {i : i * 2 for i in range(10) }

# print(dic)





# Lambda Functions -> anonymous Functions


# result = lambda x : "Even" if x % 2 == 0 else "Odd"   

# print(result(2))




# Map and Filter Functions

# Map is use to apply Function on multiple Items, it takes One Function and an iterable i,e List or dictionary or maybe list

a = [2,3,1,42,1]

result = map(lambda x : x ** 2, a)

print(list(result))

# Filter returns only the elements which passed through a certain condition and the particular element met the condition

result = filter(lambda x : x % 2 == 0 , a)

print(list(result))


# {Both Map and filter returns an object which has to be converted into list}