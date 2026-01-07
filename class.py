class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        d={"name":self.name,"marks":self.marks}
        print(d)


    @classmethod
    def school_name(cls):
        print("ABC School")

    @staticmethod
    def welcome():
        print("Welcome Students")

p1=Student("Ramya",97)
p2=Student("Amra",93)
p1.display()
p2.display()
Student.school_name()
Student.welcome()

class Student:
    def __init__(self,name):
        self.name=name
class SportsStudent(Student):
    def __init__(self,name,sports):
        super() . __init__(name)
        self.sports=sports
    def play(self):
         print(f"{self.name} plays {self.sports}")

p1= SportsStudent("Sameer","Football")
p1.play()


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)

    @classmethod
    def school_name(cls):
        print("Chennai School")
    @staticmethod
    def welcome():
        print("Welcome Students")
class SportsStudent(Student):
    def __init__(self,name,marks,sports):
        super() . __init__(name,marks)
        self.sports=sports
    def play(self):
        print(f"{self.name} plays {self.sports} and marks are {self.marks}")

p1= SportsStudent("Azees" ,97,"Batmiton")
p2= SportsStudent("Sameer",95,"Football")
p1.display()
p2.display()
p1.play() 
p2.play()
SportsStudent.school_name()
SportsStudent.welcome()