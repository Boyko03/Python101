def my_sort(*, itr = None, asc = True, key = None):
	if itr == None:
		return []

	if not len(itr):
		return itr

	br = 0
	l = len(itr)
	if type(itr) == tuple:
		br = 1
		itr = list(itr)

	if type(itr[0]) == dict:
		if key == None:
			raise ValueError('Key is required for dictionaries.')
		elif asc:
			for i in range(l):
				for j in range(1, l):
					if itr[j][key] < itr[j - 1][key]:
						tmp = itr[j]
						itr[j] = itr[j - 1]
						itr[j - 1] = tmp
		else:
			for i in range(l):
				for j in range(1, l):
					if itr[j][key] > itr[j - 1][key]:
						tmp = itr[j]
						itr[j] = itr[j - 1]
						itr[j - 1] = tmp
	
	elif asc:
		for i in range(l):
			for j in range(1, l):
				if itr[j] < itr[j - 1]:
					tmp = itr[j]
					itr[j] = itr[j - 1]
					itr[j - 1] = tmp
	else:
		for i in range(l):
			for j in range(1, l):
				if itr[j] > itr[j - 1]:
					tmp = itr[j]
					itr[j] = itr[j - 1]
					itr[j - 1] = tmp

	if br:
		itr = tuple(itr)

	return itr

def main():
	my_sort()

if __name__ == '__main__':
	main()