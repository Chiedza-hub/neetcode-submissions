class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node



class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.last = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node  = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # if list is empty
        if not new_node.next:
            self.last = new_node
        
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        self.last.next = new_node
        self.last = self.last.next
            
        

    def remove(self, index: int) -> bool:

        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next
        # remove the node 

        if curr and curr.next:
            if curr.next == self.last:
                self.last = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
