class Restaurant():
    name = ''
    category = ''
    active = False


restaurant_praca = Restaurant()
restaurant_praca.name = 'Praça'
restaurant_praca.category = 'Gourmet'
restaurant_pizza = Restaurant()

restaurants = [restaurant_pizza, restaurant_praca]

print(restaurant_praca.active)
