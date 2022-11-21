###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts a user to enter a letter
## then searches the list for that letter.
###################################################
import random
ARRAY_SIZE = 10

## Create an array of random lowercase letters.
random_letters = random.sample( 'abcdefghijklmnopqrstuvwxyx', ARRAY_SIZE )

## Get a letter from the user.
letter = input( 'Enter a lowercase letter to find: ' )

## Search the array.
found = False
for i in range( 0, ARRAY_SIZE, 1 ):
    if letter == random_letters[i]:
        found = True
        ## We can "short circuit" the loop here using break.

## Print the array
print( 'Array:', end=' ' )
for i in range( 0, ARRAY_SIZE, 1 ):
    print( random_letters[i], end=' ' )
print()

## Print whether the user's letter was found.
print( 'Found: ' + str(found) )

