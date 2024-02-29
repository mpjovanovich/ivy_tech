###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts the user to enter a value of n
## between one and ten, then prints the top n cities
## by population for 2022.
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
    'San Jose, CA (Population: 1,036,242)',
    'West Lafayette, IN (P 100000)' ]

n = int( input( 'How many cities do you want to see (1-11)?: ' ) )

while n < 1 or n > 11:
    n = int( input( 'How many cities do you want to see (1-11)?: ' ) )

## Note: we have to add one to "i" in the print statement below
## because the array is zero indexed.
for i in range( len(largest_cities) - 1, len(largest_cities) -1 - n, -1 ):
    print( str( i + 1 ) + ": " + largest_cities[i] )

