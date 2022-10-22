# Exercise: Instantiate a custom Object

## Instructions
__Step 1__

1.1 Define a class called `MyFirstClass`.

1.2 Add a print statement inside it such as `"Who wrote this?"`.

__Step 2__

Create a string variable named `index` and initialize it with a string `"Author-Book"`.

__Step 3__

3.1 Define a function called `hand_list()` with the help of `def` keyword. 

3.2 Pass the parameter `self` to it. And then pass two parameters, `philosopher` and `book` to it.

__Step 4__

4.1 Write a print statement using the `print()` function and pass the class variable by accessing it. 

__Hint: Class variables are accessed directly by calling it over the class name using dot notation.__

4.2 Write a print statement that will give output such as: `"Plato wrote the book: Republic"` where `"Plato"` is the philosopher and `"Republic"` is the book. 

__Hint: You can make use of the built-in (+) concatenation operator to join these strings.__

__Step 5__

5.1 Create and instantiate an object of that class, called `whodunnit`

5.2 Call method `hand_list()` over this object `"whodunnit"` and pass two values to it namely `"Sun Tzu"` and `"The Art of War"`.

## Self-review
1. Which of the following is the class variable in the code above?
   - MyFirstClass
   - index
   - philosopher
   - whodunnit
   ```
   Answer: 
   Explanation: 
   ```

2. How will you modify the code below if you want to include a “year” of publication in the output?
   ```python
    class MyFirstClass():
        print("Who wrote this?")
        index = "Author-Book"
        def hand_list(self, philosopher, book):
            print(MyFirstClass.index)
            print(philosopher + " wrote the book: " + book)
    
    whodunnit = MyFirstClass()
    whodunnit.hand_list("Sun Tzu", "The Art of War")
   ```
   Insert your suggestions below 
   ```python
    class MyFirstClass():
        print("Who wrote this?")
        index = "Author-Book"
        def hand_list(self, philosopher, book, year):
            print(MyFirstClass.index)
            print(philosopher + " wrote the book: " + book + " in " + year)
    
    whodunnit = MyFirstClass()
    whodunnit.hand_list("Sun Tzu", "The Art of War", "the 5th century BC")
   ```