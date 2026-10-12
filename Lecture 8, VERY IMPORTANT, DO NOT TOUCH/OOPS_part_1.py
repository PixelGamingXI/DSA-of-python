
class Magic_Schools:
    School_name = "Hogwarts School of Withcraft and Wizadry"
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    def welcome(self):
        print("Welcome", s1.name,",", "in", self.School_name, "!")        


s1 = Magic_Schools("Harry Potter", 908)
s1.welcome()
# ----------------------------------------------------------------------------------------------------------------------------




class Student:
    def __init__(self, name,Marks ):
        self.name = name
        self.marks = Marks
        
    


    def get_avg(self):
        sum = 0
        for val in self.marks:
         sum += val       
        print(s1.name, "Got an average score of ",sum/3)

s1 = Student("Harry Potter", [20, 20, 20])
s1.get_avg()