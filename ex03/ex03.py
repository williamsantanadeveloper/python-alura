from time import sleep
# 1º question
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_names = ['William', 'Kaio', 'Antônio', 'Lyra']
list_of_years = [2004, 2024]

# 2º question
for name in list_of_names:
    print(name)

# 3º question
sum_ = 0
for i in range(1, 10, 1):
    if i % 2 == 1:
        sum_ += i
print(sum_)

# 4º question
for i in range(10, 0, -1):
    # sleep(1)
    print(i)

# 5º question
number = int(input('Informe um número: '))
for i in range(0, 11):
    print(f'{number} x {i} = {number*i}')

# 6º question
try:
    numbers = [1, 2, 3, 4]
    for number in numbers:
        sum_ += numbers
except TypeError:
    print('Erro de Tipo encontrado')

# 7º question
lista_de_notas = []
for i in range(4):
    nota = int(input('Informe a nota: '))
    lista_de_notas.append(nota)

    media = sum(lista_de_notas) / len(lista_de_notas)
print(media)
