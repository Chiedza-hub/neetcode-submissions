import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search from 0 to h 
        def can_eat_all(rate):
            hours = 0
            for i in range(len(piles)):
                hours_taken = math.ceil(piles[i] / rate)
                hours += hours_taken
                if hours > h:
                    return False
            return True

        l, r = 1, sum(piles)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            if can_eat_all(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
