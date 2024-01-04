import os

restaurents = ['Pizza', 'Sushi']


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
    print('3. Ativar restaurante')
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
    print(text)


def register_restaurent():
    show_subtitle('Cadastros de novos restaurantes')

    name = input('Informe o nome do seu restaurante: ')
    restaurents.append(name)
    print(f'O restaurante {name} foi cadastado com sucesso!')

    return_menu()


def listing_restaurant():
    show_subtitle('Listando restaurantes')
    for restaurant in restaurents:
        print(f'.{restaurant}')

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
            print('Ativar restaurante')
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
