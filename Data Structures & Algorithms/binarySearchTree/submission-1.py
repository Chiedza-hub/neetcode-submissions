class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        node = Node(key, val)
        curr = self.root
        prev = None
        while curr:
            prev = curr
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                curr.val = val
                return
        if not prev:
            self.root = node
            return
        if prev.key > key:
            prev.left = node
        else:
            prev.right = node
        return




    def get(self, key: int) -> int:

        curr = self.root
        while curr:
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr.val

        return -1


    def getMin(self) -> int:
        curr = self.root
        prev = None
        while curr:
            prev = curr
            curr = curr.left
        if not prev:
            return -1
        return prev.val


    def getMax(self) -> int:

        curr = self.root
        prev = None
        while curr:
            prev = curr
            curr = curr.right
        
        if not prev:
            return -1
        return prev.val

    def remove(self, key: int) -> None:

        curr = self.root
        prev = None
        while curr:
            
            if curr.key > key:
                prev = curr
                curr = curr.left
            elif curr.key < key:
                prev = curr
                curr = curr.right
            else:
                break
        # node not found 
        if not curr:
            return 

        # node has 2 children

        if curr.left and curr.right:
            succ_parent = curr
            successor = curr.right
            while successor.left:
                succ_parent = successor
                successor = successor.left
            # copy values
            curr.val = successor.val
            curr.key = successor.key
            # delete 
            curr = successor
            prev = succ_parent
        # if node has one child
        child = curr.left if curr.left else curr.right

        # deleting the root
        if not prev:
            self.root = child
            return 

        if prev.left == curr:
            prev.left = child
        else:
            prev.right = child
        return 
        
    def getInorderKeys(self) -> List[int]:

        result = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.key)
            inorder(root.right)
        inorder(self.root)
        return result


