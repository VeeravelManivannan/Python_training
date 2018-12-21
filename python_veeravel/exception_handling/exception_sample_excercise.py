# program to catch exception 

actor = {"name" : "veeravel manivannan" , "height" : 1.65 , "weight" : 75}

def get_actors_lastname():
	try:
		return actor["lastname"]
	except KeyError:
		return None

get_actors_lastname()

print("The actors last name is %s " % get_actors_lastname() )


