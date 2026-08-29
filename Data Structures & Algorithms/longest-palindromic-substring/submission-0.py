class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
            return l + 1, r - 1
        
        for i in range(len(s)):
            # odd
            l, r = expand(i, i)
            if r - l + 1 > res_len:
                res = s[l: r + 1]
                res_len = r - l + 1
            # even
            l, r = expand(i, i + 1)
            if r - l + 1 > res_len:
                res = s[l: r + 1]
                res_len = r - l + 1
        return res