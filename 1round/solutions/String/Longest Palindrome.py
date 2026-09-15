class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd_flag = False # flag to mark
        for i in count.values():
            if i % 2 == 0:
                res = res + i
            else:
                odd_flag = True
                res = res + i - 1

        return res +1  if odd_flag else res