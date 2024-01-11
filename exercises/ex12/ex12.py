class Bank():

    def __init__(self, name, address):
        self._name = name
        self._address = address

    def __str__(self):
        return f'{self._name} {self._address}'


bradesco = Bank('Bradesco', 'RUA ABC')
print(bradesco)
