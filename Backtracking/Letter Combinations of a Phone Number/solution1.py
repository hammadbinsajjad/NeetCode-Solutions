from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        res = []

        if len(digits) == 0:
            return res

        if len(digits) == 1:
            for c in m[digits]:
                res.append(c)
            return res

        if len(digits) == 2:
            for c1 in m[digits[0]]:
                for c2 in m[digits[1]]:
                    res.append(c1 + c2)

            return res

        if len(digits) == 3:
            for c1 in m[digits[0]]:
                for c2 in m[digits[1]]:
                    for c3 in m[digits[2]]:
                        res.append(c1 + c2 + c3)

            return res

        if len(digits) == 4:
            for c1 in m[digits[0]]:
                for c2 in m[digits[1]]:
                    for c3 in m[digits[2]]:
                        for c4 in m[digits[3]]:
                            res.append(c1 + c2 + c3 + c4)

            return res