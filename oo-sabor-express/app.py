from models.restaurant import Restaurant
from models.cardapio.bebidas import Bebida
from models.cardapio.prato import Prato

restaurant_praca = Restaurant('praça', 'Gourmet')
bebida_suco = Bebida('Melancia', 5.0, 'grande')
prato_pao = Prato('Pão', 2, 'O melhor pão da cidade')


def main():
    print(bebida_suco)
    print(prato_pao)


if __name__ == '__main__':
    main()
