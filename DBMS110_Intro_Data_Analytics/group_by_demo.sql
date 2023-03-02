/*
In this demo we'll look at how to use the SQL group by clause to aggregate 
at different levels/granularities.
*/

SELECT
    PROD_CATEGORY,
    AVG( PROD_LIST_PRICE ) AS AVERAGE_LIST_PRICE
FROM PRODUCTS
GROUP BY PROD_CATEGORY
ORDER BY PROD_CATEGORY;

-- TODO: multilevel aggregation.
-- TODO: "having" clause.
