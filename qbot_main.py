import wx
from gui.mainframe import MainFrame

if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='AI智能量化投研平台')
    frm.Show()
    app.MainLoop()

