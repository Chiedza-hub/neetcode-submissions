class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = {i: [] for i in range(numCourses)}
        # get all the prereqs
        for course, prereq in prerequisites:
            reqs[course].append(prereq)

        visited, cycle = set(), set()
        path = []

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            visited.add(course)
            cycle.add(course)
            
            for prereq in reqs[course]:
                if not dfs(prereq):
                    return False
        
            path.append(course)   
            visited.add(course)
            cycle.remove(course) # no longer on the path we are on
            return path

        for i in range(numCourses):
            if not dfs(i):
                return []
        return path
            
                


        

        

