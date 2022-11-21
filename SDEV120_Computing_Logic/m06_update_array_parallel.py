###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts a user to enter the name and 
## grade of a student then updates the student's grade 
## from an existing array.
###################################################

## Here are the start arrays.
student_names = ['Alf','Brit','Cory']
student_grades = [81,94,72]

## Get the student to remove
student = input( 'Enter student name: ' )
grade = int(input( 'Enter student grade: ' ))

if student in student_names:
    ## Get the index of the student name
    student_index = student_names.index( student )
    ## Update the grades array at this index
    student_grades[student_index] = grade

## Print the arrays
for i in range( 0, len(student_names), 1 ):
    print( student_names[i] + ": " + str( student_grades[i] ) )
