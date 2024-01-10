class BankAccount():

    def __init__(self, holder='', balance=0):
        self._holder = holder
        self._balance = balance
        self._activity = False

    def __str__(self):
        return f'O titular {self._holder}, possui saldo R${self._balance} e a atividade da conta está {self._activity} por padrão'

    @classmethod
    def switch_activity(cls, account):
        account._activity = True


user1 = BankAccount('Steve', 1000)
user2 = BankAccount('Maria', 500)
user3 = BankAccount('Carlos', 500)

print(f"Antes de ativar: Conta ativa? {user3._activity}")
BankAccount.switch_activity(user3)
print(f"Depois de ativar: Conta ativa? {user3._activity}")
print(user1)
print(user2)
print(user3)


class BankAccountPythonic():
    def __init__(self, holder='', balance=0):
        self._holder = holder
        self._balance = balance
        self._activity = False

    def holder(self):
        return self._holder

    def balance(self):
        return self._balance

    def active(self):
        return self._activity

    def __str__(self):
        return f'{self._activity} {self._balance} '


user4 = BankAccountPythonic('Python', 1500)
user5 = BankAccountPythonic('Carla', 160)
print(user4)
print(f'Titular da conta 5: {user5.holder()}')


class BankCustomer():

    def __init__(self, name='', age=int, cpf='', address='', balance=float):
        self._name = name
        self._age = age
        self._cpf = cpf
        self._address = address
        self._balance = balance

    def __str__(self):
        return f'Nome: {self._name} | Idade: {self._age} | CPF: {self._cpf} | Endereço: {self._address} | Saldo: R${self._balance}'


client1 = BankCustomer('William', 19, '123.456.789-01', 'RUA ABC', 10000)
client2 = BankCustomer('Kaio', 19, '123.456.789-01', '', 30000)
client3 = BankCustomer('Antônio', 19, '123.456.789-01', 'RUA ABC', 20000)

print(client1)
print()
print(client2)
print()
print(client3)
print()
