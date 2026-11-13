"""Given the head of a singly linked list, reverse the list, and return the reversed list."""

def reverseList(head: ListNode | None) -> ListNode | None:
    cur = head
    prev = None
    
    while cur:
        temp = cur.next 
        cur.next = prev
        prev = cur
        cur = temp
        
    head = prev
    return head