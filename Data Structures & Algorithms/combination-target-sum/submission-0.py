class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start,path, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    continue

                path.append(nums[i])
                dfs(i, path, remaining - nums[i])
                path.pop()

        dfs(0, [], target)
        return result            
                   