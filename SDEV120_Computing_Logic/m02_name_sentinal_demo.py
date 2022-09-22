######################################################
# Mike Jovanovich
# SDEV 120 - M02
# This program shows how we can use a sentinal value
# to control execution of a program.
######################################################

## Enter into a 'while' loop. The loop will repeat infinitely until the sentinal
## value is provided.
EXIT_VALUE = 'Giln'

while True:

    ## Get text input from the user via the console and store it in the 'name' variable.
    name = input('Enter your name: ')

    ## Check whether the name that the user entered matches our sentinal value, 'Giln'.
    if name == EXIT_VALUE:
        ## If yes, print a success message and exit the loop / program.
        print( 'Correct - your name is Giln. You may now exit the program.' )
        break
    else:
        ## If no, print a failure message and repeat the loop.
        print( 'You guessed [' +name + ']. Failure - try again.')


