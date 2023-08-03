from typing import List

class Solution:
    def __init__(self):
        self.res = []
    def backtrack(self, i, digits, curstr):

        m = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if i == len(digits):
            self.res.append(curstr)
            return
        
        for c in m[digits[i]]:
            self.backtrack(i + 1, digits, curstr + c)

    def letterCombinations(self, digits: str) -> List[str]:
        self.backtrack(0, digits, "")

        if self.res == [""]:
            self.res = []

        return self.res