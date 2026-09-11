class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)

        keys = magazine_count.keys()

        for k, v in ransom_count.items():
            if k in keys:
                if not magazine_count[k] - v >= 0:
                    return False

            else:
                return False
        return True