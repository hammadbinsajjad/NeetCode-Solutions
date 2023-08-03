class Solution:
    def reverse(self, x: int) -> int:
        MIN_LIMIT = -(2**31)
        MAX_LIMIT = (2**31) - 1

        neg = True if x < 0 else False

        x = abs(x)

        res = 0
        while x > 0:
            print(x)
            dig = int(x % 10)
            res = (res * 10) + dig

            if res < MIN_LIMIT or res > MAX_LIMIT:
                return 0

            x =  int(x / 10)

        if neg:
            res = -res

        return res

