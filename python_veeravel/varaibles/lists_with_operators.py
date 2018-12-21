# preparing the x and y object list
x = object()
y = object()

x_list = [x] * 10 
y_list = [y] * 10 

#printing x list and y list
#print(x_list)
#print(y_list)

#counting the number of 
print("the number of occurences of x in x_list is  %d" % x_list.count(x) )
print("the number of occurences of y in y list is %d " % y_list.count(y) )

#creating the combined list which will contain both x and y 
combined_list_of_x_and_y = x_list + y_list
print("the number of occurences in x list is %d" % combined_list_of_x_and_y.count(x))


