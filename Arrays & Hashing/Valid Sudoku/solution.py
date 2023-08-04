from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):

            found = [False] * 10
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if found[int(board[i][j])]:
                    print("1")
                    return False
                else:
                    found[int(board[i][j])] = True

            found = [False] * 10
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if found[int(board[j][i])]:
                    print("2")
                    return False
                else:
                    found[int(board[j][i])] = True

        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                found = [False] * 10

                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] == '.':
                            continue
                        if found[int(board[k][l])]:
                            return False
                        else:
                            found[int(board[k][l])] = True

        return True