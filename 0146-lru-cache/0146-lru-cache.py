class DoublyLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyLinkedNode(-1,-1)
        self.tail = DoublyLinkedNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.storage = {}

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1
        
        curr = self.storage[key]
        self.remove(curr)
        self.add(curr)
        return curr.value
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node):
        temp = self.tail.prev
        temp.next = node
        self.tail.prev = node

        node.prev = temp
        node.next = self.tail

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            curr = self.storage[key]
            self.remove(curr)
            del self.storage[key]
        
        newNode = DoublyLinkedNode(key, value)
        self.storage[key] = newNode
        self.add(newNode)

        if len(self.storage) > self.capacity:
            removingNode = self.head.next
            self.remove(self.head.next)
            del self.storage[removingNode.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)