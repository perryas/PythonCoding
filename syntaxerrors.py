"""
    Syntax Errors
When we are writing Python programs, the interpreter is our first line of defense against errors.

SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

Here’s an example of a SyntaxError error message:

File "script.py", line 1
  print(Hello world!)
                  ^
SyntaxError: invalid syntax
The interpreter will tell us where (the file name and line number) it got into trouble and its best guess as to what is wrong.

After reading the error message, we can assume that the cause for this error is a lack of quotation marks around Hello world!.

Some common syntax errors are:

Misspelling a Python keyword.
Missing colon :.
Missing closing parenthesis ), square bracket ], or curly brace }.
Instructions
1.
In script.py, your coworker Carolyn wrote a Fortune Cookie program that is supposed to print out a possible fortune based on a random number and an if/elif/else statement.

Run the program to check it out.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Oh no, there are three SyntaxError errors inside script.py!

Can you find them all?
"""

# Fortune Cookie Program 🥠

import random

fortune = random.randint(0, 4)

if fortune == 0:
  print("May you one day be carbon neutral")
elif fortune == 1:  
  print("You have rice in your teeth")
elif fortune == 2:
  print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
  print("You can only connect the dots looking backwards")
elif fortune == 4:
  print("The fortune you seek is in another cookie")