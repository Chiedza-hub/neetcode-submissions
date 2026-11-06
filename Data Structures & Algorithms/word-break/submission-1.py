class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}

        def find_words_rec(s):
            if len(s) == 0:
                return True
            if s in mem:
                return mem[s]
        
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict and find_words_rec(s[i:]):
                    mem[s] = True
                    return True
            mem[s] = False
            return False

        return find_words_rec(s)

        