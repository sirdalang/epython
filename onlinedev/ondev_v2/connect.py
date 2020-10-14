# -*- coding: utf-8 -*-

# filename: connect.py
# 实现有关网络连接的功能，向外部提供连接数据

# base mod
import requests
import json
import base64
import logging
import time
from urllib import parse

# other mod
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

# local
from routerref import getsafecode
from routerref import getlogindata
from routerref import getloginid
from routerref import getupdatingclientinfourl
from routerref import getupdatingclientinfodata
from routerref import parseclientinfodata
from public import ClientInfo

str_password = '123456'
str_protocol = 'http://'
str_hostname = '10.0.0.1'

header_template = {
    'Host': '10.0.0.1', # need update
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '0', # need update. eg. '236'
    'Origin': 'http://10.0.0.1', # need update
    'Connection': 'keep-alive',
    'Referer': 'http://10.0.0.1/', # need update
}

def getrsapublickey(session): # 获取rsa公钥
    url_key = str_protocol + str_hostname + '/pc/Content.htm'
    response = session.get(url_key)
    json_key_response = json.loads (response.text)

    public_key = json_key_response['data']['key']

    formated_key = "-----BEGIN PUBLIC KEY-----\n" + public_key + "\n-----END PUBLIC KEY-----"

    return formated_key

def rsaencrypt(code, public_key_formated): # rsa加密，并转换成字符串
    rsakey = RSA.importKey(public_key_formated)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    ciphertext = base64.b64encode(cipher.encrypt(code.encode('utf-8'))).decode()
    ciphertext = parse.quote_plus(ciphertext)
    return ciphertext

def getheadertemplate(header, hostname, conentlen): # 构造一个http头
    header = header_template.copy()
    header['Host'] = hostname # 'http://ip
    header['Origin'] = hostname
    header['Referer'] = hostname
    header['Content-Length'] = conentlen
    return header

def sendpassword(session, password_ciphertext): # 发送密码，请求验证，返回身份ID

    logindata = getlogindata(password_ciphertext)

    header = {}
    header = getheadertemplate(header, str_protocol + str_hostname, str(len(logindata)))
    logging.debug (header)

    response_givepwd = session.post (str_protocol + str_hostname, data=logindata, headers=header) # post
    logging.debug('response_givepwd=' + response_givepwd.text)
    loginid = getloginid(response_givepwd.text)
    return loginid

def updating(datahandler, session, id): # 
    updatedata = getupdatingclientinfodata()
    url_update = getupdatingclientinfourl(str_protocol, str_hostname, id)
    header = {}
    header = getheadertemplate(header, str_protocol + str_hostname, str(len(updatedata)))

    while True:

        response_gethost = session.post (url_update, data=updatedata, headers=header) # post
        # logging.debug (response_gethost.text)

        list_clientinfo = []

        clientinfo = parseclientinfodata(list_clientinfo, response_gethost.text)
        datahandler.log(list_clientinfo)

        time.sleep(5)


def connect(datahandler):
    
    session = requests.Session()

    public_key = getrsapublickey(session) 
    logging.debug ('public_key=' + public_key)

    password_safecode = getsafecode(str_password) # 自编码
    logging.debug ('safe_encode=' + password_safecode)

    password_ciphertext = rsaencrypt (password_safecode, public_key) # 利用rsa加密
    logging.debug ('ciphertext=' + password_ciphertext)

    strID = sendpassword(session, password_ciphertext)

    updating (datahandler, session, strID)