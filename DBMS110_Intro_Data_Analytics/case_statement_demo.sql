/*
In this demo we'll look at how to use the SQL case statement to take
a different action depending on the value of some field.
*/
SELECT
    PROD_NAME,
    PROD_LIST_PRICE,
	-- The line below will check the given boolean expression and 
	-- execute one of the two code branches for the select.
    CASE WHEN PROD_LIST_PRICE < 20
        THEN 'Yes'
    ELSE
        'No'
    END AS CAN_AFFORD_TO_BUY
FROM PRODUCTS
FETCH FIRST 1000 ROWS ONLY;
