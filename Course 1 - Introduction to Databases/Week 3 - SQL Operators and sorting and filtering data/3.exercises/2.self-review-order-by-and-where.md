# Self-review: ORDER BY and WHERE

1. The `ORDER BY` keyword in SQL sorts the records of a table column in descending order by default.
    - True
    - False
    ```
    Answer: False
    Explanation: The ORDER BY keyword in SQL sorts the records of a table column in ascending order by default.
    ```

2. The output result of the following SQL statement is the data of all customers from Germany, as `“*”` in this context means all columns.
    ```sql
    SELECT * FROM customers WHERE Country = "Germany";
    ```
    - True
    - False
    ```
    Answer: True
    Explanation: The output result of this statement is the data of all customers from Germany. The * means all columns in the table.
    ```

3. Choose the SQL statement that shows a list of all customers who live in `India` organized alphabetically from A to Z within a database table named `“customers”`.
    -   ```sql
        SELECT * FROM customers WHERE country = "India" ORDER BY FirstName ASC;
        ```
    -   ```sql
        SELECT * FROM customers WHERE country = "India" ORDER BY FirstName DESC;
        ```
    ```
    Answer: SELECT * FROM customers WHERE country = "India" ORDER BY FirstName ASC;
    Explanation: The output result of this SQL statement shows all customers from India in alphabetical order from A to Z. This is because the ASC keyword sorts the records in ascending order.
    ```

4. Identify the effect of the following SQL statement on the “Staff” table:
    ```sql
    SELECT * FROM staff ORDER BY Country, StaffName
    ```
    - Displays the results ordered by country first then staff name.
    - Orders the result by country and ignores the staff name.
    ```
    Answer: Displays the results ordered by country first then staff name.
    Explanation: It orders the result by country first. However, if some records have the same country then it orders them by staff name.
    ```