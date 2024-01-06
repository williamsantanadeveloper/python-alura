import os

restaurants = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]


def show_program_name():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)


def show_options():
    '''Essa função é responsável por mostar as opções'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado restaurante')
    print('4. Sair \n')


def finish_app():
    '''Essa função é responsável por finalizar o app'''
    show_subtitle('Encerrando app')
    print()


def return_menu():
    '''Essa função é responsável por retornar ao menu'''
    input('\nDigite uma tecla para voltar para o menu ')
    main()


def invalid_option():
    '''Essa função é responsável para mostrar opção inválida'''
    print('Opção inválida!')
    return_menu()


def show_subtitle(text):
    '''Essa função é responsável por mostar o subtítulo'''
    os.system('cls')
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)


def register_restaurent():
    '''Essa é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    show_subtitle('Cadastros de novos restaurantes')

    name = input('\nInforme o nome do seu restaurante: ')
    category = input(f'\nInforme a categoria do restaurante {name}: ')

    dates_of_restaurents = {
        'nome':  name,
        'categoria': category,
        'ativo': False  # regra de negócio
    }

    restaurants.append(dates_of_restaurents)

    print(f'\nO restaurante {name} foi cadastado com sucesso!')

    return_menu()


def listing_restaurant():
    '''Essa função é responsável por listar os retaurantes'''
    show_subtitle('Listando restaurantes')
    for restaurant in restaurants:
        name = restaurant['nome']
        category = restaurant['categoria']
        active = 'ativado' if restaurant['ativo'] else 'desativado'
        print(f'{'Nome'.ljust(20)} {'Categoria'.ljust(20)} {'Status'}')
        print(f'-{name.ljust(18)} | {category.ljust(18)} | {active}')

    return_menu()


def active_or_desactive_restaurant():
    '''Essa função é responsável por alterar o estado do restaurante
    Inputs:
    - Nome
    - Categoria
    '''
    show_subtitle('Alternando estado restaurante')

    name = input(
        'Digite o nome do seu restaurante que deseja alterar o estado: ')
    find_restaurant = False

    for restaurant in restaurants:
        if name == restaurant['nome']:
            find_restaurant = True
            restaurant['ativo'] = not restaurant['ativo']
            msg = f'O restaurante {name} foi ativado com sucesso! ' if restaurant['ativo'] else f'O restaurante {
                name} foi desativado com sucesso!'
            print(msg)
    if not find_restaurant:
        print('O restaurante não foi encontrado')

    return_menu()


def choose_option():
    '''Essa função é responsável para o usuário escolher a opção que ele deseja
    Inputs:
    - Escolher a opção
    '''
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
    '''Essa função é responsável por agrupar o sistema'''
    os.system('cls')
    show_program_name()
    show_options()
    choose_option()


if __name__ == '__main__':
    main()
