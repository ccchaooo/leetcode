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
        self.available = list(range(1, 10))
        self.value = 0
        # 优先级,由于维护一个dict,根据available来排序
        self.priority = 9


class Solution:

    # 创建新的数独库
    def __init__(self):
        self.Sudoku = []
        self.pridict = dict()

    # 测试是否冲突
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        list_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        list_curb_dict = {
                            '00': {}, '01': {}, '02': {},
                            '10': {}, '11': {}, '12': {},
                            '20': {}, '21': {}, '22': {}}
        for y, li in enumerate(board):
            di = {}
            for x, n in enumerate(li):
                if n != '.':
                    # 判断该数字是否在同一行中出现
                    if n not in di:
                        di[n] = x
                    else:
                        return False

                    # 判断该数字是否在同一列中已出现
                    if n not in list_dict[x]:
                        list_dict[x][n] = x
                    else:
                        return False

                    # 判断该数字是否在九宫格内出现
                    # p代表该数字在九宫格的位置
                    p = str(y//3)+str(x//3)
                    if n not in list_curb_dict.get(p):
                        list_curb_dict.get(p)[n] = x
                    else:
                        return False
        return True

    # 将传入数据构造成数独库
    def constSudoku(self, board):
        self.Sudoku = [list(range(1, 10)) for x in range(9)]
        for y, row in enumerate(board):
            for x, n in enumerate(row):
                p = Point(x, y)
                if n is not '.':
                    p.available = []
                    p.value = int(n)
                p.priority = len(p.available)
                self.Sudoku[y][x] = p
        print('------构建完成-------')
        self.printRet()
        return True

    # 获取行记录
    def getRowNums(self, Sudoku, y):
        return [p.value for p in Sudoku[y]]

    # 获取列记录
    def getColNums(self, Sudoku, x):
        return [row[x].value for row in Sudoku]

    # 获取九宫格记录
    def getCubeNums(self, Sudoku, x, y):
        x_head = x
        x_end = (x // 3 + 1) * 3-1
        y_head = y
        y_end = (y // 3 + 1) * 3-1
        # 九宫格数独
        arr = []
        j = y_head
        while j <= y_end:
            row = Sudoku[j]
            i = x_head
            while i <= x_end:
                p = row[i]
                arr.append(p.value)
                i = i + 1
            j = j + 1
        return arr

    def selfCount(self,Sudoku):
        retFlag = False
        for y, row in enumerate(Sudoku):
            for x, p in enumerate(row):

                # 仅仅当前p点的value == 0 时才进行计算
                if p.value == 0:
                    # 获取当前行已用的数
                    Row = self.getRowNums(Sudoku, y)

                    # 获取当前列已用的数
                    Col = self.getColNums(Sudoku, x)

                    # 获取当前九宫格已使用的数
                    Cube = self.getCubeNums(Sudoku, x, y)

                    # 排除所有已使用的数
                    range9 = [s for s in range(1, 10)]
                    for s in Row + Col + Cube:
                        if s in range9:
                            range9.remove(s)

                    # 判断是否修改
                    if len(p.available) != len(range9):
                        retFlag = True

                    p.available = range9
                    p.priority = len(p.available)
                    if len(p.available) == 1:

                        print('------in--------')
                        print('x:', x)
                        print('y:', y)
                        print('------in--------')
                        print('------bf--------')
                        self.printRet()
                        print('------bf--------')

                        if y == 2 and x == 6:
                            print(x, y)
                            Cube = self.getCubeNums(Sudoku, x, y)

                        p.value = range9[0]

                        print('------af--------')
                        self.printRet()
                        print('------af--------')

        if retFlag is not True:
            self.printRet()

        return retFlag

    def printRet(self):
        # 返回参数
        ret = []
        for row in self.Sudoku:
            arr = []
            for p in row:
                arr.append(p.value)
            ret.append(arr)
            print(arr)
        return ret

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        list_curb_dict = {
                            '00': {}, '01': {}, '02': {},
                            '10': {}, '11': {}, '12': {},
                            '20': {}, '21': {}, '22': {}}

        # 构建完毕则自我迭代
        if self.constSudoku(board):
            flag = True
            while flag:
                flag = self.selfCount(self.Sudoku)
            # print(self.Sudoku)


    # 测试专用
    def test(self):
        s = [list(range(1, 10)) for x in range(1, 10)]
        for y, row in enumerate([list(range(1, 10)) for x in range(1, 10)]):
            for x, n in enumerate(row):
                p = Point(x, y)
                s[y][x] = p
        print(s)





b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

c = [["1", ".", ".", ".", "6", ".", ".", ".", "8"],
     [".", "4", "7", "8", ".", "5", ".", ".", "."],
     [".", "5", "9", ".", "2", "3", ".", ".", "."],
     [".", ".", "2", ".", "1", "8", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", "7", "3", "."],
     [".", ".", ".", ".", "3", ".", "9", "1", "."],
     [".", ".", ".", ".", ".", "2", ".", "4", "."],
     ["5", "7", ".", ".", "8", ".", ".", ".", "."]]

so = Solution()
# so.test()
so.solveSudoku(c)