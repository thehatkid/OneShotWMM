import wx

from frames import FormMain

if __name__ == '__main__':
    app = wx.App(False)
    frame = FormMain(None)
    frame.SetIcon(wx.Icon('res/app/icon.ico'))
    frame.Show()
    app.MainLoop()
