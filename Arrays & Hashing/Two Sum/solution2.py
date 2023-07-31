class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i, num in enumerate(nums):
            if target - num in m and m[target - num] != i:
                return [i, m[target - num]]
            else:
                m[num] = i