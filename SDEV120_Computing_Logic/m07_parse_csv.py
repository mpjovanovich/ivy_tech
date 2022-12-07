'''
Mike Jovanovich
20221207

Write a program that accepts a CSV file as input. 
The file must have a header row with column labels. 
There may be one to infinite columns.
All other rows are data rows.
There may be zero to infinite data rows.
Prompt to user to enter a column name, then print the distinct values for that column.
'''

## This demo file was taken from:
## https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities
filename = input( 'Enter the path to the CSV file: ' )

## Prompt the user for a column name.
## Convert it to lowercase so that we can ignore differences in case
## when trying to find the column in the header row.
col_name = input('Enter a column name: ' ).lower()

## Initialize an empty result set.
result = []

## Open the file for read only.
with open( filename, 'r' ) as f:
	## Grab the first row and store in a string variable.
	## The strip function gets rid of the \n character at the end of the line.
    header_record = f.readline().strip().lower()

	## Split the fields by looking for a comma, and store them in an array.
    header_fields = header_record.split(',')

	## Within that array find the index of the column that the user entered.
    col_index = header_fields.index( col_name )

	## Get the first data row (second row of the file)
    data_record = f.readline().strip()

	## As long as the current row is not empty...
    while data_record != '':
        
		## Split the data row.
        data_fields = data_record.split(',')
        
		## Check what's in the array of data fields at the position of the column
		## that the user asked for. If it is not in the result array then add it.
		## We check this so that we don't add duplicate values.
        if data_fields[col_index] not in result:
            result.append( data_fields[col_index] )

		## Get the next row for processing. 
        data_record = f.readline()

## Sort the array - just to make it readable.
result.sort()
for r in result:
    print( r )

