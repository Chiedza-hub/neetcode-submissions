# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = [], []

        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        
        while l2:
            nums2.append(l2.val)
            l2 = l2.next

        nums1.reverse()
        nums2.reverse()
        
        str1 = "".join(map(str, nums1))
        str2 = "".join(map(str, nums2))

        total = int(str1) + int(str2)
        
        tlist = [int(x) for x in str(total)]
        
        head = None
        curr = head 

        for i in range(len(tlist) -1, -1, -1):
            new_node = ListNode(tlist[i])
            if not curr:
                curr = new_node
                head = curr
            else:
                curr.next = new_node
                curr = curr.next
        return head 



        