class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute force 
        # loop through i and loop through j
        # if elements are the same, continue for j and find an element that is bigger else give one 
        '''
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
        '''
        # optimized : the monotonic stack

        res = [-1] * len(nums1)
        numsIdx = {n : i for i, n in enumerate(nums1)}

        stack = []
        for i in range(len(nums2)):
            # remove everything that is lower than the curr num in stack
            while stack and nums2[i] > stack[-1]:
                num = stack.pop()
                idx = numsIdx[num]
                res[idx] = nums2[i]
            if nums2[i] in numsIdx:
                stack.append(nums2[i])
        return res
