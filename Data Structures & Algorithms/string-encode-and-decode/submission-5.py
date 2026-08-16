class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:  
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        i = 0
        #scan word to get length first before the '#'
        #and cut out that chunck of length
        while i < len(s):
            if s[i] == '#':
                length = int(s[j:i])
                j = i + 1
                i = j + length
                res.append(s[j:i])
                j = i
            else:
                i += 1
        return res


