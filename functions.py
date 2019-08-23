"""函数库文件"""

import os
import sys

# 第三方库 - pypinyin : 将中文转拼音
try:
    from pypinyin import lazy_pinyin as lazy
except ImportError as error:
    sys.exit(1)

from typing import NoReturn, Dict, Tuple, Iterable, List

# 常量定义
_H_LOW = u'\u4e00'
_H_UPP = u'\u9fff'
_REPLACE = \
    """
update wp_posts set post_content=replace(post_content,'{old}','{new}');
update wp_posts set guid=replace(guid,'{old}','{new}');
update wp_postmeta set meta_value=replace(meta_value,'{old}','{new}');
""".strip()

def pinyin(string: str) -> str:
    """将字符串转换成拼音"""
    return ''.join(lazy(string))


def isdir(source: str) -> bool:
    """判断是否为目录"""
    return os.path.isdir(source)


def sql(correspond: Dict[str, str]) -> str:
    """生成 sql 命令"""

    # 遍历所有的文件夹对应关系 - 生成 sql 命令
    commands = list()
    for old, new in correspond.items():
        command = _REPLACE.format(new=new, old=old)
        commands.append(command)
    return "\n\n".join(commands)


def files(location: str) -> Iterable[Tuple[str, List[str]]]:
    """
    遍历某一文件夹下所有的文件
    返回生成器 - 文件夹路径&文件列表
    """
    for path, _, allfiles in os.walk(location):
        yield path, allfiles


def notepad(file: str) -> NoReturn:
    """
    尝试通过记事本打开某一文件
    files : 文件地址

    *函数会尝试判断系统类型:
        windows 系统使用 notepad 打开
        linux 系统使用 vi 打开
    """
    # 获取程序名
    program = "notepad " if os.name == "nt" else "vi"
    os.popen(program + file, "r")


def hchinese(string: str) -> bool:
    """
    检查字符串中是否含有中文:
        当含有中文时, 其文件名中至少含有一个位于
        _H_LOW - _H_UPP 的 unicode 字符
    """
    # 遍历文件名字符串
    for char in string:
        if _H_LOW <= char <= _H_UPP:
            return True
    return False


def rename(source: str, correspond: dict) -> NoReturn:
    """
    根据传入的文件夹以及
    新旧文件名对应关系批量更改文件名

    *source : 要更改的文件夹路径
    *correspond : 新旧文件名对应关系
    """
    # 切换到指定目录后进行更改名称操作
    current = os.getcwd()
    os.chdir(source)
    for old, new in correspond.items():
        os.rename(old, new)
    os.chdir(current)
