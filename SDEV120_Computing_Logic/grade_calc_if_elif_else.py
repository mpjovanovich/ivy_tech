grade = input("Enter a grade: ")
grade = int( grade )

if grade > 90:
    print( "Grade is A")
elif grade > 80:
    print( "Grade is B")
elif grade > 70:
    print( "Grade is C")
elif grade > 60:
    print( "Grade is D")
else:
    print( "Failed" )
    
print(grade)
