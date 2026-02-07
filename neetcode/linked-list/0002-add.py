from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = l1
        j = l2
        res = k = ListNode()

        carry = 0
        while i and j:
            total = i.val + j.val + carry

            k.next = ListNode(total % 10)

            carry = total // 10
            k = k.next
            i = i.next
            j = j.next

        while i:
            total = i.val + carry

            k.next = ListNode(total % 10)

            carry = total // 10
            k = k.next
            i = i.next

        while j:
            total = j.val + carry

            k.next = ListNode(total % 10)
        
            carry = total // 10
            k = k.next
            j = j.next

        if carry > 0:
            k.next = ListNode(carry)

        return res.next
    
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i1, i2 = l1, l2
        carry = 0

        dummyNode = k = ListNode()

        while i1 or i2 or carry > 0:
            val1 = i1.val if i1 else 0
            val2 = i2.val if i2 else 0

            total = val1 + val2 + carry

            k.next = ListNode(total % 10)
            carry = total // 10

            i1 = i1.next if i1 else None
            i2 = i2.next if i2 else None
            k = k.next

        return dummyNode.next
    
    def addTwoNumbers3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        
        i1, i2 = l1, l2
        carry = 0
        k = l1

        while i1 or i2 or carry > 0:
            val1 = i1.val if i1 else 0
            val2 = i2.val if i2 else 0

            total = val1 + val2 + carry
        
            k.val = total % 10
            carry = total // 10

            i1 = i1.next if i1 else None
            i2 = i2.next if i2 else None

            if not k.next:
                k.next = ListNode()
            
            k = k.next

        return l1