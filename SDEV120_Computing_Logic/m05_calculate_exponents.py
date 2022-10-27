
n = int( input( "Enter a power between 1 and 10: " ) )

base = 1
x = base**n

while x <= 1000:
    print( x )
    base += 1
    x = base**n
    
