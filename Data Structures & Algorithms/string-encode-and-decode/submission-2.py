class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            
            res += str + "#end#" 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        for i in range(len(s)):
            if s[i] == '#' and s[i: i + 5] == '#end#':
                res.append(s[start:i])
                start = i + 5
        return res

