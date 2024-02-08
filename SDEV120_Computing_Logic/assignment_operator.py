########################################################
## Mike Jovanovich
## SDEV 120 - M02
## This program is a demo of the assigment operator.
########################################################

## Declare and initialize three integer variables.
a = 0
x = 1
y = 2

print( "Values of a, x, y after variable initialization:" )
print( a,x,y )

## Let's change the value of a. We can simply assign
## it a new value with the equals sign.
a = 99

print( "Values of a, x, y after reassigning a:" )
print( a,x,y )


## Remember that the assignment operator works from right to left,
## and is a binary operator (takes two inputs).
## This expression would be evaluated in this order:
# y = 9
# x = y
# a = x
a = x = y = 9

print( "Values of a, x, y after \"chained\" assign:" )
print( a,x,y )

## We can assign a variable based on its existing value.
x = x + 1

print( "Values of a, x, y after x increment:" )
print( a,x,y )

x += 1
print( "Values of a, x, y after x increment:" )
print( a,x,y )

