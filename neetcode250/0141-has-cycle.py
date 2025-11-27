from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        if head.next is None: return False
        
        slow = head
        fast = head.next
        while slow != fast:
            slow = slow.next # type: ignore
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
        return True