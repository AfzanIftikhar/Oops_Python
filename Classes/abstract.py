# Abstraction is showing the the essential features of an object and hiding the unnecessary details of an object. Abstraction is not present in Python but it can by achieved through Library called abc(Abstract Base Class)

# i think it is very helpful for code integrity 

from abc import ABC,abstractmethod


class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def area(self):
        pass


class Square(abstract):
    def __init__(self,side):
        self.side = side

    # Initially if we are not calculating Perimeter or Area, this is not throwing any error, although we are not following rules for square or Circle, here what abstraction comes for,{Abstraction is also use to write or follow the dedicated rules, helpful for not missing any component}

    
    def perimeter(self):
        pass

    def area(self):
        pass

class Circle(abstract):
    def __init__(self,radius):
        self.radius = radius

    
    def perimeter(self):
        pass
    



obj = Square(2)
obj2 = Circle(7)



#  -------------------------Dunder Methods----------------------

# Dunder Methods are the one that starts and ends with double underscores like __init__, __str__ and many more, they automatically get called when certain actions are performed


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello my name is {self.name}"

    def __add__(self,others):
        sum = 0

        for i in others:
            sum = sum + i.age

        return f"The sum of Both ages are {self.age + sum}"



obj = Animal("Lion", 22)
obj2 = Animal("Tiger", 21)
obj3 = Animal("Dog", 12)

print(obj + (obj2,obj3))

        