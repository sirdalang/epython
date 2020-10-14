# -*- coding: utf-8 -*-

# 公共类型定义

import time

class ClientInfo: # 客户信息结构
    def __init__(self):
        self.mac = ''
        self.ip = ''
        self.name = ''
        self.time = ''
        self.down = ''
        self.down = ''
        self.up = ''
        
    def __str__(self):
        d = {}
        d['mac'] = self.mac
        d['ip'] = self.ip
        d['name'] = self.name
        d['time'] = self.time
        d['down'] = self.down
        d['up'] = self.up
        return str(d)