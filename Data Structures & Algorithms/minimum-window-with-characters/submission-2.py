class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        window, map_t = {}, {} # map of each letter and count
        have, need = 0, len(t) # tracking all letters we need and letters in t

        for ch in t:
            map_t[ch] = 1 + map_t.get(ch, 0)
            
        l = 0 # beginning of substring
        res = [-1, -1] # tracking start and stop positions
        resLen = float("infinity") # large final length to start with
        print(len(s))
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in map_t and map_t[s[r]] >= window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l +1
                # shrink window
                window[s[l]] -= 1;
                if s[l] in map_t and window[s[l]] < map_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l: r + 1] if resLen != float("infinity") else ""
