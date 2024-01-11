from models.rating import Rating


class Restaurant():
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._rating = []

        Restaurant.restaurants.append((self))

    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def listing_restaurants(cls):
        print(f'{'Nome do restaurante'.ljust(25)} {
              'Categoria'.ljust(25)} {'Avaliação'.ljust(25)} {'Status'}')
        for restaurent in cls.restaurants:
            print(f'{restaurent._name.ljust(25)} | {restaurent._category.ljust(25)} | {
                  str(restaurent.media_rating).ljust(25)} | {restaurent._active}')

    @property
    def activity(self):
        return '✓' if not self._active else '☓'

    def switch_status(self):
        self._active = not self._active

    def get_rating(self, client, note):
        if 0 < note <= 5:
            rating = Rating(client, note)
            self._rating.append(rating)

    @property
    def media_rating(self):
        if not self._rating:
            return '-'
        media = round(
            sum(rating._note for rating in self._rating) / len(self._rating), 1)
        return media
