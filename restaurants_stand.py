"""Набор классов для представления ресторанных киосков с мороженным"""

from restaurant import Restaurants

class IceCreamStand(Restaurants):
    """Добавляет наличие киоска с мороженным"""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибут киоска - список сортов мороженного"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def list_flavors(self):
        print("The ice cream stand of " + self.restaurant_name.title() + " has "
              + ', '.join(list(self.flavors)) + " sorts of ice cream")
