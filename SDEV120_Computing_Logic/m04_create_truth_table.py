######################################################
## 20220921
## Mike Jovanovich
## "Logical Operators" program.
## Contains a demo of logical operators, as well as some
## demos on order of operations.
######################################################

def CreateTruthTable( operator ):

    ## Print the header rows.
    ## The \t character is how we insert a tab.
    print( 'x\ty\t(x ' + operator + ' y)' )
    print( '------------------------' )
    
    EvalulateTruth( operator, True, True )
    EvalulateTruth( operator, True, False )
    EvalulateTruth( operator, False, True )
    EvalulateTruth( operator, False, False )
    print() ## Print a blank line to make it look neat.

def EvalulateTruth( operator, x, y ):

    ## Take the expression 'x and y' and store the results in the variable
    ## on the left.

    ## Initialize the boolean variable that will hold the result
    result_of_operation = False
    if( operator == 'and' ):
        result_of_operation = x and y
    elif( operator == 'or' ):
        result_of_operation = x or y

    print( str(x) + '\t' + str(y) + '\t' + str(result_of_operation) )

operator = input( 'Enter "and" or "or" for the operator: ' )
print() ## Print a blank line to make it look neat.

CreateTruthTable( operator )

