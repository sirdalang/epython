# -*- coding: utf-8 -*-

# 公共类型定义

import time

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

DB_PATH = 'ondev.db'

class ClientInfo: # 客户信息结构
    def __init__(self):
        self.mac = ''
        self.ip = ''
        self.name = ''
        self.time = ''
        self.down = ''
        self.up = ''
        self.online = True
        
    def __str__(self):
        d = {}
        d['mac'] = self.mac
        d['ip'] = self.ip
        d['name'] = self.name
        d['time'] = self.time
        d['down'] = self.down
        d['up'] = self.up
        d['online'] = self.online
        return str(d)

    def same(self, other):
        if (self.mac == other.mac and
            self.ip == other.ip and
            self.name == other.name and
            self.down == other.down and
            self.up == other.up and
            self.online == other.online):
            return True
        else:
            return False