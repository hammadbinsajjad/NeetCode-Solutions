from operator import itemgetter

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = [{"val":num, "index":i} for i, num in enumerate(nums)]
        m.sort(key=itemgetter("val"))
        l = 0
        r = len(nums) - 1

        while l < r:
            if m[l]["val"] + m[r]["val"] == target:
                return [m[l]["index"] , m[r]["index"]] 
            elif m[l]["val"] + m[r]["val"] > target:
                r -= 1
            else:
                l += 1