class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = [a, b, c]
        result = []

        def getMax(repeated):
            idx = -1
            maxCnt = 0
            for i in range(3):
                if i == repeated or count[i] == 0:
                    continue
                if maxCnt < count[i]:
                    maxCnt = count[i]
                    idx = i
            return idx

        repeated = -1
        while True:
            maxChar = getMax(repeated)
            if maxChar == -1:
                break
            result.append(chr(maxChar + ord('a')))
            count[maxChar] -= 1
            if len(result) > 1 and result[-1] == result[-2]:
                repeated = maxChar
            else:
                repeated = -1

        return ''.join(result)