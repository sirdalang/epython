# -*- coding: utf-8 -*-

# 数据处理

import logging

class ClientInfo:
    def __init__(self):
        self.mac=""
        self.name=""
        self.time=""
        self.down=""
        self.up=""
        
    def __str__(self):
        d = {}
        d['mac'] = self.mac
        d['name'] = self.name
        d['time'] = self.time
        d['down'] = self.down
        d['up'] = self.up
        return str(d)

class DataHandler:
    def log(self, ci):
        logging.debug (ci)