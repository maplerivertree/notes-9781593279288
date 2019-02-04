#important Details

# use capitalization for the name of the class
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

		self.odometer = 0

	def car_info(self):
		#Must use (self.make), can NOT use (make)
		info = str(self.make) + ' ' + str(self.model) + ' ' + str(self.year)
		return info

	def read_odometer(self):
		odometer = self.odometer
		return odometer

	def update_odometer(self, miles):
		self.odometer = miles

	def add_odometer(self, miles):
		self.odometer += miles

""" Call Module in CL
>>> from classes2 import Car
>>> new_car = Car('Aston Mar
>>> print(new_car.car_info()
Aston Martin DB9 2012
>>> new_car.update_odometer(
>>> print(new_car.odometer)
55000
>>> new_car.add_odometer(1)
>>> print(new_car.odometer)
550001
"""