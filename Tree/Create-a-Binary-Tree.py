class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a new node with a given value
def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# Example 
root = None
values = [5, 3, 7, 1, 4, 6, 8]
for value in values:
    root = insert(root, value)

"""
Visualization:

    5
   / \
  3   7
 / \ / \
1  4 6  8

"""
