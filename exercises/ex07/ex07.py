class Music():

    musics = []

    def __init__(self, name, artist, time=int):
        self.name = name
        self.artist = artist
        self.time = time
        Music.musics.append(self)

    def __str__(self):
        return f'{self.name} | {self.artist}'

    def listing_musics():
        for music in Music.musics:
            print(f'{music.name} do {music.artist} tem { music.time} minutos de duração')


music1 = Music('Numb', 'Linkin Park', 4)
music2 = Music('Better Now', 'Post Malone', 5)

Music.listing_musics()
