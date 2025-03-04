from tkinter import N


# TC: O(n)
# SC: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if fast==slow: break
  
        slow2=head
        while slow.next:
            if slow2==slow: return slow
            slow=slow.next
            slow2=slow2.next
        
        return 
            
            