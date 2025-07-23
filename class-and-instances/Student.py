class Student:
    school_name = "ABC University"
    def __init__(self, first_name, last_name, age, major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
    def getfullname(self):
        print("------------------------------------Student object created")
        return f"{self.first_name} {self.last_name} studying {self.major} at {self.school_name}"

class Course:
    def __init__(self):
        print("Course object created")

    title = "Introduction to Python"
    instructor = "Jane Smith"
    duration = 10  # in weeks   