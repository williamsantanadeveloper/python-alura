from models.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def __str__(self):
        return self._name
