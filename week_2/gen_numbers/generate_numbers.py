import sys
from random import randint

def generate_numbers(filename, numbers):
	numbers = int(numbers)
	with open(filename, 'w') as f:
		for i in range(numbers):
			f.write(str(randint(1, 1000)) + ' ')

def main():
	arguments = sys.argv
	arguments.pop(0)
	generate_numbers(arguments[0], arguments[1])

if __name__ == '__main__':
	main()