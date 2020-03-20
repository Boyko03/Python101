from simplify_fraction import simplify_fraction

def collect_fractions(fractions):
	n = 0
	d = 1
	for fraction in fractions:
		d *= fraction[1]

	for fraction in fractions:
		n += fraction[0] * (d // fraction[1])

	return simplify_fraction((n, d))


def main():
	pass

if __name__ == '__main__':
	main()