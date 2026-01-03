from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head
        
        n = self.getLength(head)
        k = k % n
        if k == 0:
            return head

        # find the new tail
        newTail = head
        for i in range(n - k - 1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None

        # connect the last element of newHead to old head
        iter = newHead
        while iter:
            if iter.next is None:
                iter.next = head
                break
            iter = iter.next

        return newHead


    def getLength(self, head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count