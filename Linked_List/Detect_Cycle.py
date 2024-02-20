# Problem: Given a linked list, detect if it contains a cycle. A cycle in a linked list occurs when a node's next points back to a previous node in the list. 
# For example, in the linked list 1->2->3->4->5->2, node 5 points back to node 2, creating a cycle.

Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

# Example usage
# Create a linked list with a cycle: 1->2->3->4->5->2
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next  # Create a cycle

# Check if the linked list has a cycle
print(has_cycle(head))  # Output: True
