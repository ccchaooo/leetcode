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
        self.value = 0


class Solution:

    # 创建新的数独库
    def __init__(self):
        # self.Sudoku = [[0]*9 for i in range(9)]
        self.Sudoku = []
        self.board = []

    # 获取行记录
    def getRowNums(self, y):
        return self.board[y]

    # 获取列记录
    def getColNums(self, x):
        return [n[x] for n in self.board]

    # 获取九宫格记录
    def getCubeNums(self, x, y):
        return 0

    def selfCount(self):
        for y, row in enumerate(self.board):
            for x, n in enumerate(row):
                p = Point(x, y)
                # 获取当前行已用的数
                Row = self.getRowNums(y)

                # 获取当前列已用的数
                Col = self.getColNums(x)

                # 排除所有已使用的数
                range9 = [x for x in range(1, 10)]
                for x in Row + Col:
                    if x in range9:
                        range9.remove(x)
                p.available = range9
                if len(range9) == 1:
                    p.value = range9[0]
                else:
                    p.value = 0

                # 存入数独库
                self.Sudoku[x][y] = p
            return self.Sudoku

    # 构建数独库
    def constBoard(self):
        self.board = [[0]*9 for i in range(1, 10)]
        for y, row in enumerate(board):
            for x, n in enumerate(row):
                if n is '.':
                    self.board[y][x] = 0
                else:
                    self.board[y][x] = int(n)
        return True

    def constSudoku(self):
        self.Sudoku  = [list(range(1, 10)) for x in range(9)]
        for y, row in enumerate([list(range(1, 10)) for x in range(1, 10)]):
            for x, n in enumerate(row):
                p = Point(x, y)
                self.Sudoku[y][x] = p
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        list_curb_dict = {
                            '00': {}, '01': {}, '02': {},
                            '10': {}, '11': {}, '12': {},
                            '20': {}, '21': {}, '22': {}}

        # 构建完毕则自我迭代一次
        if self.constBoard() and self.constSudoku():
            for y, row in enumerate(self.selfCount()):
                for x, p in enumerate(row):
                    if p.value > 0:
                        self.board[x][y] = p.value

        return True


    # 测试专用
    def test(self):
        s = [list(range(1, 10)) for x in range(1, 10)]
        for y, row in enumerate([list(range(1, 10)) for x in range(1, 10)]):
            for x, n in enumerate(row):
                p = Point(x, y)
                s[y][x] = p
        print(s)





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
# so.test()
print(so.solveSudoku(board))