# partail function ar for reusing function 


def some_function(u,v,w,x):
	return u*4 + v*3 + w*2 + x

#partial functions needs to be imported
from functools import partial
some_partial_function = partial(some_function,10,5,1)


#making the partial function return 60
print("making the partial function return 60 the value returned is %d"  % some_partial_function(3))

#trying another partial function , which will use all 3 values
some_other_partial_function = partial(some_function,10,5,1,3)
print("defining all value in the partial function %d " % some_other_partial_function())
