class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = collections.defaultdict(int),collections.defaultdict(int)
        left, right, valid = 0,0,0
        for c in s1:
            need[c] = need.get(c,0) + 1

        while right < len(s2):
            c = s2[right]
            right += 1
            # window renew
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while left < right and (right-left) >= len(s1):
                if len(need) == valid: # judge if find valid substring
                    return True
                d = s2[left]
                left += 1
                # window renew
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1 # first remove valid
        return False