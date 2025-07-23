from Student import Student, Course

def main():
    # Create a Student object
    student1 = Student("John Doe", "Smith", 20, "Computer Science")
    # Create a map object to demonstrate isinstance
    map_ob = {}
    print(f"Name: {student1.getfullname()}, Age: {student1.age}, Major: {student1.major}")


if __name__ == "__main__":
    main()
