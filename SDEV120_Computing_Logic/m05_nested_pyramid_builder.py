######################################################
## 20221101
## Mike Jovanovich
## "Pyramid Builder" program.
## Basic demo of nested loops.
######################################################

n = int(input( "Enter a number between 5 and 10: " ))

## 'Top' of pyramid
for i in range( 1, n+1, 1 ):
    for j in range( 1, i+1, 1 ):
        print( "*", end="" )
    print()

## 'Bottom' of pyramid
for i in range( 1, n+1, 1 ):
    for j in range( n+1, i, -1 ):
        print( "*", end="" )
    print()

