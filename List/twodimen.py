"""_summary_
Two-Dimensional (2D) Lists
We’ve seen that the items in a list can be numbers or strings. Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists.

Once more, let’s look at a class height example:

Noelle is 61 inches tall
Ava is 70 inches tall
Sam is 67 inches tall
Mia is 64 inches tall
Previously, we saw that we could create a list representing both Noelle’s name and height:

noelle = ["Noelle", 61]
We can put several of these lists into one list, such that each entry in the list represents a student and their height:

heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]
We will often find that a two-dimensional list is a very good structure for representing grids such as games like tic-tac-toe.

#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]
Let’s practice creating our own 2D list!

Instructions
1.
A new student named "Vik" has joined our class. Vik is 68 inches tall. Add a sublist to the end of the heights list that represents Vik and his height.


Stuck? Get a hint
2.
Create a two-dimensional list called ages where each sublist contains a student’s name and their age. Use the following data:

"Aaron" is 15
"Dhruti" is 16
"""

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]

heights.append(["Vik", 68])
print(heights)

ages = [["Aaron", 15], ["Dhruti", 16]]
print(ages)