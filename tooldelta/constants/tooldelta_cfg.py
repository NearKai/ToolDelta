LAUNCH_CFG: dict = {
    "启动器启动模式(请不要手动更改此项, 改为0可重置)": 0,
    "是否记录日志": True,
    "全局GitHub镜像": "",
    "插件市场源": "",
}
"默认登录配置"

LAUNCH_CFG_STD: dict = {
    "启动器启动模式(请不要手动更改此项, 改为0可重置)": int,
    "是否记录日志": bool,
    "全局GitHub镜像": str,
    "插件市场源": str,
}
"默认登录配置标准验证格式"

LAUNCHER_NEOMEGA_STD: dict = {
    "服务器号": int,
    "密码": str,
    "验证服务器地址(更换时记得更改fbtoken)": str,
}
LAUNCHER_NEOMEGA_DEFAULT: dict = {
    "服务器号": 0,
    "密码": "",
    "验证服务器地址(更换时记得更改fbtoken)": "",
}
LAUNCHER_NEOMG2TD_DEFAULT: dict = {
    "服务器号": 0,
    "密码": "",
    "验证服务器地址(更换时记得更改fbtoken)": "",
}
LAUNCHER_NEOMG2TD_STD: dict = {
    "服务器号": int,
    "密码": str,
    "验证服务器地址(更换时记得更改fbtoken)": str,
}


LAUNCHER_EULOGIST_DEFAULT: dict = {}
LAUNCHER_EULOGIST_STD: dict = {}

LAUNCHER_BEWS_STD: dict = {"服务端开放地址": str}
"启动器: BEWSServer 启动配置验证格式"

LAUNCHER_BEWS_DEFAULT: dict = {"服务端开放地址": ""}
"启动器: BEWSServer 默认启动配置"
