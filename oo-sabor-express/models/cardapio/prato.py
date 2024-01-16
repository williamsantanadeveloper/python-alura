from models.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, name, price=float, description=''):
        super().__init__(name, price)
        self._description = description

    def __str__(self):
        return self._name

    def aplicar_desconto(self):
        self._price -= (self._price * 0.05)
        self._price = max(0, self._price)
        return self._price
