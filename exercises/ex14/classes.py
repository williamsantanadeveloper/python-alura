from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def __str__(self):
        return f'{self._marca} - {self._modelo}'

    @abstractmethod
    def ligar(self):
        pass


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def ligar(self):
        print(f'O carro {self._modelo} está ligado')

    def __str__(self):
        return f'{self._marca} - {self._modelo} - {self._cor}'
