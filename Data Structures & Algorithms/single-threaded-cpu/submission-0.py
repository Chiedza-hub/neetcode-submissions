import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for idx, task in enumerate(tasks):
            task.append(idx)

        tasks.sort(key = lambda x: x[0])# sort by enqueuetime

        minHeap = []
        result = []
        i = 0
        curr_time = tasks[0][0] # first enqueue time 

        while i < len(tasks) or minHeap:
            while i < len(tasks) and tasks[i][0] <= curr_time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if minHeap:
                processt, idx = heapq.heappop(minHeap)
                curr_time += processt
                result.append(idx)
            else:
                curr_time = tasks[i][0]

        return result 




           