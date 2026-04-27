class Solution:
    def reverse(self, x: int) -> int:
        y = x
        x = abs(x)
        res = int(str(x)[::-1])
        if y < 0:
            res *= -1
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res