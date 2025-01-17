from nakuru.entities.components import *
from nakuru import (
    GroupMessage,
    FriendMessage
)
from botpy.message import Message, DirectMessage
import psutil
import os
import platform as sys_platform

class SysStatQCBotPlugin:
    """
    初始化函数, 可以选择直接pass
    """
    def __init__(self) -> None:
        pass

    def run(self, message: str, role: str, platform: str, message_obj, qq_platform):
        if message == "sys" or message == "系统状态":
            core_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
            sysmem_info = psutil.virtual_memory()
            cpu_info = psutil.cpu_times
            disk_info = psutil.disk_usage('/')
            cpu_ststs = psutil.cpu_stats()
            cpu_freq = psutil.cpu_freq()
            # system_version = sys_platform.platform()获取系统的完整版本信息，这里使用别名sys_platform
            system_version = "Ubuntu 22.04 LTS (GNU/Linux 5.15.0-84-generic x86_64)"
            res = f"""【服务器当前状态】
操作系统: {system_version}
进程内存占用: {core_mem:.2f}MB
总内存: {sysmem_info.total / 1024 / 1024:.2f}MB
已用内存: {sysmem_info.used / 1024 / 1024:.2f}MB
空闲内存: {sysmem_info.free / 1024 / 1024:.2f}MB
内存使用率: {sysmem_info.percent:.2f}%
用户态CPU时间: {cpu_info().user:.2f}秒
系统态CPU时间: {cpu_info().system:.2f}秒
空闲CPU时间: {cpu_info().idle:.2f}秒
CPU使用率: {psutil.cpu_percent(interval=1):.2f}%
CPU逻辑核心数: {psutil.cpu_count()}
CPU物理核心数: {psutil.cpu_count(logical=False)}
CPU上下文切换次数: {cpu_ststs.ctx_switches}
CPU中断次数: {cpu_ststs.interrupts}
CPU软中断次数: {cpu_ststs.soft_interrupts}
CPU异常次数: {cpu_ststs.syscalls}
CPU当前频率: {cpu_freq.current:.2f}MHz
CPU最大频率: {cpu_freq.max:.2f}MHz
CPU最小频率: {cpu_freq.min:.2f}MHz
总磁盘空间: {disk_info.total / 1024 / 1024 / 1024:.2f}GB
已用磁盘空间: {disk_info.used / 1024 / 1024 / 1024:.2f}GB
空闲磁盘空间: {disk_info.free / 1024 / 1024 / 1024:.2f}GB
磁盘使用率: {disk_info.percent:.2f}%
            """
            if platform == "gocq":
                """
                QQ平台指令处理逻辑
                """
                return True, tuple([True, [Plain(res)], "helloworld"])
            elif platform == "qqchan":
                """
                频道处理逻辑(频道暂时只支持回复字符串类型的信息，返回的信息都会被转成字符串，如果不想处理某一个平台的信息，直接返回False, None就行)
                """
                return True, tuple([True, res, "sysstatqcbot"])
        else:
            return False, None
             
    def info(self):
        return {
            "name": "SysStatQCBot",
            "desc": "查看机器状态的插件",
            "help": "回复sys即可查看机器状态",
            "version": "v1.0.0",
            "author": "Soulter"
        }


        # 热知识：检测消息开头指令，使用以下方法
        # if message.startswith("原神"):
        #     pass
