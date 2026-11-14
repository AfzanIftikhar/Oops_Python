# --------------------- Decorater ---------------------

# A decorator is a function which modifies another function without changing its original code


def decorator(func):
    def wrapper(a,b):
        print("The addition of you numbers is ")
        func(a,b)
        print("Thank you !")
    return wrapper
    


@decorator
def add(a,b):
    print( a + b)


add(12,12)


# Args & kwargs


def adding(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)



adding(1,5,2,63,21,32,21)