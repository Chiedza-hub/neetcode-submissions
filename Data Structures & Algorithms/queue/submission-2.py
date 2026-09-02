class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    
class Deque:

    def __init__(self):
        self.head = None
        self.tail = self.head


    def isEmpty(self) -> bool:
        return self.head is None
        

    def append(self, value: int) -> None:
        new_node = Node(value)

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = self.tail = new_node 
         
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = self.head.prev
        else:
            self.head = self.tail = new_node 

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        temp = self.tail.value
        if self.head == self.tail:
            self.head = self.tail.prev
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

        return temp
    

    def popleft(self) -> int:

        if self.isEmpty():
            return -1
        
        temp = self.head.value
        if self.tail == self.head:
            self.tail = self.head.next
        new_head = self.head.next
        if self.head.next:
            self.head.next.prev = None
        self.head = new_head

        return temp
        
