class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        amount = 0
        max_amount = 0

        while start < end:
            gap = end - start
            amount = min(heights[start], heights[end]) * gap
            max_amount = max(amount, max_amount)

            if (heights[end] > heights[start]):
                start += 1
            else:
                end -= 1

        return max_amount