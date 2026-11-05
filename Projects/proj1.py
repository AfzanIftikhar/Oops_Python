# -------------------------- Bank Account System --------------------------
#  Practicing Encapsulation

class BankAccount:
    def __init__(self,name, balance = 0):
        self.name = name
        self.__balance = balance # -> Private Attribute

    def deposit(self,amount_Added):

        if amount_Added  > 0:
            self.__balance += amount_Added
            return f"{amount_Added} Amount Added"
        else:
            return "Amount should be Greater then 0"
            

    def withdrawn(self,amount_Withdrawn):
        if amount_Withdrawn > self.__balance:
            return "Withdrawn amount should not be greater then current balance"

        elif amount_Withdrawn % 500 == 0 and amount_Withdrawn >0 :
            self.__balance -= amount_Withdrawn
            return f"{amount_Withdrawn} amount deducted from your account"

        else:
            return "Amount must be greater then 0 and should be multiple of 500"
        
    def current_balance(self):
        return f"Current Balance is {self.__balance}"




obj = BankAccount("Ali" , 2000)

print(obj.deposit(1000))
print(obj.withdrawn(200))
print(obj.current_balance())
        


        