class Solution:
    '''
    "or" "and" in if loop are sensitive to sequence
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        row = len(strs)
        col = len(strs[0])

        for c in range(col):
            for r in range(1, row):
                this_str, pre_str = strs[r], strs[r-1]
                if c >= len(this_str) or c >= len(pre_str) or this_str[c] != pre_str[c]: # sensitive to sequence
                    return strs[r][:c]

        return strs[0]