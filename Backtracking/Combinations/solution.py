from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combs = set(combinations(range(1,n + 1), k))
        return [[x for x in comb] for comb in combs]