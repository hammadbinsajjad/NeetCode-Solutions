from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        v = digits[-1] + 1
        if v >= 10:
            carry = 1
            v = v % 10
        else:
            carry = 0
        digits[-1] = v

        if carry != 0:
            for i in range(len(digits) - 2, -1, -1):
                v = digits[i] + carry
                if v >= 10:
                    carry = 1
                    v = v % 10
                else:
                    carry = 0
                digits[i] = v

        if carry != 0:
            digits = [1] + digits
        
        return digits