import sys

def reduce_file_path(path):
	path = path.split('/')

def main():
	path = sys.argv[1]
	print(reduce_file_path(path))

if __name__ == '__main__':
	main()