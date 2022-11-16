## Author:  [Firstname Lastname]
## Date:    [Date]

## In this program we have an existing course roster. 
## We keep track of student names, and whether the student is
## active or inactive. Students should not appear on the roster
## more than once.

## The user is prompted to enter a letter indicating a command:
##   "m" for modify student 'active' status
##   "p" for print roster.
##   "q" for quit.


## This constant tells us whether an item was found by the "get_student_index" function.
NOT_FOUND_INDEX = -1
## This constant defines how many characters each column is in the print.
PRINT_COLUMN_WIDTH = 24 

def get_student_index( students, name ):

    student_index = NOT_FOUND_INDEX

    ## TODO:
    ## Loop through the students, comparing each element against "name".
    ## If a match is found, store the index of the match in "student_index"
    ## for ???
        ## if ???
            ## student_index = ???
    
    ## Return the result to the calling function.
    return student_index


def modify_student_status( status, student_index ):

    ## TODO:
    ## Toggle the status from T to F or from F to T
    ## depending on the current value.
    ## status[student_index] = ???
    return


def print_students( students, status ):

    for i in range( 0, len(students), 1 ):
        first_col_string = 'Student: ' + students[i]
        second_col_string = 'Active: ' + str(status[i])

        ## The "ljust" command adds spaces to the end of the string until it meets 
        ## the specified length. Try adjusting the constant value and see what happens.
        print( first_col_string.ljust( PRINT_COLUMN_WIDTH ) + 
            second_col_string.ljust( PRINT_COLUMN_WIDTH ) )


def main():

    ## This array is the starting list of students.
    students = [ 'Ivan', 'Lorne', 'Junna', 'Caitlyn', 'Edward' ]
    ## This array tells whether the corresponding student is active (True) or inactive (False).
    status = [ True, True, True, True, False ]

    ## Prompt the user to enter a command letter.
    command = input( 'Enter a command (m,p,q): ' )

    while command != 'q':

        if command == 'm':
            ## Modify 'status' status
            name = input( 'Enter student name: ' )
            student_index = get_student_index( students, name )

            ## TODO:
            ## Only modify the student status if a match was found.
            ## Check the value of "student_index".
            ## if ???
            modify_student_status( status, student_index )

        elif command == 'p':
            ## Print roster
            print_students( students, status )

        ## Prompt the user to enter a command letter.
        command = input( 'Enter a command (m,p,q): ' )


## This is the entry point for the program.
main()

