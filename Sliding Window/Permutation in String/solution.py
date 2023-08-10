class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        if size > len(s2):
            return False
        first = s1[0]
        count_s1 = [0] * 26

        for c in s1:
            count_s1[ord(c) - 97] += 1

        count_s2 = [0] * 26
        
        l = 0

        for r in range(len(s2)):
            count_s2[ord(s2[r]) - 97] += 1

            if (r - l + 1) > size:
                count_s2[ord(s2[l]) - 97] -= 1
                l += 1

            if count_s2 == count_s1:
                return True

        return False
