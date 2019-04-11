def pass_func():
	pass

def X_two(x):
	return x*2

def even_check(x):
	if x%2==0:
		print('yes')
	else:
		print('no')

def compare(a, b):
	if a >= b:
		print('да')
	else:
		print('нет')

lambda x, y: x%y

def printing(func):
	def wrapper(*args):
		print("Our arguments: ", args)
		a = func(*args)
		print("Their sum: ", a)
	return wrapper

@printing
def sum(a, b):
	return a + b

s1 = list(map(int, input().split()))
s2 = list(filter(lambda x: x > 10, s1))

a = 3
def dirty(x):
	return x**a

def clean(x, b):
	return x**b

def minmax(l):
	return min(l), max(l)

def check_leap(year):
	return year%400==0 or year%100!=0 and year%4==0

def season(num):
	seasons = {
		'winter': [12, 1, 2], 
		'spring': [3, 4, 5],
		'summer': [6, 7, 8],
		'autumn': [9, 10, 11],
		}
	if num<1 or num>12:
		print('error')
		pass
	for key in seasons:
		if num in seasons[key]:
			return key

def date(day, month, year):
	months = {
		1: list(range(1, 32)),
		2: {True: list(range(1, 30)), False: list(range(1, 29))}[check_leap(year)],
		3: list(range(1, 32)),
		4: list(range(1, 31)),
		5: list(range(1, 32)),
		6: list(range(1, 31)),
		7: list(range(1, 32)),
		8: list(range(1, 32)),
		9: list(range(1, 31)),
		10: list(range(1, 32)),
		11: list(range(1, 31)),
		12: list(range(1, 32)),
	}
	return day in months[month]

def sorting(li):
	return sorted(filter(lambda x: type(x) == float or type(x) == int, li))

print(sorting([16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']))