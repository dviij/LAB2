class point(object):
	def __init__ (self,x=0,y=0):
		self.x=x
		self.y=y

	def distance (self):
		return(self.x**2+self.y**2)**0.5

p1=point(6,8)
print(p1.distance())
