###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts a user to enter the name of a student 
## then adds the student to an existing array.
###################################################

## Here's the start array
student_names = ['Alf','Brit','Cory']

## We add the user's new record here
student = input( 'Enter student name: ' )
student_names.append( student )

## Print the array
for i in range( 0, len(student_names), 1 ):
    print( student_names[i] )

