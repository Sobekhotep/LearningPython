# Simple car model
from car import Car


def run():

    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())

    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()


if __name__ == "__main__":
    run()

