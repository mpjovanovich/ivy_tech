###################################################
## Mike Jovanovich
## SDEV 120
## This is a testbed for methods in Python.
###################################################

## Default parameters (optional named arguments for some parameters)
## Owners and pets are required by the caller - everything else is optional.
## def PrintPets( owners, pets, seperator=': ', include_null_pets=True ):
##     print( 'PETS' )
##     print( '--------------------------' )
##     for i in range( len( owners ) ):
##         pet = pets[i]
##         if pet != '' or include_null_pets:
##             print( owners[i] + seperator + pets[i] )
##     print( '--------------------------' )

## Classic option - positional arguments
def PrintPets( owners, pets, separator, include_null_pets ):
    print( 'PETS' )
    print( '--------------------------' )
    for i in range( len( owners ) ):
        pet = pets[i]
        if pet != '' or include_null_pets:
            print( owners[i] + separator + pets[i] )
    print( '--------------------------' )


owners = [
'George Washington',
'Catherine the Great',
'Cersei Lannister',
'Moses',
'Valis',
]
pets = [
'Larry the Hen',
'Pauline (\'Five Paws\') Puma',
'',
'Ollie Orangecat',
'Subsatellite Sirius-Eta-971'
]
show_empty_pets = False

## Positional arguments
##PrintPets( owners, pets, ': ', True )
##PrintPets( owners, pets, ' - ', False )

## Named arguments
## NOTE: The argument name for the function/method DOES NOT have to match our local
## variable name; see "include_null_pets" below.
## PrintPets( owners=owners, pets=pets, separator=': ', include_null_pets=show_empty_pets )

## Defaults arguments
## PrintPets( owners, pets )

