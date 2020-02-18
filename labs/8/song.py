class Song:
	def __init__(self, artist, genre, length, album):
		self.artist = artist
		self.genre = genre
		self.length = length
		self.album = album

ready_to_let_go = Song("Cage The Elephant", "Indie Rock", 188, "Ready To Let Go")
despacito = Song("Luis Fonsi", "Reggaeton", 229, "VIDA")

print(dir(despacito))