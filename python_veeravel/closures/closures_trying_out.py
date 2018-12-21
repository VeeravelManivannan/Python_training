
#Scenario1: inner function not returning anything , only using and printing
def outer_function(outer_function_variable_passed_as_arguement):
	variable_defined_inside_outer_function = "I am a variable_defined_inside_outer_function "
	
	def inner_function():
		print("inside inner function , printing all variables of outer function")
		print("values from outer function \n %s"  % outer_function_variable_passed_as_arguement)
		print("values defined n outer function \n %s" % variable_defined_inside_outer_function)
	inner_function()



#Scenario2: inner function not returning anything , 1. innre function is returned as function object  2. innerfunction also retruns 
def outer_function2(outer_function2_variable_passed_as_arguement):
	variable_defined_inside_outer_function2 = "I am a variable_defined_inside_outer_function2 "
	
	def inner_function2():
		return (outer_function2_variable_passed_as_arguement + "---" + variable_defined_inside_outer_function2 )
		#print(outer_function2_variable_passed_as_arguement + "---" + variable_defined_inside_outer_function2)
	return inner_function2



#main code starts here
outer_function("arguement to outerfunction")
print("-----------------------------------------------------------------------------------------------------------------------------")

function_object1=outer_function2("arguement to outerfunction2")
print("calling the inner_function_2 object %s " % function_object1() )



	


