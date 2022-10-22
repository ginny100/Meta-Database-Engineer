# Self-review: Create Database, create table and insert data

1. The following SQL statement can be used to create a database for a bookshop:
    ```sql
    CREATE bookshop DATABASE
    ```
    - True
    - False
    ```
    Answer: False
    Explanation: CREATE DATABASE bookshop is the right syntax to create the bookshop database in SQL. 
    ```

2. The following SQL statement can be used to create a `"Customers"` table in a bookshop database:
    ```sql
    CREATE TABLE customers (customerName VARCHAR(100), customerAddress VARCHAR(100));
    ```
    - True
    - False
    ```
    Answer: True
    Explanation: This is the right syntax to create the Customers table in SQL. 
    ```

3. Identify the correct SQL command to insert a new record of data in a table.
    -   ```sql
        INSERT INTO SELECT
        ```
    -   ```sql
        INSERT INTO
        ```
    ```
    Answer: INSERT INTO
    Explanation: The INSERT INTO command is used to insert new records in a table.
    ```

4. Which of the following SQL statements can you use to insert a record for a customer named `"Karl"`, aged `21` into a table called `"Customers"`?
    -   ```sql
        INSERT name, age INTO customer table values "Karl" "21"
        ```
    -   ```sql
        INSERT INTO customer (name, age) VALUES ("Karl", 21);
        ```
    -   ```sql
        INSERT customer SET name = "Karl" and age = 21
        ```
    ```
    Answer: INSERT INTO customer (name, age) VALUES ("Karl", 21);
    Explanation: This is the right SQL syntax to insert new record of data into the Customer table.
    ```

5. Identify the missing keyword in the following SQL statement.
    ```sql
    INSERT INTO customers (ID, name) ____ (7, "Tom");
    ```
    -   ```sql
        INSERT INTO customers (ID, name) VALUES (7, "Tom");
        ```
    -   ```sql
        INSERT INTO customers (ID, name) VALUES (7, "Tom");
        ```
    ```
    Answer: INSERT INTO customers (ID, name) VALUES (7, "Tom");
    Explanation: This is the correct SQL statement to INSERT a new record to the customer's table. 
    ```