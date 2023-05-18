# encoding:utf8

from pathlib import Path
import sys
TOP_DIR = Path(__file__).parent.parent.joinpath("../engine")
sys.path.append(TOP_DIR)

import backtrader as bt
from .algos import *
from loguru import logger
from .strategy_base import StrategyBase

class StratgeyAlgo(StrategyBase):
    def __init__(self, algos, algos_init=None):
        self.inds = {}
        if algos_init:
            for algo in algos_init:
                algo(self)

        self.algos = algos

    def next(self):
        context = {
            'strategy': self
        }
        run_algos(context, self.algos)
