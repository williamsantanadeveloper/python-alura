from math import pow

# 1º question
person = {
    'name': 'William',
    'age': 19,
    'city': 'Aracaju'
}

for info in person.values():
    print(info)

# 2º question
person['age'] = 55
person['job'] = 'Developer Front-End'
del person['name']
print(person)

# 3 question
square = {
    'one': pow(1, 2),
    'two': pow(2, 2),
    'three': pow(3, 2),
    'four': pow(4, 2),
    'five': pow(5, 2)
}

print(square)


# 4º question

print(person.get('surname'))  # verificando se existe a key surname

# 5º question

phrase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."

count_letters = {}

letters = phrase.split()

for letter in letters:
    count_letters[letter] = count_letters.get(letter, 0) + 1

print(count_letters)
