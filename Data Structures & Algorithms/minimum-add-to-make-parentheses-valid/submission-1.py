class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        pending = 0 # ( adds and ) subtracts 
        stack = []
        for p in s:
            if p == "(":
                stack.append(p)
                pending += 1
            else:
                if stack: 
                    pending -= 1
                    stack.pop()
                else:
                    pending += 1
        # return the positive number always 
        return pending 
