def simplify_fraction(fraction):
	nom = fraction[0]
	denom = fraction[1]

	if denom == 0:
		raise ValueError('Dividing by zero.')
	
	for i in range(2, nom + 1):
		if nom % i == 0 and denom % i == 0:
			nom //= i
			denom //= i

	return (nom, denom)

def main():
	pass

if __name__ == '__main__':
	main()