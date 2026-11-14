# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Approach:
# 1. Find the middle node - Fast and Slow Pointer
# 2. reverse the second half of the list - Using pointers - current, previous, next/temp
# 3. merge the two half using two pointers
# TC: #1 O(n) + #2 O(n/2) + #3 O(n/2) ~ O(n)
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # 1. Find the middle node - Fast and Slow Pointer
        fast, slow = head, head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
        
        # 2. reverse the second half of the list - Using pointers - current, previous, next/temp
        prev, curr = None, slow
        
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
            
        # 3. merge the two half using two pointers
        first, second = head, prev
        
        while second.next:
            temp1, temp2 = first.next, second.next 
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
        
        
        