# Encapsulation -> Encapsulation is a concept where all the data(Variables) and code(Functions) are kept inside a single class. it means Hiding the internal details of how things works internally and only exposing the necessary parts to the outside world. This is done to protect the data from being accessed or modified directly from outside the class, ensuring that it can only be changed in controlled ways.

# class Factory:
#     a = "Peshawar"

#     def show(self):
#         print("hello i am showing")    


# class Peshawar(Factory):
#     def show(self):
#         print(super().a)



# obj = Peshawar()
# obj.show()      # As You can see we can access the variable of a parent class very easily, and we don't have any private variables that we can't access from outside the class. this is called encapsulation

# Access Modifiers -> Access modifiers Means how we give access to the variables and methods of a class. there are 3 types of access modifiers in python. 1. Public 2. Protected 3.  Private
# 1. Public -> All the attributes and methods of a class we were using all over the time are public by default
# 2. Protected -> Protected members are basically same as public members but they can be written as naming convention for developers to understand that these are protected members , and it can be written with single underscore(_) eg:


# class Factory:
#     _a = "Isb"

#     def show(self):
#         print(self._a)


# obj1 = Factory()
# obj1._a = #"Karachi" # As you can see we can change the value of a protected variable from outside and also inside the class
# obj1.show()



# 3. Private -> Private members are those members which can only be accessed inside the class and can't be accessed from outside the class, and it can be written with double underscore(__) eg:

# class Factory:
#     __a = "Islamabad"

#     def __show(self):
#         print(self.__a)

#     def show(self):
#         self.__show()  # This method is used to access the private method __show() from outside the class

# obj1 = Factory()
# To access private members we can write an extra method inside the class which will return the value of private members and we can call that method from outside the class to access the private members, eg:
# obj1.show()

# Getters and setters Methods in enacapsulation
# Getters methods are used to get the value of a prt the value of a private variable, and these methivate variable and Setters method are use  to access the private members of a class 

class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age    # -> Private Variable

    # Getters Methods to get the private member value
    def get_age(self):
        return self.__age

    # Setters Methods to set the Private members value
    def set_age(self,age):
        if(self.__age > 0):
             self.__age = age
        else:
            print("Age must be a positive integar")


p = Student("Afzan", 22)

print(p.get_age())