class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # loop through all strings and check each index is the same 

        res = ""
        ref = strs[0]
        i = 0
        while i < len(ref):
            for word in strs:
                if i >= len(word) or word[i] != ref[i]:
                    return res
            res += ref[i]
            i += 1
        return res

