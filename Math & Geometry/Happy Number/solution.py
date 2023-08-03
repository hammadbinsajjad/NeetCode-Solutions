class Solution:
    def square_sum(self, n):
        s = 0
            
        while n > 0:
            s += int(n % 10)**2
            n = n // 10

        return s

    def isHappy(self, n: int) -> bool:
        visited = set()
        t = n
        while t not in visited:
            visited.add(t)
            t = self.square_sum(t)

        if t == 1:
            return True
        else:
            return False
    
    

        