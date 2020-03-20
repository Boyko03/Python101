def is_palindrome(word):
	return word == word[::-1]

def contains_word(word, text):
	if is_palindrome(word):
		return text.count(word)
	return text.count(word) + text[::-1].count(word)

def word_counter():
	word = input('Enter word: ')
	size = input('Enter matrix size (format: N M): ')

	n = int(size.split(' ')[0])
	m = int(size.split(' ')[1])

	if(len(word) > min([n, m])):
		return 'Invalid number of rows or columns!'

	matrix = []
	rows_inputed = 0
	print('Enter matrix: ')
	while rows_inputed < n:
		row_input = input()
		row = row_input.strip().split(' ')
		if len(row) != m:
			return 'Wrong input!'
		matrix.append(row)
		rows_inputed += 1

	word_occurances = 0

	for row in matrix:
		word_occurances += contains_word(word, ''.join(row))

	for i in range(m):
		column = []
		for row in matrix:
			column.append(row[i])

		word_occurances += contains_word(word, ''.join(column))	

	for c in range(n + m - 1):
		diagonal = []
		for i in range(n):
			for j in range(m):
				if i + j == c:
					diagonal.append(matrix[i][j])
		word_occurances += contains_word(word, ''.join(diagonal))	

	for c in range(1 - m, n):
		diagonal = []
		for i in range(n):
			for j in range(m):
				if i - j == c:
					diagonal.append(matrix[i][j])
		word_occurances += contains_word(word, ''.join(diagonal))	

	return word_occurances

print(word_counter())