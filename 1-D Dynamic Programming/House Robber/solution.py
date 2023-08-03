from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            if i == 2:
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
            else:
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2], nums[i] + nums[i - 3])


        if len(nums) == 2:
            return max(nums)

        return nums[-1]