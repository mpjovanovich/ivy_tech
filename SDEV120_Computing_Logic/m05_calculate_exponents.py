## Prompt the user to enter a number between 1 and 10. Print all of the base 
## values raised to that power that are less than 1000; e.g. 1^n, 2^n, 3^n, ...

n = int( input( "Enter a power between 1 and 10: " ) )

base = 1
x = base**n

while x <= 1000:
    print( x )
    base += 1
    x = base**n
    
