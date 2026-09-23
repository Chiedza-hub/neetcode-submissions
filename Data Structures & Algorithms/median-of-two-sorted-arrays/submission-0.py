class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def getKth(a, b, k):
            l1 = len(a)
            l2 = len(b)

            if l2 < l1:
                a, b = b, a
            
            if len(a) == 0:
                return b[k - 1]

            if k == 1:
                return min(a[0], b[0])

            i = min(len(a), k // 2)
            j = min(len(b), k // 2)

            if a[i - 1] <= b[j - 1]:
                return getKth(a[i:], b, k - i)
            else: 
                return getKth(a, b[j:], k - j)

        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2

        if total % 2 == 0:
            return (getKth(nums1, nums2, total // 2) + getKth(nums1, nums2, (total // 2) + 1)) / 2.0
        else:
            return getKth(nums1, nums2, (total + 1) // 2)
        
        
            

