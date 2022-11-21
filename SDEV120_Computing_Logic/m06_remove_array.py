###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts a user to enter the name of a student 
## then removes the student from an existing array.
###################################################

## Here's the start array
student_names = ['Alf','Brit','Cory']

## Get the student to remove.
student = input( 'Enter student name: ' )

## If we try to remove a value that isn't there we get an error.
## Try commenting the line below and see what happens.
if student in student_names:
    student_names.remove( student )

## Print the array
for i in range( 0, len(student_names), 1 ):
    print( student_names[i] )

