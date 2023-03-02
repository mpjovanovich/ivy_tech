/*
"Group by cube" in SQL allows us to construct a data cube,
aggregating to various levels with one command.
This is useful when there is a hierarchy in the data, as with
the below example where product subcategory is nested in the
category dimension.

Note that where you see "null" - it translates to "all", the
total for all categories and/or subcategories given the grouping.
null, null indicates the "grand total" in this case.
*/

SELECT 
    PROD_CATEGORY,
    PROD_SUBCATEGORY,
    SUM(PROD_LIST_PRICE) SUM_PRICE
FROM PRODUCTS 
GROUP BY CUBE(PROD_CATEGORY, PROD_SUBCATEGORY)

