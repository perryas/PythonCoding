"""

Modifying 2D Lists
Now that we know how to access two-dimensional lists, modifying the elements should come naturally.

Let’s return to a classroom example, but now instead of heights or test scores, our list stores the student’s favorite hobby!

class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
"Jenny" changed their mind and is now more interested in "Meditation".

We will need to modify the list to accommodate the change to our class_name_hobbies list. To change a value in a two-dimensional list, reassign the value using the specific index.

# The list of Jenny is at index 0. The hobby is at index 1. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)
Would output:

[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
Negative indices will work as well.

# The list of Jenny is at index 0. The hobby is at index 1. 
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)
Would output:

[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Football"]]
Instructions
1.
Our school is expanding! We are welcoming a new set of students today from all over the world.

Using the provided table, create a two-dimensional list called incoming_class to represent the data. Each sublist in incoming_class should contain the name, nationality, and grade for a single student.

Name	Nationality	Grade Level
"Kenny"	"American"	9
"Tanya"	"Russian"	9
"Madison"	"Indian"	7

Print incoming_class to see our list.


Stuck? Get a hint
2.
"Madison" passed an exam to advance a grade. She will be pushed into 8th grade rather than her current 7th in our list.

Modify the list using double brackets [][] to make the change. Use positive indices.

Print incoming_class to see our change.


Stuck? Get a hint
3.
"Kenny" likes to be called by his nickname "Ken". Modify the list using double brackets [][] to accommodate the change but only using negative indices.

Print incoming_class to see our change.
"""

#Your code below:
incoming_class = [["Kenny", "American", 9],["Tanya", "Russian", 9], ["Madison", "Indian", 7]]

print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)