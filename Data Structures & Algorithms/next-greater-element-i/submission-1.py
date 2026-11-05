class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute force 
        # loop through i and loop through j
        # if elements are the same, continue for j and find an element that is bigger else give one 
        result = [-1 for i in range(len(nums1))] 
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    idx = j + 1
                    while idx < len(nums2):
                        if nums2[idx] > nums2[j]:
                            result[i] = nums2[idx]
                            break
                        idx += 1
                    break


        return result