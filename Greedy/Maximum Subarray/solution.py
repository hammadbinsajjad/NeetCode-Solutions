from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        i = 1
        for n in nums[1:len(nums)]:
            if n > current_sum + n:
                current_sum = n
            else:
                current_sum =  n + current_sum
            max_sum = max(current_sum, max_sum)
            i += 1

        return max_sum
            