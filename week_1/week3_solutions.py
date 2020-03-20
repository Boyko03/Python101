def anagram(str1, str2):
	str1 = str1.lower()
	str2 = str2.lower()

	l1 = [s for s in str1]
	l1.sort()
	l1 = ''.join(l1)
	l2 = [s for s in str2]
	l2.sort()
	l2 = ''.join(l2)

	if l1 == l2:
		return 'ANAGRAMS'
	else:
		return 'NOT ANAGRAMS'

"""
print(anagram("TOP_CODER", "COTO_PRODE"))
print(anagram("kilata", "cvetelina_yaneva"))
print(anagram("BRADE",  "BEARD"))
"""

def is_credit_card_valid(number):
	number = str(number)
	if len(number) % 2 == 0:
		return False

	odd = number[-2::-2]
	even = number[::-2]
	s = 0
	for d in odd:
		d = int(d) * 2
		while  d:
			s += d % 10
			d //= 10
	s += sum([int(d) for d in even])
	
	return s % 10 == 0

"""
print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
"""

def prime(num):
	for i in range(2, num + 1):
		if num % i == 0 and num != i:
			return False

	return True

def goldbach(n):
	l = []
	m = n // 2
	for i in range(2, m + 1):
		if prime(i) and prime(n - i):
			l.append((i, n - i))
	return l

"""
print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
"""

def plan(m, i, j):
	s = 0
	x = len(m)
	y = len(m[0])
	for a in range(x):
		for b in range(y):
			if \
			(a == i - 1 and (b == j - 1 or b == j or b == j + 1)) or \
			(a == i + 1 and (b == j - 1 or b == j or b == j + 1)) or \
			(a == i and (b == j - 1 or b == j + 1)):
				e = int(m[a][b]) - int(m[i][j])
				s += e if e > 0 else 0
			else:
				s += int(m[a][b])

	return s

def matrix_bombing_plan(m):
	x = len(m)
	y = len(m[0])
	result = {}
	for i in range(x):
		for j in range(y):
			result[(i, j)] = plan(m, i, j)

	return result

size = input("Enter matrix size (format: N M): ")
n = int(size.split(' ')[0])
m = int(size.split(' ')[1])

matrix = []
rows_inputed = 0
print('Enter matrix: ')
while rows_inputed < n:
	row_input = input()
	row = row_input.strip().split(' ')
	matrix.append(row)
	rows_inputed += 1

print(matrix_bombing_plan(matrix))