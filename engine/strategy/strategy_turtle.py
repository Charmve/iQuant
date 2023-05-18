from pathlib import Path
import sys
TOP_DIR = Path(__file__).parent.parent.joinpath("../engine")
sys.path.append(TOP_DIR)

import backtrader as bt
from engine.strategy.strategy_base import StrategyBase


class TurtleTradingStrategy(StrategyBase):
    params = dict(
        N1=20,  # ���氲ͨ���Ϲ��t
        N2=10,  # ���氲ͨ���¹��t
    )

    def __init__(self):
        self.order = None
        self.buy_count = 0  # ��¼�������
        self.last_price = 0  # ��¼����۸�
        # ׼����һ����Ļ���300������Լ��close��high��low ��������
        self.close = self.datas[0].close
        self.high = self.datas[0].high
        self.low = self.datas[0].low
        # �������氲ͨ���Ϲ죺��ȥ20�յ���߼�
        self.DonchianH = bt.ind.Highest(self.high(-1), period=self.p.N1, subplot=True)
        # �������氲ͨ���¹죺��ȥ10�յ���ͼ�
        self.DonchianL = bt.ind.Lowest(self.low(-1), period=self.p.N2, subplot=True)
        # �������氲ͨ���Ϲ�ͻ�ƣ�close>DonchianH��ȡֵΪ1.0����֮Ϊ -1.0
        self.CrossoverH = bt.ind.CrossOver(self.close(0), self.DonchianH, subplot=False)
        # �������氲ͨ���¹�ͻ��:
        self.CrossoverL = bt.ind.CrossOver(self.close(0), self.DonchianL, subplot=False)
        # ���� ATR
        self.TR = bt.ind.Max((self.high(0) - self.low(0)),  # ������߼�-������ͼ�
                             abs(self.high(0) - self.close(-1)),  # abs(������߼�?ǰһ�����̼�)
                             abs(self.low(0) - self.close(-1)))  # abs(������ͼ�-ǰһ�����̼�)
        self.ATR = bt.ind.SimpleMovingAverage(self.TR, period=self.p.N1, subplot=False)
        # ���� ATR��ֱ�ӵ��� talib ��ʹ��ǰ��Ҫ��װ python3 -m pip install TA-Lib
        # self.ATR = bt.talib.ATR(self.high, self.low, self.close, timeperiod=self.p.N1, subplot=True)

    def next(self):
        # ������ж�����ִ���У��Ͳ����µĲ�λ����
        if self.order:
            return

            # �����ǰ���ж൥
        if self.position.size > 0:
            # �൥�Ӳ�:�۸�����������۵�0.5��ATR�ҼӲִ������ڵ���3��
            if self.datas[0].close > self.last_price + 0.5 * self.ATR[0] and self.buy_count <= 4:
                print('if self.datas[0].close >self.last_price + 0.5*self.ATR[0] and self.buy_count <= 4:')
                print('self.buy_count', self.buy_count)
                # ���㽨�ֵ�λ��self.ATR*�ڻ���Լ����300*��֤�����0.1
                self.buy_unit = max((self.broker.getvalue() * 0.01) / self.ATR[0], 1)
                self.buy_unit = int(self.buy_unit)  # ���׵�λΪ��
                # self.sizer.p.stake = self.buy_unit
                self.order = self.buy(size=self.buy_unit)
                self.last_price = self.position.price  # ��ȡ����۸�
                self.buy_count = self.buy_count + 1
            # �൥ֹ�𣺵��۸����2��ATRʱֹ��ƽ��
            elif self.datas[0].close < (self.last_price - 2 * self.ATR[0]):
                print('elif self.datas[0].close < (self.last_price - 2*self.ATR[0]):')
                self.order = self.sell(size=abs(self.position.size))
                self.buy_count = 0
            # �൥ֹӯ�����۸�ͻ��10����͵�ʱֹӯ�볡 ƽ��
            elif self.CrossoverL < 0:
                print('self.CrossoverL < 0')
                self.order = self.sell(size=abs(self.position.size))
                self.buy_count = 0

                # �����ǰ���пյ�

        else:  # ���û�гֲ֣��ȴ��볡ʱ��
            # �볡: �۸�ͻ���Ϲ����ҿղ�ʱ������
            if self.CrossoverH > 0 and self.buy_count == 0:
                print('if self.CrossoverH > 0 and self.buy_count == 0:')
                # ���㽨�ֵ�λ��self.ATR*�ڻ���Լ����300*��֤�����0.1
                self.buy_unit = max((self.broker.getvalue() * 0.01) / self.ATR[0], 1)
                self.buy_unit = int(self.buy_unit)  # ���׵�λΪ��
                self.order = self.buy(size=self.buy_unit)
                self.last_price = self.position.price  # ��¼����۸�
                self.buy_count = 1  # ��¼���ν��׼۸�
            # �볡: �۸�����¹����ҿղ�ʱ
            elif self.CrossoverL < 0 and self.buy_count == 0:
                print('self.CrossoverL < 0 and self.buy_count == 0')

