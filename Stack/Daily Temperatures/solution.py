from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = deque()

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                t = stack.pop()
                res[t[0]] = i - t[0]

            stack.append((i, temp))

        return res