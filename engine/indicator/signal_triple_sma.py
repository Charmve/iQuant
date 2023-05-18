import backtrader as bt


# �Զ����ź�ָ��
class SignalTripleSMA(bt.Indicator):
    lines = ('signal',)  # ���� signal �ߣ������źŷ��� signal line ��
    params = dict(
        short_period=5,
        median_period=20,
        long_period=60)

    def __init__(self):
        self.s_ma = bt.ind.SMA(period=self.p.short_period)
        self.m_ma = bt.ind.SMA(period=self.p.median_period)
        self.l_ma = bt.ind.SMA(period=self.p.long_period)

        # ���ھ��������ھ����Ϸ��������ھ���Ҳ�ڳ��ھ����Ϸ������߶�ͷ���У�ȡֵΪ1����֮��ȡֵΪ0
        self.signal1 = bt.And(self.m_ma > self.l_ma, self.s_ma > self.m_ma)
        # ������ self.signal1 �Ļ��������������жϵõ���һ��ͬʱ��������������ʱ�䣬��һ����������Ϊ1����������Ϊ0
        self.buy_signal = bt.If((self.signal1 - self.signal1(-1)) > 0, 1, 0)
        # ���ھ����´����ھ���ʱ��ȡֵΪ1����֮ȡֵΪ0
        self.sell_signal = bt.ind.CrossDown(self.s_ma, self.m_ma)
        # �������źźϲ���һ���ź�
        self.lines.signal = bt.Sum(self.buy_signal, self.sell_signal * (-1))
