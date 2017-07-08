class Bike(object):
	def __init__(self, price, speed, miles=0):
		self.price = price
		self.speed = speed
		self.miles = miles

	def display(self):
		print self.price
		print self.speed
		print self.miles

		return self

	def ride(self):
		self.miles += 10
		print "ride!!"
		print self.miles
		return self

	def reverse(self):
		self.miles -= 5
		print "reversing!!!"
		print self.miles
		return self


sunday = Bike(450, 22)
volume = Bike(325, 18)
animal = Bike(400, 20)

#sunday.ride().ride().ride().reverse().display()
volume.ride().ride().reverse().reverse().display()
animal.reverse().reverse().reverse().display()