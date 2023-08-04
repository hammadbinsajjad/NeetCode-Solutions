from typing import List

class Solution:
    def __init__(self):
        self.dp = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Base Case
        if len(s) == 0:
            return True

        if s in self.dp:
            return self.dp[s]

        # Recursive Case
        for i in range(len(s)):
            if s[0:i + 1] in wordDict:
                st = s[i + 1:len(s)]
                if self.wordBreak(st, wordDict):
                    self.dp[st] = True
                    return True
        self.dp[s] = False
        return False
        