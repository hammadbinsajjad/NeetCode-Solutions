import bisect

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        return i if i < len(nums) and nums[i] == target else -1