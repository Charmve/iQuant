import backtrader as bt


# �Զ����ź�ָ��
class SignalDoubleSMA(bt.Indicator):
    lines = ('signal',)  # ���� signal �ߣ������źŷ��� signal line ��
    params = dict(
        short_period=5,
        long_period=20)

    def __init__(self):
        self.s_ma = bt.ind.SMA(period=self.p.short_period)
        self.l_ma = bt.ind.SMA(period=self.p.long_period)
        # ���ھ����ϴ����ھ��ߣ�ȡֵΪ1����֮�����ھ����´����ھ��ߣ�ȡֵΪ-1
        self.lines.signal = bt.ind.CrossOver(self.s_ma, self.l_ma)
