# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node_values = []
        def find_sums(head):
            curr_sum = 0
            while head:
                if head.val == 0 and curr_sum:
                    node_values.append(curr_sum)
                    curr_sum = 0
                curr_sum += head.val
                head = head.next 

        find_sums(head)
        res = None
        curr = res
        for val in node_values:
            newNode = ListNode(val)
            if not res:
                res = curr = newNode
            else:
                curr.next = newNode
                curr = curr.next
        return res
