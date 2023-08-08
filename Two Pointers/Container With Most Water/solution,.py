from typing import List


class Solution:
    def calculateArea(self, l, r, heights):
        return min(heights[l], heights[r]) * abs(l - r)

    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_area = 0

        while l < r:
            cur_area = self.calculateArea(l, r, height)

            max_area = max(cur_area, max_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area

