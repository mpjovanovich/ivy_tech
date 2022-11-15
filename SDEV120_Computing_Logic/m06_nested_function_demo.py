###################################################
## Mike Jovanovich
## SDEV 120
## This program demonstrates how functions can be
## nested inside of each other.
###################################################

arr = ['a','b','c','d']

## Method 1 - "condensed" format:
## How many function calls are in the line below? 
## What are the names of the functions that are called?
## In what order are these functions evaluated?
print( 'The length of the array is: ' + str( len( arr ) ) )

## TODO: demo in class.

## Method 2 - "expanded" format:
length = len( arr )
s_length = str( length )
s_output = 'The length of the array is: ' + s_length
print( s_output )

