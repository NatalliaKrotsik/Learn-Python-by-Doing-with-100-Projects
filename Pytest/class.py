class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

