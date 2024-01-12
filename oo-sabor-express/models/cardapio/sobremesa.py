from models.cardapio.item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    def __init__(self, name, price=float, description='', type1='', size=''):
        super().__init__(name, price)
        self._description = description
        self._type1 = type1
        self._size = size

    def __str__(self):
        return f'{self._name}, {self._price}, {self._type1}'

    def aplicar_desconto(self):
        self._price -= (self._price * 0.10)
