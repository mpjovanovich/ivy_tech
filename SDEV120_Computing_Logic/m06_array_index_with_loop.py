###################################################
## Mike Jovanovich
## SDEV 120
## This program demonstrates basic indexing into an array
## using a for loop.
###################################################

## Here's a sample array...
arr = ['a','b','c','d']

## We can create a counter variable that we can then use to
## access an element by index - by its position within the array.
for i in range( len( arr ) ):
    print( 'The current index is: ' + str(i) )
    print( 'The array value at this position is: ' + arr[i] )

