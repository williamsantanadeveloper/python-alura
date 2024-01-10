class Person():

    def __init__(self, name='', age=0, job=''):
        self._name = name
        self._age = age
        self._job = job

    def __str__(self):
        return f'{self._name}, {self._age} anos e é {self._job}'

    @property
    def salutation(self):
        if self._job:
            return f'Olá, sou {self._name}! Estou trabalhando com {self._job}'
        else:
            return f'Olá sou {self._name}'

    def birthday(self):
        self._age += 1


william = Person('William', 19, 'Developer')
william.birthday()
william.birthday()
william.birthday()

print(william.salutation)

