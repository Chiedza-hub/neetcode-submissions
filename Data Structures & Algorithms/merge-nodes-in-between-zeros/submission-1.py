# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy 
        curr_sum = 0
        curr = head.next
        while curr:
            if curr.val == 0:
                tail.next = ListNode(curr_sum)
                tail = tail.next
                curr_sum = 0
            curr_sum += curr.val
            curr = curr.next 

        return dummy.next
