#One thought , why are sets made to have only unique elements ? because the purpose  of sets in python is to find union, intersection and set difference 

#converting an array to set 
some_array_with_Duplicatenames= ["arjun","duplicatetendulkar","kulkarni","vinayak" ,"duplicatetendulkar"]

#converting to set and printing it
some_set = set(some_array_with_Duplicatenames)

print(some_set)

#some examples_to_demonstrate
diwali_event_attendees = set(["arjun","duplicatetendulkar","kulkarni","vinayak" ])

christmas_event_attendees = set (["ganesh","duplicatetendulkar","dharavi","aparna" ])

print("only diwali : %s" % diwali_event_attendees.difference(christmas_event_attendees))
print("attending 1 or both events : %s"  %  diwali_event_attendees.union(christmas_event_attendees) )
print("attending only both events : %s " % diwali_event_attendees.intersection(christmas_event_attendees) )
print("semmetric_difference, meaning people who attended only 1 event  : %s " % diwali_event_attendees.symmetric_difference(christmas_event_attendees) )





