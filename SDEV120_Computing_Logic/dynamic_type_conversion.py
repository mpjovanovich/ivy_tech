###################################################
## Mike Jovanovich
## SDEV 120 - M02
## This program demonstrates dynamic typic and conversion
## in Python.
###################################################

## PYTHON IS A DYNAMICALLY TYPED LANGUAGE! Let's see what
## this means.

## We will intialize two variables, and output the data types.
## I've called the some_int and some_float - we'll see that
## the data types can change though... so those are a poor choice
## for variable names.
some_int = 1
some_float = 1.1
print( "Type of some_int: {0}".format( type(some_int) ) )
print( "Type of some_float: {0}".format( type(some_float) ) )
print()

## Python will implicitly convert some_int to a float on assigment
## to something that needs float functinoality (decimals)
some_int = some_float
print( "Type of some_int: {0}".format( type(some_int) ) )
print( "Type of some_float: {0}".format( type(some_float) ) )
print()

## It will go back to an int again on assignment.
some_int = 1
print( "Type of some_int: {0}".format( type(some_int) ) )
print( "Type of some_float: {0}".format( type(some_float) ) )
print()

## If we do some operation that requires decimal precision, it will
## be "promoted" to a float.
## In this case: 1 / some_float is a float. Then we assign that float
## to some_int.
some_int = 1 / some_float
print( "Type of some_int: {0}".format( type(some_int) ) )
print( "Type of some_float: {0}".format( type(some_float) ) )
print()
