# Inheritence in python is when a child class can access all the properties of a parent class. A child can inherit all the properties of a parent class, but a parent class can not inherit all the properties of child class

# class Animal:
#     a = 'I am a variable in Parent Class' # -> Class attribute 

#     def __init__(self,name):
#         self.name = name

#     def showName(self):
#         print(f"your name is {self.name}")    

#     def show(self):
#         print("I am a method in Parent class")   # -> Instance method



# class Human(Animal):
#     pass

# person1 = Human('Afzan')


# print(person1.showName())



# Super() functionality 
# The Super method is used in the constructor of a child class, just to initialize the parent class attributes
# -> suppose we are adding some additional info or additional data to the child class then we have to initialize the existing properties in the parent class so we will use the super functionality

class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        # print(f"Hello my name is {self.name} and my age is {self.age}")   # -> This will throw an error
        print(f"hello this is {self.name}")


class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")
         


animal1 = Animal("horse")
person1 = Human("Afzan", 22)

# This will throw an error if are trying to print the age in the parent class however it will run the child class so to resolve this issue, if we adding more functionalities to the child class we have to handle these additional changes by writing own methods
animal1.show()
person1.show()



# Multiple Inheritence 
# => Multiple inheritence is One child class has many parent class


class Father:
    def __init__(self,name):
        pass


class Mother:
    def __init__(self):
        pass

class Child(Father,Mother):
    def __init__(self):
        pass




# Multi-level Inheritence

# GrandParents -> parents -> Child, Understanding the structure


# Structure of Multi-level inheritence look like this : 

class Factory:
    def __init__(self, materials, zips):
        self.materials = materials,
        self.zips = zips


class PeshawarFactory(Factory):
    def __int__(self,materials,zips,color):
        super().__init__(materials,zips)
        self.color = color

class IslamabadFactory(PeshawarFactory):
    def __init__(self, materials, zips,color, pockets):
        super().__init__(materials, zips, color)
        self.pockets = pockets