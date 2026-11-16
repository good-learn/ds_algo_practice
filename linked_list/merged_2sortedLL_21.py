# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Approach: Step 1. Create a dummy node, use a current pointer to track the forming connections
# Step 2.  add as you compare through both list
# Note we are not creating a new linked list, we are just rearranging the pointers
# TC: O(n + m) ~ O(n)
# SC: O(1) (for dummy helper node)
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        dummy = ListNode()
        curr = dummy


        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next