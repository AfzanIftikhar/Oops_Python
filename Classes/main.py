
#  ----------------------- C l a s s e s  -----------------------------------

# Classes: -> Classes are the bluePrint of object, it has 3 things -> Attributes,methods and open functions => Variable inside class is called attribute, => Function inside class is called methods

# class Factory():
#     a = 12      # -> Attributes

#     def hello(self):    # -> Methods
#         print("Hello how are you")


#     print("Hello i am getting initialized")    # -> open functons


# print(Factory().a)

# Factory().hello()


# Objects : => Objects are just the variables, we store the classes in the variable and the variable is now an object


class Factory:
    # The following __init__ is a constructor which can take parameters as the classes can't take parameters directly so it it takes the parameters in the constructor

    def __init__(self,material,zips,pockets):
               # -> Self is use to trace the location of the object,self trace the location in the ram, suppose the postion of the object is 100 in ram so the following thing will become like 100.material = material and so on..
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your object contains {self.material} material, {self.zips} zips and {self.pockets} pockets.")


reebok = Factory("leather" , 4 , 3)
campus = Factory("Nylon" , 3, 3)

reebok.show()
campus.show()



class Animal:
    age = 12 # -> Class Attribute

    def __init__(self,age):

        self.age = age  # -> Instance Attribute

    def show(self):     # -> instance Method

        print(f"hello brother how are you, your age is {self.age}")    

    @classmethod

    def hello(cls):  # -> Class Method: Directly targeting class not targeting any object hence we can't get the value of let suppose Age.and can be written as @classMethod in form of decorator
        print("hello, HI")


    @staticmethod

    def static():
        print(f"Hello this is static method")


obj = Animal(12)

obj.show()    
obj.hello()
obj.static()



# -------------End of classes---------------

