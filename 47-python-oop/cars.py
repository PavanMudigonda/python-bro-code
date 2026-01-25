# Python Object Oriented Programming
# object = A "bundle" of related attributes and methods(functions)
#          Ex. phone, cup, book, car, dog
#           You need a "class" to create many objects of the same type

# class = (blueprint) used to design the structure and layout of an object

# method = A function that is defined inside a class

# DUNDER means double underscore __init__ = constructor method

# create a class
class Car:   # define class name
    # attributes
    def __init__(self, make, model, year, color):  # constructor method
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0
        self.for_sale = False

    # define class methods inside the class
    def drive(self):
        print(f"The {self.make} is driving.")

    def stop(self):
        print(f"The {self.make} has stopped.")
    
    def left_turn(self):
        print(f"The {self.make} is turning left.")
    def right_turn(self):
        print(f"The {self.make} is turning right.")
    def park(self):
        print(f"The {self.make} is parked.")

# # create objects (instances) of the Car class
# camry_car = Car("Toyota", "Camry", 2020, "Blue")
# civic_car = Car("Honda", "Civic", 2019, "Red")

# # access attributes
# print(camry_car.make)   # Output: Toyota
# print(civic_car.model)  # Output: Civic
# print(camry_car.year)  # Output: 2020
# # call methods
# camry_car.drive(camry_car.make)
# civic_car.park(civic_car.make)
# camry_car.left_turn(camry_car.make)
# civic_car.right_turn(civic_car.make)
# camry_car.stop(camry_car.make)
# civic_car.drive(civic_car.make)