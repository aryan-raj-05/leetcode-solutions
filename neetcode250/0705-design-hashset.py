class MyHashSet:
    class _Node:
        def __init__(self, key: int, next=None) -> None:
            self.key = key
            self.next = next

    def __init__(self):
        self.n = 1000
        self.table: list[MyHashSet._Node | None] = [None] * self.n

    def add(self, key: int) -> None:
        bucket = key % self.n
        node = self.table[bucket]
        while node:
            if node.key == key:
                return
            node = node.next
        self.table[bucket] = MyHashSet._Node(key, self.table[bucket])

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

    def contains(self, key: int) -> bool:
        bucket = key % self.n
        node = self.table[bucket]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False