# # 1.    Person class — Create a Person class with name and age attributes and a method introduce() that prints "Hi, I'm X and I'm Y years old."

# class Person:
#     name = "Afzan"
#     age = 22

#     def introduce(self):
#         print(f"hello i am {self.name} , and my age is {self.age}")

# Person().introduce()




# # 2.  Rectangle — Create a Rectangle class with width and height. Add methods area() and perimeter().

# class Rectangle:
#     width = 15
#     height = 7

#     def Area(self):
#         area  = self.width * self.height
#         print(f"The area of a Recatngle is {area}")

#     def Perimeter(self):
#         Perimeter = 2 * (self.width + self.height)
#         print(f"The perimeter of a rectangle is {Perimeter}")



# obj =  Rectangle()
# obj.Area() , obj.Perimeter()



# # 3.     Counter — Create a Counter class that starts at 0, with methods increment(), decrement(), and reset().

# class Counter:
#     count = 0

#     def increment(self):
#         for i in range(1,11):
#             self.count += 1
#             print(self.count)

#     def decrement(self):
#         for i in range(11,1, -1):
#             self.count -= 1        
#             print(self.count)

#     def reset(self):
#         self.count = 0            
#         print(f"the count value is reseted to : {self.count}")


# counts =  Counter()

# counts.increment()
# counts.decrement()
# counts.reset()


# # 4.    BankAccount (basic) — balance attribute, methods deposit(amount) and withdraw(amount). Print the balance after each operation.



# class Bank:
    

#     def __init__(self,balance, amount):
#         self.balance = balance
#         self.amount = amount

#     def deposit(self):
#         self.balance += self.amount
#         print(self.balance)

#     def withdraw(self):
#         self.balance -= self.amount
#         print(self.balance)


# obj1 = Bank(1900,3300)     

# obj1.deposit()
# obj1.withdraw()




# # adding removing and showing songs in Classes

# class Songs:

#     def __init__(self,name):
#         self.name = name
#         self.songs = []


#     def addMusic(self,music):
#         self.songs.append(music)
#         print(f"Music added {music}")

#     def DeleteMusic(self,music):
#         if music in self.songs:
#             self.songs.remove(music)
#             print(f"Music Removed{music}")

#     def myPlaylist(self):
#         for songs in self.songs:
#             print(songs)            



# musics = Songs("Fav")

# musics.addMusic("Khat")
# musics.addMusic("Hamnava Mere")
# musics.addMusic("BabyDoll")
# musics.addMusic("Him & I")
# musics.DeleteMusic("Hamnava Mere")
# musics.myPlaylist()




# ----------------------------------------------------------------------------------------------------------------------


# 1.    Animal and Dog: Create an Animal class with name and a speak() method. Make Dog and Cat subclasses that override speak().


# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def name(self):
#         print(f"My name is {self.name}")

#     def speak(self):
#         print(f"I speak {self.language}")    


# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         print(f"I speak meow meow")


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         print(f"I speak Bark Bark")



# animal1 = Animal("any")
# animal2 = Cat('White Cat')
# animal3 = Dog("German Shepard Dog")

# animal2.speak()
# animal3.speak()



# Vehicle and Car: Vehicle has brand and year. Car inherits it and adds doors. Print all the details.

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = brand
#     def show(self):
#         print(f'This Car is from {self.brand} & its model is {self.year} and it has {self.doors} doors')
        


# class Car(Vehicle):
#     def __init__(self, brand, year, doors):
#         super().__init__(brand, year)
#         self.doors = doors
   

# car1  = Car('BMW' , '2010', 2)



# car1.show()
# ----------------------------------------------------------------------------------------------------------------------


# 3.    Using super(): Create Person(name, age) and Student(name, age, roll_no). Use super().__init__() in Student


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"My name is {self.name}, and my age is {self.age}, my roll no is {self.roll_no}")


# class Student(Person):
#     def __init__(self,name,age,roll_no):
#         super().__init__(name,age)
#         self.roll_no = roll_no

# student1 = Student('afzan','21','456')

# student1.show()

# ----------------------------------------------------------------------------------------------------------------------

# 4. 	Method inheritance: Create Shape with a describe() method that prints "I am a shape". Make Circle and Square inherit it without overriding, then call it on both.


class Shape:
    def describe(self):
        print("I am a shape")


class Circle(Shape):
    pass

class Square(Shape):
    pass



circle = Circle()

square = Square().describe()


# ----------------------------------------------------------------------------------------------------------------------


# 5.	isinstance and issubclass: Using the classes above, check which object belongs to which class and which class is a subclass of which.


# issubclass is use to find if one class is an subclass of another class, it will take (2 classes) the first class is the one we are checking and the other class is the one we are comparing the first class


# isinstance is use to find that whether an object is an instance of a class or not it it is an instance the return value will be true else false 

print(issubclass(Circle,Shape))

# So from the above statement we can find out that the Circle is a subclass of Shape class

print(isinstance(circle,Circle ))
# And from this statement we can find out that circle is the instance of classs Circle






# Hirearchal inheritence

# 6.	Employee hierarchy: Employee (name, salary), Manager (adds team list), Developer (adds programming languages). Each overrides get_details() and extends the parent's output using super().

#  {From this question we also learnt that not only the attributes are initialized or extend but also the methods can also be extend to the lower child classes as you can see here}

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def get_details(self):
#         print(f"hello my name is {self.name}, and my salary is {self.salary}")



# class Manager(Employee):
#     def __init__(self, name, salary, team_list):
#         super().__init__(name, salary)
#         self.team_list = team_list
#     def get_details(self):
#         return super().get_details() + f"team : {self.team_list}" 
        

# class Developer(Manager):
#     def __init__(self, name, salary, team_list,programming_language):
#         super().__init__(name, salary, team_list)
#         self.programming_language = programming_language

#     def get_details(self):
#        return super().get_details() + f" we are working on {self.programming_language} programming language"
    
    


# 7.	Method overriding with extension: A BankAccount with deposit() and withdraw(). Create SavingsAccount, which adds interest, and CurrentAccount, which allows overdraft by overriding withdraw().

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = amount + self.balance
        
    def withdraw(self,amount):
        if amount  > self.balance:
            print("Insuffeicent balance")
        else:
            self.balance = self.balance - amount
            print("Amount withdrawn")

class Saving_account(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        super().deposit() + interest