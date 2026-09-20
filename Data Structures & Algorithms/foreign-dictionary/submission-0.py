class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        dic = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2= words[i], words[i + 1]
            minlen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    dic[w1[j]].add(w2[j])
                    break

        visited = {} # c : True/False if in visited
        result = []


        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True # True means in path
            for d in dic[c]:
                if dfs(d):
                    return True
            result.append(c)
            visited[c] = False

        for char in dic:
            if dfs(char):
                return ""
        result.reverse()
        return "".join(result)

        



        