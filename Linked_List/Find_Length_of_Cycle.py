class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_cycle_length(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return 0  # No cycle

    # Move one pointer around the cycle until it meets the other pointer again
    current = slow
    length = 0
    while True:
        current = current.next
        length += 1
        if current == slow:
            break

    return length

# Create a linked list with a cycle: 1->2->3->4->5->2
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next  # Create a cycle

cycle_length = find_cycle_length(head)
print("Length of the cycle:", cycle_length)
