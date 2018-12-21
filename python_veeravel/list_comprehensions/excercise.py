#List comprehensions
import random

#creating a list of random numbers
import random
random_list = []

for i in range(10):
	random_list.append(random.randint(1,897))

print("List before seperating out things %s "  % random_list)

#using list comprehension creating an odd and even list

odd_list = [some_number for some_number in random_list if some_number % 2 != 0]

print("The odd list is %s " % odd_list)

#printing the even list , with even lesser code (doing the list comprehension code inline )

print("the even list is %s " % [some_number for some_number in random_list if some_number % 2 == 0])
