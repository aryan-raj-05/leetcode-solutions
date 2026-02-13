from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = temp = head
        for _ in range(n):
            ptr = ptr.next # pyright: ignore

        if not ptr:
            return head.next # pyright: ignore
        
        while ptr.next:
            ptr = ptr.next
            temp = temp.next # pyright: ignore

        temp.next = temp.next.next # pyright: ignore
        return head

    def removeNthFromEnd_twoPass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Some Edge Cases
        # 1. The Last Node (n = 1)
        # 2. The First Node (n = len(list))
        # 3. Single Node List

        # Time: linear O(n)
        # Space: constant O(1)
        # Two Pass Solution
        if not head or head.next is None:
            return None

        size = 0
        i = head
        while i:
            size += 1
            i = i.next

        if n == size:
            return head.next

        # the general case and last node case have same code
        nodeIdx = size - n
        i, prev = head, None
        for _ in range(nodeIdx):
            prev = i
            i = i.next # pyright: ignore
        prev.next = i.next # pyright: ignore

        return head