"""界面与逻辑"""

import tkinter.messagebox as msgbox
from tkinter.filedialog import askdirectory
from tkinter import Button, Entry, Label, Menu, StringVar, Tk
from typing import Callable, NoReturn

import config
import functions

ROOT = Tk()


_PATH = StringVar()  # 路径动态存储
_RESIZEABLE_X = False  # 在水平方向是否可以拉伸
_RESIZEABLE_Y = False  # 在垂直方向是否可以拉伸

# 定义回调函数
def _load_help() -> NoReturn:
    """打开帮助文件"""
    functions.notepad(config.HELP)


def _exit() -> NoReturn:
    """退出程序 - 销毁窗口"""
    ROOT.destroy()


def _select() -> NoReturn:
    """询问选择文件夹地址"""
    _PATH.set(askdirectory())


def success(console: bool) -> NoReturn:
    """输出成功消息"""
    # 判断是否为命令行模式
    if console:
        print(config.SUCCESS_MSG)
        return

    # GUI 模式
    msgbox.showinfo(
        title=config.SUCCESS_TITLE,
        message=config.SUCCESS_MSG
    )


def failed(console: bool) -> NoReturn:
    """输出失败消息"""
    # 判断是否为命令行模式
    if console:
        print(config.FAILED_MSG)
        return

    # GUI 模式
    msgbox.showerror(
        title=config.FAILED_TITLE,
        message=config.FAILED_MSG
    )


def need(console: bool) -> NoReturn:
    """输出重选文件消息"""
    # 判断是否为命令行模式
    if console:
        print(config.INFO_MSG)
        return

    # GUI 模式
    msgbox.showinfo(
        title=config.INFO_TITLE,
        message=config.INFO_MSG
    )


def init(function: Callable) -> NoReturn:
    """界面初始化函数"""
    # 选择文件函数包装
    def run():
        return function(_PATH.get())

    # 顶部菜单栏
    _menubar = Menu(ROOT)
    _menubar.add_command(label="选择文件夹", command=_select)
    _menubar.add_command(label="帮助", command=_load_help)
    _menubar.add_command(label="退出", command=_exit)

    # 路径标签
    _label = Label(ROOT, text="选择路径 : ")
    _label.grid(row=0, column=0)

    # 路径输入框
    _choose_entry = Entry(ROOT, textvariable=_PATH)
    _choose_entry.grid(row=0, column=1)

    # 选择与执行按钮
    _run_btn = Button(ROOT, text="开始运行", command=run)
    _run_btn.grid(row=0, column=2)

    # 配置界面
    ROOT.resizable(_RESIZEABLE_X, _RESIZEABLE_Y)
    ROOT.config(menu=_menubar)
    ROOT.title(config.TITLE)
