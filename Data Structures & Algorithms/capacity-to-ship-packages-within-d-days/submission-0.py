class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            numdays = 1
            currCap = cap
            for weight in weights:
                if (currCap - weight < 0) :
                    numdays += 1
                    # prune as soon as you know it wont work
                    if numdays > days:
                        return False
                    currCap = cap # make fresh day 
                currCap -= weight
            return True

        while l <= r:
            cap = (l + r) // 2
            if (canShip(cap)):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res


        