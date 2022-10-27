## Prompt the user to enter a dividend and divisor integer (division result = 
## dividend / divisor). Print all of the non-zero multiples of the divisor that 
## are less than or equal to the dividend. Keep track of the number of multiples 
## and print that value; this will be the whole portion the division.

dividend = int( input( "Enter a dividend: " ) )
divisor = int( input( "Enter a divisor: " ) )

whole_result = 0

## Inefficient method:
for i in range( 1, dividend + 1, 1 ):
    if i % divisor == 0:
        print( i )
        whole_result += 1

## ## Better method:
## for i in range( divisor, dividend + 1, divisor ):
##     print( i )
##     whole_result += 1

print( "Whole result from division: " + str(whole_result) )

