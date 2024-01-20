-- Average weighted score 
-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    -- Declare variables
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE average_score DECIMAL(10, 2);
    DECLARE id INT;

    -- Declare a cursor to iterate through rows
    DECLARE userscursor CURSOR FOR
        SELECT average_score, id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET done = TRUE;
    -- Open the cursor
    OPEN userscursor;
    my_loop: LOOP
        -- Fetch the next row
        FETCH userscursor INTO average_score, id;

        -- Exit the loop if there are no more rows
        IF done THEN
            LEAVE my_loop;
        END IF;

        CALL ComputeAverageWeightedScoreForUser(id);
        -- Perform actions for each row
        -- Your custom logic here using col1_value and col2_value
    END LOOP;

    -- Close the cursor
    CLOSE userscursor;
END //

DELIMITER ;
