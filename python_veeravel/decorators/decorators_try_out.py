# A function which throws an exception/error , is later decorated to stop throwing that error and print a message to the user 

#Benefits of decorator
	# Benefit1 : If there are code which are alreday calling "function x or method x , or object  x" , when these methos needs to be changed , then the "callers" need not be changed    
	# Benefit2 : This eliminates the need for interfaces , which causes other problem
        # Benefit3 : If the change is only for one program , the functions can be easily decorated for only 1 purpose 


'''
#Example1:First a simple decorator to illustrate , how decorator works 
def decorator_simple_function_without_arguements(somefunc):
	def inner_function():
		print("I am decorating simple_function_without_arguements")
		somefunc()		
	return inner_function

@decorator_simple_function_without_arguements
def simple_function_without_arguements():
	print("I am a simple function without arguemnets ")	


print("This is how it looks , when we call the simple_function_without_arguements after decoration : \n "  )
simple_function_without_arguements()
'''


#Example2: when we decorate , change the arguements passed to a function
def decorator_simple_function_without_arguements(somefunc):
	def inner_function(arguement_from_outer_func):
		print("Hello i got this arguemnet passed to older function :" + arguement_from_outer_func )
		print("I am playing with that function and concatenating this : ")
		print(arguement_from_outer_func + "-----"  + "my own concatenation")
	return inner_function

@decorator_simple_function_without_arguements
def simple_function_without_arguements(any_string_arguement_from_old_function):
	#print(any_string_arguement_from_old_function)
	pass	


print("This is how it looks , when we call the simple_function_without_arguements after decoration : \n "  )
simple_function_without_arguements("veeravel's arg to older function")
















"""
@Decorator_for_function_which_does_not_check_zero_division
def function_which_does_not_check_zero_division(divisor,divident):
	return divisor/divident


#print("calling the function , which will throw an error %d" % function_which_does_not_check_zero_division(25,0))


#Creating a decorator, which will stop the program from throwing an error  

def Decorator_for_function_which_does_not_check_zero_division(some_function_arguement):
	def someinnerfunction():
		if divident == 0 :
		print("")
"""


	
	


