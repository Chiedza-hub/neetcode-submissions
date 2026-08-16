class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "]" : "[", "}" : "{"} # close parenth : open parenth
        for c in s:
            if c in pairs: # if c is a close parenth
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False



