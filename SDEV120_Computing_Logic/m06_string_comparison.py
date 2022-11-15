###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts the user to enter two strings.
## It prints "Match." if the are the same, and "Not a match."
## if they are different.
###################################################

## Get user input.
string1 = input( 'Enter the first string: ' )
string2 = input( 'Enter the first string: ' )

## We start by initializing a comparison variable. We will 
## assume that the strings are the same until we find that they're not.
strings_match = True

## If we look at some letter in the first string and the second string doesn't
## have the same letter in that position, then it's not a match.
for i in range( 0, len( string1 ), 1 ):
    if string1[i] != string2[i]:
        strings_match = False
        ## We want this here so we can abort the loop as soon as we know
        ## that they're not a match. No point comparing the remaining letters.
        break 
        

## Print the result.
if strings_match == True:
    print( 'Match.' )
else:
    print( 'Not a match.' )
