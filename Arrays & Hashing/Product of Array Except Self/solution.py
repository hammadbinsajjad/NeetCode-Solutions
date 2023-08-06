from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

            