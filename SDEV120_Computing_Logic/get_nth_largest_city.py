###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts the user to enter a value for
## the 'nth' largest city in the US for 2022 and prints
## that city.
###################################################

## Let's assume we have a list that is already sorted.
largest_cities = [
    'New York City, NY (Population: 8,622,357)',
    'Los Angeles, CA (Population: 4,085,014)',
    'Chicago, IL (Population: 2,670,406)',
    'Houston, TX (Population: 2,378,146)',
    'Phoenix, AZ (Population: 1,743,469)',
    'Philadelphia, PA (Population: 1,590,402)',
    'San Antonio, TX (Population: 1,579,504)',
    'San Diego, CA (Population: 1,469,490)',
    'Dallas, TX (Population: 1,400,337)',
    'San Jose, CA (Population: 1,036,242)' ]

position = int( input( 'Enter which largest city you want from 1-10: ' ) )

while position < 1 or position > 10:
    position = int( input( 'Enter which largest city you want from 1-10: ' ) )

## Print the one that was asked for.
## Note: we have to subtract one from the user-entered position 
## because the array is zero indexed.
print( largest_cities[position - 1] )

