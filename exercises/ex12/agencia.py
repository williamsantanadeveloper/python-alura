from ex12.ex12 import Bank


class Agency(Bank):
    def __init__(self, name, address, number=int):
        super().__init__(name, address)
        self._number = number

    def __str__(self):
        return f'{self._name}, {self._address}, {self._number}'
