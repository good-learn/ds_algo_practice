# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## Approach: Using hashset, you loop once but the SC will be O(n)
# TC: O(n)
# SC: O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        myset = set()

        iter = head
        while iter:
            if iter in myset:
                return True
            myset.add(iter)
            iter = iter.next
        return False  

## Optimized Approach: loop only once, fast and slow pointer, SC is O(1)
# TC: O(n)
# SC: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False