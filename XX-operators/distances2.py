class DistanceException(Exception):

	def __init__(self, message, value):
		super().__init__(message)
		self.message = message
		self.value = value

	def __str__(self):
		return f'DistanceException - {self.message} caused by {self.value}'


class Distance:
	def __init__(self, value=0):
		self.value = value

	def __add__(self, other):
		if isinstance(other, int):
			new_value = self.value + other
		elif isinstance(other, Distance):
			new_value = self.value + other.value
		else:
			raise DistanceException('Incorrect Type', other)
		return Distance(new_value)

	def __sub__(self, other):
		if isinstance(other, int):
			new_value = self.value + other
		elif isinstance(other, Distance):
			new_value = self.value - other.value
		else:
			raise DistanceException('Incorrect Type', other)
		return Distance(new_value)

	def __truediv__(self, amount):
		if isinstance(amount, int):
			new_value = self.value / amount
		else:
			raise DistanceException('Incorrect Type', amount)
		return Distance(new_value)

	def __floordiv__(self, amount):
		if isinstance(amount, int):
			new_value = self.value // amount
		else:
			raise DistanceException('Incorrect Type', amount)
		return Distance(new_value)

	def __mul__(self, amount):
		if isinstance(amount, int):
			new_value = self.value * amount
		else:
			raise DistanceException('Incorrect Type', amount)
		return Distance(new_value)

	def __str__(self):
		return f'Distance[{self.value}]'


try:
	d1 = Distance(6)
	d2 = Distance(3)

	print(d1 + d2)
	print(d1 - d2)
	print(d1 / 2)
	print(d2 // 2)
	print(d2 * 2)
	print(d1 + 'John')
except DistanceException as exp:
	print('-' * 25)
	print(exp)
	print(exp.message)
	print(exp.value)
