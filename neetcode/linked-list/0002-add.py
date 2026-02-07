from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i1, i2 = l1, l2
        carry = 0
        k = l1

        while i1 or i2 or carry > 0:
            val1 = i1.val if i1 else 0
            val2 = i2.val if i2 else 0

            total = val1 + val2 + carry
        
            k.val = total % 10 # pyright: ignore
            carry = total // 10

            i1 = i1.next if i1 else None
            i2 = i2.next if i2 else None

            if not k.next and (i1 or i2 or carry > 0): # pyright: ignore
                k.next = ListNode()
            
            k = k.next # pyright: ignore

        return l1
