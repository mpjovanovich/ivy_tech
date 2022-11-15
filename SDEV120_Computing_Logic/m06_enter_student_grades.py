###################################################
## Mike Jovanovich
## SDEV 120
## This program prompts a user to enter the name of a student 
## then the student’s final grade. It continues until the user 
## types “done”, then prints the names and grades.
###################################################

## Here's a sample array...
student_names = []
student_grades = []

student = input( 'Enter student name, or type "done": ' )

while student != 'done':
    grade = int( input( 'Enter student grade: ' ) )
    student_names.append( student )
    student_grades.append( grade )
    student = input( 'Enter student name, or type "done": ' )

for i in range( 0, len(student_names), 1 ):
    print( student_names[i] + ": " + str(student_grades[i]) )

