class Restaurent():
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurent()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_praca.ativo = False

nome_restaurante = restaurante_praca.nome
categoria = restaurante_praca.categoria
active = 'ativo' if restaurante_praca.ativo else 'desativado'

nome_restaurante = 'Bistrô'

if restaurante_praca.ativo == True:
    print(f'O restaurante {nome_restaurante} está {active}!')
else:
    print(f'O restaurante {nome_restaurante} está {active}!')

print(vars(restaurante_praca))


restaurant_pizza = Restaurent()
restaurant_pizza.nome = 'Pizza Place'
restaurant_pizza.categoria = 'Fast Food'


if restaurant_pizza.categoria == 'Fast Food':
    print(f'A categoria do restaurante {restaurant_pizza.nome} é {restaurant_pizza.categoria}')
else:
    print(f'A categoria do restaurante {restaurant_pizza.nome} não é {restaurant_pizza.categoria}')

restaurant_pizza.ativo = True

print(f'Nome: {restaurante_praca.nome} - Categoria: {restaurant_pizza.categoria}')
