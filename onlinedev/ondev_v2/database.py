# -*- coding: utf-8 -*-

# 数据库相关

import sqlite3
import logging

from public import ClientInfo
from public import DB_PATH

class db:
    def __init__(self):
        logging.debug ("db enter")
        self.db = sqlite3.connect(DB_PATH)
        self.db.execute('CREATE TABLE IF NOT EXISTS table_mac('
                'MAC CHAR(20) PRIMARY KEY NOT NULL'
            ')')
        self.db.commit()

    def gettablename(mac):
        name = 'table_' + mac
        return name

    def create_table(self, mac): # 创建mac表
        name = db.gettablename(mac)
        sql = ('CREATE TABLE IF NOT EXISTS ?('
                'ID INT PRIMARY KEY NOT NULL,'
                'IP CHAR(20),'
                'NAME CHAR(20),'
                'TIME CHAR(20),'
                'DOWN CHAR(8),'
                'UP CHAR(8),'
            ')')
        self.db.execute(sql, (name))
    
    def insert_data(self, mac, clientinfo):
        name = gettablename(mac)
        sql = ('INSERT INTO ?(IP,NAME,TIME,DOWN,UP) '
            'VALUES(?,?,?,?,?)')
        self.db.execute(sql, (name,clientinfo.ip,clientinfo.name,
            clientinfo.time,clientinfo.down,clientinfo.up))
        

    def log(self, clientinfo):
        mac = clientinfo.mac

        cursor = self.db.execute('SELECT MAC FROM table_mac')
        if mac not in cursor: # 新的mac
            self.create_table(mac)
        
        self.insert_data (mac, clientinfo)
