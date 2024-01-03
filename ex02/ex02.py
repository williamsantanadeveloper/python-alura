# 1º question


def verify_parity(number):

    number = int(number)

    if number % 2 == 0:
        return 'par'
    return 'impar'


print(verify_parity(2))
print(verify_parity(3))

# 2º question


def user_age(number):

    number = int(number)

    children = number >= 0 and number <= 12
    young = number >= 13 and number <= 18
    adult = number > 18

    if children:
        return 'Criança'
    elif young:
        return 'Adolescente'
    elif adult:
        return 'Adulto'
    else:
        return 'Informe um número inteiro'


print(user_age(28))
print(user_age(15))
print(user_age(2))

# 3º question


def verify_account(user, password):
    user = input('Informe seu usuário: ').lower()
    password = input('Informe sua senha: ')

    if user == 'user' and password == '123':
        return 'Acesso liberado!'
    else:
        return 'Acesso negado!'


print(verify_account('user', '123'))
print(verify_account('user', '123'))

# 4º question


def calculating_coordinates(x, y):

    x = float(x)
    y = float(y)

    first_quadrant = x > 0 and y > 0
    second_quadrant = x < 0 and y > 0
    third_quadrant = x < 0 and y < 0
    fourth_quadrant = x > 0 and y < 0

    if first_quadrant:
        return f'Primeiro Quadrante, valores x = {x} e y = {y}'
    elif second_quadrant:
        return f'Segundo Quadrante, valores x = {x} e y = {y}'
    elif third_quadrant:
        return f'Terceiro Quadrante, valores x = {x} e y = {y}'
    elif fourth_quadrant:
        return f'Quarto Quadrante, valores x = {x} e y = {y}'
    else:
        return 'Informe valores válidos'


print(calculating_coordinates(1, 1))
print(calculating_coordinates(-1, 1))
print(calculating_coordinates(-1, -1))
print(calculating_coordinates(1, -1))
