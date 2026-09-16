class Solution:
    # sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c,0)+1
            while left< right and window.get(c) >1: # no repeating window
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right-left)

        return res