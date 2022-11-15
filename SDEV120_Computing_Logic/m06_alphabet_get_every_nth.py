###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts the user to enter a value of n
## then prints every nth value of the alphabet.
###################################################

## This python list (array) holds characters for each letter of the alphabet.
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

n = int( input( 'Enter a value for "n": ' ) )

## Where did we get the arguments that we're plugging into the range function below?
for i in range( n-1, len( alphabet ), n ):
    print( alphabet[i], end=' ' )

print()
