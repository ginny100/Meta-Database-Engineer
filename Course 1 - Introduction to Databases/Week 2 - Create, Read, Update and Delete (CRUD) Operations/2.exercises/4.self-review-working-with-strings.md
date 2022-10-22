# Self review: Working with strings

1. A college database contains a table called `“Students”` that has three columns: `username`, `full name` and `email address`. The `username` column contains alphanumeric values such as `“St001”` and has a fixed length of five characters. Select the correct SQL syntax for the username column.
    -   ```sql
        username CHAR(5)
        ```
    -   ```sql
        username VARCHAR(5)
        ```
    ```
    Answer: username CHAR(5)
    Explanation: The username has a fixed length of 5 characters.
    ```

2. Which of the following SQL statements uses the right syntax to create the `Student` table in a college database with character limits?
    -   ```sql
        CREATE TABLE students (username CHAR, fullName VARCHAR, email VARCHAR);
        ```
    -   ```sql
        CREATE TABLE students (username CHAR(5), fullName VARCHAR(100), email VARCHAR(255));
        ```
    ```
    Answer: CREATE TABLE students (username CHAR(5), fullName VARCHAR(100), email VARCHAR(255));
    Explanation: This is the right SQL statement, because it defines all columns with suitable character lengths.
    ```

3. You are sourcing feedback from students on college services. Each student can provide up to 10000 characters worth of feedback in an online form, which will then be stored in a database. Identify the correct SQL syntax to create the `“Feedback”` column.
    -   ```sql
        article TEXT(10000)
        ```
    -   ```sql
        article CHAR(10000)
        ```
    ```
    Answer: article TEXT(10000)
    Explanation: TEXT is a string datatype that can be used to define columns requiring less than 65535 characters such as the body content of an article.
    ```

4. TINYTEXT is a string data type used to define columns with small letter characters only.
    - False
    - True
    ```
    Answer: False
    Explanation: With TINYTEXT, columns can hold any type of character and a maximum length of 255 characters.
    ```