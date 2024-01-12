from models.restaurant import Restaurant
from models.cardapio.bebidas import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa

restaurant_praca = Restaurant('praça', 'Gourmet')
bebida_suco = Bebida('Melancia', 5, 'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão', 2, 'O melhor pão da cidade')
sobremesa1 = Sobremesa('Pudim', 5, 'Ao leite', 'G')
sobremesa1.aplicar_desconto()
prato_pao.aplicar_desconto()

# restaurant_praca.add_itens_no_cardapio(bebida_suco)
# restaurant_praca.add_itens_no_cardapio(prato_pao)


def main():
    # restaurant_praca.exibir_cardapio
    print(sobremesa1)
    print(bebida_suco)


if __name__ == '__main__':
    main()
