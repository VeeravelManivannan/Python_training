SomeString = "SomeTrivialString"
SomeFloating = 13.1
SomeDecimal = 24

if SomeString == "SomeTrivialString":
    print("String value matched and the value is %s" % SomeString)
if SomeFloating == 13.1 and isinstance(SomeFloating , float) :     
    print("floating point number is correct %f " % SomeFloating)
if SomeDecimal == 24 and isinstance(SomeDecimal , int):
    print("decimal value is correct %d " % SomeDecimal)
    print("float printed as decimal %d " % SomeFloating)

