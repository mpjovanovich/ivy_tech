/******************************************************
* Mike Jovanovich
* SDEV 120 - M02
* This program is a demo of the assigment operator.
******************************************************/
#include <stdio.h>
 
int main(int argc, char *argv[]) 
{
    printf( "\r\n" );

    ///////////////////////////////////////////////////////////
    // Explicit Conversion
    ///////////////////////////////////////////////////////////

    ///////////////////////////////////////
    // Letter to int conversion demo
    ///////////////////////////////////////

    // Variables are declared and initialized:
    // Data type, name/identifier, value 
    char some_letter = 'a';

    // Explicit conversion - we are using the cast operator,
    // (), to change a char to an int.
    int converted_letter = (int)some_letter;
    printf( "The letter '%c' has been converted to int: %d\r\n", some_letter, converted_letter );

    ///////////////////////////////////////
    // Float to int demo
    ///////////////////////////////////////
    float test_float = 21.7;

    // We lose precision when we convert from float to int. There
    // is no longer a way to retain decimal precision - the decimal
    // part is truncated.
    int float_as_int = (int)test_float;
    printf( "Float %1.1f was explicitly converted to int: %d\r\n", test_float, float_as_int );

    ///////////////////////////////////////////////////////////
    // Implicit Conversion
    ///////////////////////////////////////////////////////////

    // If we don't use an explicit cast like above, the compiler will
    // do an implicit conversion to get to the right data type.

    // For a simple assignment statement...
    float some_float = 1.1;
    int some_int = some_float;
    printf( "Float %1.1f was implicitly converted to int: %d\r\n", some_float, some_int );

    // The same goes for expressions...
    some_float = 1.1;
    some_int = 1;
    float float_result = some_float / some_int;
    int int_result = some_float / some_int;

    // The int_result will implicitly cast 
    printf( "Float result of expression: %1.1f / %d = %1.1f\r\n", some_float, some_int, float_result );
    printf( "Int result of expression: %1.1f / %d = %d\r\n", some_float, some_int, int_result );

    // The main function in C will always return an integer.
    // We can just pass back the value zero as a literal.
    printf( "\r\n" );
    return 0;
}
