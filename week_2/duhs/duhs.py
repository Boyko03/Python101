import os
import sys

def duhs(path):
	s = 0
	dirr = os.scandir(path)
	for entry in dirr:
		if entry.is_dir():
			s += duhs(f'{path}/{entry.name}')
		else:
			s += os.stat(path).st_size
	
	return s

def main():
	path = sys.argv[1]
	print(f'{path} size is: {round(duhs(path) / 1024 / 1024, 1)} M')

if __name__ == '__main__':
	main()