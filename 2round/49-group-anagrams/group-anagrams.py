class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # HashMap
        res = []
        anagrams_hash = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in anagrams_hash:
                anagrams_hash[k].append(s)
            else:
                anagrams_hash[k] = [s]

        # for key, value in enumerate(anagrams_hash):
        for key, value in anagrams_hash.items():
            res.append(value)

        return res 
        # could be short as return list(anagrams_hash.values())
            