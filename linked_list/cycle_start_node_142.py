# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## Approach: Using fast and slow pointer
# TC: O(n)
# SC: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None
    
    

## Approach: Using hashset
# TC: O(n)
# SC: O(n)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myset = set()
        iter = head
        while iter:
            if iter in myset:
                return iter
            myset.add(iter)
            iter = iter.next
        return None