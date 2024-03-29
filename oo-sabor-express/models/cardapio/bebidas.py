from models.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def __str__(self):
        return self._name

    def aplicar_desconto(self):
        self._price -= (self._price * 0.08)
        self._price = max(0, self._price)
        return self._price
