class Solution:
    board = []
    totalnum = 0
    totaliterate = 0  # count iteration times
    posTofill = dict()  # we use this dict to keep track of which pos we should try in the next.( we choose the one that are most constrained)

    def emptyInRow(self, row):
        cnt = 0
        for num in self.board[row]:
            if num == ".":
                cnt += 1
        return cnt

    def emptyInCol(self, col):
        cnt = 0
        for row in self.board:
            if row[col] == ".":
                cnt += 1
        return cnt

    def emptyInGrid(self, row, col):
        cnt = 0
        subRow = row//3
        subCol = col//3
        for rownumber in range(subRow*3, subRow*3+3):
            for colnumber in range(subCol*3, subCol*3+3):
                if self.board[rownumber][colnumber] == ".":
                    cnt += 1
        return cnt

    def vaildInRow(self, num, row):
        for item in self.board[row]:
            if (item == str(num)):
                return False
        return True

    def vaildInColumn(self, num, col):
        for row in range(len(self.board)):
            if self.board[row][col] == str(num):
                return False
        return True

    def validInSubGrid(self, num, row, col):
        # make sure which grid the num belongs to
        subRow = row//3
        subCol = col//3
        for rownumber in range(subRow*3, subRow*3+3):
            for colnumber in range(subCol*3, subCol*3+3):
                if self.board[rownumber][colnumber] == str(num):
                    return False
        return True

    def updateposTofill(self, row, col, add):
        # if add -> add = 1 if delete add=-1, add=1 means add number into (row,col)
        # after add nums to position (row,col) update self.posTofill
        subrow = row//3
        subcol = col//3

        for pos in self.posTofill:
            # whithin same grid
            if (pos[0] >= subrow*3 and pos[0] <= subrow*3+3 and pos[1] >= subcol*3 and pos[1] >= subcol*3+3):
                self.posTofill[pos] -= 1*add
            # in same row or col
            if pos[0] == row or pos[1] == col:
                self.posTofill[pos] -= 1*add

        if add == 1:
            self.posTofill.pop((row, col))
        else:
            self.posTofill[(row, col)] = self.emptyInRow(
                row)+self.emptyInCol(col) + self.emptyInGrid(row, col)
        # re sort self.posTofill
        self.posTofill = dict(
            sorted(self.posTofill.items(), key=lambda item: item[1]))

    def backtrack(self, row, col):
        if self.totalnum >= 81:
            print('arrived')
            return True

    def solveSudoku(self, board: list[list[str]]) -> None:

        # def backtrack(self, row, col):

        #     self.totaliterate += 1
        #     # print(row, col, self.totalnum, self.totaliterate)
        #     print(len(self.posTofill))
        #     if self.totalnum == 81:
        #         print('I arrive here!')
        #         return True

        #     #  add num and update posTofill. we suppose we can find valid num at row,col
        #     self.updateposTofill(row, col, 1)
        #     if len(self.posTofill) == 0:
        #         next_pos = [row, col]
        #     else:
        #         next_pos = list(self.posTofill.keys())[0]
        #     next_row = next_pos[0]
        #     next_col = next_pos[1]

        #     for num in range(1, 10):
        #         # check column, check row, check 3*3 grid
        #         if self.vaildInColumn(num, col) and self.vaildInRow(num, row) and self.validInSubGrid(num, row, col):
        #             # this num is valid at [row,col] so we add num
        #             self.board[row][col] = str(num)
        #             self.totalnum += 1
        #             # check if all subsequent nums are valid
        #             if self.backtrack(next_row, next_col):
        #                 return True
        #             else:
        #                 # this num is not valid we should try next num
        #                 self.totalnum -= 1
        #                 self.board[row][col] = "."

        #     # if all num from 1->9 is tried still not working
        #     # remove num from (row,col) and update posTofill
        #     self.updateposTofill(row, col, -1)
        #     return False

        # def solveSudoku(self, board: list[list[str]]) -> None:
        #     """
        #     Do not return anything, modify board in-place instead.
        #     """
        #     self.board = board[::]
        #     self.totalnum = 0
        #     self.posTofill = dict()
        #     for i in range(len(self.board)):
        #         for j in range(len(self.board[i])):
        #             if self.board[i][j] != ".":
        #                 self.totalnum += 1
        #             else:
        #                 # find nums already in same line, same row and same grid
        #                 cnt = self.emptyInRow(
        #                     i)+self.emptyInCol(j) + self.emptyInGrid(i, j)
        #                 self.posTofill[(i, j)] = cnt
        #     # order self.posTofill by value
        #     self.posTofill = dict(
        #         sorted(self.posTofill.items(), key=lambda item: item[1]))
        #     print(self.posTofill)
        #     first_pos = list(self.posTofill.keys())[0]
        #     print(first_pos)
        #     value = self.backtrack(first_pos[0], first_pos[1])
        #     board = self.board
        #     print(value)
        #     print(self.board)

        # print(self.totaliterate)


s = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
board = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."]
]
s.solveSudoku(board)
