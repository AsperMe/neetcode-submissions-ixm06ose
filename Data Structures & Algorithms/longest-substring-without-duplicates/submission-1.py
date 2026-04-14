class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = {}
        l = 0
        max_len = 0

        for r, ch in enumerate(s):
            if ch in char_set and char_set[ch] >= l:
                l = char_set[ch] + 1
            char_set[ch] = r
            max_len = max(max_len, r-l+1)
        return max_len 