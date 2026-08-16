class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  have to be same size to be anagrams
        if len(s) != len(t):
            return False
        mp_s = {}
        mp_t = {}
        for x in s:
            mp_s[x] = 1 + mp_s.get(x, 0)
        for y in t:
            mp_t[y] = 1 + mp_t.get(y, 0)
        
        if mp_s == mp_t:
            return True
            
        return False
        