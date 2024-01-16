from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, name, price):
        self._name = name.title()
        self._price = price

    @abstractmethod
    def aplicar_desconto(self):
        pass
