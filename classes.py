#Classes
# self prefix, Method(self)

class occupation():
	"""docstring for ClassName"""
	def __init__(self, name, hours, wages):
		self.name = name
		self.hours = hours
		self.wages = wages

		#NO underlines for methods
		#You MUST include self as an arg
	def start_time(self, t1):
		print('Your work starts at '+t1+' in the morning.')



my_job = occupation('PM', 10, '150K')
my_job_name = my_job.name
print(my_job_name)

my_job.start_time('9:30')



		