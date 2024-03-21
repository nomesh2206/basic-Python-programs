def isSorted(head):
    #code here 
    if head is None or head.next is None:
        return 1

    # Check if the list is in increasing order
    current = head
    while current.next is not None:
        if current.value > current.next.value:
            break
        current = current.next

    if current.next is None:
        return 1

    # Check if the list is in decreasing order
    current = head
    while current.next is not None:
        if current.value < current.next.value:
            break
        current = current.next

    if current.next is None:
        return 1

    return 0
