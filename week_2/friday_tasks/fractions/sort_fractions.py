def sort_fractions(fractions, asc=True):
	d = 1
	for fraction in fractions:
		d *= fraction[1]

	count = len(fractions)
	for i in range(count):
		for j in range(1, count):
			if fractions[j][0] * (d // fractions[j][1]) < fractions[j - 1][0] * (d // fractions[j - 1][1]):
				tmp = fractions[j]
				fractions[j] = fractions[j - 1]
				fractions[j - 1] = tmp

	if not asc:
		fractions.reverse()
		return fractions
	return fractions

def main():
	pass

if __name__ == '__main__':
	main()