#  ---------------- Payment Process system ---------------------------
# Practicing Polymorphism in Python
import uuid


class Payment:
    def __init__(self,amount,sender_name):
        if amount <= 0 :
            raise ValueError("Amount must be greater than 0")
                
        self.amount = amount
        self.sender_name = sender_name
        self.transaction_id = str(uuid.uuid4())
       

    def process_payment(self):
        return f"An Amount of {self.amount} has been paid by {self.sender_name} "



class JazzCash(Payment):
    def __init__(self, amount, sender_name,mobile_number,):
        super().__init__(amount, sender_name,)
        self.mobile_number = mobile_number
        
    # Overriding the processPayment method

    def process_payment(self):
        
        return f"An Amount of {self.amount} has been paid by {self.sender_name} via JazzCash \n Acc no : {self.mobile_number} \n transaction Id : {self.transaction_id}"


    def transaction_detail(self):
        return f"Sender Name : {self.sender_name} \t Amount : {self.amount} \n transaction Id : {self.transaction_id} \t Mobile Number : {self.mobile_number}"


class EasyPaisa(Payment):
    def __init__(self, amount, sender_name,Acc_no):
        super().__init__(amount, sender_name,)
        self.acc_no = Acc_no

    # Overriding the processPayment method
    def process_payment(self):
       
       return f"An Amount of {self.amount} has been paid by {self.sender_name} via EasyPaisa \n Acc no : {self.acc_no} "
    
    def transaction_detail(self):
        return f"Sender Name : {self.sender_name} \t Amount : {self.amount} \n transaction Id : {self.transaction_id} \t Mobile Number : {self.acc_no}"
class BankTransfer(Payment):
    def __init__(self, amount, sender_name,Bank_name):
        super().__init__(amount, sender_name,)
        self.Bank_name = Bank_name
    # Overriding the processPayment method

    def process_payment(self):
        
        return f"An Amount of {self.amount} has been paid by {self.sender_name} via Bank Transfer \n Bank Name : {self.Bank_name} "
    
    def transaction_detail(self):
        return f"Sender Name : {self.sender_name} \t Amount : {self.amount} \n transaction Id : {self.transaction_id} \t Bank Name : {self.Bank_name}"


Payment1 = JazzCash(1000,'afzan',9233432234,)
Payment2 = EasyPaisa(2000,'Zaid',9231231231,)
Payment3 = BankTransfer(3000,'Muhtasib Shah',"United Bank Limited")

Payments = [Payment1,Payment2,Payment3]

for payment in Payments:
    print(payment.process_payment())
    print(payment.transaction_detail())
         

