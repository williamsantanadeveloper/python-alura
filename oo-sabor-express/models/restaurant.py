class Restaurant():
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False

        Restaurant.restaurants.append((self))

    def __str__(self):
        return f'{self.name} | {self.category}'

    def listing_restaurants():
        for restaurent in Restaurant.restaurants:
            print(f'{restaurent.name} | {restaurent.category} | {restaurent.active}')

restaurant_praca = Restaurant('Praça', 'Gourmet')
restaurant_pizza = Restaurant('Pizza Express', 'Italiana')

Restaurant.listing_restaurants()
