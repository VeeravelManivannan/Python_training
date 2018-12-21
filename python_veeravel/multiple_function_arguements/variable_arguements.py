#Foo function returns the amount of extra arguemnets received
def foo(fixedarguement1 , fixedarguemnet2 , fixedarguement3 , *extraarguemnets):
	#print(len(list(extraarguemnets))) # Both of them works
        #print("No of extra arguements are %d" % len(extraarguemnets))
	# question what type of data is "extraarguemnets" ?
        # It is of type tuple
        #print(type(extraarguemnets))
	
	#Returning the amount of extra arguemnets recieved
	return len(extraarguemnets)
        


#The bar function must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.
def bar(**variablearguementwithkeywords):
	if variablearguementwithkeywords.get("magicnumber")==7	:
		return True
	else:
		return False



#The main program starts here 
print("The number of extra arguements returned by foo is %d " % foo("hello", "hi" , "buddy" , "we" , "are" , "extra" , "arguemnets"))

print("Calling bar function  with magic number 7 returns : %s " % bar(magicnumber=7))





