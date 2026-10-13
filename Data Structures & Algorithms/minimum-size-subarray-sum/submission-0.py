class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf')

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum >= target:
                    result = min(result, j-i+1)
                    break

        return 0 if result == float("inf") else result            