"""主要运行函数"""

import sys

import ui
import functions

def run(path, console = False):
	# 当从UI抓到的地址不是目录时, 不运行
	if not functions.isdir(path):
		ui.need(console)
		return False
	files = functions.files(path)
	correspond = dict()
	for file in files:
		if functions.hchinese(file):
			new = functions.pinyin(file)
			correspond[file] = new
	try:
		functions.rename(path, correspond)
	except PermissionError as error:
		ui.failed(console)
	command = functions.sql(correspond)
	fopen = open(ui._SQL, 'w')
	fopen.write(command)
	fopen.close()
	ui.success(console)
	functions.notepad(ui._SQL)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		ui.init(run)
		ui.root.mainloop()
	else:
		path = sys.argv[1]
		run(path, True)