# Self review: Practicing table creation

1. Which of the following SQL syntax statements can you use to create a table? Select all that apply.
    -   ```sql
        CREATE table_name TABLE;
        ```
    -   ```sql
        CREATE TABLE table_name;
        ```
    -   ```sql
        create table table_name;
        ```
    -   ```sql
        CREATE TABLE table name;
        ```
    ```
    Answer: CREATE TABLE table_name;
            create table table_name;
    Explanation: These are valid CREATE TABLE syntaxes.
    ```

2. Select all steps to create a table in the database.
    - Use the `CREATE TABLE` command.
    - Select a database.
    - Write the table name.
    - Define the columns of the table with relevant data types.
    - Use the `FROM` keyword.
    ```
    Answer: Use the CREATE TABLE command.
            Select a database.
            Write the table name.
            Define the columns of the table with relevant data types.
    Explanation: "CREATE TABLE" is the SQL command to create a table in the database.
                 Selecting a database is very important as each table must belong to a specific database.
                 The table name must be specified in the SQL create table statement
                 Defining the columns of the table with relevant data types is particularly important to ensure only required data is stored in the database.
    ```

3. Identify which of the following SQL statements can be used to create a table called `“Products”` for an online store. The table must contain two columns named `“ID”` and `“Quantity.”` The values within both columns must be whole numbers.
    -   ```sql
        CREATE TABLE products (ID INT, quantity INT);
        ```
    -   ```sql
        CREATE TABLE products (ID CHAR, quantity VARCHAR);
        ```
    ```
    Answer: CREATE TABLE products (ID INT, quantity INT);
    Explanation: This is the correct syntax to create the required table.
    ```

4. Which of the following SQL statements can be used to build a table that stores data about cell phone products?
    -   ```sql
        CREATE TABLE cell_phone (name VARCHAR(), productionDate DATE, price DECIMAL);
        ```
    -   ```sql
        CREATE TABLE cell_phone (name VARCHAR(100), productionDate DATE, price DECIMAL);
        ```
    ```
    Answer: CREATE TABLE cell_phone (name VARCHAR(100), productionDate DATE, price DECIMAL);
    Explanation: This is the right syntax to create the cell phone product table.
    ```

5. You need to create a table called `"Players"`. The table must contain two columns. The first column is called `"playername"` and holds the names of each player as a text data type. The second column is called `"playerAge"` and contains the age of each player as a whole number value. Identify the correct syntax to create this table.
    -   ```sql
        CREATE TABLE Players (playerName VARCHAR(100), playerAge DECIMAL);
        ```
    -   ```sql
        CREATE TABLE Players (playerName VARCHAR(100), playerAge INT);
        ```
    ```
    Answer: CREATE TABLE Players (playerName VARCHAR(100), playerAge INT);
    Explanation: This is the right syntax to create the customers table in SQL.
    ```