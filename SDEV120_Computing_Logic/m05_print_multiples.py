
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

