def memory(n):
	"""
	>>> f = memory(10)
	>>> f = f(lambda x: x*2)
	20
	>>> f = f(lambda x: x - 7)
	13
	>>> f = f(lambda x: x > 5)
	True
	"""
	def all(func):
		nonlocal n
		n = func(n)
		print(n)
		return all
	return all