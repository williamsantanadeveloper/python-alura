from models.restaurant import Restaurant

restaurant_praca = Restaurant('praça', 'Gourmet')

restaurant_praca.get_rating('Gui', 9)
restaurant_praca.get_rating('Laís', 8)
restaurant_praca.get_rating('Emy', 2)


def main():
    Restaurant.listing_restaurants()


if __name__ == '__main__':
    main()
