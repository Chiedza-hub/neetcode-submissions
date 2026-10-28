class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        len_hay = len(haystack)

        for i in range(len_hay):
            if i + len_n <= len_hay and haystack[i:i + len_n] == needle:
                return i
        return -1
