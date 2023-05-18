# encoding:utf8
import backtrader as bt
from .algos import *
from loguru import logger
from .strategy_base import StratgeyAlgoBase


class StratgeyBuyHold(StratgeyAlgoBase):
    def __init__(self, weights=None):
        self.algos = [
            RunOnce(),
            SelectAll(),
        ]

