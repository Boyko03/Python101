class Song:
	def __init__(self, title, artist, album, length):
		self.title = title
		self.artist = artist
		self.album = album
		self.length = length

	def __str__(self):
		return f'{self.artist} - {self.title} from {self.album} - {self.length}'

if __name__ == '__main__':
	main()