# Importing datetime library for using date functions
import datetime

# Class definitions
class User(object):
	"""This class is to request fullname and birthday of different users and perform multiple operations on it"""
	def __init__(self,fullname, birthday):
		self.name=fullname
		self.birthday=birthday # yyyymmdd

# Extract first and last names
		names_pieces=fullname.split(" ")
		self.first_name=names_pieces[0]
		self.last_name=names_pieces[1]

	def age(self):
		"""Return the age of the uses in years"""
		today = datetime.date.today()
		#today=datetime.date(2001,5,12)
		yyyy_temp=self.birthday[0:4]
		yyyy=int(yyyy_temp)
		mm=int(self.birthday[4:6])
		dd=int(self.birthday[6:8])
		dob=datetime.date(yyyy,mm,dd)
		age_in_days=(today-dob).days
		age_in_years=age_in_days/365
		return int(age_in_years)

# Instances or object creation
user1=User("Vimal Kumarasamy" , '19920829')
user2=User('Nikita Goswami' , '19930518')

# Calling the object
print(user1.name, user1.age())
print(user2.name, user2.age())

# Understanding what does the class have
# help(User)