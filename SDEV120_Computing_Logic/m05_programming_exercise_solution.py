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

    for y in range( map_size, 0, -1 ):
        ## Print the y axis labels
        print( str(y) + SPACER, end = "" )

        for x in range( 1, map_size + 1, 1 ):
            if x == treasure_x and y == treasure_y:
                print( "X" , end = "" )
            else:
                print( " " , end = "" )
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
    if coordinate < 1 or coordinate > map_size:
        return False
    else:
        return True

def main():
    valid_map_size = False
    map_size = int( input( "Enter the size of the map in the range (1,9): " ) )
    valid_map_size = map_size_is_valid( map_size )

    while map_size_is_valid( map_size ) == False:
        print( "Invalid map size - must fall within range (1,9)." )
        map_size = int( input( "Enter the size of the map in the range (1,9): " ) )
        valid_map_size = map_size_is_valid( map_size )

    valid_coordinate = False
    treasure_x = int( input( "Enter the x coordinate for the treasure: " ) )
    valid_coordinate = coordinate_is_valid( treasure_x, map_size )

    while valid_coordinate == False:
        print( "Invalid coordinate - outside bound of map." )
        treasure_x = int( input( "Enter the x coordinate for the treasure: " ) )
        valid_coordinate = coordinate_is_valid( treasure_x, map_size )

    valid_coordinate = False
    treasure_y = int( input( "Enter the y coordinate for the treasure: " ) )
    valid_coordinate = coordinate_is_valid( treasure_y, map_size )

    while valid_coordinate == False:
        print( "Invalid coordinate - outside bound of map." )
        treasure_y = int( input( "Enter the y coordinate for the treasure: " ) )
        valid_coordinate = coordinate_is_valid( treasure_y, map_size )

    print_map( map_size, treasure_x, treasure_y )

## This is the entry point for the program.
main()
