# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Harry")
# print(s1.name)
# del s1.name
# print(s1.name)
#-------------------------------------------------------------------------------------------------------------------------------------



from ast import Name
from encodings.punycode import generate_integers


class Greeting:
    def __init__(self, type):
        self.type = type
       
    def hello(self):
        print("Hello Person")
    
    def welcome(self):
        print("Hello Person")



class Manners(Greeting):
    def __init__(self, Name, type):
        super().__init__(type)
        self.name = Name
        super().hello()

p2 = Manners("Name", "Shantanu")
print(p2.type)
#--------------------------------------------------------------------------------------------------------------------------------------------------
