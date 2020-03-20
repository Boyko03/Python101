import re
#for sum of numbers

def sum_of(num):
	suma = 0
	for d in num:
		suma += int(d)
	return suma

def is_number_balanced(number):
	s_num = str(number)
	l = len(s_num)
	if l == 1:
		return True
	if l % 2:
		r = s_num.split(s_num[l // 2])
		num1 = r[0]
		num2 = r[1]
	else:
		num1 = s_num[:l // 2]
		num2 = s_num[l // 2:]
	sum1 = sum_of(num1)
	sum2 = sum_of(num2)

	return sum1 == sum2
	
"""
print(is_number_balanced(9))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))
"""

def increasing_or_decreasing(seq):
	l = len(seq)
	if seq[1] > seq[0]:
		for i in range(1, l):
			if seq[i - 1] > seq[i]:
				return False
		return 'Up!'
	elif seq[1] < seq[0]:
		for i in range(1, l):
			if seq[i - 1] < seq[i]:
				return False
		return 'Down!'
	else:
		return False

"""
print(increasing_or_decreasing([1,2,3,4,5]))
print(increasing_or_decreasing([5,6,-10]))
print(increasing_or_decreasing([1,1,1,1]))
print(increasing_or_decreasing([9,8,7,6]))
"""

def sum_of_numbers(input_string):
	nums = [int(i) for i in re.findall(r'\d+', input_string)]

	return sum(nums)

print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("1101"))
print(sum_of_numbers("1111O"))
print(sum_of_numbers("1abc33xyz22"))
print(sum_of_numbers("0hfabnek"))