class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)  # mapping count to list of anagrams
        
        for s in strs:
            count = [0] * 26  # a ... z
            for x in s:
                count[ord(x) - ord("a")] += 1 # increment the index when you see the letter
            res[tuple(count)].append(s)  # cast to tuple for python syntax

        return list(res.values())
             
