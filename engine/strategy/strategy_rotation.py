'''
Author: Charmve yidazhang1@gmail.com
Date: 2023-05-18 22:00:31
LastEditors: Charmve yidazhang1@gmail.com
LastEditTime: 2023-05-18 22:18:05
FilePath: /Qbot/iQuant/engine/strategy/strategy_rotation.py
Version: 1.0.1
Blogs: charmve.blog.csdn.net
GitHub: https://github.com/Charmve
Description: 

Copyright (c) 2023 by Charmve, All Rights Reserved. 
Licensed under the MIT License.
'''
# encoding:utf8

from pathlib import Path
import sys
TOP_DIR = Path(__file__).parent.parent.joinpath("../engine")
sys.path.append(TOP_DIR)

import backtrader as bt
from loguru import logger
from indicator.indicator_rsrs import RSRS


class StrategyRotation(bt.Strategy):
    params = dict(
        period=20,  # 动量周期

    )

    def __init__(self):
        # 指标计算
        self.inds = {}
        self.rsrs = RSRS(self.datas[0])
        for data in self.datas:
            self.inds[data] = bt.ind.ROC(data, period=self.p.period)

    def next(self):
        # 计算to_buy,判断roc>0.02
        # 计算to_sell,判断roc<0
        # 判断当前已经持仓
        to_buy = []
        to_sell = []
        holding = []
        for data, roc in self.inds.items():
            #if roc[0] > 0.02:
            if self.rsrs[0] > 1:
                to_buy.append(data)

            #if roc[0] < 0:

            if self.rsrs[0] < 0.8:
                to_sell.append(data)

            if self.getposition(data).size > 0:
                holding.append(data)

        for sell in to_sell:
            if self.getposition(sell).size > 0:
                logger.debug('清仓'+sell.p.name)
                self.close(sell)

        new_hold = list(set(to_buy + holding))
        for data in to_sell:
            if data in new_hold:
                new_hold.remove(data)



        if len(new_hold) == 0:
            #logger.info('新仓位为空')
            return

        # 等权重分配 todo: 已持仓的应应该不变，对cash对新增的等权分配
        weight = 1 / len(new_hold)
        for data in new_hold:
            self.order_target_percent(data, weight)





