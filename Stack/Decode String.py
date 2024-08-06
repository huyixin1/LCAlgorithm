class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = "" # current string being decoded
        curr_num = 0 # current number being processed
        
        for c in s:
            if c.isdigit():
                curr_num = curr_num*10 + int(c)
            elif c == '[':
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif c == ']':
                pre_str = stack.pop()  
                pre_num = stack.pop()  
                curr_str = pre_str + curr_str * pre_num # eg:a2[c]
            else:
                curr_str += c
        
        return curr_str