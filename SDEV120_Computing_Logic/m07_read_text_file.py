
###################################################
## Mike Jovanovich
## SDEV 120
## This program demos several ways to read a file in Python.
###################################################

filename = "temp_data.txt"

## Note: The repr function prints control characters (e.g. line feeds) 
## using their text representations.

####################################################
## Read the whole file at once.
####################################################
print( "Reading the whole file:" )
with open( filename, mode="r" ) as f:
    data = f.read()
    print( repr( data ) )
print()


####################################################
## Read one line at a time.
####################################################
print( "Reading one line at a time:" )
with open( filename ) as f:
    ## Read one line 
    line = f.readline()

    ## This line says "while the variable 'line' is not empty".
    while line != '':
        print( "Line: " + repr(line) )
        line = f.readline()
print()


####################################################
## Read one char at a time.
####################################################
print( "Reading one char at a time:" )
with open( filename ) as f:
    ## Read one character
    c = f.read(1)

    ## This line says "while the variable 'c' is not empty".
    while c != '':
        print( "Char: " + repr(c) )
        c = f.read(1)
print()
