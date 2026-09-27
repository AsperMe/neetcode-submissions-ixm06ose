class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        i, j = len(a) -1, len(b) - 1
        while i>=0 or j>=0 or carry>0:
            digA = int(a[i]) if i>=0 else 0
            digB = int(b[j]) if j>=0 else 0

            total = digA + digB + carry
            result.append(total%2)
            carry = total // 2

            i-=1
            j-=1

        result.reverse()
        return ''.join(map(str, result))    