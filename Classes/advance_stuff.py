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