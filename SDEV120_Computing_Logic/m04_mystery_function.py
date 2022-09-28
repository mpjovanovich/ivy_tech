###############################################################
##
## Mike Jovanovich
## 20220927
## This program does ???
##
###############################################################

NUMERICAL_INPUT_BOUNDARY = 999999999

def SomeFunction( first, second ):
    result = first
    if first > second:
        result = first
    else:
        result = second
    return result

## Does this do the same thing as above?
def SomeFunction_v2( first, second ):
    result = first
    if first < second:
        result = second
    return result

## Does this do the same thing as above?
def SomeFunction_v3( first, second ):
    if first > second:
        return first
    else:
        return second

x = 0
y = 0

## Why init these to these particular values?
result = -1 * NUMERICAL_INPUT_BOUNDARY

x = int( input( "Enter a number: " ) );
y = int( input( "Enter a number: " ) );

result = SomeFunction( result, x )
result = SomeFunction( result, y )

print( "Max: " + str( result ) )

## result = SomeFunction_v2( result, x )
## result = SomeFunction_v3( result, x )


