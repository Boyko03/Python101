def sum_of_digits(n):
	if n < 0:
		n *= -1
	sum = 0
	while n != 0:
		sum *= 10
		sum += n % 10
		n //= 10
	return sum;

#print(sum_of_digits(1325132435356))
#print(sum_of_digits(123))
#print(sum_of_digits(6))
#print(sum_of_digits(-10))

def to_digits(n):
	a = [];
	br = 0
	if(n < 1):
		return -1
	while n != 0:
		a.append(n % 10);
		n //= 10;
		br += 1
	i = 0;
	while i < br // 2:
		tmp = a[i]
		a[i] = a[br - i - 1];
		a[br - i - 1] = tmp;
		i += 1;
	return a;

def to_digits2(n):
	return [int(i) for i in str(n)]

#print(to_digits(123))
#print(to_digits(99999))
#print(to_digits(123023))

def to_number(digits):
	num = 0;
	while digits:
		tmp = digits.pop(0);
		tmp = to_digits(tmp);
		while tmp:
			num *= 10;
			num += tmp.pop(0);
		
	return num;

def to_number2(digits):
	number_str = "".join([str(d) for d in digits])
	return int(number_str)

#print(to_number([1,2,3]))
#print(to_number([9,9,9,9,9]))
#print(to_number([1,2,3,0,2,3]))
#print(to_number([21, 2, 33]))

def fact_digits(n):
	n = to_digits(n);
	fact = 0;
	while n:
		tmp = n.pop(0);
		f = 1;
		for i in range(1, tmp+1):
			f *= i;
		fact += f;
	return fact;

#print(fact_digits(111))
#print(fact_digits(145))
#print(fact_digits(999))

def palindrome(n):
	n = str(n);
	l = len(n);
	for i in range(l // 2):
		if n[i] != n[l - i - 1]:
			return False;
	return True;

#print(palindrome(121))
#print(palindrome("kapak"))
#print(palindrome("baba"))

def count_vowels(str):
	count = 0
	str = str.lower();
	for ch in str:
		if ch in ['a', 'e', 'i', 'o', 'u', 'y']:
			count += 1;

	return count

#print(count_vowels("Python"))
#print(count_vowels("Theistareykjarbunga")) #It's a volcano name!
#print(count_vowels("grrrrgh!"))
#print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
#print(count_vowels("A nice day to code!"))

def count_consonants(str):
	count = 0
	str = str.lower();
	for ch in str:
		if ch in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']:
			count += 1;

	return count

#print(count_consonants("Python"))
#print(count_consonants("Theistareykjarbunga") #It's a volcano name!)
#print(count_consonants("grrrrgh!"))
#print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
#print(count_consonants("A nice day to code!"))

def char_histogram(string):
	d = {};
	for s in string:
		if s in d:
			d[s] += 1;
		else:
			d[s] = 1;
	return d;

#print(char_histogram("Python!"))
#print(char_histogram("AAAAaaa!!!"))

def sum_matrix(m):
	sum = 0;
	for e in m:
		while e:
			sum += e.pop(0)
	return sum

"""
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m))

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))
"""

def nan_expand(times):
	if times != 0:
		return "Not a " * times + "NaN"
	else:
		return ""

"""
print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))
"""

def prime_factorization(n):
	d = {}
	i = 2
	while n != 1:
		if n % i == 0:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
			n //= i
			i = 1
		i += 1
	l = []
	for key in d:
		l.append((key, d[key]))
	return l;

"""
print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))
"""

def group(n):
	new_list = [n.pop(0)]
	r_list = [[new_list[0]]]
	i = 0
	j = 0
	for x in n:
		if x == new_list[i]:
			r_list[j].append(x)
		else:
			j += 1
			r_list.append([x])
		new_list.append(x)
		i += 1
	return r_list

"""
print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))
"""

def max_consecutive(items):
	items = group(items)
	max_len = 0
	for item in items:
		i_len = len(item)
		if i_len > max_len:
			max_len = i_len
	return max_len

"""
print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
"""

