## Author:  [Firstname Lastname]
## Date:    [Date]
## This program accepts a four bit binary number from the user as input.
## The user must enter the digits one at a time starting with the most
## significant bit (leftmost) and moving toward the least significant bit (rightmost).
## Each of the component binary digits are displayed in decimal representation,
## then the result (sum) is displayed as output.


## This function accepts a bit value (1 or zero) as a string and its position within the binary number.
## It returns the decimal equivalent as an integer.
def ConvertBinaryToDecimal( bit_value, position ):
    ## bit_value was passed into this function as a string.
    ## In order to do math on it we will first convert it to an integer
    bit_value = int( bit_value )
    
    ## The * operator is multiplication
    ## The ** operator is Python's way of doing exponents - 2^position
    ## The calculation below is:
    ##      (2^position) x bit_value
    result = 2**position * bit_value
    
    ## Return the integer that we just calculated to the calling function (main)
    return result


def main():
    ## Prompt the user for input.
    ## We will refer to the four bits by their position - [three][two][one][zero]
    ## E.g: If the input binary number is 0 1 0 1 then the position three bit is 0, the position two bit is 1...

    ## Get the bit (zero or one) at position three and calculate its decimal representation.
    ## Then call our function to do the conversion and store the result in a variable.
    position_three_bit = input( 'Enter the position three bit: ' )
    position_three_decimal = ConvertBinaryToDecimal( position_three_bit, 3 )
    print( 'The decimal equivalent is: ' + str( position_three_decimal ) )
    
    ## Get the bit (zero or one) at position two and calculate its decimal representation.
    ## Then call our function to do the conversion and store the result in a variable.
    position_two_bit =   input( 'Enter the position two bit: ' )
    ## TODO: Get and print this decimal value.
    
    ## Get the bit (zero or one) at position one and calculate its decimal representation.
    ## Then call our function to do the conversion and store the result in a variable.
    position_one_bit =   input( 'Enter the position one bit: ' )
    ## TODO: Get and print this decimal value.
    
    ## Get the bit (zero or one) at position zero and calculate its decimal representation.
    ## Then call our function to do the conversion and store the result in a variable.
    position_zero_bit =  input( 'Enter the position zero bit: ' )
    ## TODO: Get and print this decimal value.

    decimal_number = None
    ## TODO: Sum the decimal values above to get the total decimal result. Store in the variable decimal_number.

    ## This temporary variable helps us write the print statement in a more compact form.
    binary_number = position_three_bit + position_two_bit + position_one_bit + position_zero_bit
    
    ## decimal_number is currently an int. We have to convert it to a string to use it in the print function.
    ## We can do this with the str function.
    decimal_number = str( decimal_number )

    ## Print the output of the program.
    print( '--------------------' )
    print( 'You entered the binary number ' + binary_number )
    print( 'The decimal equivalent is ' + decimal_number )


## This is the entry point for the program.
main()
