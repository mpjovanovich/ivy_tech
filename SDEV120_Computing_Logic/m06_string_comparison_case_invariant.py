###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts the user to enter two strings.
## It prints "Match." if the are the same, and "Not a match."
## if they are different. Casing for letters does not matter.
###################################################

## Get user input.
string1 = input( 'Enter the first string: ' )
string2 = input( 'Enter the second string: ' )

## We start by initializing a comparison variable. We will 
## assume that the strings are the same until we find that they're not.
strings_match = True
string1 = string1.upper()
string2 = string2.upper()

## If we look at some letter in the first string and the second string doesn't
## have the same letter in that position, then it's not a match.
for i in range( 0, len( string1 ), 1 ):
    ## How many times will these conversions happen?
    ## Is there a better place to put them?

    if string1[i] != string2[i]:
        strings_match = False
        break 
        
## Print the result.
if strings_match == True:
    print( 'Match.' )
else:
    print( 'Not a match.' )
