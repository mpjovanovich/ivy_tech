///////////////////////////////////////////////////////////////
//
// 20220828
// Mike Jovanovich
// 'Length of a String' program.
// In this program the user is prompted to enter text. The 
// program returns the length of the string. The program quits
// when the user enters the string 'quit'.
//
// You can compile the program on a terminal with gcc, like the following:
// gcc c_string_sentinal.c -o c_string_sentinal
// You can then run the program by typing ./c_string_sentinal
//
///////////////////////////////////////////////////////////////

// Load standard libraries so that we have access to function calls
// that we're going to need.
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Every C program has a main function - that's how it knows where to start.
int main( int arc, char *argv[] )
{
    // Declare the string variable to hold text that the user enters.
    char user_input[255];
    int length = 0;

    // Get the user input until the user types 'quit':
    while( 1 == 1 )
    {

        // Prompt the user to enter some text
        printf( "Put in some text: " );

        // Store the results in variable 'user_input'.
        scanf( "%254s", user_input );

        if( strcmp(user_input,"quit" ) == 0 )
            return 0;

        length = 0;
        int char_index = 0;
        char current_char = -1;
        while( current_char != '\0' )
        {
            length++;
            printf( "The current character is: [%c].\r\n", user_input[char_index] );
            current_char = user_input[char_index];
            char_index++;
        }

        printf( "The length of your string is:  %d characters.\r\n", length - 1 );
        printf( "Type 'quit' to exit the program, or continue.\r\n" );
    }

    return 0;
}
