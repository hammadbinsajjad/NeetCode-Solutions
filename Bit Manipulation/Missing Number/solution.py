class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s1 = len(nums)*(len(nums)+1) / 2
        s2 = 0
        for n in nums:
            s2 += n

        return int(s1 - s2)