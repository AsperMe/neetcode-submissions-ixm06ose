class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        curr = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])

            if i == curr:
                count += 1
                curr = farthest

        return count    