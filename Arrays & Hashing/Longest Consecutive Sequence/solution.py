from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        max_len = 1
        current_len = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_len += 1
                max_len = max(current_len, max_len)
            else:
                print(nums[i])
                current_len = 1
            print(current_len)

        return max_len
