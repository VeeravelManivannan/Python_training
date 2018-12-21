def decorator( fn ):
  def wrapper( ):
    print( "Befor the function is called" )
    fn( )
    print( "After the function is called" )

  return wrapper

@decorator
def bar( ):
  print ("Hello World!")

#foo = decorator( bar )
#foo( )

bar( )
