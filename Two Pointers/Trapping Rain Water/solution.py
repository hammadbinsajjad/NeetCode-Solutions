from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_maxs = [0] * n
        right_maxs = [0] * n

        for i in range(1, n):
            left_maxs[i] = max(height[i - 1], left_maxs[i - 1])

        for i in range(n - 2, -1, -1):
            right_maxs[i] = max(height[i + 1], right_maxs[i + 1])

        s = 0
        for i in range(0, n):
            v = max(0, min(left_maxs[i], right_maxs[i]) - height[i])
            s += v
        return s

