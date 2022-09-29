###############################################################
##
## Mike Jovanovich
## 20220927
## This program does ???
##
###############################################################

def SomeFunction( first, second ):
    result = first
    if first > second:
        result = first
    else:
        result = second
    return result

def SomeFunction_v2( first, second ):
    if first > second:
        return first
    else:
        return second

def SomeFunction_v3( first, second ):
    result = first
    if first < second:
        result = second
    return result

x = 0
y = 0
result = None

x = int( input( "Enter a number: " ) );
y = int( input( "Enter a number: " ) );

## result = SomeFunction( x, y )
## result = SomeFunction_v2( x, y )
## result = SomeFunction_v3( x, y )

print( "Result: " + str( result ) )
