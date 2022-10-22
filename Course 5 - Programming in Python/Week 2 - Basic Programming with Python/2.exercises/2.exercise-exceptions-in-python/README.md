# Exercise: Exceptions in Python

By the end of this exercise, you will be able to trap exceptions.

## Exercise
Your task in this exercise is to add code to trap exceptions and handle them in a more user-friendly way. 

### IndexError
The below code has one problem. It is trying to locate an item from the list that does not exist. Running the code will throw the __IndexError__. Add exception handling to stop the error from being thrown and return a more user-friendly message such as "Item does not exist in the list".
```python
# Starter code
items = [1,2,3,4,5]
item = items[6]
print(item)
```

### ZeroDivisionError
In math there are rules about dividing by zero. The below code is trying to do just that and will throw a ZeroDivisionError. Add exception handling to return back 0 instead of allowing the error to be thrown.
```python
# Starter code
def divide_by(a, b):
    return a / b

ans = divide_by(40, 0)
print(ans)
```

### FileNotFoundError
The code below is looking for a file that does not exist. Add exception handling to catch this error and return the following "The file could not be found".
```python
# Starter code
with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())
```