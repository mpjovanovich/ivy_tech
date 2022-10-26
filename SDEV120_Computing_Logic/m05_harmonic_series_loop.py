## Mike Jovanovich
## 20221024
## This program accepts a number of terms from the user and
## calculates the harmonic series up to that term.

n = int( input( "Enter final term for series: " ) )

## Initialize the result
result = 0.0

for i in range( 1, n + 1, 1 ):
    result += 1/i

## Or we could use a while loop. Both are correct.
## i = 1
## while i <= n:
##    result += 1/i
##    i = i+1

print( f"The first {n} terms of the harmonic series sum to {result}" )

