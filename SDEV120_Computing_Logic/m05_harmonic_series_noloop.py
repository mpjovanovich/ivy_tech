## Mike Jovanovich
## 20221024
## This program accepts a number of terms from the user and
## calculates the harmonic series up to that term.

n = int(input( "Enter final term for series: " ))

## Initialize the result
result = 0.0

## Start adding the terms one at a time.
if n >= 1:
   result += 1/1 
if n >= 2:
   result += 1/2 
if n >= 3:
   result += 1/3 

## What would we do if we needed more terms?
## This is practically impossible without a loop.

print( f"The first {n} terms of the harmonic series sum to {result}" )

