# Application of closure

#Function , which is a generic multiplier
def generic_multiplier(actual_multiple_number):
	def specific_multiplier(number_to_be_multipliedwith):
		return actual_multiple_number * number_to_be_multipliedwith
	return specific_multiplier

#multiplier of 6
multiplier_of_6=generic_multiplier(6)
multiplier_of_2=generic_multiplier(2)
multiplier_of_9=generic_multiplier(9)

print("10 multiplied by 6 is %d" % multiplier_of_6(10))
print("10 multiplied by 2 is %d" % multiplier_of_2(10))
print("10 multiplied by 9 is %d" % multiplier_of_9(10))

		
