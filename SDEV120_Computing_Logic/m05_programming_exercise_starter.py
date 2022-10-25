## Author:  [Firstname Lastname]
## Date:    [Date]
## This 'treasure hunt' program accepts a map size and an x and y 
## coordinate from the user. The map size must be no larger than 9.
## Coordinate provided by the user must fall within the map.
## It then paints a grid of the map, printing a capital 'X' on the 
## coordinates that the user provided.

BORDER_DELIMITER = '-'
SPACER = " "

## This will print a line of delimiters and spacers based on the size
## of the map.
def print_top_border( map_size ):
    print( BORDER_DELIMITER + SPACER, end = "" )
    for x in range( 1, map_size + 1, 1 ):
        print( BORDER_DELIMITER + SPACER, end = "" )
    print( BORDER_DELIMITER + SPACER, end = "" )

def print_x_labels( map_size ):
    print( BORDER_DELIMITER + SPACER, end = "" )
    for x in range( 1, map_size + 1, 1 ):
        print( str(x) + " ", end = "" )
    print( BORDER_DELIMITER + SPACER, end = "" )

def print_map( map_size, treasure_x, treasure_y ):

    ## Print the top border.
    print_top_border( map_size )
    print()

    for y in range( 1, map_size + 1, 1 ):
        ## Print the y axis labels
        print( str(y) + SPACER, end = "" )

        for x in range( 1, map_size + 1, 1 ):

            ## TODO: the line below should print either an empty spot on the map
            ## or an X if it matches the user coordinates. Replace it with the correct logic.
            print( "?" , end = "" )

            print( SPACER, end = "" )

        ## Print the final delimeter for the far right side of the map.
        print( BORDER_DELIMITER + SPACER, end = "" )
        print()

    ## Print the x axis labels.
    print_x_labels( map_size )
    print()

## This function returns false if the coordinate is outside the
## bounds of the map (1,9).
def map_size_is_valid( map_size ):
    if map_size < 1 or map_size > 9:
        return False
    else:
        return True

## This function returns false if the coordinate is outside the
## bounds of the map (1,map size).
def coordinate_is_valid( coordinate, map_size ):
    ## TODO: complete this function.
    return True 

def main():
    map_size = int( input( "Enter the size of the map in the range (1,9): " ) )
    while not map_size_is_valid( map_size ): 
        print( "Invalid map size - must fall within range (1,9)." )
        map_size = int( input( "Enter the size of the map in the range (1,9): " ) )

    treasure_x = int( input( "Enter the x coordinate for the treasure: " ) )
    ## TODO: call coordinate_is_valid function to validate input until it's valid.

    treasure_y = int( input( "Enter the y coordinate for the treasure: " ) )
    ## TODO: call coordinate_is_valid function to validate input until it's valid.

    print_map( map_size, treasure_x, treasure_y )

## This is the entry point for the program.
main()

