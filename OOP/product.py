class product(object):
	"""docstring for product"""
	def __init__(self,price, name, weight, brand, cost):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = 'for sale'

	def sell(self):
		self.status = 'sold'
		return self

	def