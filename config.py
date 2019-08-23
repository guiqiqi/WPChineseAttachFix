"""配置文件"""

HELP = "help.txt" # 帮助文件地址
SQL = "sql.txt" # sql 文件保存地址

TITLE = "WP中文图片名修复工具" # 程序标题

SUCCESS_TITLE = "操作成功" # 成功标题
SUCCESS_MSG = "文件名已更改, 请在数据库中执行 {file} 中的语句".format(file=SQL) # 成功提示语

FAILED_TITLE = "操作失败" # 失败标题
FAILED_MSG = "更改失败, 请查看程序是否有该文件夹读取权限" # 失败提示语

INFO_TITLE = "提示" # 提示标题
INFO_MSG = "请检查选择的文件夹是否正确" # 提示语
