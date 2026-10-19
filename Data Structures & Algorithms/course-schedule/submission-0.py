from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        requirements = defaultdict(list)
        visited = set()

        for course in prerequisites:
            requirements[course[0]].append(course[1])
            
        def dfs(course):
            if course in visited:
                return False

            if not requirements[course]:
                return True
            
            visited.add(course)
            for prereq in requirements[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            requirements[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        


        