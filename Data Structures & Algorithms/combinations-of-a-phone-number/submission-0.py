class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        result = []
        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"rqps",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(i, path):
            if i == len(digits):
                result.append(path)
                return 

            for ch in phone[digits[i]]:
                dfs(i+1, path + ch)

        dfs(0, "")
        return result        