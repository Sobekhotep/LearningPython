from car import Car

from electric_car import ElectricCar


my_beetle = Car('volksvagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.get_descriptive_name())

