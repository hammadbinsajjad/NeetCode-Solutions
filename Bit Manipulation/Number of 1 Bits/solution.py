class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 1
        count = 0
        for _ in range(32):
            if (n & x) == x:
                count += 1
            x = x << 1
        return count
