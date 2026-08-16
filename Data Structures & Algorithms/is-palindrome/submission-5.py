class Solution:
    def isPalindrome(self, s: str) -> bool:
        # parse with two pointers, from the left and the right till they meet 
        end = len(s) - 1
        start = 0
        
        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True