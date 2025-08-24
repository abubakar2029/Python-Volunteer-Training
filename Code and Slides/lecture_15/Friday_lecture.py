# # self

# class Std:
#   class_name = "ABC" # class variable
  
#   def __init__(self,name):
#       self.name = name # instance variables

#   def greet(self):
#       print("Hello, my name is", self.name)

#   @staticmethod
#   def greet2():
#       print("hello")

# a = Std("Aa")


# b = Std("Bb")

# print(a.greet())
# a.greet2()
# print(b.greet())

# Std.greet2()
# # Std.greet()


# # Protected + Private

# # private keyword os attribut ya method ko private banata hai
# class Std2:
#     _balance = 0
#     def __init__(self, name):
#         self.name = name
        

# a2 = Std2("Aa")
# a2._balance


# multiple-inheritance
# class Car_01:
#     def start(self):
#         print("Car is starting")

# class Car_02:
#     def stop(self):
#         print("Car is stopping")

# class New_Car(Car_01, Car_02):
#     def accelerate(self):
#         print("Car is accelerating")

# c = New_Car()
# c.start()
# c.stop()
# c.accelerate()

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         # we have to calculate average
#         sum = 0
#         for i in range(len(self.marks)):
#             sum += self.marks[i]
#         return sum / len(self.marks)

# std_01 = Student("Amit", [90, 80, 70,88])
# # std_01.average()        
# print(std_01.average())


# ATM system 
# classes Account, SavingsAccount, CurrentAccount
# deposit, withdraw

class Account: # Parent class
    def __init__(self, PIN,balance = 0, name="ADA",):
        self.balance = balance # 5000
        self.name = name
        self.__PIN = PIN # encapsulation - private
    
    def withDraw(self,amount,PIN):
        
        if (not PIN==self.__PIN):
        #   agar pins match nhi krta 
        #  1112 == 1234
            return "Pin is incorrect"

        # 10000
        if (self.balance>amount):
            # 5000 > 1000 
            self.balance -= amount
            # balance = 5000 - 1000
            # balance = 4000
            return f"Balance updated to {self.balance}"
    
    def deposit(self,amount):
        if(amount<=0):
            return "Insufficient amount"
        
        self.balance+=amount
        return f"Balance updated to {self.balance}"
    
    
class SavingsAccount(Account):
    def withDraw(self,PIN,amount):
        if(self.balance>2000):
            # True
            return super().withDraw(PIN,amount) 
           #  
        
        return "Your balance is insufficient"
            
class CurrentAccount(Account):
    def withDraw(self, amount):
        super().withDraw(amount)
        
a1= SavingsAccount(1234,5000)
# a1 
result = a1.withDraw(1234,1000)
print(result)