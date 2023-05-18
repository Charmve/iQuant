'''
Author: Charmve yidazhang1@gmail.com
Date: 2023-05-18 22:00:28
LastEditors: Charmve yidazhang1@gmail.com
LastEditTime: 2023-05-18 22:12:21
FilePath: /Qbot/iQuant/engine/datafeed/expr/expr_mgr.py
Version: 1.0.1
Blogs: charmve.blog.csdn.net
GitHub: https://github.com/Charmve
Description: 

Copyright (c) 2023 by Charmve, All Rights Reserved. 
Licensed under the MIT License.
'''
from pathlib import Path
import sys
TOP_DIR = Path(__file__).parent.parent.parent.joinpath(".")
sys.path.append(TOP_DIR)

import re
from .ops import Operators, register_all_ops
from .base import Feature
from common import Singleton


@Singleton
class ExprMgr:
    def __init__(self):
        register_all_ops()

    def parse_field(self, field):
        # Following patterns will be matched:
        # - $close -> Feature("close")
        # - $close5 -> Feature("close5")
        # - $open+$close -> Feature("open")+Feature("close")
        if not isinstance(field, str):
            field = str(field)

        re_func = re.sub(r"(\w+\s*)\(", r"Operators.\1(", field)
        # print('re_runc',re_func)
        return re.sub(r"\$(\w+)", r'Feature("\1")', re_func)

    def get_expression(self, feature):
        feature = self.parse_field(feature)
        try:
            expr = eval(feature)
        except:
            print('error', feature)
            raise
        return expr
