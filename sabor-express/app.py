import os

restaurents = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]


def show_program_name():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)


def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado restaurante')
    print('4. Sair \n')


def finish_app():
    show_subtitle('Encerrando app')
    print()


def return_menu():
    input('\nDigite uma tecla para voltar para o menu ')
    main()


def invalid_option():
    print('Opção inválida!')
    return_menu()


def show_subtitle(text):
    os.system('cls')
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)


def register_restaurent():
    show_subtitle('Cadastros de novos restaurantes')

    name = input('\nInforme o nome do seu restaurante: ')
    category = input(f'\nInforme a categoria do restaurante {name}: ')

    dates_of_restaurents = {
        'nome':  name,
        'categoria': category,
        'ativo': False  # regra de negócio
    }

    restaurents.append(dates_of_restaurents)

    print(f'\nO restaurante {name} foi cadastado com sucesso!')

    return_menu()


def listing_restaurant():
    show_subtitle('Listando restaurantes')
    for restaurant in restaurents:
        name_restaurent = restaurant['nome']
        category = restaurant['categoria']
        active = 'ativado' if restaurant['ativo'] else 'desativado'
        print(f'{'Nome'.ljust(20)} {'Categoria'.ljust(20)} {'Status'}')
        print(f'-{name_restaurent.ljust(18)} | {category.ljust(18)} | {active}')

    return_menu()


def active_or_desactive_restaurant():
    show_subtitle('Alternando estado restaurante')

    name = input(
        'Digite o nome do seu restaurante que deseja alterar o estado: ')
    find_restaurant = False

    for restaurante in restaurents:
        if name == restaurante['nome']:
            find_restaurant = True
            restaurante['ativo'] = not restaurante['ativo']
            msg = f'O restaurante {name} foi ativado com sucesso! ' if restaurante['ativo'] else f'O restaurante {
                name} foi desativado com sucesso!'
            print(msg)
    if not find_restaurant:
        print('O restaurante não foi encontrado')

    return_menu()


def choose_option():
    try:
        chosen_option = int(input('Escolha uma opção: '))
        # choose_option = int(choose_option)

        # print(chosen_option == 1)
        # print(type(choose_option), type(1))

        if chosen_option == 1:
            register_restaurent()
        elif chosen_option == 2:
            listing_restaurant()
        elif chosen_option == 3:
            active_or_desactive_restaurant()
        elif chosen_option == 4:
            finish_app()
        else:
            invalid_option()
    except:
        invalid_option()


def main():
    os.system('cls')
    show_program_name()
    show_options()
    choose_option()


if __name__ == '__main__':
    main()
