# trying to use in operator with string
find_me = "catchme"
string_list = ["hello" , "catchme" , "nomatch"]
if find_me in string_list:
    print("the expected value was found ")


#The in operator is really nice, it works 
some_tupule = ("tupule String" , 57 )
tupule_list = [("tupule String" , 57 ), (34,56) ]
if some_tupule in tupule_list:
    print(some_tupule)
