"""
Type Errors
A TypeError is reported by the Python interpreter when an operation is applied to a variable of an inappropriate type.

This can occur in Python when one attempts to use an operator on something of the incorrect type.

For example, let’s see what happens when we try and add together two incompatible types:

piggy_bank = '2' + 0.25
There will be an TypeError error message:

Traceback (most recent call last):
  File "script.py", line 1, in <module>
    piggy_bank = '2' + 0.25
TypeError: must be str, not float
This error is reporting that 0.25 is not a string.

Some common type errors are:

Accidentally adding or subtracting a string value.
Call a function on something of the incorrect type.
Instructions
1.
The word got out in the office that you are a pro bug catcher!

Another peer Alisha pops out of the blue and hands you a program that calculates the area of a triangle, a rectangle, and a circle.

Run the program to check it out.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Oh no, there’s one TypeError error!

Can you find it?
"""

# Area Calculator 📏

import math

base = 20
height = 30
area = base * height / 2

print("The triangle area is", area)

length = 2
width = 12
area = length * width

print("The rectangle area is" + str(area) )
    
radius = 36
area = math.pi * radius * radius
    
print("The circle area is", area)