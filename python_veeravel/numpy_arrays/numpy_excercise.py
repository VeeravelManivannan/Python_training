weightlist = [89,98,78,101,171,76]
heightlist = [1.78,1.66,1.89,1.76,1.88,1.76]

#printing datatype 
#print(type(weightlist))

import numpy

#converting array to numpy array
numpy_weightlist = numpy.array(weightlist)
numpy_heightlist = numpy.array(heightlist)


print("Printing a weight list , without numpy  %s" % weightlist )
print("Printing a weight list , with numpy %s " % numpy_weightlist )


#print(numpy_weightlist)
print((numpy_heightlist /numpy_weightlist) **2)


# Print only heights greater than 180
print("printing only height list greater than 180 cm %s " % numpy_heightlist[numpy_heightlist>1.8])

#converting all the weights from kilograms to pounds 
numpy_weightlist_inpounds = numpy_weightlist * 2.2

print("weight list in pounds %s " % numpy_weightlist_inpounds)


