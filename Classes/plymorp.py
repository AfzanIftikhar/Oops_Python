# PolyMorphism -> Poly means many morphism means forms -> it means we can have same functions with different functionalities


# class Animal:
#     def show(self):
#         print("hello i am showing")


# class Human(Animal):
#     def show(self):
#         print("Heloo i am also showing")



# obj = Human()

# obj.show()


# As you can see we have 2 classes 1.  Animal 2. Human and both have same function name show but different functionality this is called polymorphism, and this method is also called method overriding because we are overriding the show method of Animal class in Human class.


# You have a parent class Animal with a method speak(). Two child classes, Dog and Cat, each define their own speak(). You put one Dog, one Cat, and one plain Animal in a list and loop over it, calling speak() on each.

# # parent class
# class Animal:
#     def speak(self):
#         print("random sound")


# # Child class 1
# class Dog(Animal):
#     def speak(self):
#         print("Bark Bark")


# # Child class 2
# class Cat(Animal):
#     def speak(self):
#         print("Meow meow")



# obj = Animal()
# obj1 = Cat()
# obj2 = Dog()

# Class_lst = [obj,obj1,obj2]


# for i in Class_lst:
#     print(i.speak())


# A Shape class has a method area() that returns 0. You want Circle and Rectangle to each give their own area().

# What does each child class need to store, and what does it need to do with area()?


# class Shape:
   
#     def area(self):
#         return 0


# class Circle(Shape):

#     def __init__(self, radius ):
        
#         self.radius = radius

#     def area(self):
#         pi = 3.14
#         a = pi * self.radius *self.radius
#         return a


# class Rectangle(Shape):

#     def __init__(self, length, width):
#        self.length = length
#        self.width = width

#     def area(self):
        
#         r=self.length * self.width
#         return r



# Object1 = Shape()
# Object2 = Circle(10)
# Object3 = Rectangle(40,20)


# listing = [Object1,Object2,Object3]

# for i in listing:
#     print(i.area())


# An Employee class has get_salary() that returns 1000. A Manager class inherits from it and also defines get_salary(), but it wants the parent’s salary plus a bonus of 500.

# How can Manager reuse the parent’s result instead of rewriting it, and what number does it return?


class Employee:
    def get_Salary(self):
        return 1000


class Manager(Employee):
    def get_Salary(self):
        return super().get_Salary() + 500


obj = Manager()

print(obj.get_Salary())


# In Java, you can write two methods with the same name but different parameters. Python doesn’t allow that: if you define a function twice with the same name, the second one replaces the first.

# How can you make one add() function work for both 2 numbers and 3 numbers?



# def add(a,b, *args):
#     return a + b  +   sum(args) 
    


# print(add(1,2,3,4,5,6))


# You’re building a payment system with CardPayment, PayPalPayment, and CashPayment. Each has a pay(amount) method that works differently. You want a checkout(payment, amount) function that works with any payment type without checking which one it is.

# How would you structure the classes so checkout never needs an if or elif?


class Payment:

    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print("Amount payed")



class CardPayment(Payment):
    def pay(self, amount):
        print("Amount Paid using Card")



class PaypalPayment(Payment):
    def pay(self, amount):
        print("Amount paid via Paypal")



class CashPayment(Payment):
    def pay(self,amount):
        print("Amount Paid through Cash ")