from models.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, name, description, price=float):
        super().__init__(name, price)
        self._description = description

    def __str__(self):
        return self._name
