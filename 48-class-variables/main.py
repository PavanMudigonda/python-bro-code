# ============================================
# CHAPTER 47: CLASS VARIABLES
# ============================================
# Class Variables = Shared among ALL instances of a class
#                   Defined within the class but outside any methods
#                   Allow you to share data among all objects created from the class
#
# Instance Variables vs Class Variables:
# - Instance variables: Unique to each object (self.name, self.age)
# - Class variables: Shared by all objects (class_year, number_of_students)
#
# Key Concepts:
# - Class variables are defined directly in class body
# - Access via ClassName.variable (preferred) or instance.variable
# - Useful for counters, constants, default values
# - Changes affect all instances

# =============================================
# CLASS DEFINITION WITH BOTH VARIABLE TYPES
# =============================================
class Student:

    # =============================================
    # CLASS VARIABLES (Shared by all instances)
    # =============================================
    class_year = "2025"     # All students in the same year
    number_of_students = 0  # Counter for total students

    # =============================================
    # CONSTRUCTOR METHOD
    # =============================================
    def __init__(self, name, age):  # Constructor method
        # Instance variables (unique to each object)
        self.name = name  # Each student has their own name
        self.age = age    # Each student has their own age
        
        # =============================================
        # ACCESSING CLASS VARIABLES
        # =============================================
        # Increment the class variable using ClassName.variable
        # This increments the counter each time a new Student is created
        Student.number_of_students += 1  
        # Note: Using Student.number_of_students (not self.number_of_students)
        #       is preferred for clarity that we're modifying a class variable

# =============================================
# CREATE STUDENT INSTANCES
# =============================================
# Each time we create a Student, number_of_students increments
Student1 = Student("SpongeBob", 15)  # Counter = 1
Student2 = Student("Patrick", 16)     # Counter = 2
Student3 = Student("Squidward", 17)   # Counter = 3
Student4 = Student("Sandy", 16)       # Counter = 4

# =============================================
# ACCESS INSTANCE AND CLASS VARIABLES
# =============================================
# Each student has their own name (instance variable)
# But they all share the same class_year (class variable)
print(f"{Student1.name} is in the class of {Student1.class_year}.")  # SpongeBob is in the class of 2025.
print(f"{Student2.name} is in the class of {Student2.class_year}.")  # Patrick is in the class of 2025.
print(f"{Student3.name} is in the class of {Student3.class_year}.")  # Squidward is in the class of 2025.
print(f"{Student4.name} is in the class of {Student4.class_year}.")  # Sandy is in the class of 2025.

# Access class variable using class name (best practice)
print(f"Total number of students: {Student.number_of_students}")  # Output: 4

# =============================================
# KEY TAKEAWAYS
# =============================================
# - Instance variables (self.name): Unique per object
# - Class variables (class_year): Shared across all objects
# - Modify class variables using ClassName.variable
# - Useful for tracking data across all instances