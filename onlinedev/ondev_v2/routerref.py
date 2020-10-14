# -*- coding: utf-8 -*-

# 定义路由器页面解析相关特殊功能

import json
import logging
import time
from urllib import parse

from public import ClientInfo
from public import TIME_FORMAT

string_a = "RDpbLfCPsJZ7fiv"
string_d = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW"

def securityEncode(a, b, d):
    p = 187; q = 187
    g = len(a); h = len(b); m = len(d)
    e = max(g, h)
    c = ""
    for k in range(e):
        q=p=187
        if k >= g:
            q = b[k]
        else:
            if k >= h:
                p = a[k]
            else:
                p = a[k]
                q = b[k]

        #print (p,q,m)

        if isinstance(p, str):
            p = ord(p)
        if (isinstance(q, str)):
            q = ord(q)
        if (isinstance(m, str)):
            m = ord(m)

        #print (p,q,m)

        c = c + d[ (p ^ q) % m ]

    return c

def getsafecode(password):
    return securityEncode(string_a, password, string_d)

def getlogindata(password_ciphertext): # 构造发送密码请求的数据（二进制）
    # 构造json数据
    dict_post_pwd = {}
    dict_post_pwd['method'] = 'do'
    dict_post_pwd['login'] = {}
    dict_post_pwd['login']['password'] = password_ciphertext
    dict_post_pwd['login']['encrypt_type'] = 1

    json_post_pwd = json.dumps (dict_post_pwd)
    data_post_pwd = json_post_pwd.encode()

    return data_post_pwd

def getloginid(passwordresponse): # 解析发送密码的返回数据中的身份ID
    json_login_info = json.loads (passwordresponse)
    text_loginid = json_login_info['stok']
    return text_loginid

def getupdatingclientinfourl(protocol, host, id): # 构造获取设备信息地址
    return protocol + host + '/stok=' + id + '/ds'

def getupdatingclientinfodata(): # 构造发送获取设备信息的数据（二进制）
    dict_get_hosts_info = {}
    dict_get_hosts_info['hosts_info'] = {}
    dict_get_hosts_info['hosts_info']['table'] = 'online_host'
    dict_get_hosts_info['network'] = {}
    dict_get_hosts_info['network']['name'] = 'iface_mac'
    dict_get_hosts_info['method'] = 'get'
    text_get_hosts_info = json.dumps (dict_get_hosts_info)
    data_get_hosts_info = text_get_hosts_info.encode()
    return data_get_hosts_info

def parseclientinfodata(list_clientinfo, text): # 解析客户段信息

    dict_text = json.loads (text)
    dict_devlist = dict_text['hosts_info']['online_host']

    # logging.debug (dict_devlist)

    localtime = time.localtime()
    str_localtime = time.strftime(TIME_FORMAT,localtime)

    for k in dict_devlist:
        # logging.debug (k)
        for t in k:
            # logging.debug (k[t])
            info = k[t]
            clientinfo = ClientInfo()
            clientinfo.time = str_localtime
            clientinfo.mac = info['mac']
            clientinfo.ip = info['ip']
            clientinfo.name = parse.unquote_plus(info['hostname'])
            clientinfo.down = info['down_speed']
            clientinfo.up = info['up_speed']
            list_clientinfo.append (clientinfo)
            break;

    # logging.debug (list_clientinfo)