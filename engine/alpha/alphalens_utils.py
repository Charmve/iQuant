'''
Author: Charmve yidazhang1@gmail.com
Date: 2023-05-18 22:00:33
LastEditors: Charmve yidazhang1@gmail.com
LastEditTime: 2023-05-18 22:33:59
FilePath: /Qbot/iQuant/engine/alpha/alphalens_utils.py
Version: 1.0.1
Blogs: charmve.blog.csdn.net
GitHub: https://github.com/Charmve
Description: 

Copyright (c) 2023 by Charmve, All Rights Reserved. 
Licensed under the MIT License.
'''
# encoding:utf8
import pandas as pd
from alphalens.utils import get_clean_factor_and_forward_returns

from pathlib import Path
import sys
TOP_DIR = Path(__file__).parent.parent.joinpath("engine")
sys.path.append(TOP_DIR)

# 将tears.py中的get_values()函数改为to_numpy()

def make_alphalens_datas(df, alpha_col):
    # alphalens接受的数据必须是双索引，date,code
    alpha_df = df.set_index([df.index, 'code'])
    alpha_df.sort_index(level=0, inplace=True, ascending=True)
    # 使用pivot_table把因子值，按symbol提出来
    close_df = df.pivot_table(index='date', columns='code', values='close', dropna=True)
    return alpha_df[alpha_col], close_df


if __name__ == '__main__':
    from datafeed.dataloader import Dataloader

    df = Dataloader().load_one_df(['000300.SH', '399006.SZ', 'SPX'],
                                  names=['close', 'mom_20', 'rate'], fields=['$close',
                                                                             '$close/Ref($close,20)-1',
                                                                             '$close/Ref($close,1)-1'
                                                                             ])
    alpha_df, close_df = make_alphalens_datas(df, 'mom_20')
    print(alpha_df, close_df)

    from alphalens.utils import get_clean_factor_and_forward_returns

    # 将tears.py中的get_values()函数改为to_numpy()
    ret = get_clean_factor_and_forward_returns(alpha_df, close_df)
    print(ret)

    from alphalens.tears import create_returns_tear_sheet

    create_returns_tear_sheet(ret, long_short=False)
