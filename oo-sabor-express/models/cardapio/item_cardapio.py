from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, name, price=float):
        self._name = name.title()
        self._price = price

    @abstractmethod
    def aplicar_desconto(self):
        pass
