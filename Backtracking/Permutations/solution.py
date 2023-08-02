from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[x for x in perm] for perm in set(permutations(nums))]
        return res
