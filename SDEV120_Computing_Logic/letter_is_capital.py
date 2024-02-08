###################################################
## Mike Jovanovich
## SDEV 120 - M02
## This program prompts a user to input a letter,
## then tells the user whether it is a capital letter.
###################################################

## Prompt the user for a letter.
input_letter = input( "Enter a letter: " )
print( "The type of input_letter is: " + str(type(input_letter)) )

## Convert that letter to an int.
converted_letter = ord( input_letter )
print( "The type of converted_letter is: " + str(type(converted_letter)) )

## Use an ASCII lookup on the int to figure out if it's capital.
if converted_letter < 65:
    print( "Letter " + input_letter + " is not capital." )
elif converted_letter > 90:
    print( "Letter " + input_letter + " is not capital." )
else:
    print( "Letter " + input_letter + " is capital." )
