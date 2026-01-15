"""
Idea 1: 
    Use an array to store objects of the type:
    class Node
        hash_code: int
        key: any
        value: any
        next: Node (for chaining in case of collisions)
"""
class MyHashMap:
    class _Node:
        def __init__(self, key: int, value: int, next=None) -> None:
            self.key = key
            self.value = value
            self.next= next

    def __init__(self):
        self.n = 1000 # since at most 10**4 calls can be made to any instance function in this class
        self.table: list[MyHashMap._Node | None] = [None] * self.n

    def put(self, key: int, value: int) -> None:
        bucket = key % self.n
        node = self.table[bucket]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        self.table[bucket] = MyHashMap._Node(key, value, self.table[bucket])

    def get(self, key: int) -> int:
        bucket = key % self.n
        node = self.table[bucket]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        bucket = key % self.n
        node = self.table[bucket]
        prev = None
        while node:
            if node.key == key:
                if prev is None:
                    self.table[bucket] = node.next
                else:
                    prev.next = node.next
                return
            prev = node
            node = node.next