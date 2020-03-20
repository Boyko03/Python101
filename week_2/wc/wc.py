import sys

def wc(arg, file):
	if arg == 'chars':
		with open(file, 'r') as f:
			chars = f.read()
			print(chars)
		return len(chars)
	elif arg == 'words':
		with open(file, 'r') as f:
			words = f.read()
		return len(words.split())
	elif arg == 'lines':
		with open(file, 'r') as f:
			lines = f.readlines()
		return len(lines)
	else:
		return 'Invalid command!'

def main():
	arg = sys.argv
	print(wc(arg[1], arg[2]))

if __name__ == '__main__':
	main()