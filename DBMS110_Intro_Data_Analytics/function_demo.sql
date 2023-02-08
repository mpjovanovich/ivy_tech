CREATE OR REPLACE FUNCTION get_games_ordinal_number( games_id in NUMBER )
RETURN NUMBER
IS 
    games_season VARCHAR(128);
    games_number NUMBER;
BEGIN 
    SELECT SEASON
    INTO games_season
    FROM GAMES
    WHERE ID = games_id;

    WITH SEASON_GAMES AS
    (
        SELECT ID, GAMES_YEAR, ROW_NUMBER() OVER(ORDER BY GAMES_YEAR) as ordinal
        FROM GAMES 
        WHERE SEASON = games_season
    )
    SELECT ordinal INTO games_number FROM SEASON_GAMES WHERE ID = games_id;

    RETURN( games_number ); 
END;
