######################################################
# Mike Jovanovich
# 20221102
# This program accepts a string from the user, then 
# prints a message for each letter telling the user
# its position in the overall string.
# We introduce the concept of efficient loop calculations.
######################################################

input_string = input( 'Enter a string: ' )

####################################################
# Bad way...
####################################################

current_position = 1
for l in input_string:
    letter_count = len( input_string )
    print( 'The letter ' + l + ' is in position ' + 
        str(current_position) + '/' + str(letter_count) )
    current_position += 1


####################################################
# Good way...
####################################################

## ## We pulled some work out of the loop body, so that
## ## we don't have to do the same thing each time it runs.
## letter_count = str(len( input_string ))
## current_position = 1
## for l in input_string:
##     print( 'The letter ' + l + ' is in position ' + 
##         str(current_position) + '/' + letter_count )
    current_position += 1
