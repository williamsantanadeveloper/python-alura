class Music():
    name = ''
    author = ''
    time = float


music1 = Music()
music1.name = 'numb'
music1.author = 'Linkin Park'
music1.time = 3.06

music2 = Music()
music2.name = 'Better Now'
music2.author = 'Post Malone'
music2.time = 3.51

music3 = Music()
music3.name = 'X1'
music3.author = 'MC Cabelinho'
music3.time = 3.09

print(vars(music1))
print(vars(music2))
print(vars(music3))
