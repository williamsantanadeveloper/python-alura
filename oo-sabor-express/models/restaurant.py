class Restaurant():
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False

        Restaurant.restaurants.append((self))

    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def listing_restaurants(cls):
        print(f'{'Nome do restaurante'.ljust(25)} {'Categoria'.ljust(25)} {'Status'}')
        for restaurent in cls.restaurants:
            print(f'{restaurent._name.ljust(25)} | {restaurent._category.ljust(25)} | {restaurent._active}')

    @property
    def activity(self):
        return '✓' if self._active else '☓'

    def switch_status(self):
        self._active = not self._active


restaurant_praca = Restaurant('praça', 'Gourmet')
restaurant_praca.switch_status()
restaurant_pizza = Restaurant('pizza Express', 'Italiana')

Restaurant.listing_restaurants()
