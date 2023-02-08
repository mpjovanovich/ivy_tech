-- Needed to print the value of variables.
SET SERVEROUTPUT ON

-- Declare any vars that we need.
DECLARE 
    some_text VARCHAR2(128);
    some_number NUMBER;

-- Var declarations must be followed by a BEGIN/END block.
BEGIN
    -- We can assign with the := operator.
    some_text := 'Here''s muh text.';
    some_number := 999

    -- We can 'print' to the console with the DBMS_OUTPUT.PUT_LINE function.
    DBMS_OUTPUT.PUT_LINE(some_text);
    DBMS_OUTPUT.PUT_LINE(some_number);
END;
