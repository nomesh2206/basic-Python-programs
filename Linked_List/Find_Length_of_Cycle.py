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
