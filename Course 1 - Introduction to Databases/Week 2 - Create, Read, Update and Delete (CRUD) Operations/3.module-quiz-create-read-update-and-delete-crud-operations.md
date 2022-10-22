# Module quiz: Create, Read, Update and Delete (CRUD) Operations

1. The following SQL clause creates a table named staff within a database:
    ```sql
    CREATE staff TABLE;
    ```
    - True
    - False
    ```
    Answer: False
    Explanation: The table name should be written after the TABLE keyword.
    ```

2. The following SQL statement creates a table named `staff`, with two columns called `name` and `address`:
    ```sql
    CREATE TABLE staff (name VARCHAR(100), address VARCHAR(100));
    ```
    - True
    - False
    ```
    Answer: True
    Explanation: This is the right syntax to create the staff table with name and address columns in SQL.
    ```

3. What is the SQL command to add a new record of data in the staff table?
    -   ```sql
        ADD INTO staff
        ```
    -   ```sql
        INSERT staff INTO
        ```
    -   ```sql
        INSERT INTO staff
        ```
    ```
    Answer: INSERT INTO staff
    Explanation: The INSERT INTO command is used to insert new records in a table.
    ```

4. Which is the right command syntax to update the staff table in SQL?
    -   ```sql
        UPDATE Table staff
        ```
    -   ```sql
        UPDATE staff
        ```
    ```
    Answer: UPDATE staff
    Explanation: This is the right way to use the UPDATE command.
    ```

5. EDIT command is used to modify data in a database table.
    - True
    - False
    ```
    Answer: False
    Explanation: The UPDATE command is used to modify data in the database.
    ```

6. Which one of the following SQL statements updates the staff email address for the individual named `“Karl”` in the staff table?
    -   ```sql
        UPDATE staff SET email = 'Karl@email.com' WHERE name = 'Karl';
        ```
    -   ```sql
        UPDATE staff SET name = 'Karl@email.com' WHERE email = 'Karl';
        ```
    -   ```sql
        UPDATE staff WHERE ID = 16 SET email = 'Karl@email.com';
        ```
    ```
    Answer: UPDATE staff SET email = 'Karl@email.com' WHERE name = 'Karl';
    Explanation: This is the right syntax to update the staff email in the staff table.
    ```

7. Select the right keyword to complete the missing part of the following statement:
    ```sql
    INSERT INTO staff (ID, name) ___ (7, “Tom”);
    ```
    -   ```sql
        VALUES
        ```
    -   ```sql
        DATA
        ```
    ```
    Answer: VALUES
    Explanation: VALUES is the correct SQL keyword to use here to insert a new record in the staff table.
    ```

8. A staff table consists of three columns called name, email and age. Which of the following SQL statements selects all available data in all three columns in the staff table? Select all correct answers.
    -   ```sql
        SELECT * FROM staff
        ```
    -   ```sql
        SELECT name, email, age FROM staff
        ```
    -   ```sql
        SELECT name, email AND age FROM staff
        ```
    ```
    Answer: SELECT * FROM staff
            SELECT name, email, age FROM staff
    Explanation: You can use these syntaxes to select all the columns available in the staff table.
    ```

9. The following SQL statement returns all staff phone numbers from the staff table:
    ```sql
    SELECT phoneNumber FROM staff;
    ```
    - True
    - False
    ```
    Answer: True
    Explanation: This is the right SQL statement to return the staff phone numbers.
    ```

10. Which of the following SQL statements deletes all records of data from the staff table without deleting the table itself? Select all correct answers.
    -   ```sql
        TRUNCATE TABLE staff
        ```
    -   ```sql
        DROP TABLE staff
        ```
    -   ```sql
        DELETE FROM staff
        ```
    ```
    Answer: DELETE FROM staff
            TRUNCATE TABLE staff
    Explanation: DELETE FROM staff deletes all rows in the "customers" table, without deleting the table.
                 TRUNCATE TABLE staff deletes the data inside the customers table, but not the table itself.
    ```