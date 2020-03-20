import sys

def cat2(arguments):
	arguments.pop(0)
	while arguments:
		with open(arguments[0], 'r') as f:
			print(f.read())
		arguments.pop(0)

def main():
	arguments = sys.argv
	cat2(arguments)

if __name__ == '__main__':
	main()