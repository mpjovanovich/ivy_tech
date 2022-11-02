
#########################################
# This program removes all numbers from a
# user input string.
#########################################

input_string = input( 'Enter a string: ' )

output_string = ''
for char in input_string:
    
    if char.isnumeric() == True:
        continue

    output_string += char

print( 'This string without numbers is: ' + output_string )

