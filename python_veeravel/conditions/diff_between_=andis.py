string_list1 = ["value1", "value2" , "value3"]
string_list2 = ["value1", "value2" , "value3"]
string_list3 = string_list1

#comparing the values of two variables
if string_list1==string_list2 :
    print("the values of two variables are the same ")

#if only the values are equal and not the instances , then print the message 
if string_list1==string_list2 and string_list1 is not 	string_list2:
    print(" both the values are instances are not the same ")


if string_list1==string_list3 and string_list1 is string_list3:
    print(" both the values are instances are the same ")








