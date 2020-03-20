import sys

def cat(arguments):
	with open(arguments, 'r') as f:
		print(f.read())

def main():
	arguments = sys.argv[1]
	cat(arguments)

if __name__ == '__main__':
	main()