#objects and classes example 

class vehicle:
	name = ""
	price = ""
	vehicle_type = "car"
	color = ""

	def description(self):
		print("This is a %s %s which would be %s in color and it would cost you $%s" % (self.name , self.vehicle_type , self.color , self.price ) )



#object creation time :)

myobject1 = vehicle()
myobject1.name = "ferrari"
myobject1.color = "red"
myobject1.price = 100


myobject1.description()

