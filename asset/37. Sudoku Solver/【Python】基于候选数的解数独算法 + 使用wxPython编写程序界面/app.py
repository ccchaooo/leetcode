# -*- coding: utf-8 -*-
"""###################
基于候选数的数独求解UI界面
Author: Alex_P @UCAS
###################"""

import wx
import Sudoku
from numpy import zeros, int32

"""#################wx.App类#################"""


class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)  # 显示窗口
        # self.frame.Show(False)# 隐藏窗口
        self.SetTopWindow(self.frame)  # 设置为顶层窗口
        return True


"""#################wx.Frame瀛愮被#################"""


class Frame(wx.Frame):
    # 初始化界面
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "An Easy Sukudo Solver", size=(400, 500))
        self.setupMenuBar()  # 菜单
        panel = wx.Panel(self, -1)  # 面板
        wx.StaticText(panel, -1, "Sukudo", (150, 20), (80, -1), wx.ALIGN_CENTER)
        # (位置), (大小), 居中
        mapPosX = 30  # 左上角起始点x坐标
        mapPosY = 50  # 左上角起始点y坐标
        textWidth = 25  # 文本框宽度
        idleWidth = 10  # 横向间距
        idleHeight = 35  # 纵向间距
        sperateLength = 10  # 九宫格间距
        # 初始化数独输入框
        for i in range(0, 9):
            for j in range(0, 9):
                Map_i_j = "self.Map_" + "%d" % i + "_" + "%d" % j  # self.Map_0_0...Map_i_j...Map_8_8
                exec(
                    Map_i_j + " = wx.TextCtrl(panel, -1, '0', pos = (mapPosX + j * (textWidth + idleWidth) + j // 3 * sperateLength, mapPosY + i * idleHeight + i // 3 * sperateLength), size = (textWidth, -1), style = wx.TE_CENTER)")
        # 初始化按钮
        self.button = wx.Button(panel, -1, "Solve", pos=(152, 385), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.OnClickButton, self.button)  # 事件绑定
        self.button.SetDefault()  # 设置为默认按钮
        # 初始化阵列
        self.Sudoku = zeros((9, 9), dtype=int32)  # 数独阵列
        self.Solution = zeros((9, 9), dtype=int32)  # 解阵列

    # 点击按钮的事件响应
    def OnClickButton(self, event):
        Label = self.button.GetLabel()  # 获取按钮状态
        # 解数独
        if Label == "Solve":
            self.button.SetLabel("Waiting...")  # 按钮提示等待
            FAllZero = True  # 全零标识
            for i in range(0, 9):
                for j in range(0, 9):
                    # self.Map_0_0...Map_i_j...Map_8_8
                    Map_i_j = "self.Map_" + "%d" % i + "_" + "%d" % j
                    # 读取输入阵列
                    exec("self.Sudoku[i][j] = " + Map_i_j + ".GetValue()")
                    # 检验输入数独阵列是否合乎要求(0~9)
                    if self.Sudoku[i][j] != 0 and self.Sudoku[i][j] != 1 and self.Sudoku[i][j] != 2 and self.Sudoku[i][
                        j] != 3 and self.Sudoku[i][j] != 4 and self.Sudoku[i][j] != 5 and self.Sudoku[i][j] != 6 and \
                            self.Sudoku[i][j] != 7 and self.Sudoku[i][j] != 8 and self.Sudoku[i][j] != 9:
                        dlg = wx.MessageDialog(self, "Only numbers (0~9, 0 for blank) allowed!", "Error", wx.OK)
                        dlg.ShowModal()
                        dlg.Destroy()
                        self.button.SetLabel("Solve")  # 刷新按钮
                        return
                    # 检验数独阵列是否输入
                    if FAllZero == True and self.Sudoku[i][j] != 0:
                        FAllZero = False
            # 错误提示
            if FAllZero == True:
                dlg = wx.MessageDialog(self, "Please input your Sukudo!", "Error", wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                self.button.SetLabel("Solve")  # 刷新按钮
                return
            # Sudoku.Print_Sudoku(self.Sudoku)
            self.Solution = Sudoku.Solve_Sudoku(self.Sudoku, 0)  # 解数独
            Sudoku.FSingleSolution = False  # 刷新求解函数状态
            # Sudoku.Print_Sudoku(self.Solution)
            for i in range(0, 9):
                for j in range(0, 9):
                    Map_i_j = "self.Map_" + "%d" % i + "_" + "%d" % j  # self.Map_0_0...Map_i_j...Map_8_8
                    exec(Map_i_j + ".SetValue(str(self.Solution[i][j]))")  # 输出解阵列
            self.button.SetLabel("Clear")
        # 清除
        elif Label == "Clear":
            for i in range(0, 9):
                for j in range(0, 9):
                    Map_i_j = "self.Map_" + "%d" % i + "_" + "%d" % j  # self.Map_0_0...Map_i_j...Map_8_8
                    exec(Map_i_j + ".SetValue('0')")  # 清除数独阵列
            self.button.SetLabel("Solve")

    # 建立菜单
    def setupMenuBar(self):
        self.CreateStatusBar()  # 创建
        Menu = wx.MenuBar()  # 总菜单
        programMenu = wx.Menu()  # 程序菜单
        # 将关于加入程序菜单
        menuabout = programMenu.Append(wx.ID_ABOUT, "&About", "About this program")
        # 将退出加入程序菜单
        menuexit = programMenu.Append(wx.ID_EXIT, "&Exit", "Exit program")
        Menu.Append(programMenu, "&Menu")  # 将程序菜单加入总菜单
        # 事件绑定
        self.Bind(wx.EVT_MENU, self.onAbout, menuabout)  # 关于事件
        self.Bind(wx.EVT_MENU, self.onExit, menuexit)  # 退出事件
        self.SetMenuBar(Menu)

    # 点击关于的事件响应
    def onAbout(self, evt):
        dlg = wx.MessageDialog(self, "An Easy Sudoku Solver\n'0' represents blank\n\nAuthor: Alex_Pan @UCAS",
                               "About this program", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    # 点击退出的事件响应
    def onExit(self, evt):
        self.Close(True)


"""#################主函数#################"""


def main():
    app = App()
    app.MainLoop()  # 将app作为主事件消息循环


"""#################main#################"""
if __name__ == '__main__':
    main()