class Veiculo():
    def __init__(self, marca, modelo):
        self._marca = marca.title()
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'{self._marca}, {self._modelo}, Status: {self._ligado}'


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas=int):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'{self._marca}, {self._modelo}, {status}, {self._portas}'


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        tipo = 'esportiva'.title() if self._tipo == 'esportiva' else 'casual'
        return f'{self._marca}, {self._modelo}, {tipo}'
