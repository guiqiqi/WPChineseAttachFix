"""主要运行文件"""

import sys
from typing import NoReturn, Dict, List

import ui
import config
import functions

def run(father: str, console: bool = False) -> NoReturn:
    """
    主要运行函数:
        1. 首先判断运行的主文件夹是否存在
        2. 通过 os.walk 遍历所有的文件与文件夹对应:
            有中文则进行保存更改
        3. 尝试对文件进行重命名
        4. 生成 sql 命令列表

    *当传入的 console 为 True 时 - 在 console 内进行结果显示
    """
    # 当从UI抓到的地址不是目录时, 不运行
    if not functions.isdir(father):
        ui.need(console)
        return

    # 遍历文件夹获取对应
    iterator = functions.files(father)
    paths: Dict[str, Dict[str, str]] = dict()

    for path, files in iterator:
        # 当在 paths 中不存在记录时 - 新建
        if not path in paths:
            paths[path] = dict()

        # 判断文件名是否含有中文
        for file in files:
            if functions.hchinese(file):
                renamed = functions.pinyin(file)
                paths[path][file] = renamed

    # 尝试重命名
    try:
        for path, corresponds in paths.items():
            functions.rename(path, corresponds)
    except PermissionError as _error:
        ui.failed(console)

    # 生成 sql 命令
    commands: List[str] = list()
    for _, corresponds in paths.items():
        command = functions.sql(corresponds)
        commands.append(command)

    # 保存 sql 命令
    with open(config.SQL, 'w') as handler:
        handler.write('\n'.join(commands))

    # 生成成功提示
    ui.success(console)
    functions.notepad(config.SQL)


# 判断是否为主运行文件
if __name__ == "__main__":
    if len(sys.argv) == 1:
        ui.init(run)
        ui.ROOT.mainloop()
    else:
        _PATH = sys.argv[1]
        run(_PATH, True)
