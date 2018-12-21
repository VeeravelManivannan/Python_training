#Basic string operations learnt
#Split - Splitting a string
#Slice - Slicing a string , slicing a string syntax [start, stop , step (start from where)]
#length - length of string
#count - count the number of occurences
#starts with & end with 
#Upper and lower


split_example = "hello india"
print(split_example.split(" "))

#also size of 
print("the size of string is %d " % len(split_example) )

#also find index
print("index of space first l is %d " % split_example.index("l"))

slice_example1 = "0123456789"
print(slice_example1[1:7:])


slice_example2 = "0123456789"
print(slice_example2[1:7:2])

#Reversing using slice logic
#reversing_using_slice_example = "0123456789"
#print(reversing_using_slice_example[-1::])



