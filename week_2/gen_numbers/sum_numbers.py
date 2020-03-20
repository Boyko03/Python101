import sys

def sum_numbers(file):
	with open(file, 'r') as f:
		numbers = f.read().split()

	s = 0

	for i in numbers:
		s += int(i)

	return s

def main():
	file = sys.argv[1]
	print(sum_numbers(file))

if __name__ == '__main__':
	main()