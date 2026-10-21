class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        result = r

        def Ship(cap):
            ships, curr_cap = 1, cap
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr_cap = cap

                curr_cap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if Ship(cap):
                result = min(result, cap)
                r = cap - 1
            else:
                l = cap + 1

        return result

