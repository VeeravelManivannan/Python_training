def febonacci_generator():
	sum = 0 
	value = 1 
	yield sum 
	for x in range (100):
		sum = sum + value
		yield sum


#Printing the fibonacci 
#for i in febonacci_generator():
#	print(i)

#Getting only x numbers

count = 0 

for i in febonacci_generator():
	if count > 4:
		break
	print(i)
	count= count + 1
            
