###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts a user to enter the name of a student 
## then removes the student from an existing array and another
## parallel array.
###################################################

## Here are the start arrays.
student_names = ['Alf','Brit','Cory']
student_grades = [81,94,72]

## Get the student to remove
student = input( 'Enter student name: ' )

## We can't just do "student_names.remove( student ).
## That would leave the student's grade in the grades array.

if student in student_names:
    ## Get the index of the student name
    student_index = student_names.index( student )
    ## Remove the contents of this index for all arrays in the
    ## set of parallel arrays.
    student_names.pop( student_index )
    student_grades.pop( student_index )

## Print the arrays
for i in range( 0, len(student_names), 1 ):
    print( student_names[i] + ": " + str( student_grades[i] ) )
