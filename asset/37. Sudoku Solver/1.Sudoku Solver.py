# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
# Empty cells are indicated by the character '.'
#
# Note:
#
#     The given board contain only digits 1-9 and the character '.'.
#     You may assume that the given Sudoku puzzle will have a single unique solution.
#     The given board size is always 9x9.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.x = y
        self.available = []
        self.value = '.'


class Solution:

    # 创建新的数独库
    def __init__(self):
        self.Sudoku = [[0]*9 for i in range(9)]
        self.board = []

    def getRowAvailableNums(self, y):
        return [[range(9)].remove(n) for n in self.board[y]]

    def getColAvailableNums(self, x):
        return [[range(9)].remove(n[x]) for n in self.board]

    def getCubeAvailableNums(self, x, y):
        return 0
        pass
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board

        list_curb_dict = {
                            '00': {}, '01': {}, '02': {},
                            '10': {}, '11': {}, '12': {},
                            '20': {}, '21': {}, '22': {}}
        for y, row in enumerate(self.Sudoku):
            for x, n in enumerate(row):
                p = Point(x, y)
                # 获取当前行可用的数
                RowAvailable = self.getRowAvailableNums(y)
                # 获取当前列可用的数
                ColAvailable = self.getColAvailableNums(x)
                # 获取当前方阵可用的数
                CubeAvailable = self.getCubeAvailableNums(x,y)
                p.available = [[[range(9)].remove(n) for n in RowAvailable].remove(n) for x in ColAvailable]
                if(len(p.available) == 1):
                    p.value = p.available[0]
                elif(len(p.available) > 1):
                    p.value = 0
        print(self.Sudoku)
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

so = Solution()
print(so.solveSudoku(board))