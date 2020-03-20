from utls import Utls

class Polynomial(Utls):
	def __init__(self, pol):
		self.pol = pol

	def get_derivative(self):
		terms = self.to_terms()
		pol = []

		for term in terms:
			if 'x' not in term.term:
				continue
			pol += term.get_term_derivative()

		if len(pol) == 0:
			return 0

		return ' + '.join(pol)



if __name__ == '__main__':
	main()