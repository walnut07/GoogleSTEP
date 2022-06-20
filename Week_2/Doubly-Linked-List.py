# Pure Doubly Linked List
# My intention is to get familiar with Doubly Linked List before implementing the LRU cache algorithm.

class Node:
    def __init__(self, next = None, prev = None, data = None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:   
    # Adding a node at the front of the list
    def __init__(self):
        self.head = None

    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data = new_data)

        # 3: Make next of the new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node
        
        # 5. move the head to point to the new node
        self.head = new_node


    def insertAfter(self, prev_node, new_data):
        # 1: check if prev_node is not NULL
        if prev_node == None:
            print("This node doesn't exist in DDL")
            return
        
        # 2: allocate node and 3: put in the data
        new_node = Node(data = new_data)

        # 4: Make next of new_node as next of next of prev_node
        new_node.next = prev_node.next

        # 5: Make the next of new_node as new_node
        prev_node.next = new_node

        # 6: Make the prev of new_node as prev_node
        new_node.prev = prev_node

        # 7: Change previous of new_node's next node
        if new_node.next != None:
            new_node.next.prev = new_node

    def append(self, new_data):
        # 1: allocate node and 2: put in the data 
        new_node = Node(data = new_data)
        last = self.head

        # 3: This new_node is going to be the last node, 
        # so make next of this node as NULL
        new_node.next = None

        # 4: If the DLL is empty, make prev of the new_node as NULL
        if self.head == None:
            new_node.prev = None
            self.head = new_node
            return 
        
        # 5: traverse till the last node
        while last.next != None:
            last = last.next
        
        # 6: Make the next of last node as new_node
        last.next = new_node
        
        # 7: Make the previous of new_node as last
        new_node.prev = last

        return

dll = DoublyLinkedList()
dll.append(3)
dll.insertAfter(dll.head.next, 4)
print(dll)



        
# python3 cache.py