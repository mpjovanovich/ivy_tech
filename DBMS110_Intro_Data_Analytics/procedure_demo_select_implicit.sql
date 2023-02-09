CREATE OR REPLACE PROCEDURE FETCH_PERSON_BY_REGION_PRC
AS
    c_result SYS_REFCURSOR;
BEGIN
    /* 
    Very basic select. We normally wouldn't use a stored
    procedure for this, but we will to keep the demo simple.
    */
    OPEN c_result FOR
    SELECT
            PERSON.FULL_NAME
        FROM 
            PERSON
            JOIN PERSON_REGION ON PERSON.ID = PERSON_REGION.PERSON_ID
        FETCH FIRST 10 ROWS ONLY;
    dbms_sql.return_result(c_result);
END;
/

EXEC FETCH_PERSON_BY_REGION_PRC;
