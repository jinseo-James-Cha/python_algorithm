"""
Least Recently Used Cache => get or put is also considered as Used => place at the end.

- Store key-value pair
- Update key-value pair

Get
- Given a key, if exists, return the value. If it doesn't, return -1.
- When an existing key is fetched, remove from the list and then Move it to the back.

Put
- If key is already exists, remove from the list and cache
- When a new key-value pair is added, create a new linked list node and put it at the back.
- When a new key-value pair is added and the size of the data structure exceeds capacity, remove the linked list node at the front.

"""

class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyLinkedList(-1,-1)
        self.tail = DoublyLinkedList(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        curr = self.cache[key]
        self.remove(curr)
        self.add(curr)
        return curr.val
        
    def put(self, key: int, value: int) -> None:
        # check key and remove old if exists
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        # create new node and add in the tail
        new_node = DoublyLinkedList(key, value)
        self.cache[key] = new_node
        self.add(new_node)

        if len(self.cache) > self.capacity:
            first_node = self.head.next
            self.remove(first_node)
            del self.cache[first_node.key]
    
    def add(self, node):
        prev_tail = self.tail.prev
        
        prev_tail.next = node
        node.prev = prev_tail

        self.tail.prev = node
        node.next = self.tail
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)