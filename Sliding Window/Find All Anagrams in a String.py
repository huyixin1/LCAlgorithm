class Solution:
    # find all permutation p in string s
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = {}
        need = {}
        left, right, valid = 0, 0, 0
        res = []
        for c in p:
            need[c] = need.get(c,0) +1 # get(c,0) safely access c-value
        while right < len(s):
            c = s[right]
            right += 1
            # renew window
            if c in need:
                window[c] = window.get(c,0) +1
                if window[c] == need[c]: 
                    valid += 1   # how many characters in the window has same frequency as need     
            while left < right and right - left >= len(p):
                if valid == len(need): # is anagram
                    res.append(left)
                d = s[left]
                left += 1
                # renew window
                if d in need:
                    if window[d] == need[d]: # already added, move to next
                        valid -= 1
                    window[d] -= 1
        return res