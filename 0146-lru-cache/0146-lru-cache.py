"""
capacity > 0

O(1)
search -> map, set, index in list
insert, delete -> map, set, linkedlist

hashmap[key] = linkedlist node
head <-> node2 <-> node1 <-> tail

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
        self.head = DoublyLinkedList(-1,-1)
        self.tail = DoublyLinkedList(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
        
    # O(1)
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        # if found
        # take out the node and put into tail
        found_node = self.hashmap[key]
        self.remove(found_node)
        self.insert(found_node)
        return found_node.val

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    # O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            old_node = self.hashmap[key]
            self.remove(old_node)

        new_node = DoublyLinkedList(key, value)
        self.hashmap[key] = new_node
        self.insert(new_node)

        # if it is more than the capacity -> remove the first one
        if len(self.hashmap) > self.capacity:
            first_node = self.head.next
            self.remove(first_node)
            del self.hashmap[first_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)