# -*- coding: utf-8 -*-

# 数据库相关

import sqlite3
import logging

from public import ClientInfo
from public import DB_PATH

class db:
    def __init__(self):
        logging.debug ("db enter")

        self.macbuffer = dict()

        self.db = sqlite3.connect(DB_PATH)
        self.db.execute('CREATE TABLE IF NOT EXISTS table_mac('
                'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                'MAC CHAR(20) UNIQUE NOT NULL,'
                'TABLENAME CHAR(20) NOT NULL,'
                'NAME CHAR(20) NOT NULL'
            ')')
        
        sql = 'SELECT mac,tablename,name from table_mac'
        cursor = self.db.execute(sql)
        logging.debug (cursor)
        for k in cursor:
            logging.debug (k)
            self.macbuffer[k[0]] = {'tablename':k[1],'name':k[2]}
        
        logging.debug(self.macbuffer)

        self.db.commit()

    def gettablename(self, mac): # 获取mac对应的表名
        name = 't_' + mac.replace('-','_')
        return name

    def logmac(self, mac,name): # 记录mac
        tablename = self.gettablename(mac)

        if mac not in self.macbuffer:
            sql = ('INSERT INTO table_mac (TABLENAME, MAC, NAME) '
                'values(?,?,?)')
            self.db.execute(sql, [tablename,mac,name])
            self.macbuffer[mac] = {'tablename':tablename,'name':name}
        else:
            if self.macbuffer[mac]['name'] != name:
                sql = 'UPDATE table_mac SET name = ? WHERE mac = ?'
                self.db.execute(sql, [name, mac])
                self.macbuffer[mac]['name'] = name
    

    def create_table_dev(self, mac): # 创建dev表
        tablename = self.gettablename(mac)
        sql = ('CREATE TABLE IF NOT EXISTS {0} ('
                'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                'IP CHAR(20),'
                'NAME CHAR(20),'
                'TIME CHAR(20),'
                'DOWN CHAR(8),'
                'UP CHAR(8),'
                'ONLINE INTEGER'
            ')').format(tablename)
        self.db.execute(sql)
    
    def insert_data(self, mac, clientinfo):
        tablename = self.gettablename(mac)
        sql = ('INSERT INTO %s(IP,NAME,TIME,DOWN,UP,ONLINE) '
            'VALUES(?,?,?,?,?,?)') % (tablename)
        self.db.execute(sql, [clientinfo.ip,clientinfo.name,
            clientinfo.time,clientinfo.down,clientinfo.up,clientinfo.online])

    def log(self, clientinfo):
        mac = clientinfo.mac

        self.logmac (clientinfo.mac,clientinfo.name)
        self.create_table_dev (mac)
        self.insert_data (mac, clientinfo)

        self.db.commit()
