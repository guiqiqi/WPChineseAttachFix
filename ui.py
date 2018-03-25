"""界面与逻辑"""

from tkinter.filedialog import askdirectory
from tkinter import *
import tkinter.messagebox as msgbox
from tkinter.ttk import *

import functions

root = Tk()

# 定义常量
_HELP = '帮助.txt' # 帮助文件名
_SQL = "sql.txt" # sql语句文件名
_PATH = StringVar() # 路径动态存储
# 成功提示语
_SUCEESS = ["成功", "文件名已经更改, 请在数据库中执行%s中的语句" % _SQL]
# 失败提示语
_FAILED = ["失败", "更改失败, 请查看程序是否有该文件夹读取权限"]
# 需要选择文件夹
_NEED = ["提示", "请检查选择的文件夹是否正确"]
_resizableX = False # 在水平方向是否可以拉伸
_resizableY = False # 在垂直方向是否可以拉伸
_title = "WP中文图片名修复工具" # 界面标题

# 定义回调函数
_load_help = lambda : functions.notepad(_HELP)
_exit = lambda : root.destroy()
_select = lambda : _PATH.set(askdirectory())
success = lambda console : msgbox.showinfo(title = _SUCEESS[0],
	message = _SUCEESS[1]) if not console else print(_SUCEESS[1])
failed = lambda console : msgbox.showerror(title = _FAILED[0],
	message = _FAILED[1]) if not console else print(_FAILED[1])
need = lambda console : msgbox.showinfo(title = _NEED[0],
	message = _NEED[1]) if not console else print(_NEED[1])

def init(function):
	run = lambda : function(_PATH.get())
	# 顶部菜单栏
	_menubar = Menu(root)
	_menubar.add_command(label = "选择文件夹", command = _select)
	_menubar.add_command(label = "帮助", command = _load_help)
	_menubar.add_command(label = "退出", command = _exit)

	# 路径标签
	_label = Label(root, text = "选择路径 : ")
	_label.grid(row = 0, column = 0)

	# 路径输入框
	_choose_entry = Entry(root, textvariable = _PATH)
	_choose_entry.grid(row = 0, column = 1)

	# 选择与执行按钮
	_run_btn = Button(root, text = "开始运行", command = run)
	_run_btn.grid(row = 0, column = 2)

	# 配置界面
	root.resizable(_resizableX, _resizableY)
	root.config(menu = _menubar)
	root.title(_title)
