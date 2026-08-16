class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         
        l = 1
        r = max(piles)
        min_rate = r
        while l <= r:
            #m = l + (r // 2)
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours > h:
                l = m + 1
            else: 
                min_rate = m
                r = m - 1
        return min_rate
