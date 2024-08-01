class Solution:
    '''
    "or" "and" in if loop are sensitive to sequence
    scan by column
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        row = len(strs)
        col = len(strs[0]) # based on the first element

        for c in range(col):
            for r in range(1, row):
                this_str, pre_str = strs[r], strs[r-1]
                if c >= len(this_str) or c >= len(pre_str) or this_str[c] != pre_str[c]: # sensitive to sequence
                    return strs[r][:c]

        return strs[0]
    
class Solution:
# scan by row
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        prefix = strs[0]
        def lcp(str1, str2):
            length = min(len(str1), len(str2))
            for i in range(length):
                if str1[i] != str2[i]:
                    return str1[:i]
            return str1[:length] # ensure always return to a value
        
        for i in range(1, len(strs)):
            prefix = lcp(prefix, strs[i])

        return prefix
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs=sorted(strs) # alphabetically sorted
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 