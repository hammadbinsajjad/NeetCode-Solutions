import math
def cm(s):
    return ord(s) - 65

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c = [0] * 26
        m = -math.inf 
        for r in range(len(s)):
            c[cm(s[r])] += 1
            mf = max(c)
            while (r - l + 1) - mf > k:
                c[cm(s[l])] -= 1
                l += 1

            m = max(r - l + 1, m)

        return m