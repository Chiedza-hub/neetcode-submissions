class Solution:
    def maxArea(self, heights: List[int]) -> int:
        end = 0
        amount = 0
        max_amount = 0

        for i, h in enumerate(heights):
            end = i + 1
            while end < len(heights):
                gap = end - i
                amount = min(h, heights[end]) * gap
                max_amount = max(amount, max_amount)
                end += 1

        return max_amount