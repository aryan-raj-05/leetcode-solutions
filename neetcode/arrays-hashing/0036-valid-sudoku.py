from typing import List

class Solution:
    def isValidSudoku_optimized(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                box_index = (i // 3) * 3 + j // 3

                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for 3 x 3 squares
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                count = set()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] == ".":
                            continue
                        elif board[i + k][j + l] in count:
                            return False
                        else:
                            count.add(board[i + k][j + l])

        # columns
        for i in range(9):
            count = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in count:
                    return False
                else:
                    count.add(board[i][j])

        # rows
        for i in range(9):
            count = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in count:
                    return False
                else:
                    count.add(board[j][i])

        return True
