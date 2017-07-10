class MathDojo(object):
	def __init__(self, *numbs):
		
		self.numbs = numbs

	def add(self, *numbs):
		start = '0'
		print str(type(start)) + ','.join(numbs)
		
		return self
	
MathDojo().add(2).add(2, 5)