# -*- coding: utf-8 -*-

import logging

from connect import connect 
from data import DataHandler

logging.basicConfig(level=logging.DEBUG,format='%(filename)s:%(lineno)d %(levelname)s %(message)s')

datahandler = DataHandler()

connect(datahandler)