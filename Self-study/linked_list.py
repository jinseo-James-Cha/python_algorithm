class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # add a node at the end
    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        
        cur.next = Node(value)
    
    # print linklist value
    def print_all(self):
        cur = self.head

        while cur is not None:
            print(cur.data)
            cur = cur.next
    
    # get index node
    def get_node(self, index):
        i = 0
        cur = self.head

        while i != index:
            cur = cur.next
            i += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        # exception for head change, index == 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # get previous node to add new node on "next"
        prev_node = self.get_node(index - 1)

        # temporarily save previous' next node to connect into "new node" 
        next_node = prev_node.next

        # save the old next node to new next node's next
        new_node.next = next_node

        # add new node to prev
        prev_node.next = new_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index - 1)
        cur_node = self.get_node(index)

        prev_node.next = cur_node.next


            


l = LinkedList(5)
l.append(4)
l.append(3)
# l.print_all()

# l.get_node(0)
# l.get_node(1)
# l.get_node(2)

l.add_node(1, 22)
l.print_all()
l.delete_node(1)
l.print_all()