class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0

        while start < len(numbers):
            for i in range(start + 1, len(numbers)):
                if numbers[start] + numbers[i] == target:
                    return [start + 1, i + 1]
            start += 1
        return []