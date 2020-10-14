# -*- coding: utf-8 -*-

# 数据处理

import logging
import time
from public import ClientInfo
from public import TIME_FORMAT

MAX_SIZE = 1

def timeover60(start, end): # 判断时间是否超时
    time_start = time.strptime(start, TIME_FORMAT)
    time_end = time.strptime(end, TIME_FORMAT)
    if abs(time_start - time_end) > 60:
        return True
    else:
        return False

def checkinfo (list_cli, listbuf): # 执行缓存检查，进行过滤更新（有限更新）
    # 逐设备处理
    for cli in list_cli:
        if len(listbuf) < MAX_SIZE:
            listbuf.append({cli.mac, cli})
        else:
            # 上线处理
            if cli.mac not in listbuf[-1]: # 新上线
                listbuf[-1][cli.mac] = cli
            else: # 已有设备
                if cli.same(listbuf[-1][cli.mac]): # 信息未变化
                    listbuf[-1][cli.mac].time = cli.time # 仅更新时间
                else:
                    listbuf[-1][cli.mac] = cli # 全部更新
    
    localtime = time.localtime()
    str_localtime = time.strftime(TIME_FORMAT,localtime)

    list_cli_mac = []
    for k in list_cli:
        list_cli_mac.append(k.mac)

    # 整体处理
    # 下线处理
    if len(listbuf) > 0:
        removedev = [] # 记录需要删除的mac地址
        for devmac in listbuf[-1]:
            if devmac not in list_cli_mac: # 下线
                if (timeover60(listbuf[-1][devmac].time, str_localtime)): # 已足够长时间
                    #listbuf[-1].pop(dev.mac)
                    removedev.append(devmac)
                else:
                    pass
                

class DataHandler:
    def __init__(self):
        self.clibuf = [{}] # 参考队列，队列以时间前后为分隔
    def log(self, list_cli):
        for cli in list_cli:
           logging.debug (cli)
        
        checkinfo (list_cli, self.clibuf)