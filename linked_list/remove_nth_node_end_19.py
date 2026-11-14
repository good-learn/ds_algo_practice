# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
## Approach: two pointers with different beginnngs, that is with the gap of n
# made use of dummy node to accomodate edge cases (removal of 1st node)
# TC: O(n)
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy = ListNode()
        dummy.next = head
        
        fast, slow = head, dummy
        
        for _ in range(n):
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next 
        
        return dummy.next
        