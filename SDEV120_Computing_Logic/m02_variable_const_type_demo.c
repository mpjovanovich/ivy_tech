/******************************************************
* Mike Jovanovich
* SDEV 120 - M02
* This program is a demo of variables and constants in C.
******************************************************/
#include <stdio.h>
 
int main(int argc, char *argv[]) 
{
    // Data type, name/identifier, value 
    int some_number = 0;

    // I can reassign a value to a variable as often as
    // I want.
    some_number = 7;
    some_number = 99999;
    some_number = -32;

    // Let's declare a constant value
    const float PI = 3.14159;

    // The compiler will not let us change the value of PI
    // since we used the const keyword.
    // Uncomment this code and try...
    //PI = 123;

    return 0;
}
