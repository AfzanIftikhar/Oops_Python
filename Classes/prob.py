# 1.    Person class — Create a Person class with name and age attributes and a method introduce() that prints "Hi, I'm X and I'm Y years old."

class Person:
    name = "Afzan"
    age = 22

    def introduce(self):
        print(f"hello i am {self.name} , and my age is {self.age}")

Person().introduce()




# 2.  Rectangle — Create a Rectangle class with width and height. Add methods area() and perimeter().

class Rectangle:
    width = 15
    height = 7

    def Area(self):
        area  = self.width * self.height
        print(f"The area of a Recatngle is {area}")

    def Perimeter(self):
        Perimeter = 2 * (self.width + self.height)
        print(f"The perimeter of a rectangle is {Perimeter}")



obj =  Rectangle()
obj.Area() , obj.Perimeter()



# 3.     Counter — Create a Counter class that starts at 0, with methods increment(), decrement(), and reset().

class Counter:
    count = 0

    def increment(self):
        for i in range(1,11):
            self.count += 1
            print(self.count)

    def decrement(self):
        for i in range(11,1, -1):
            self.count -= 1        
            print(self.count)

    def reset(self):
        self.count = 0            
        print(f"the count value is reseted to : {self.count}")


counts =  Counter()

counts.increment()
counts.decrement()
counts.reset()


# 4.    BankAccount (basic) — balance attribute, methods deposit(amount) and withdraw(amount). Print the balance after each operation.



class Bank:
    

    def __init__(self,balance, amount):
        self.balance = balance
        self.amount = amount

    def deposit(self):
        self.balance += self.amount
        print(self.balance)

    def withdraw(self):
        self.balance -= self.amount
        print(self.balance)


obj1 = Bank(1900,3300)     

obj1.deposit()
obj1.withdraw()




# adding removing and showing songs in Classes

class Songs:

    def __init__(self,name):
        self.name = name
        self.songs = []


    def addMusic(self,music):
        self.songs.append(music)
        print(f"Music added {music}")

    def DeleteMusic(self,music):
        if music in self.songs:
            self.songs.remove(music)
            print(f"Music Removed{music}")

    def myPlaylist(self):
        for songs in self.songs:
            print(songs)            



musics = Songs("Fav")

musics.addMusic("Khat")
musics.addMusic("Hamnava Mere")
musics.addMusic("BabyDoll")
musics.addMusic("Him & I")
musics.DeleteMusic("Hamnava Mere")
musics.myPlaylist()