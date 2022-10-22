# Module quiz: Getting started with Python

1. Python is a dynamically typed language. What does this mean?
   - Python requires that you specify the type of variable before it being assigned.
   - Python supports both functional and object oriented programming.
   - Python requires you to explicitly set the correct data type  and value before assigning a variable.
   - Python does not require a type for a variable declaration. It automatically assigns the data type at run time.
   ```
   Answer: Python does not require a type for a variable declaration. It automatically assigns the data type at run time.
   Explanation: When variables are declared in Python they are automatically assigned a data type.
   ```

2. How do you create a block in Python?
   - A block is created using a colon following by a new line and indentation
   - A block is created by a new line
   - A block is created using a semi colon and a new line
   - A block is created using a semi colon and indentation
   ```
   Answer: A block is created using a colon following by a new line and indentation
   Explanation: A block of code created by using a colon, new line and indentation.
   ```

3. When declaring variable in Python, can a variable name contain white space?
   - Yes
   - No
   ```
   Answer: No
   Explanation: A variable must not contain white space.
   ```

4. How can a variable be deleted in python?
   - The del keyword
   - The def keyword
   - The remove keyword
   - A variable cannot be deleted
   ```
   Answer: The del keyword
   Explanation: The del keyword is used to delete a variable by typing del variable name.
   ```

5. In Python, how can you convert a number to a string?
   - enumerate()
   - float()
   - int()
   - str()
   ```
   Answer: str()
   Explanation: To convert a number to a string you need to use the str() function. This will change an int like 8 to “8”.
   ```

6. An Integer - int in Python can be converted to type Float by using the float function?
   - True
   - False
   ```
   Answer: True
   Explanation: The float function can be used to covert a type int to a float for better precision.
   ```

7. What is the purpose of break in a for loop in Python?
   - It controls the flow of the loop and stops the current loop from executing any further.
   - To terminate the code
   - The break statement will suspend the code until continue is run. 
   - The break keywork is used to debug a for loop. 
   ```
   Answer: It controls the flow of the loop and stops the current loop from executing any further.
   Explanation: The break keyword will stop the loop from executing and transfer the control to the next block of code.
   ```

8. An enumerate function is used to provide the index of the current iteration of a for loop.
   - True
   - False
   ```
   Answer: True
   Explanation: An enumerate function is used to provide the index of current iteration of a for loop.
   ```

9. What will be the output of the code below:
   ```python
    a = isinstance(str, "aa")
    print(a)
   ```
   - It will throw an error. 
   - “aa”  
   - False  
   - True
   ```
   Answer: It will throw an error.
   Explanation: It will throw a TypeError as the correct format here must be isinstance("aa", str)
   ```

10. Select all the valid input() formats among the following.
    - ```python
      "" = input("My name is: " + name)
      ```
    - ```python
      name = input("What is your name? ")
      ```
    - ```python
      input("")
      ```
    - ```python
      input()
      ```
    ```
    Answer: name = input("What is your name? ")
            input("")
            input()
    Explanation: name = input("What is your name? ") is the standard format for using input(),
                The input() can work even without assignment to some variable and an empty prompt,
                The input() can work even without assignment to some variable.
    ```