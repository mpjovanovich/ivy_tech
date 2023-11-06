STUDIO_COMMISSION = 30.0
ONE_BEDROOM_COMMISION = 55.0
TWO_BEDROOM_COMMISION = 75.0
THREE_BEDROOM_COMMISION = 100.0 

salesperson_id = input( "Enter the salesperson ID: " )
salesperson_name = input( "Enter the salesperson name: " )
num_bedrooms = int(input( "Enter the number of bedrooms: " ))

commission = 0
if num_bedrooms == 0:
    commission = STUDIO_COMMISSION
elif num_bedrooms == 1:
    commission = ONE_BEDROOM_COMMISION
elif num_bedrooms == 2:
    commission = TWO_BEDROOM_COMMISION
elif num_bedrooms == 3:
    commission = THREE_BEDROOM_COMMISION

print( "--------------------" )
print( f"Salesperson = {salesperson_name}" )
print( f"ID = {salesperson_id}" )
print( f"Commission = ${commission:.2f}" )
print( "--------------------" )
