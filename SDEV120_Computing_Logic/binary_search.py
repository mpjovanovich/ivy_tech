################################################################
## BINARY SEARCH ALGORITHM
################################################################

## This program determines if list contains city. This search is performed "in
## place"; we do not make a copy # of the list.

import math

cities = [
    "Amsterdam",
    "Bangkok",
    "Barcelona",
    "Beijing",
    "Berlin",
    "Buenos Aires",
    "Cairo",
    "Cape Town",
    "Chicago",
    "Dubai",
    "Dublin",
    "Istanbul",
    "Jakarta",
    "Johannesburg",
    "Lagos",
    "Lisbon",
    "London",
    "Los Angeles",
    "Madrid",
    "Melbourne",
    "Mexico City",
    "Miami",
    "Montreal",
    "Mumbai",
    "Nairobi",
    "New York",
    "Oslo",
    "Paris",
    "Rome",
    "São Paulo",
    "Seoul",
    "Shanghai",
    "Singapore",
    "Stockholm",
    "Sydney",
    "Tokyo",
    "Toronto",
    "Vienna",
    "Warsaw",
    "Zürich",
]

## Flag variable to indicate whether city was fund
found_index = -1

## These variables determine the current portion of the list
## that we are searching.
lower_bound = 0
upper_bound = len(cities)

## Prompt the user for the city that they want to find
## Lowercase to make case insensitive comparison
target_city = input('Enter city to find: ').strip().lower()

## Check if the target is at the middle value
while True:
    ## Determine halfway point based on current bounds
    midpoint = math.floor((upper_bound - lower_bound) / 2)

    ## Get middle value from the current list
    middle_index = math.floor(lower_bound + midpoint)

    ## Get city from list
    ## Lowercase to make case insensitive comparison
    city = cities[middle_index].lower()

    if city == target_city:
        found_index = middle_index
        break
    elif target_city < city:
        ## Cut list in half by adjusting upper bound
        upper_bound = middle_index
    elif target_city > city:
        ## Cut list in half by adjusting lower bound
        lower_bound = middle_index + 1

    ## If there is nothing left to search, exit the loop
    if upper_bound == lower_bound:
        break

## Let user know if city was found
print(f'Index of city: {found_index}')
