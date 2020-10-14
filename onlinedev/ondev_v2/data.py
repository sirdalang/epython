# -*- coding: utf-8 -*-

# 数据处理

import logging
from public import ClientInfo


class DataHandler:
    def log(self, list_cli):
        for cli in list_cli:
            logging.debug (cli)