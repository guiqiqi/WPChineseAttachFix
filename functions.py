"""函数库文件"""

import os

# 第三方库 - pypinyin : 将中文转拼音
try:
	from pypinyin import lazy_pinyin as lazy
except ImportError as error:
	os._exit(1)

# 常量定义
_H_LOW = u'\u4e00'
_H_UPP = u'\u9fff'
_REPLACE = \
"""
update wp_posts set post_content=replace(post_content,'{old}','{new}');
update wp_posts set guid=replace(guid,'{old}','{new}');
update wp_postmeta set meta_value=replace(meta_value,'{old}','{new}');
""".strip()

# 将字符串转换成拼音
pinyin = lambda string : ''.join(lazy(string))
# 判断是否为目录
isdir = lambda source : os.path.isdir(source)

def sql(correspond):
	commands = list()
	for old, new in correspond.items():
		command = _REPLACE.format(new = new, old = old)
		commands.append(command)
	return "\n\n".join(commands)

def files(location):
	"""获取某一文件夹下的所有文件
	location : 文件夹地址
	files(location) : list
	"""
	location = location.strip("\\")
	flist = os.listdir(location)
	for name in flist[:]:
		full = location + "/" + name
		if isdir(full) : flist.remove(name)
	return flist

def notepad(file):
	"""通过记事本打开某一文件
	files : 文件地址
	notepad(files) : None
	"""
	program = "notepad " if os.name == "nt" else "vi"
	os.popen(program + file, "r")

def hchinese(string):
	"""检查字符串中是否含有中文
	string : 传入带检测的字符串
	hchinese(string) : boolean
	"""
	for char in string:
		if _H_LOW <= char <= _H_UPP:
			return True
	return False

def rename(source, correspond):
	"""根据传入的文件夹以及
	新旧文件名对应关系批量更改文件名
	source : 要更改的文件夹路径
	correspond : 新旧文件名对应关系
	rename(source, coorespond) : None
	"""
	current = os.getcwd()
	os.chdir(source)
	for old, new in correspond.items():
		os.rename(old, new)
	os.chdir(current)
