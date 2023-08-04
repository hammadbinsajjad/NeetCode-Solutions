class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for n in nums:
            m[n] = m.get(n, 0) + 1

        m = sorted(m, reverse=True, key=lambda x:m[x])

        res = [0] * k
        i = 0
        for key in m:
            if i == k:
                break
            res[i] = key
            i += 1
        return res

        