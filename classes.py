#Classes
# self prefix, Method_name(self), use method to change attri

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

	def change_job(self, new_job):
		print('My current job is a ' + str(self.name) + ' and my new job is the below: ')
		self.name = new_job
		print(str(self.name))


my_job = occupation('PM', 10, '150K')
my_job_name = my_job.name

print(my_job_name)
print('\n')

my_new_job = my_job.change_job('golfer')


my_job.start_time('9:30')



		