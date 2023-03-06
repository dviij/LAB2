class car:
	def __init__(self,modelname,year):
		self.modelname=modelname
		self.year=year
	def display(self):
		print(self.modelname,self.year)

c1=car("toyota",2003)
c1.display()