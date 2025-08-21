# Management System for pets

class Pet:
  def __init__(self,name,age,id) -> None:
     self.name=name
     self.age=age
     self._id = id # protected
     self.__company_id = 323 # private
  
  def speak(self): 
    pass
  
  def info(self):
    print(f"I am {self.name} and my id is {self._id}")

  def company_info(self):
    print(f"My company id is {self.__company_id}")

  def treatment(self): # abstraction
    print("Done")
    # call the doctor
    # take an appointment 
    # call the rescue team on time

class Dog(Pet):

  def speak(self): # polymorphism
    # pura logic
     print("Barks")

class Cat(Pet):
  def speak(self):
     print("Meow")

# ahmed = Student()
pets = [Dog("Buddy",10,43), Cat("winkers",8,11)]
#       0                     1

for pet in pets: # hr baar aak object
    pet.info()
    pet.speak()