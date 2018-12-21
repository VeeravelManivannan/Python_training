#simple formatting of string
some_string = "trivial string"
some_another_string = "another trivial string"
print("formatted string is %s " % some_string )

#showing the usage of tupules
print("examples of tupule is : %s %s "  % (some_string , some_another_string))

#Excercise
data = ("john" , "carter" , 53.47) 
welcome_msg = "Hello"

#formatting and displaying a welcome message , using a combination of tupule and floating point
print( welcome_msg + " %s %s your bill is %.2f"  % data  )

