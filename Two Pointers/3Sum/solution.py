import bisect
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        i = 0
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                v = nums[i] + nums[l] + nums[r]

                if v < 0:
                    l += 1
                elif v > 0:
                    r -= 1
                else:
                    res.append(sorted([nums[l], nums[r], nums[i]]))
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            i += 1

        return res
