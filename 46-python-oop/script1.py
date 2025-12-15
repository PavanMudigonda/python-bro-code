# first import the Car class from cars module

from cars import Car


# create objects (instances) of the Car class
camry_car = Car("Toyota", "Camry", 2020, "Blue")
civic_car = Car("Honda", "Civic", 2019, "Red")

# # access attributes
print(camry_car.make)   # Output: Toyota
print(civic_car.model)  # Output: Civic
print(camry_car.year)  # Output: 2020
# # call methods
camry_car.drive()
civic_car.park()
camry_car.left_turn()
civic_car.right_turn()
camry_car.stop()
civic_car.drive()