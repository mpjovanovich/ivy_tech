######################################################
# Mike Jovanovich
# 20221102
# This program shows how we can use a sentinal value
# to control execution of a program.
######################################################

## The user will be repeatedly prompted to enter a name until the
## mystery name is provided.
MYSTERY_NAME = 'Pencil Pete'

## Initialize the name to an empty value.
name = ''

while name != MYSTERY_NAME:

    ## Get text input from the user via the console and store it in the 'name' variable.
    name = input('Guess a name: ')

    ## Check whether the name that the user entered matches our sentinal value, 'Giln'.
    if name == MYSTERY_NAME:
        ## If yes, print a success message and exit the loop / program.
        print( 'Correct!' )
    else:
        ## If no, print a failure message and repeat the loop.
        print( 'You guessed [' +name + ']. Failure - try again.')

