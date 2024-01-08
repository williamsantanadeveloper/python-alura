# 1º question
class Car():
    def __init__(self, model, color, age=int):
        self.model = model
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.model} | {self.age}'


camaro_amarelo = Car('Camaro', 'Yellow', 2018)

print(camaro_amarelo)

# 2º question


class Restaurant():
    def __init__(self, name, category, locality, activity=bool, number=int):
        self.name = name
        self.category = category
        self.activity = activity
        self.locality = locality
        self.number = number

    def __str__(self):
        return f'{self.name} | {self.category} | {self.activity}'


restaurant1 = Restaurant('Sal & Brasa', 'Rodízio',
                         'Avenida Santos Dumont', True, 75)

print(restaurant1)

# 3º question


class Restaurant2():
    def __init__(self, name, category, locality, activity=False, number=int):
        self.name = name
        self.category = category
        self.activity = activity
        self.locality = locality
        self.number = number

    def __str__(self):
        return f'{self.name} | {self.category} | {self.activity}'


restaurant2 = Restaurant2('Pizza Planet', 'Italiana', 'Avenida ABC', 123)

print(restaurant2)


# 4º question

class Client():
    def __init__(self, name, age=int, height=float):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'{self.name}'


client1 = Client('William', 19, 1.73)
client2 = Client('User1', 76, 1.90)
client3 = Client('User2', 29, 1.81)

print(client1, client2, client3, sep='\n')
