CREATE OR REPLACE FUNCTION GET_GAMES_ORDINAL_NUMBER_FUN( games_id in NUMBER )
RETURN NUMBER
IS 
    l_games_season VARCHAR(128);
    l_games_number NUMBER;
BEGIN 
    SELECT SEASON
    INTO l_games_season
    FROM GAMES
    WHERE ID = games_id;

    WITH SEASON_GAMES AS
    (
        SELECT ID, GAMES_YEAR, ROW_NUMBER() OVER(ORDER BY GAMES_YEAR) as ordinal
        FROM GAMES 
        WHERE SEASON = l_games_season
    )
    SELECT ordinal INTO l_games_number FROM SEASON_GAMES WHERE ID = games_id;

    RETURN( l_games_number ); 
END;
/
SELECT GET_GAMES_ORDINAL_NUMBER_FUN( 12 ) AS GAMES_ORDINAL FROM DUAL;
