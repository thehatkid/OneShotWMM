import wx


class PanelEventPage(wx.Panel):
    def __init__(
        self, parent, page: dict, page_number: int,
        id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(680, 400),
        style = wx.TAB_TRAVERSAL, name = wx.EmptyString
    ):
        self.page = page
        self.number = page_number

        # Create panel
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bs_main = wx.BoxSizer(wx.VERTICAL)

        fgs_data = wx.FlexGridSizer(1, 4, 0, 0)
        fgs_data.AddGrowableCol(2)
        fgs_data.SetFlexibleDirection(wx.BOTH)
        fgs_data.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Event page conditions properties
        sbs_conditions = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'Conditions'), wx.VERTICAL)
        fgs_conditions = wx.FlexGridSizer(0, 3, 0, 0)
        fgs_conditions.SetFlexibleDirection(wx.BOTH)
        fgs_conditions.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Event page condition: Switch 1
        self.chkbox_sw1 = wx.CheckBox(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'Switch', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_conditions.Add(self.chkbox_sw1, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spctl_sw1_id = wx.SpinCtrl(sbs_conditions.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 5000, 1)
        self.spctl_sw1_id.Enable(False)
        fgs_conditions.Add(self.spctl_sw1_id, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_sw1 = wx.StaticText(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'is ON', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_sw1.Wrap(-1)
        self.txt_sw1.Enable(False)
        fgs_conditions.Add(self.txt_sw1, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # Event page condition: Switch 2
        self.chkbox_sw2 = wx.CheckBox(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'Switch', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_conditions.Add(self.chkbox_sw2, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spctl_sw2_id = wx.SpinCtrl(sbs_conditions.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 5000, 1)
        self.spctl_sw2_id.Enable(False)
        fgs_conditions.Add(self.spctl_sw2_id, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_sw2 = wx.StaticText( sbs_conditions.GetStaticBox(), wx.ID_ANY, 'is ON', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_sw2.Wrap(-1)
        self.txt_sw2.Enable(False)
        fgs_conditions.Add(self.txt_sw2, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # Event page condition: Variable
        self.chkbox_var = wx.CheckBox(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'Variable', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_conditions.Add(self.chkbox_var, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spctl_var_id = wx.SpinCtrl(sbs_conditions.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 5000, 1)
        self.spctl_var_id.Enable(False)
        fgs_conditions.Add( self.spctl_var_id, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_var_1 = wx.StaticText(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'is', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_var_1.Wrap(-1)
        self.txt_var_1.Enable(False)
        fgs_conditions.Add(self.txt_var_1, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgs_conditions.Add((0, 0), 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spctl_var_value = wx.SpinCtrl(sbs_conditions.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -9999999, 9999999, 0)
        self.spctl_var_value.Enable(False)
        fgs_conditions.Add(self.spctl_var_value, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_var_2 = wx.StaticText(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'or above', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_var_2.Wrap(-1)
        self.txt_var_2.Enable(False)

        fgs_conditions.Add(self.txt_var_2, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # Event page condition: Self switch
        self.chkbox_selfsw = wx.CheckBox( sbs_conditions.GetStaticBox(), wx.ID_ANY, 'Self switch', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_conditions.Add(self.chkbox_selfsw, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cmbbox_selfsw = wx.ComboBox(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'A', wx.DefaultPosition, wx.DefaultSize, ['A', 'B', 'C', 'D'], wx.CB_READONLY)
        self.cmbbox_selfsw.SetSelection(0)
        self.cmbbox_selfsw.Enable(False)
        fgs_conditions.Add(self.cmbbox_selfsw, 0, wx.EXPAND | wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_selfsw = wx.StaticText(sbs_conditions.GetStaticBox(), wx.ID_ANY, 'is ON', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selfsw.Wrap(-1)
        self.txt_selfsw.Enable(False)
        fgs_conditions.Add(self.txt_selfsw, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbs_conditions.Add(fgs_conditions, 1, wx.EXPAND, 5)
        fgs_data.Add(sbs_conditions, 0, wx.EXPAND | wx.ALL, 5)

        # Event page graphic properties
        sbs_graphic = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'Graphic'), wx.VERTICAL)
        fgs_graphic = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_graphic.SetFlexibleDirection(wx.BOTH)
        fgs_graphic.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txt_char_name = wx.StaticText(sbs_graphic.GetStaticBox(), wx.ID_ANY, 'Name:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_char_name.Wrap(-1)
        fgs_graphic.Add(self.txt_char_name, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.txtctl_char_name = wx.TextCtrl(sbs_graphic.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtctl_char_name.SetMaxLength(255)
        fgs_graphic.Add(self.txtctl_char_name, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.txt_char_tileid = wx.StaticText(sbs_graphic.GetStaticBox(), wx.ID_ANY, 'Tile ID:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_char_tileid.Wrap(-1)
        fgs_graphic.Add(self.txt_char_tileid, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.spctl_char_tileid = wx.SpinCtrl(sbs_graphic.GetStaticBox(), wx.ID_ANY, '0', wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 0)
        fgs_graphic.Add(self.spctl_char_tileid, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.txt_char_hue = wx.StaticText(sbs_graphic.GetStaticBox(), wx.ID_ANY, 'Hue:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_char_hue.Wrap(-1)
        fgs_graphic.Add(self.txt_char_hue, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.spctl_char_hue = wx.SpinCtrl(sbs_graphic.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 360, 0)
        fgs_graphic.Add(self.spctl_char_hue, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.txt_char_blend = wx.StaticText(sbs_graphic.GetStaticBox(), wx.ID_ANY, 'Blending:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_char_blend.Wrap(-1)
        fgs_graphic.Add(self.txt_char_blend, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.cmbbox_char_blend = wx.ComboBox(sbs_graphic.GetStaticBox(), wx.ID_ANY, 'Normal', wx.DefaultPosition, wx.DefaultSize, ['Normal', 'Sub', 'Add'], wx.CB_READONLY)
        self.cmbbox_char_blend.SetSelection(0)
        fgs_graphic.Add(self.cmbbox_char_blend, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.txt_char_opacity = wx.StaticText(sbs_graphic.GetStaticBox(), wx.ID_ANY, 'Opacity:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_char_opacity.Wrap(-1)
        fgs_graphic.Add(self.txt_char_opacity, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.spctl_char_opacity = wx.SpinCtrl(sbs_graphic.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 0)
        fgs_graphic.Add(self.spctl_char_opacity, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.txt_char_pattern = wx.StaticText(sbs_graphic.GetStaticBox(), wx.ID_ANY, 'Direction, Pattern:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_char_pattern.Wrap(-1)
        fgs_graphic.Add(self.txt_char_pattern, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        gs_char_pattern = wx.GridSizer(0, 2, 0, 0)

        self.cmbbox_char_direction = wx.ComboBox(sbs_graphic.GetStaticBox(), wx.ID_ANY, '1', wx.DefaultPosition, wx.DefaultSize, ['1', '2', '3', '4'], wx.CB_READONLY)
        self.cmbbox_char_direction.SetSelection(0)
        gs_char_pattern.Add(self.cmbbox_char_direction, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.cmbbox_char_pattern = wx.ComboBox(sbs_graphic.GetStaticBox(), wx.ID_ANY, '1', wx.DefaultPosition, wx.DefaultSize, ['1', '2', '3', '4'], wx.CB_READONLY)
        self.cmbbox_char_pattern.SetSelection(0)
        gs_char_pattern.Add(self.cmbbox_char_pattern, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        fgs_graphic.Add(gs_char_pattern, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        sbs_graphic.Add(fgs_graphic, 1, wx.EXPAND, 5)
        fgs_data.Add(sbs_graphic, 0, wx.EXPAND | wx.ALL, 5)

        # Event page options
        fgs_props = wx.FlexGridSizer(0, 1, 0, 0)
        fgs_props.AddGrowableRow(1)
        fgs_props.SetFlexibleDirection(wx.BOTH)
        fgs_props.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbs_options = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'Options'), wx.VERTICAL)
        fgs_options = wx.FlexGridSizer(0, 1, 0, 0)
        fgs_options.SetFlexibleDirection(wx.BOTH)
        fgs_options.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.chkbox_moveanim = wx.CheckBox(sbs_options.GetStaticBox(), wx.ID_ANY, 'Move animation', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_options.Add(self.chkbox_moveanim, 0, wx.EXPAND | wx.ALL, 5)
        self.chkbox_stopanim = wx.CheckBox(sbs_options.GetStaticBox(), wx.ID_ANY, 'Stop animation', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_options.Add(self.chkbox_stopanim, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)
        self.chkbox_dirfix = wx.CheckBox(sbs_options.GetStaticBox(), wx.ID_ANY, 'Direction fix', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_options.Add(self.chkbox_dirfix, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)
        self.chkbox_through = wx.CheckBox(sbs_options.GetStaticBox(), wx.ID_ANY, 'Through', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_options.Add(self.chkbox_through, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)
        self.chkbox_aot = wx.CheckBox(sbs_options.GetStaticBox(), wx.ID_ANY, 'Always on top', wx.DefaultPosition, wx.DefaultSize, 0)
        fgs_options.Add(self.chkbox_aot, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sbs_options.Add(fgs_options, 1, wx.EXPAND, 5)
        fgs_props.Add(sbs_options, 1, wx.EXPAND | wx.ALL, 5)

        # Event page trigger
        sbs_trigger = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'Trigger'), wx.VERTICAL)
        fgs_trigger = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_trigger.SetFlexibleDirection(wx.BOTH)
        fgs_trigger.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txt_evtrigger = wx.StaticText(sbs_trigger.GetStaticBox(), wx.ID_ANY, 'On:', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_evtrigger.Wrap(-1)
        fgs_trigger.Add(self.txt_evtrigger, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cmbbox_trigger = wx.ComboBox(sbs_trigger.GetStaticBox(), wx.ID_ANY, 'Action button', wx.DefaultPosition, wx.DefaultSize, ['Action button', 'Player touch', 'Event touch', 'Autorun', 'Parallel'], wx.CB_READONLY)
        self.cmbbox_trigger.SetSelection(0)
        fgs_trigger.Add(self.cmbbox_trigger, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbs_trigger.Add(fgs_trigger, 0, wx.EXPAND, 5)
        fgs_props.Add(sbs_trigger, 0, wx.ALL, 5)
        fgs_data.Add(fgs_props, 0, wx.EXPAND, 5)
        bs_main.Add(fgs_data, 0, wx.EXPAND, 5)

        # Event page commands
        bs_evcmds = wx.BoxSizer(wx.VERTICAL)
        self.txt_evcmds = wx.StaticText(self, wx.ID_ANY, 'List of Event Commands: (WIP)', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_evcmds.Wrap(-1)
        bs_evcmds.Add(self.txt_evcmds, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.lb_evcmds = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, [], wx.LB_OWNERDRAW)
        self.lb_evcmds.Enable(False)
        bs_evcmds.Add(self.lb_evcmds, 1, wx.EXPAND | wx.ALL, 5)
        bs_main.Add(bs_evcmds, 1, wx.EXPAND, 5)

        self.SetSizer(bs_main)
        self.Layout()

        self.render_page()
        self.render_event_commands()

        # Binding events
        self.chkbox_sw1.Bind(wx.EVT_CHECKBOX, self.on_condition_checkbox)
        self.chkbox_sw2.Bind(wx.EVT_CHECKBOX, self.on_condition_checkbox)
        self.chkbox_var.Bind(wx.EVT_CHECKBOX, self.on_condition_checkbox)
        self.chkbox_selfsw.Bind(wx.EVT_CHECKBOX, self.on_condition_checkbox)

    def on_condition_checkbox(self, event: wx.CommandEvent) -> None:
        """On checkbox wxWidgets event."""

        chkbox = event.GetEventObject()
        chkbox_id = chkbox.GetId()
        chkbox_check = chkbox.IsChecked()

        if chkbox_id == self.chkbox_sw1.GetId():
            if chkbox_check:
                self.spctl_sw1_id.Enable()
                self.txt_sw1.Enable()
            else:
                self.spctl_sw1_id.Disable()
                self.txt_sw1.Disable()
        elif chkbox_id == self.chkbox_sw2.GetId():
            if chkbox_check:
                self.spctl_sw2_id.Enable()
                self.txt_sw2.Enable()
            else:
                self.spctl_sw2_id.Disable()
                self.txt_sw2.Disable()
        elif chkbox_id == self.chkbox_var.GetId():
            if chkbox_check:
                self.spctl_var_id.Enable()
                self.spctl_var_value.Enable()
                self.txt_var_1.Enable()
                self.txt_var_2.Enable()
            else:
                self.spctl_var_id.Disable()
                self.spctl_var_value.Disable()
                self.txt_var_1.Disable()
                self.txt_var_2.Disable()
        elif chkbox_id == self.chkbox_selfsw.GetId():
            if chkbox_check:
                self.cmbbox_selfsw.Enable()
                self.txt_selfsw.Enable()
            else:
                self.cmbbox_selfsw.Disable()
                self.txt_selfsw.Disable()

        event.Skip()

    def render_page(self) -> None:
        """Set values from event page to controls."""

        cond = self.page['condition']
        gfx = self.page['graphic']

        # Event page conditions
        if cond['switch1_valid']:
            self.chkbox_sw1.SetValue(True)
            self.spctl_sw1_id.Enable()
            self.spctl_sw1_id.SetValue(cond['switch1_id'])
            self.txt_sw1.Enable()

        if cond['switch2_valid']:
            self.chkbox_sw2.SetValue(True)
            self.spctl_sw2_id.Enable()
            self.spctl_sw2_id.SetValue(cond['switch2_id'])
            self.txt_sw2.Enable()

        if cond['variable_valid']:
            self.chkbox_var.SetValue(True)
            self.spctl_var_id.Enable()
            self.spctl_var_value.Enable()
            self.spctl_var_id.SetValue(cond['variable_id'])
            self.spctl_var_value.SetValue(cond['variable_value'])
            self.txt_var_1.Enable()
            self.txt_var_2.Enable()

        if cond['self_switch_valid']:
            self.chkbox_selfsw.SetValue(True)
            self.cmbbox_selfsw.Enable()
            self.cmbbox_selfsw.SetValue(cond['self_switch_ch'])
            self.txt_selfsw.Enable()

        # Event page graphic
        self.txtctl_char_name.SetValue(gfx['character_name'])
        self.spctl_char_tileid.SetValue(gfx['tile_id'])
        self.spctl_char_hue.SetValue(gfx['character_hue'])
        self.cmbbox_char_blend.SetSelection(gfx['blend_type'])
        self.spctl_char_opacity.SetValue(gfx['opacity'])
        self.cmbbox_char_direction.SetSelection(gfx['direction'])
        self.cmbbox_char_pattern.SetSelection(gfx['pattern'])

        # Event page options
        self.chkbox_moveanim.SetValue(self.page['walk_anime'])
        self.chkbox_stopanim.SetValue(self.page['step_anime'])
        self.chkbox_dirfix.SetValue(self.page['direction_fix'])
        self.chkbox_through.SetValue(self.page['through'])
        self.chkbox_aot.SetValue(self.page['always_on_top'])

        # Event page trigger
        self.cmbbox_trigger.SetSelection(self.page['trigger'])

    def render_event_commands(self) -> None:
        """Parse and make listbox of event commands."""
        # TODO: parse RPG event commands codes
        pass
