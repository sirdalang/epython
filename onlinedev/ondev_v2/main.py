# -*- coding: utf-8 -*-

import logging

from connect import connect 
from data import DataHandler
from database import db

logging.basicConfig(level=logging.DEBUG,format='%(filename)s:%(lineno)d %(levelname)s %(message)s')

database = db()
datahandler = DataHandler(database)

connect(datahandler)

