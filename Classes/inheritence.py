# Inheritence in python is when a child class can access all the properties of a parent class. A child can inherit all the properties of a parent class, but a parent class can not inherit all the properties of child class

class Animal:
    a = 'I am a variable in Parent Class' # -> Class attribute 

    def __init__(self,name):
        self.name = name

    def showName(self):
        print(f"your name is {self.name}")    

    def show(self):
        print("I am a method in Parent class")   # -> Instance method



class Human(Animal):
    pass

person1 = Human('Afzan')


print(person1.showName())