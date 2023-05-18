import wx
from gui.widgets.widget_matplotlib import MatplotlibPanel
from gui.widgets.widget_web import WebPanel
from engine.config import DATA_DIR_BKT_RESULT
from bokeh.plotting import figure, output_file, show, save


# https://zhuanlan.zhihu.com/p/376248349
def OnBkt(event):
    wx.MessageBox('ok')


class PanelBacktest(wx.Panel):
    def __init__(self, parent):
        super(PanelBacktest, self).__init__(parent)

        # 回测按钮
        # self.btn_bkt = wx.Button(self, label="回测")
        # self.Bind(wx.EVT_BUTTON, OnBkt, self.btn_bkt)

        # 进度条

        self.layout()

    def layout(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hbox)

        hbox.Add(wx.StaticText(self,label='请选择基准:'))
        combo_benchmarks = wx.ComboBox(self, size=(180, 25))
        combo_benchmarks.SetItems(['沪深300指数(000300.SH)','标普500指数(SPY)'])
        hbox.Add(combo_benchmarks)

        # 上面是一个panel
        # panel = wx.Panel(self)
        # gauge = wx.Gauge(panel, range=100, pos=(0, 50),
        #                      size=(180, -1))
        # gauge.SetValue(88)

        # vbox.Add(panel, 0)
        btn = wx.Button(self, label="回测分析")
        self.Bind(wx.EVT_BUTTON, self.OnClick, btn)
        vbox.Add(btn)

        # 底部是一个浏览器
        web = WebPanel(self)
        vbox.Add(web, 1, wx.EXPAND)
        web.show_file(DATA_DIR_BKT_RESULT.joinpath('bkt_result.html'))

        # web.show_url('http://www.jisilu.cn')

        self.web = web

    def OnClick(self, event):
       pass
