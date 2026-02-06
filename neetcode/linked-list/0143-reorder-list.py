from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Optimized, Time: O(n), Space: O(1)
    # 1. Find the middle point of the list
    # 2. reverse the second half of the list
    # 3. merge the two lists alternatingly
    def reorderList2(self, head: Optional[ListNode]) -> None:
        # 1. find the middle part
        slow, fast = head, head.next    # pyright: ignore
        while fast and fast.next:
            slow = slow.next    # pyright: ignore
            fast = fast.next.next

        # 2. reversing the second half
        second = slow.next      # pyright: ignore
        prev = slow.next = None # pyright: ignore
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. merging the two lists alternate manner
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


    # Naive Solution, uses extra memory
    # Time: O(n), Space: O(n)
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
