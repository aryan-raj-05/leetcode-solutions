from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        newHead = ListNode()
        cur_node = newHead
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next
            cur_node = cur_node.next

        while l1:
            cur_node.next = l1
            l1 = l1.next
            cur_node = cur_node.next

        while l2:
            cur_node.next = l2
            l2 = l2.next
            cur_node = cur_node.next

        return newHead.next