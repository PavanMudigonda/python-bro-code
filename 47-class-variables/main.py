# Class Variables. = Shared among all instances of a class.
#                    Defined within the class constructor but outside any methods.
#                    Allow you to share data among all objects created from the class.

class Student:

    class_year = "2025"     # Class variable
    number_of_students = 0  # Class variable

    def __init__(self, name, age):  # Constructor method
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        # this is how you would access a class variable inside the class
        Student.number_of_students += 1  # Increment class variable each time a new student object/instance is created

# Note: You can also use self.number_of_students, but using the class name is preferred for clarity.
Student1 = Student("SpongeBob", 15)
Student2 = Student("Patrick", 16)
Student3 = Student("Squidward", 17)
Student4 = Student("Sandy", 16)

print(f"{Student1.name} is in the class of {Student1.class_year}.")
print(f"{Student2.name} is in the class of {Student2.class_year}.")
print(f"{Student3.name} is in the class of {Student3.class_year}.")
print(f"{Student4.name} is in the class of {Student4.class_year}.")
print(f"Total number of students: {Student.number_of_students}")