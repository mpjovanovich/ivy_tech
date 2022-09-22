###################################################
## Mike Jovanovich
## SDEV 120 - M02
## This program prompts a user to input a letter,
## then tells the user whether it is a capital letter.
###################################################

def main():
    ## Prompt the user for a letter.
    input_letter = input( "Enter a letter: " )
    
    ## Call our method to see if it's capital.
    is_capital = LetterIsCapital( input_letter )

    ## Call the method we made to print output based on the result.
    PrintResult( input_letter, is_capital )

    ## When a function returns nothing, it's called a void function.
    ## We don't have to put the return keyword in here if it's void - it's optional.
    ## Be consistent with your choice throughout the code.
    return

def LetterIsCapital( letter ):

    ## Declare a boolean variable and initialize it.
    is_capital = False

    ## Convert the input letter to an int.
    converted_letter = ord( letter )

    ## Use an ASCII lookup on the int to figure out if it's capital.
    if converted_letter < 65:
        is_capital = False
    elif converted_letter > 90:
        is_capital = False
    else:
        is_capital = True

    return is_capital

def PrintResult( letter, is_capital ):
    if is_capital:
        print( "Letter " + letter + " is capital." )
    else:
        print( "Letter " + letter + " is not capital." )

    return

## This is the program start point.
## Functions must be defined before calling main
main()

