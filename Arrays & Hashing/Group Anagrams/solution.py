from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            st = str(sorted(s))
            if st in m:
                m[st].append(s)
            else:
                m[st] = [s]

        res = []
        for val in m.values():
            res.append(val)

        return res