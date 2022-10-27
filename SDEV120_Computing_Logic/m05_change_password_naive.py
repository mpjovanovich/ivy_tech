## Prompt the user to enter a new password. Reject the password if it fails 
## to conform to the expected length (4-10 characters). Display a message 
## letting the user know if the password change was successful.

MIN_LENGTH = 4
MAX_LENGTH = 10

success = False
pwd = input( "Please enter a new password: " )

for i in range( 2 ):
    if len(pwd) < 4 or len(pwd) > 10:
        print( f"Password must be between {MIN_LENGTH} and {MAX_LENGTH} characters." )
        pwd = input( "Please enter a new password: " )
    else:
        success = True

if success:
    print( "Password has been reset." )
else:
    print( "Failed to change password: max password reset attempts exceeded." )
