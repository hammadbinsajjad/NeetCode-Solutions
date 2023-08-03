from copy import deepcopy
from typing import List

class Solution:
    def dp(self, nums):
        for i in range(2, len(nums)):
            if i == 2:
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
            else:
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2], nums[i] + nums[i - 3])

        if len(nums) == 2:
            return max(nums)

        return nums[-1]

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]
        
        if len(nums) == 2:
            return max(nums)

        nums1 = deepcopy(nums[:-1])
        nums2 = deepcopy(nums[1:])

        return max(self.dp(nums1), self.dp(nums2))