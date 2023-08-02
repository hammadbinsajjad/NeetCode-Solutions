from heapq import heapify, heappush, heappop, nlargest

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            y = abs(heappop(stones))
            x = abs(heappop(stones))
            if y > 0:
                heappush(stones, -1 * (y - x))

        if len(stones) == 1:
            return abs(stones[0])
        else:
            return 0
