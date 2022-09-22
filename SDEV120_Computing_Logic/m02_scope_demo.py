
###################################################
## Mike Jovanovich
## SDEV 120 - M02
## This program demonstrates several concepts related to scope
###################################################

## This is a global variable.
some_number_global = 1

def SetGlobals():
    ## Python requires the use of the global keyword in order
    ## to use globals inside of a function.
    global some_number_global
    some_number_global = 2
    return

## We are allowed to use the name some_number as the input identifier here
## even though we've used it as a variable name in the main function -
## but the variable being operated on within AddOne is NOT the same as some_number.

## AddOne makes its own copy of the input variable to work with as a local variable.
## This variable is "scoped" to AddOne. When the function is done, the copy falls out of scope
## and is inaccessable to the rest of the program.
def AddOne( some_number ):
    some_number = some_number + 1
    return

## Variables have been renamed in this version to add some clarity.
## We also return a result.
def AddOneV2( input_number ):
    output_number = input_number + 1
    return output_number

def main():
    ################################################################
    ## Globals demo
    ################################################################

    ## We can use the global variable inside of another function.
    ## This variable is the one defined at the top of the file.
    print( some_number_global )

    ## We will change the value of the global variable inside of below method.
    SetGlobals()
    print( some_number_global )

    ################################################################
    ## Locals demo
    ################################################################

    ## Make a new int. It will be scoped to the main function.
    some_number = -1

    ## See notes in the method header. This doesn't achieve the result we want.
    AddOne( some_number )
    print( some_number )

    ## Call the new and improved function. But it still doesn't work. What's missing?
    AddOneV2( some_number )
    print( some_number )

    ## We need to use the assignment operator to take the output from AddOneV2 and store 
    ## the result in some_number.
    some_number = AddOneV2( some_number )
    print( some_number )

main()
