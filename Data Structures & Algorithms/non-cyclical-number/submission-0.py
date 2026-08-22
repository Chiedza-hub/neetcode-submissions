class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            total = sum(int(digit) ** 2 for digit in str(n))
            
            if total in seen:
                return False
            
            if total == 1:
                break

            seen.add(total)
            n = total
        return True
