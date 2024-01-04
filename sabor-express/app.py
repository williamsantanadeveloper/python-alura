import os

restaurents = []


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
    os.system('cls')
    print('Encerrando app')
    print()


def invalid_option():
    print('Opção inválida!')
    input('Digite uma tecla para voltar para o menu principal ')
    main()


def register_restaurent():
    os.system('cls')
    print('Cadastros de novos restaurantes')

    name = input('Informe o nome do seu restaurante: ')
    restaurents.append(name)
    print(f'O restaurante {name} foi cadastado com sucesso!')
    input('Digite uma tecla para voltar para o menu principal')
    main()


def listing_restaurant():
    os.system('cls')
    for restaurant in register_restaurent():
        print(restaurant)


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
