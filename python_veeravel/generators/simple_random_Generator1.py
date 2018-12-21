import random

def random_number_Generator():
	for i in range(3):
		#Yields random number in the range 1 to 10 
		yield random.randint(1,10)
	
        for i in range(4):
		#yields random number in the range 11  to 20
		yield random.randint(11,20)


## printing every number generated using the generator function
 
for i in random_number_Generator():
	print ("value generatord from random number %d " % i)


## printing only the first 5 numbers from the generator

print("printing only the first 5 numbers in random number generator")

for i in range(5):
	print ("value generator from random number %d " % next(random_number_Generator()))

