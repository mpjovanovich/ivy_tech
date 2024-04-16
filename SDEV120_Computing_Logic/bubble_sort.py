## ###############################################
## Bubble Sort Algorithm
## ###############################################

# For a good visual representation see:
# https://miro.medium.com/v2/resize:fit:1400/1*-qR66X2iwdcjhaqq10y9JQ.gif

values = [3, 7, -4, 1]

# We will compare one item to the next, so set the end
# to one position prior to the end to avoid an off-by-one
# index error.
current_end = len(values) - 1

## In the outer loop, quit once all of the values are locked in.
while current_end > 0:
    ## In the inner loop, compare pairs until we hit the
    ## "locked in" values.
    for i in range(0, current_end, 1):
        ## If the left value is greater than the right value...
        if values[i] > values[i + 1]:
            ## Swap!
            tmp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = tmp

    ## current end value is "locked in"
    ## decrement by one
    current_end = current_end - 1

print(values)
