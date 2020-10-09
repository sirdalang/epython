# onlinedev_v2.py
# 利用python进行动态网页解析，在TPLINK TL-WDR6320 1.0.14 上进行分析和反向，流程通过
# 关键步骤有：
# 1.网页加载流程
# 2.网页身份认证方式
# 3.RAS加密，公钥与私钥，BASE64，URL编码
#
# 需要安装 crypto
# v1.0.0 20201010

import os
import time
import datetime
import requests
import json
import base64
import rsa
from urllib import parse
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

#securityEncode: function (a, b, d) {
#    var c = "", e, g, h, m, p = 187, q = 187; 
#    g = a.length; h = b.length; 
#    m = d.length; e = g > h ? g : h; 
#    for (var k = 0; k < e; k++)
#       q = p = 187, k >= g ? q = b.charCodeAt(k) : k >= h ? p = a.charCodeAt(k) : (p = a.charCodeAt(k), q = b.charCodeAt(k)), c += d.charAt((p ^ q) % m); 
#     return c
#}

# when key is 
# "
# MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoVBwJv2pBtrr9ZY9C4lgqNo5+dFI+3A6W80h+8CzpCxsgl8Dic7JYmcTfOrtYtYJ6Vma3ZWx+NK1bJk8DFipOnDewVVJ6wmucnryF3OlfcIjLZsYjh4Sq2mdZfg0lOThTvh8z4V2jO6fWh91iwOOeCokGoMw9V+QyQevtCr5pSQIDAQAB
# "
#



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

        print (p,q,m)

        if isinstance(p, str):
            p = ord(p)
        if (isinstance(q, str)):
            q = ord(q)
        if (isinstance(m, str)):
            m = ord(m)

        print (p,q,m)

        c = c + d[ (p ^ q) % m ]

    return c


string_a = "RDpbLfCPsJZ7fiv"
string_b = "123456"
string_c = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW"

result = securityEncode (string_a, string_b, string_c)

print ("result=" + result)

# 获取rsa公钥，这个公钥并不会一直变化
url_host = 'http://10.0.0.1'
url_key = url_host + '/pc/Content.htm'
session = requests.Session()
response = session.get(url_key)
json_key_response = json.loads (response.text)

public_key = json_key_response['data']['key']
print (public_key)

#public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoVBwJv2pBtrr9ZY9C4lgqNo5+dFI+3A6W80h+8CzpCxsgl8Dic7JYmcTfOrtYtYJ6Vma3ZWx+NK1bJk8DFipOnDewVVJ6wmucnryF3OlfcIjLZsYjh4Sq2mdZfg0lOThTvh8z4V2jO6fWh91iwOOeCokGoMw9V+QyQevtCr5pSQIDAQAB"

public_key_formated = "-----BEGIN PUBLIC KEY-----\n" + public_key + "\n-----END PUBLIC KEY-----"

print (public_key_formated)

# 注意，rsa算法在加密的过程中会“加盐”，因此每次加密得到的结果都不一样
rsakey = RSA.importKey(public_key_formated)
cipher = Cipher_pkcs1_v1_5.new(rsakey)
ciphertext = base64.b64encode(cipher.encrypt(result.encode('utf-8'))).decode()
print ("ciphertext=" + ciphertext)
ciphertext = parse.quote_plus(ciphertext)
print ("ciphertext=" + ciphertext)

#temp_un = "hefx+Vkvn9YkFqr6NkXX02Gej/ZSrP3lCg1wlhpqBvJrpe9jSbdfROGzMaFW6uofU3lDmF8NDkqJmLwFuoqUUDSy/RqrOLM6u2fi1ymWQ6rjpdmq8hCcqwEHQy0LdHibrGxS5WXiXeAl8vVZnntYXxfGDpIrgJ+M2g3PDovfdUc="
#temp_en = "hefx%2BVkvn9YkFqr6NkXX02Gej%2FZSrP3lCg1wlhpqBvJrpe9jSbdfROGzMaFW6uofU3lDmF8NDkqJmLwFuoqUUDSy%2FRqrOLM6u2fi1ymWQ6rjpdmq8hCcqwEHQy0LdHibrGxS5WXiXeAl8vVZnntYXxfGDpIrgJ%2BM2g3PDovfdUc%3D";
#ciphertext = "hefx%2BVkvn9YkFqr6NkXX02Gej%2FZSrP3lCg1wlhpqBvJrpe9jSbdfROGzMaFW6uofU3lDmF8NDkqJmLwFuoqUUDSy%2FRqrOLM6u2fi1ymWQ6rjpdmq8hCcqwEHQy0LdHibrGxS5WXiXeAl8vVZnntYXxfGDpIrgJ%2BM2g3PDovfdUc%3D"

#     my = "T0lxzU0nRe5xRELkIG0SWb1SrIRlvvNy/8XWQCto2CqQ2znTJrnaG6ALMGqnUukeYo4iiKwpO3mP5wLcPIIf1JSUjMkLK/jByF5NvPcVSgGwbBZ/jUS/aXDHAtkdsQtb2aDz4Q+nEibQ6CgxVocR67rlo78oC1MZmV5wvz/hxxk="

#print (temp_un)
#print (parse.quote_plus(temp_un))
#print (temp_en)
#exit ()

print (ciphertext)

# 发送密码，并获得登陆ID

header_pwd = {
    'Host': '10.0.0.1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '0', # need update. eg. '236'
    'Origin': 'http://10.0.0.1',
    'Connection': 'keep-alive',
    'Referer': 'http://10.0.0.1/',
}

print (ciphertext)

dict_post_pwd = {}
dict_post_pwd['method'] = 'do'
dict_post_pwd['login'] = {}
dict_post_pwd['login']['password'] = ciphertext
dict_post_pwd['login']['encrypt_type'] = 1

json_post_pwd = json.dumps (dict_post_pwd)

data_post_pwd = json_post_pwd.encode()

print (data_post_pwd)

header_pwd['Content-Length'] = str(len(data_post_pwd))

print (header_pwd)

response_givepwd = session.post (url_host, data=data_post_pwd, headers=header_pwd) # post

print ("send")

print (response_givepwd.text)

json_login_info = json.loads (response_givepwd.text)
text_loginid = json_login_info['stok']

print (text_loginid)

url_getonlinedev = url_host + '/stok=' + text_loginid + '/ds'
dict_get_hosts_info = {}
dict_get_hosts_info['hosts_info'] = {}
dict_get_hosts_info['hosts_info']['table'] = 'online_host'
dict_get_hosts_info['network'] = {}
dict_get_hosts_info['network']['name'] = 'iface_mac'
dict_get_hosts_info['method'] = 'get'

print (dict_get_hosts_info)

text_get_hosts_info = json.dumps (dict_get_hosts_info)
data_get_hosts_info = text_get_hosts_info.encode()

print (data_get_hosts_info)

header_gethost = header_pwd # re-ref
header_gethost['Content-Length'] = str(len(data_get_hosts_info))

response_gethost = session.post (url_getonlinedev, data=data_get_hosts_info, headers=header_gethost) # post

print ("send")

print (response_gethost.text)
