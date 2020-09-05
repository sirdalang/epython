import nmap
import time
import logging
from logging.handlers import RotatingFileHandler

# python的一个练习：
# 获取局域网内的在线设备，并记录为日志

class DevInfo:
    def __init(self):
        self.last_online_time = 0.0
        self.dev_ip = ''
        self.dev_mac = ''

logger = logging.getLogger('mylogger')
logger_simple = logging.getLogger('mylogger_simple')

def init_logger_simple():
    # logger_simple
    logger_simple.setLevel(level=logging.INFO)
    fmt = '%(asctime)s - %(message)s'
    format_str = logging.Formatter(fmt)
    handle = RotatingFileHandler('log_simple',maxBytes=100*1024, backupCount=2, encoding='utf-8')
    handle.setFormatter(format_str)

    handle.namer = lambda x: 'log_simple.' + x.split('.')[-1]
    logger_simple.addHandler(handle)


def init_logger():
    # logger
    logger.setLevel(level=logging.INFO)
    fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    format_str = logging.Formatter(fmt)
    handle = RotatingFileHandler('log',maxBytes=100*1024, backupCount=2, encoding='utf-8')
    handle.setFormatter(format_str)

    handle.namer = lambda x: 'log.' + x.split('.')[-1]
    logger.addHandler(handle)

def describe_devs(devdict):
    str = '\n'
    for key in devdict:
        str = str + ('%(key)s\n'%{'key':key})
    logger.info (str)

def scan(devdict):

    time_now = time.time()
    logger.debug ("scanning: %(time)s"%{'time':time.asctime(time.localtime(time_now))})

    nm = nmap.PortScanner()
    nm.scan('192.168.0.1/24', arguments='-sn')

    # 扫描并更新
    for host in nm.all_hosts():
        if host in devdict:
            logger.debug ('exist, update, %(ip)s'%{'ip':host})
            devdict[host].last_online_time = time_now
        else:
            logger.info ('new, insert, %(ip)s'%{'ip':host})
            logger_simple.info ('%(ip)s on'%{'ip':host})
            newitem = DevInfo()
            newitem.last_online_time = time_now
            newitem.dev_ip = host
            newitem.dev_mac = ''
            devdict[host] = newitem
            describe_devs (devdict)

    outdate = []

    # 清除过时项 (1 min)
    for key in devdict:
        #if time_now - devdict[key].last_online_time > 1 * 60:
        if key not in nm.all_hosts():
            outdate.append(key)
    
    for key in outdate:
        logger.info ('%(ip)s out of date, removed'%{'ip':key})
        logger_simple.info ('%(ip)s off'%{'ip':host})
        del devdict[key]
        describe_devs (devdict)


def onlinedev():
    logger.info('onlinedev start...')

    devdict = {}

    while True:
        scan(devdict)
        time.sleep(60)


if __name__ == '__main__':
    init_logger()
    init_logger_simple()
    onlinedev()