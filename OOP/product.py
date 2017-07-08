class product(object):
	"""docstring for product"""
	def __init__(self,price, name, weight, brand, cost):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = 'for sale'
		self.reason = 'reason'

	def sell(self):
		self.status = 'sold'
		return self

	def tax(self):
		self.price = (self.price * 1.1)
		print self.price
		return self

	def exchange(self, reason):
		if self.reason == 'defective':
			self.price = 0
		elif self.reason == 'new in box':
			self.status = 'For sale'
		elif self.reason == 'opened in box':
			self.status = 'used'
			self.price = (self.price * .8)
		return self

	def display(self):
		print self.price, self.name, self.weight, self.brand, self.status
		return self

glass = product(5, 'glass', 2, 'nike', 1)

glass.display()