class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []

        for key in count:
            if count[key] > len(nums) // 3:
                result.append(key)

        return result        