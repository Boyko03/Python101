import sys
from polynomials import Polynomial

def solution(arg):
	pol = Polynomial(arg)
	der =  pol.get_derivative()

	return f'The derivative of f(x) = {arg} is:\nf\'(x) = {der}'

def main():
	args = sys.argv

	print(solution(args[1]))


if __name__ == '__main__':
	main()