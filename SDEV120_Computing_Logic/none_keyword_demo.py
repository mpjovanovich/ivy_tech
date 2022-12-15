
def get_max( input_list ):
    # No... bad
    # max_value = 0
    # max_value = -99999999999
    # max_value = input_list[0]

    # Yes - good!
    max_value = None

    ## If the list is not empty, we will assign the first element
    ## as the max, then compare it against the other elements.
    if len( input_list ) > 0:
        max_value = input_list[0]
        for x in list:
            if max_value == None or x > max_value:
                max_value = x

    return max_value

## We start with an empty list.
my_list = []

## Run some code that may or may not add items to the list...
## ...
## ...

max_val = get_max( my_list )

if max_val == None:
    print( 'The list contains no elements.' )
else:
    print( 'The max value is ' + str(max_val) )
