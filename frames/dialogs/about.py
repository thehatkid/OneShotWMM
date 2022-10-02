import wx


class DialogAbout(wx.Dialog):
    def __init__(self, parent):
        # Create dialog frame
        wx.Dialog.__init__(
            self, parent, id=wx.ID_ANY,
            title='About this program...',
            pos=wx.DefaultPosition, size=wx.Size(400, 300),
            style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        )
        self.SetSizeHints(wx.Size(400, 300), wx.Size(400, 300))

        bs_panel = wx.BoxSizer(wx.VERTICAL)

        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_main = wx.BoxSizer(wx.VERTICAL)

        fgs_content = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_content.AddGrowableRow(1)
        fgs_content.SetFlexibleDirection(wx.BOTH)
        fgs_content.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Application icon
        self.bm_icon = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('res/app/icon_32.png', wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_content.Add(self.bm_icon, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # About title
        self.txt_title = wx.StaticText(self.panel, wx.ID_ANY, 'OneShot World Machine Maker', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_title.Wrap(-1)
        self.txt_title.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        fgs_content.Add(self.txt_title, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgs_content.Add((0, 0), 1, wx.EXPAND, 5)

        # About description
        self.txt_description = wx.StaticText(self.panel, wx.ID_ANY, 'OneShot World Machine Maker is a tool made by hat_kid for editing map events of OneShot console version.\n\nMade with wxWidgets.', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_description.Wrap(1)
        fgs_content.Add(self.txt_description, 1, wx.EXPAND | wx.ALL, 5)

        bs_main.Add(fgs_content, 1, wx.EXPAND | wx.ALL, 5)

        # Dialog OK button
        sdbs = wx.StdDialogButtonSizer()
        self.sdbsOK = wx.Button(self.panel, wx.ID_OK)
        sdbs.AddButton(self.sdbsOK)
        sdbs.Realize()
        bs_main.Add(sdbs, 0, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(bs_main)
        self.panel.Layout()
        bs_main.Fit(self.panel)
        bs_panel.Add(self.panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_panel)
        self.Layout()
        self.Centre(wx.BOTH)
