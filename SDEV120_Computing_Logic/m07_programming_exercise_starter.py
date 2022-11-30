'''
Author:  [Firstname Lastname]
Date:    [Date]

In This program we read records from a file line by line.
The records consist of ID/name pairs, separated by a tilde (~).
These ID/name pairs are parsed and stored in parallel arrays.

The user is prompted to type a, p, or q to add, print, or quit.
'Add' prompts the user to enter an integer id, then a name.
The ID/name pair is then appended to the records file.
'Print' prints the raw contents of the records file.
'''
import os

## These constants store the path to the output file
OUTPUT_PATH = 'm07_prog_ex_output'
RECORDS_FILE_PATH = os.path.join( OUTPUT_PATH, 'records.dat' )

## These global variables store the records in memory
_record_ids = []
_record_names = []

def add_record( uid, name ):
    ## Add the record to the in memory parallel arrays.
    _record_ids.append( uid )
    _record_names.append( name )

    ## TODO: Add the record to the permanent file on disk.
    return

def load_records():
    ## Read the contents of the file that's on disk, and copy them to
    ## the in memory parallel arrays.
    if os.path.exists( RECORDS_FILE_PATH ):
        with open( RECORDS_FILE_PATH, mode='r' ) as records_file:
            for line in records_file:
                stripped_line = line.strip()
                ## TODO: add the id and name to the parallel arrays
    return

def print_raw_records():
    ## Print exactly what's in the file.
    if os.path.exists( RECORDS_FILE_PATH ):
        ## TODO: Print exactly what's in the file.
        ## Remove the line below.
        print()
    else:
        print( "No records to print." )
    return

def main():

    ## Create the output directory if it doesn't exist.
    if not os.path.exists( OUTPUT_PATH ):
        os.makedirs( OUTPUT_PATH )

    ## Load any existing records into the parallel arrays in memory.
    load_records()

    ## Prompt the user to enter a command letter.
    command = input( 'Enter a command (a,p,q): ' )

    while command != 'q':
        if command == 'a':
            uid = input( 'Enter ID number: ' )

            ## Don't create the record if this ID exists
            if uid in _record_ids:
                print( 'There is already a record with ID: ' + uid )
            else:
                name = input( 'Enter name: ' )
                add_record( uid, name )
        elif command == 'p':
            print_raw_records()

        ## Prompt the user to enter a command letter.
        command = input( 'Enter a command (a,p,q): ' )
    return

## This is the entry point for the program.
main()

