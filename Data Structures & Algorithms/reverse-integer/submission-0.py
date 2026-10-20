class Solution:
    def reverse(self, x: int) -> int:
        min_x = -2**31
        max_x = (2**31) - 1

        negative = False
        if x < 0:
            negative = True
            x = -1 * x

        # reverse the string
        str_x = str(x)
        new_x = str_x[::-1]
        new_x = int(new_x)
        
        if negative:
            result = -1 * new_x
            if result < min_x:
                return 0
            return result
        
        if new_x > max_x:
            return 0
        return new_x

        
