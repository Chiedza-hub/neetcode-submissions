class Node:
    def __init__(self, value: int, key: int):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0) 
        self.tail = Node(0, 0)
        self.head.next =  self.tail
        self.tail.prev = self.head 
        self.nodeMap = {}
        self.numNodes = 0
        
    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        if self.head.next != node:
            # move to front
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next 
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            
        return self.nodeMap[key].value
       

    def put(self, key: int, value: int) -> None:
        
        # if it exists update the value
        if key in self.nodeMap:
            self.nodeMap[key].value = value
            self.get(key)
            return 
        
        # else check capacity 
        if self.numNodes == self.capacity:
            remove_key = self.tail.prev.key
            # if only one 
            if self.head.next == self.tail.prev:
                self.head.next = self.tail 
                self.tail.prev = self.head
            else:
                new_last = self.tail.prev.prev
                new_last.next = self.tail
                self.tail.prev = new_last
            # remove it from Map
            del self.nodeMap[remove_key]
            self.numNodes -= 1

        
        # add to front
        new_node = Node(value, key)
        if self.head.next == self.tail:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
            new_node.prev = self.head
            
        else:
            new_node.next = self.head.next
            self.head.next.prev = new_node
            new_node.prev = self.head
            self.head.next = new_node

        self.numNodes += 1
        self.nodeMap[key] = new_node
        

        













