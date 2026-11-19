class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_left = Node(0, 0)
        self.dummy_right = Node(0, 0)
        self.dummy_left.next = self.dummy_right
        self.dummy_right.prev = self.dummy_left
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self, node):
        self.dummy_right.prev.next = node
        node.prev = self.dummy_right.prev
        self.dummy_right.prev = node
        node.next = self.dummy_right
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.dummy_left.next
                del self.cache[lru.key]
                self.remove(lru)
            self.cache[key] = Node(key, value)
            node = self.cache[key]
            self.insert(node)

                

