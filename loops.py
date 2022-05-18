"""

LOOPS
Nested Loops
Loops can be nested in Python, as they can with other programming languages. We will find certain situations that require nested loops.

Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
Using a for or while loop can be useful here to get each team:

for team in project_teams:
  print(team)
Would output:

["Ava", "Samantha", "James"]
["Lucille", "Zed"]
["Edgar", "Gabriel"]
But what if we wanted to print each individual student? In this case we would actually need to nest our loops to be able loop through each sub-list. Here is what it would look like:

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)
This would output:

Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel
Let’s practice writing a nested loop!

Instructions
1.
We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.

We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

Checkpoint 2 Passed
2.
Loop through the sales_data list using the following guidelines:

For our temporary variable of the for loop, call it location.
print() out each location list.
Checkpoint 3 Passed

Stuck? Get a hint
3.
Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.

By the end, you should have the sum of every number in the sales_data nested list.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Print out the value of scoops_sold outside of the nested loop.
"""

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for i in location:
    scoops_sold += i
print(scoops_sold)