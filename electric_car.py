"""Набор классов для представления электромобилей"""
from car import Car


class Battery():
    """Простая модель аккумулятора автомобиля"""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумуляторов"""
        if self.battery_size == 70:
            distance_range = 240
        elif self.battery_size == 85:
            distance_range = 270

        message = "This car can go approximately " + str(distance_range)
        message += " miles on the full charge."
        print(message)

    def upgrade_battery(self):
        """Проверяет размер аккумулятора и устанавливает мощность = 85 кВт/ч,
        если он имеет другое значение."""
        if self.battery_size == 85:
            pass
        else:
            self.battery_size = 85


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """У электромобилей нет бензобака"""
        print("This car doesn't need a gas tank!")

