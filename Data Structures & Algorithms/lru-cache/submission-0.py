class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ha = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.ha:
            return -1

        node = self.ha[key]
        self._remove(node)
        self._insert_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.ha:
            node = self.ha[key]
            node.value = value
            self._remove(node)
        else:
            node = Node(key, value)
            self.ha[key] = node

        self._insert_front(node)

        if len(self.ha) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.ha[lru.key]
            

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    


        
