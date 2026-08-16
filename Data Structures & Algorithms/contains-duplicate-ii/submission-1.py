class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        j = 0
        for i in range(len(nums)):
            if abs(j - i) > k:
                window.remove(nums[j])
                j+=1

            if nums[i] in window:
                return True
            window.add(nums[i])
        return False   