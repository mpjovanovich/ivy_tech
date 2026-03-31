## Binary search algorithm - determine if list contains city
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

## Use flag variable to indicate whether city was fund
found = False

## Prompt the user for the city that they want to find
target_city = input('Enter city to find: ')

## Check if the target is at the middle value
while found == False:
    ## Get middle value from the current list
    middle_index = math.floor(len(cities) / 2)
    city = cities[middle_index]

    if city == target_city:
        found = True
        break
    elif len(city) == 1:
        ## If this is the last item in the list exit the loop;
        ## there is nothing left to search for
        break
    elif target_city < city:
        ## Cut list in half
        ## Use bottom half of the current list
        cities = cities[:middle_index]
    elif target_city > city:
        ## Cut list in half
        ## Use top half of the current list
        cities = cities[middle_index + 1:]

## Let user know if city was found
print(f'Found: {found}')
