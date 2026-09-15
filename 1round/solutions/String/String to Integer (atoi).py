class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 -1
        INT_MIN = -(2**31)
        sign = 1
        i = 0
        res = 0
        
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s): # all whitespace
            return 0

        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1  
        elif i < len(s) and s[i] == '+':
            i += 1 # positivity is neither present
        if i == len(s): # all signed
            return 0
        while i < len(s) and s[i] == "0": # skip leading 0
            i += 1

        start = i
        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i += 1
        if start == i: # no digits found
            return 0
        res *= sign

        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        else: return res
