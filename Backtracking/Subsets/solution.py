from copy import deepcopy
from typing import List
class Solution:
    def __init__(self):
        self._subsets = []
    def backtrack(self, nums, subset, i):
        if i == len(nums):
            self._subsets.append(subset)
            return

        _subset = deepcopy(subset)
        self.backtrack(nums, deepcopy(_subset), i + 1)
        _subset.append(nums[i])
        self.backtrack(nums, _subset, i + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [], 0)
        return self._subsets
