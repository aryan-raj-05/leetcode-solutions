from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        table = {}

        i = head
        while i:
            tmp = Node(i.val)
            table[i] = tmp
            i = i.next

        i = head
        while i:
            table[i].next = table[i.next] if i.next else None
            table[i].random = table[i.random] if i.random else None
            i = i.next

        return table[head]
        