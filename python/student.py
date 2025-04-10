class Student:
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level=10

    def __str__(self):
        return self.lname +":" + str(self.id)
    
    def greeting(self):
        print(f"hello, I am {self.fname}, nice to meet you")
    def take_exam(self):
        self.energy_level -=1
    def get_energy_level(self):
        return self.energy_level
    
s1 = Student("John", "Smith", 1234)
s1.greeting()
print(s1)
s1.take_exam
print(s1.get_energy_level())