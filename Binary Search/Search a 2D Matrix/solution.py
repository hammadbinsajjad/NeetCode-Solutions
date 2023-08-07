import bisect
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = [x[0] for x in matrix]

        row_ind = bisect.bisect_left(rows, target)
        print(row_ind)

        if row_ind >= len(matrix):
            row_ind = len(matrix) - 1

        if matrix[row_ind][0] > target and row_ind > 0:
            row_ind -= 1
        elif matrix[row_ind][0] < target and row_ind < len(matrix) - 1:
            row_ind += 1

        col_ind = bisect.bisect_left(matrix[row_ind], target)
        print(col_ind)
        if col_ind < len(matrix[0]) and col_ind >= 0:
            if matrix[row_ind][col_ind] == target:
                return True
        
        return False
