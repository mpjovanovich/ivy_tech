###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts a user to enter five years' worth
## of temperatures for the current day of the year, 
## calculates the average,then prints yearly temperatures 
## that were input and the delta relative to the average.
###################################################

## This is how many decimal places we want to show in the final result.
PRECISION = 2

## This is the number of temperatures that we will prompt the user to enter.
TEMPERATURE_SIZE = 5

## For this program we want to create an array then change the values.
## We will initialize the array with zeroes.
temps = []
for i in range( 0, TEMPERATURE_SIZE, 1 ):
    temps.append( 0.0 )

## Prompt the user to enter temperature values, then store those
## values in the array.
for i in range( TEMPERATURE_SIZE - 1, -1, -1 ):
    current_temp = float( input( f'Enter the temperature from {i} years ago: ' ) )
    temps[i] = current_temp

## Add together all of the values in the array
temps_sum = 0
for i in range( 0, TEMPERATURE_SIZE, 1 ):
    temps_sum += temps[i]

## DEMO: SHOULD THIS BE INSIDE OR OUTSIDE OF THE LOOP?
## How many times will the average be calculated?
## Calculate the average.
##temps_average = temps_sum / TEMPERATURE_SIZE 

## Print the delta for each year relative to the average.
for i in range( TEMPERATURE_SIZE - 1, -1, -1 ):

    ## DEMO: SHOULD THIS BE INSIDE OR OUTSIDE OF THE LOOP?
    ## How many times will the average be calculated?
    ## Calculate the average.
    temps_average = temps_sum / TEMPERATURE_SIZE 

    ## Calculate how far off the year "i" is from the average, then print.
    current_temp = temps[i]
    temp_delta = round( current_temp - temps_average, PRECISION )
    print( f'Temperature {i} years ago: {current_temp}; Delta from average: {temp_delta}' )

