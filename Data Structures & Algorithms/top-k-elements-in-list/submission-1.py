class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {} # number:frequency
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            mp[num] = 1 + mp.get(num, 0)
        for n, c in mp.items(): # mp.items is a key, value tupple hence n, c
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):  # from last element to 0, decerementing by one 
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
