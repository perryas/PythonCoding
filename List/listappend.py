"""_summary_
Growing a List: Append
We can add a single element to a list using the .append() Python method.

Suppose we have an empty list called garden:

garden = []
We can add the element "Tomatoes" by using the .append() method:

garden.append("Tomatoes")
 
print(garden)
Will output:

['Tomatoes']
We see that garden now contains "Tomatoes"!

When we use .append() on a list that already has elements, our new element is added to the end of the list:

# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]
 
# Append a new element
garden.append("Green Beans")
print(garden)
Will output:

['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']
Let’s use the .append() method to manipulate a list.

Instructions
1.
Jiho works for a gardening store called Petal Power. Jiho keeps a record of orders in a list called orders.

Use print to inspect the orders he has received today.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Jiho just received a new order for "tulips". Use append to add this string to orders.

Checkpoint 3 Passed

Stuck? Get a hint
3.
Another order has come in! Use append to add "roses" to orders.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Use print to inspect the orders Jiho has received today.
"""

orders = ["daisies", "periwinkle"]
orders.append("tulips")
orders.append("roses")
print(orders)