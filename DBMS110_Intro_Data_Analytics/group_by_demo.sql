/*
In this demo we'll look at how to use the SQL group by clause to aggregate 
at different levels/granularities.
*/

SELECT
    PROD_CATEGORY,
    COUNT(*) AS NUMBER_OF_ITEMS,
    AVG( PROD_LIST_PRICE ) AS AVERAGE_LIST_PRICE
FROM PRODUCTS
GROUP BY PROD_CATEGORY
ORDER BY PROD_CATEGORY;

/*
Let's suppose that we only care about these stats when we have at least
1000 items in a category. We can use the 'HAVING' clase to filter an 
aggregate result. It works just like 'WHERE', but with aggregate fields.
*/
/*
SELECT
    PROD_CATEGORY,
    COUNT(*) AS NUMBER_OF_ITEMS,
    AVG( PROD_LIST_PRICE ) AS AVERAGE_LIST_PRICE
FROM PRODUCTS
GROUP BY PROD_CATEGORY
HAVING COUNT(*) > 1000
ORDER BY PROD_CATEGORY;
*/

-- TODO: multilevel aggregation.

