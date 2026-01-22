from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        stack = []
        i = head
        while i:
            stack.append(i)
            i = i.next

        i = head
        while stack and stack[-1] != i:
            node = stack.pop()

            if i.next == node:
                node.next = None
                return
            
            j = i.next
            i.next = node
            node.next = j

            i = j

        i.next = None