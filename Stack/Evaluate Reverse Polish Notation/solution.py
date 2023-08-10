from collections import deque
from math import ceil, floor
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        ops = {
            "+":lambda x1, x2: x1 + x2, 
            "-":lambda x1, x2: x2 - x1, 
            "*":lambda x1, x2: x1 * x2, 
            "/":lambda x1, x2: floor(x2 / x1) if x2 / x1 > 0 else ceil(x2 / x1),

        }

        for el in tokens:
            if el not in ops:
                stack.append(int(el))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(ops[el](n1, n2))

        return stack[-1]
