import wx
from typing import List

from ..panels.eventpage import PanelEventPage


class DialogEvent(wx.Dialog):
    def __init__(self, parent, eventdata: dict):
        self.data = eventdata
        self.evpage_panels: List[wx.Panel] = []

        # Create dialog frame
        wx.Dialog.__init__(
            self, parent, id=wx.ID_ANY,
            title=f'Edit event - [{self.data["id"]:04}: {self.data["name"]}]',
            pos=wx.DefaultPosition, size=wx.Size(705, 580),
            style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.RESIZE_BORDER
        )

        self.SetSizeHints(wx.Size(705, 540), wx.DefaultSize)

        bs_panel = wx.BoxSizer(wx.VERTICAL)

        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_main = wx.BoxSizer(wx.VERTICAL)
        ws_props = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        sbs_props = wx.StaticBoxSizer(wx.StaticBox(self.panel, wx.ID_ANY, 'Event properties'), wx.VERTICAL)
        fgs_props = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_props.SetFlexibleDirection(wx.BOTH)
        fgs_props.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txt_name = wx.StaticText(sbs_props.GetStaticBox(), wx.ID_ANY, 'Name:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_name.Wrap(-1)
        fgs_props.Add(self.txt_name, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtctl_name = wx.TextCtrl(sbs_props.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtctl_name.SetMaxLength(100)
        fgs_props.Add(self.txtctl_name, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.txt_pos = wx.StaticText(sbs_props.GetStaticBox(), wx.ID_ANY, 'Position (X, Y):', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_pos.Wrap(-1)
        fgs_props.Add(self.txt_pos, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgs_pos_ctl = wx.FlexGridSizer(1, 2, 0, 0)
        fgs_pos_ctl.AddGrowableCol(0)
        fgs_pos_ctl.AddGrowableRow(0)
        fgs_pos_ctl.SetFlexibleDirection(wx.HORIZONTAL)
        fgs_pos_ctl.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.spctl_pos_x = wx.SpinCtrl(sbs_props.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 0)
        fgs_pos_ctl.Add(self.spctl_pos_x, 1, wx.EXPAND | wx.ALL, 5)
        self.spctl_pos_y = wx.SpinCtrl(sbs_props.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 0)
        fgs_pos_ctl.Add(self.spctl_pos_y, 1, wx.EXPAND | wx.ALL, 5)

        fgs_props.Add(fgs_pos_ctl, 1, wx.EXPAND, 5)
        sbs_props.Add(fgs_props, 1, wx.EXPAND, 5)
        ws_props.Add(sbs_props, 0, wx.ALL, 5)

        fgs_pages = wx.FlexGridSizer(1, 0, 0, 0)
        fgs_pages.AddGrowableCol(0)
        fgs_pages.AddGrowableRow(0)
        fgs_pages.SetFlexibleDirection(wx.BOTH)
        fgs_pages.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # TODO: make actions on new, delete, clear event pages
        self.btn_page_new = wx.Button(self.panel, wx.ID_ANY, 'New\nEvent Page', wx.DefaultPosition, wx.Size(96, 48), 0)
        fgs_pages.Add(self.btn_page_new, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)
        self.btn_page_delete = wx.Button(self.panel, wx.ID_ANY, 'Delete\nEvent Page', wx.DefaultPosition, wx.Size(96, 48), 0)
        fgs_pages.Add(self.btn_page_delete, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)
        self.btn_page_clear = wx.Button(self.panel, wx.ID_ANY, 'Clear\nEvent Page', wx.DefaultPosition, wx.Size(96, 48), 0)
        fgs_pages.Add(self.btn_page_clear, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        ws_props.Add(fgs_pages, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)
        bs_main.Add(ws_props, 0, wx.EXPAND, 5)

        self.nb_eventpage = wx.Notebook(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bs_main.Add(self.nb_eventpage, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        sdbs = wx.StdDialogButtonSizer()
        self.sdbsOK = wx.Button(self.panel, wx.ID_OK)
        sdbs.AddButton(self.sdbsOK)
        self.sdbsCancel = wx.Button(self.panel, wx.ID_CANCEL)
        sdbs.AddButton(self.sdbsCancel)
        sdbs.Realize()
        bs_main.Add(sdbs, 0, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(bs_main)
        self.panel.Layout()
        bs_main.Fit(self.panel)
        bs_panel.Add(self.panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_panel)
        self.Layout()
        self.Centre(wx.BOTH)

        self.render_event_props()
        self.make_notebook_tabs()

    def render_event_props(self) -> None:
        """Set values from event properties to controls."""
        self.txtctl_name.SetValue(self.data['name'])
        self.spctl_pos_x.SetValue(self.data['x'])
        self.spctl_pos_y.SetValue(self.data['y'])

    def make_notebook_tabs(self) -> None:
        """Creates panels with event pages."""
        page_counter = 0
        for page in self.data['pages']:
            panel = PanelEventPage(self.nb_eventpage, page, page_counter)
            self.evpage_panels.append(panel)
            self.nb_eventpage.AddPage(panel, f'Page {str(page_counter + 1)}')
            page_counter += 1
