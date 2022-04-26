"""
Name Errors
A NameError is reported by the Python interpreter when it detects a variable that is unknown.

This can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. The Python interpreter will display the line of code where the NameError was detected and indicate which name is found that was not defined.

Here’s an example of a NameError error message:

File "script.py", line 1, in <module>
    print(score)
NameError: name 'score' is not defined
This error is suggesting that the variable score was never defined in the program. Oops.

Some common name errors are:

Misspelling a variable name.
Forgetting to define a variable.
"""
# Who Wants To Be A Millionaire 💰 

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3 = 'Test'
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  score += 100b
  print("\nCorrect!")
else:
  print("\nNope, sorry!")