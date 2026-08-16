class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        length = 0
        start = 0
        count = 0


        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]] += 1    
            else:
                mp[s[i]] = 1
            
            #check if valid 
            window = i - start + 1
            max_letter = max(mp.values())

            if window - max_letter <= k:
                length = max(length, window)
            else:
                mp[s[start]] -= 1
                start += 1
                
        return length
            


        

        
