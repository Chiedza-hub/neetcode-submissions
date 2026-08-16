class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is bigger than s2
        if len(s1) > len(s2): return False
        # create a hashmap for s1
        count1 = {}
        for c in s1: 
            count1[c] = 1 + count1.get(c, 0)
            
        length = len(count1)
        # compare the hashmaps of s1 and s2
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == length:
                    return True
        return False
        

        

       
            