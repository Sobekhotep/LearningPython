"""Набор классов для представления ресторанов"""


class Restaurants():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит отформатированное название ресторана, тип кухни
        и количество обслуженных клиентов"""
        print("The restaurant's name is " + self.restaurant_name.title() + ".")
        print("The cuisine type of " + self.restaurant_name.title() + " is "
              + self.cuisine_type + ".")
        print("The restaraunt is served " + str(self.number_served) + " clients now.")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт"""
        print("The restaurant " + self.restaurant_name.title() + " is open now!")

    def set_number_served(self, number):
        """Позволяет задать количество обслуженных клиентов"""
        self.number_served = number

    def increment_number_served(self, number):
        """Позволяет увеличить количество обслуженных клиентов на заданную величину"""
        self.number_served += number
