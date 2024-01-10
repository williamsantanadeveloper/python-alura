from ex11 import Book

book1 = Book('piratas', 'Fulano', 1992)
print(f'Antes de emprestar: {book1._available}')
book1.lend()
print('Depois de emprestar: {}'.format(book1._available))

year = 2002
livros_disponiveis = Book.verify_avaliable(year)

print(f'Livros dispoíveis em {year}: {livros_disponiveis}')


def main():
    Book.verify_avaliable()


if __name__ == '__main__':
    main()
