def diff(a, b):
	return a - b

a = 2 + 3
b = a + a

assert b == a * 2
assert a == 3 + 2
assert diff(a, b) == a - b
