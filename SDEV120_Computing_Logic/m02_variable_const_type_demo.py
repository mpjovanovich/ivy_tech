######################################################
# Mike Jovanovich
# SDEV 120 - M02
# This program is a demo of variables and constants in Python.
######################################################

some_number = 0;

## I can reassign a value to a variable as often as
## I want.
some_number = 7;
some_number = 99999;
some_number = -32;

## Let's declare a constant value. This would normally
## Go at the top of the file.
PI = 3.14159;
print( "The value of PI is: ", str(PI) )

## There is nothing in Python that prevents a dev from changing
## the value of our "constant".
## We only know that it's a constant because all caps is a convention
## for declaring a constant.
PI = 123;
print( "The value of PI is: ", str(PI) )

