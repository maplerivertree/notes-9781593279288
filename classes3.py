#inheritance, 
""" when creating child class, 
the parent class must be in the same file, 
and appear before the child class"""

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


class eCar(Car):
	#two lines below inherit parent class
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

		#Add subclass specific attributes
		self.truck_size = 100
		###Add an attribute that is defined by another class
		self.battery = Battery()

	def truck_info(self):
		info = 'Battery size is ' + str(self.truck_size) + '-kWh battery.'
		return info

class Battery():
	def __init__(self, battery_size = 80):
		self.battery_size = battery_size

	def battery_info(self):
		info = 'Your battery size is ' + str(self.battery_size) + 'kWh.'
		return info.title()

	def get_range(self):
		if self.battery_size > 90:
			info = 'One charge can go more than 100KM'
		else:
			info = 'One charge can go maximum 100KM'

		return info
