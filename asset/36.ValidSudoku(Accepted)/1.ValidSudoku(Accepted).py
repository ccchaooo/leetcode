# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


class Solution:
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

b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

so = Solution()
print(so.isValidSudoku(b))

