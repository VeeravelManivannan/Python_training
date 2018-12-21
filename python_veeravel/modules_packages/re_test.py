import re

unsortedfunctionlist=[]

print ("working with re")
recontents = dir(re)
for value in recontents:
	if not value.startswith("-"):
		if value.find("find") != -1 :
			unsortedfunctionlist.append(value)

unsortedfunctionlist = ["b","a"]

print(" before sorting the list ")
print(unsortedfunctionlist)
unsortedfunctionlist.sort()
print(unsortedfunctionlist)
 			
