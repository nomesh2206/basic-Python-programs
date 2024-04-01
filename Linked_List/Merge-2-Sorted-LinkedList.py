def sortedMerge(head1, head2):
    # code here
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
        
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else :
        head = head2
        head2 = head2.next
    
    curr = head
    while head1 != None and head2 != None:
        if head1.data < head2.data:
            curr.next = head1
            head1= head1.next
        else:
            curr.next = head2
            head2 = head2.next
        
        curr = curr.next
        
    if head1 != None:
        curr.next = head1
    else :
        curr.next = head2
    
    return head
