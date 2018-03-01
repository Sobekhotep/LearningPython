# Model of electric car
from car import ElectricCar


def run():

    my_tesla = ElectricCar('tesla', 'model s', 2016)

    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()


if __name__ == "__main__":
    run()

