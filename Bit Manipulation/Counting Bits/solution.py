class Solution:
    def count1s(self, n):
        x = 1
        count = 0
        for _ in range(32):
            if (n & x) == x:
                count += 1
            x = x << 1
        return count
    def countBits(self, n: int) -> List[int]:
        l = [0] * (n + 1)
        for i in range(n + 1):
            l[i] = self.count1s(i)

        return l
