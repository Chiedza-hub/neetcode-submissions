class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        count = 0
        first = 0
        for i in range(len(s)):
            if s[i] in seen:
                count = max(count, i - first)
                first = max(seen[s[i]] + 1, first) # slide to the next index
            seen[s[i]] = i
            count = max(count, i - first + 1)
        return count
                
                



    