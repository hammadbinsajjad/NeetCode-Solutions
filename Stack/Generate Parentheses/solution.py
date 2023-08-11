from collections import deque
from typing import List

class Solution:
    def __init__(self):
        self.res = list()
        self.seen = set()

    def bt(self, l, r, s, n):
        if l + r == 2*n:
            self.res.append(s)
            return

        if s in self.seen:
            return
        
        self.seen.add(s)

        if l < n:
            self.bt(l + 1, r, s + '(', n)
        
        if r < l:
            self.bt(l, r + 1, s + ')', n)
        

    def generateParenthesis(self, n: int) -> List[str]:
        s = '()'
        self.bt(0, 0, "", n)
        return sorted(self.res)
