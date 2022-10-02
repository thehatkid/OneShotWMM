import wx
import json
import traceback
from copy import deepcopy

from ..dialogs.event import DialogEvent
from ..dialogs.about import DialogAbout


class FormMain(wx.Frame):
    def __init__(self, parent) -> None:
        self.json_filepath = None
        self.json_data = None
        self.need_save = False

        # Create form frame
        wx.Frame.__init__(
            self, parent, id=wx.ID_ANY,
            title='OneShot World Machine Maker',
            pos=wx.Point(-1, -1), size=wx.Size(620, 440),
            style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL,
            name='OneShot World Machine Maker'
        )

        self.SetSizeHints(wx.Size(450, 300), wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        # Menu bar
        self.mb = wx.MenuBar(0)

        self.mb_file = wx.Menu()

        self.mb_file_load = wx.MenuItem(self.mb_file, wx.ID_OPEN, '&Load...\tCtrl+O', 'Load JSON file of map events', wx.ITEM_NORMAL)
        self.mb_file.Append(self.mb_file_load)

        self.mb_file_save = wx.MenuItem(self.mb_file, wx.ID_SAVE, '&Save\tCtrl+S', 'Save JSON file of map events', wx.ITEM_NORMAL)
        self.mb_file_save.Enable(False)
        self.mb_file.Append(self.mb_file_save)

        self.mb_file.AppendSeparator()

        self.mb_file_exit = wx.MenuItem(self.mb_file, wx.ID_EXIT, '&Exit\tAlt+F4', 'Quit from this program', wx.ITEM_NORMAL)
        self.mb_file.Append(self.mb_file_exit)

        self.mb.Append(self.mb_file, '&File')

        self.mb_help = wx.Menu()

        self.mb_help_about = wx.MenuItem(self.mb_help, wx.ID_ABOUT, '&About...\tF1', 'Show about this program', wx.ITEM_NORMAL)
        self.mb_help.Append(self.mb_help_about)

        self.mb.Append(self.mb_help, '&Help')

        self.SetMenuBar(self.mb)

        bs_panel = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bs_main = wx.BoxSizer(wx.VERTICAL)

        fgs_content = wx.FlexGridSizer(2, 2, 0, 0)
        fgs_content.AddGrowableCol(1)
        fgs_content.AddGrowableRow(0)
        fgs_content.SetFlexibleDirection(wx.BOTH)
        fgs_content.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Tree list control: RPG map events list
        self.tctl_events = wx.TreeCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.tctl_events.SetMinSize(wx.Size(240, -1))
        self.tctl_events.SetMaxSize(wx.Size(240, -1))
        fgs_content.Add(self.tctl_events, 1, wx.EXPAND | wx.ALL, 5)

        # Assign custom icons to tree list control
        il_events = wx.ImageList(16, 16)
        il_events.Add(wx.Image('res/icons/image.png', wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        il_events.Add(wx.Image('res/icons/page.png', wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        il_events.Add(wx.Image('res/icons/color_wheel.png', wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        self.tctl_events.AssignImageList(il_events)

        sbs_info = wx.StaticBoxSizer(wx.StaticBox(self.panel, wx.ID_ANY, 'OneShot: World Machine Edition'), wx.VERTICAL)
        ws_info = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.txt_welcome = wx.StaticText(sbs_info.GetStaticBox(), wx.ID_ANY, 'Welcome to OneShot World Machine Maker by hat_kid!', wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_welcome.Wrap(-1)
        ws_info.Add(self.txt_welcome, 0, wx.ALL, 5)

        sbs_info.Add(ws_info, 1, wx.EXPAND, 5)

        fgs_content.Add(sbs_info, 1, wx.EXPAND | wx.ALL, 5)
        fgs_content.Add((0, 0), 1, wx.EXPAND, 5)

        fgs_buttons = wx.FlexGridSizer(1, 0, 0, 0)
        fgs_buttons.SetFlexibleDirection(wx.BOTH)
        fgs_buttons.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # TODO: Map event management (add, rename, delete, etc.)
        self.btn_pl1 = wx.Button(self.panel, wx.ID_ANY, 'Placeholder', wx.DefaultPosition, wx.Size(-1, 32), 0)
        fgs_buttons.Add(self.btn_pl1, 0, wx.ALL, 5)
        self.btn_pl2 = wx.Button(self.panel, wx.ID_ANY, 'Placeholder', wx.DefaultPosition, wx.Size(-1, 32), 0)
        fgs_buttons.Add(self.btn_pl2, 0, wx.ALL, 5)
        self.btn_pl3 = wx.Button(self.panel, wx.ID_ANY, 'Placeholder', wx.DefaultPosition, wx.Size(-1, 32), 0)
        fgs_buttons.Add(self.btn_pl3, 0, wx.ALL, 5)
        fgs_content.Add(fgs_buttons, 1, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        bs_main.Add(fgs_content, 1, wx.EXPAND, 5)

        self.panel.SetSizer(bs_main)
        self.panel.Layout()
        bs_main.Fit(self.panel)
        bs_panel.Add(self.panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_panel)
        self.Layout()
        self.Centre(wx.BOTH)

        # Binding events
        self.Bind(wx.EVT_CLOSE, self.on_form_close)
        self.Bind(wx.EVT_MENU, self.on_menu_item)
        self.tctl_events.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_tree_item_activated)

    def on_form_close(self, event: wx.CloseEvent) -> None:
        """On form close wxWidgets event."""

        # Ask to save current json if needed
        result = self.check_for_save()
        if result == wx.ID_YES:
            # If user pressed yes button
            self.save_json()
        elif result == wx.ID_NO:
            # If user pressed no button
            self.need_save = False
        elif result == wx.ID_CANCEL:
            # If user canceled dialog
            return

        event.Skip()

    def on_menu_item(self, event: wx.CommandEvent) -> None:
        """On menu bar item selection wxWidgets event."""

        if event.Id == wx.ID_OPEN:
            # Ask to save current json if needed
            result = self.check_for_save()
            if result == wx.ID_YES:
                # If user pressed yes button
                self.save_json()
            elif result == wx.ID_NO:
                # If user pressed no button
                self.need_save = False
            elif result == wx.ID_CANCEL:
                # If user canceled dialog
                return

            # Make file open dialog
            filedlg = wx.FileDialog(
                self,
                'Open JSON map events...',
                wildcard='JSON serialized file (*.json)|*.json|All files (*.*)|*.*', 
                style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
            )
            dlgresult = filedlg.ShowModal()

            if dlgresult == wx.ID_CANCEL:
                # If user canceled dialog
                return

            # Load JSON file from selected filepath
            filepath = filedlg.GetPath()
            self.load_json(filepath)
            filedlg.Destroy()
        elif event.Id == wx.ID_SAVE:
            # Save file
            if self.json_filepath:
                self.save_json()
        elif event.Id == wx.ID_EXIT:
            # Close form
            self.Close()
        elif event.Id == wx.ID_ABOUT:
            # Show application about page
            dlg = DialogAbout(self)
            dlg.ShowModal()
            dlg.Destroy()

    def on_tree_item_activated(self, event: wx.TreeEvent) -> None:
        """On tree item activated wxWidgets event."""

        # Get event ID of tree item
        item_id = self.tctl_events.GetItemData(event.GetItem())

        if item_id < 0:
            # Return if it's root tree item
            return

        try:
            dlg = DialogEvent(self, self.json_data['events'][item_id])
        except Exception as exc:
            # Print traceback
            traceback.print_exc()
            # Show error message box
            wx.MessageBox(
                f'{exc.__class__.__name__}: {exc}\n\nLet hat_kid know this!',
                f'Error while opening map event [{self.json_data["events"][item_id]["id"]:04}: {self.json_data["events"][item_id]["name"]}]',
                wx.ICON_ERROR
            )
        else:
            result = dlg.ShowModal()

            if result == wx.ID_OK:
                # Get values from dialog
                name = dlg.txtctl_name.GetValue()
                pos_x = dlg.spctl_pos_x.GetValue()
                pos_y = dlg.spctl_pos_y.GetValue()

                # Get pages from dialog panels
                pages = deepcopy(self.json_data['events'][item_id]['pages'])
                page_count = 0
                for panel in dlg.evpage_panels:
                    # Event page conditions
                    pages[page_count]['condition']['switch1_valid'] = panel.chkbox_sw1.IsChecked()
                    pages[page_count]['condition']['switch2_valid'] = panel.chkbox_sw2.IsChecked()
                    pages[page_count]['condition']['variable_valid'] = panel.chkbox_var.IsChecked()
                    pages[page_count]['condition']['self_switch_valid'] = panel.chkbox_selfsw.IsChecked()
                    pages[page_count]['condition']['switch1_id'] = panel.spctl_sw1_id.GetValue()
                    pages[page_count]['condition']['switch2_id'] = panel.spctl_sw2_id.GetValue()
                    pages[page_count]['condition']['variable_id'] = panel.spctl_var_id.GetValue()
                    pages[page_count]['condition']['variable_value'] = panel.spctl_var_value.GetValue()
                    pages[page_count]['condition']['self_switch_ch'] = panel.cmbbox_selfsw.GetValue()

                    # Event page character graphic
                    pages[page_count]['graphic']['character_name'] = panel.txtctl_char_name.GetValue()
                    pages[page_count]['graphic']['tile_id'] = panel.spctl_char_tileid.GetValue()
                    pages[page_count]['graphic']['character_hue'] = panel.spctl_char_hue.GetValue()
                    pages[page_count]['graphic']['blend_type'] = panel.cmbbox_char_blend.GetSelection()
                    pages[page_count]['graphic']['opacity'] = panel.spctl_char_opacity.GetValue()
                    pages[page_count]['graphic']['direction'] = panel.cmbbox_char_direction.GetSelection()
                    pages[page_count]['graphic']['pattern'] = panel.cmbbox_char_pattern.GetSelection()

                    # Event page options
                    pages[page_count]['walk_anime'] = panel.chkbox_moveanim.IsChecked()
                    pages[page_count]['step_anime'] = panel.chkbox_stopanim.IsChecked()
                    pages[page_count]['direction_fix'] = panel.chkbox_dirfix.IsChecked()
                    pages[page_count]['through'] = panel.chkbox_through.IsChecked()
                    pages[page_count]['always_on_top'] = panel.chkbox_aot.IsChecked()

                    # Event page trigger
                    pages[page_count]['trigger'] = panel.cmbbox_trigger.GetSelection()

                    page_count += 1

                if not self.need_save and (
                    name != self.json_data['events'][item_id]['name'] or
                    pos_x != self.json_data['events'][item_id]['x'] or
                    pos_y != self.json_data['events'][item_id]['y'] or
                    pages != self.json_data['events'][item_id]['pages']
                ):
                    self.need_save = True

                # Change values in current JSON data
                self.json_data['events'][item_id]['name'] = name
                self.json_data['events'][item_id]['x'] = pos_x
                self.json_data['events'][item_id]['y'] = pos_y
                self.json_data['events'][item_id]['pages'] = pages

                # Change current name in tree item text
                self.tctl_events.SetItemText(event.GetItem(), f'{name} (ID: {dlg.data["id"]})')
                self.tctl_events.SetItemImage(event.GetItem(), (2 if name == '!collectible' else 1))

            dlg.Destroy()

    def check_for_save(self) -> int:
        """Checks if we have unsaved changes."""
        if self.need_save:
            dlg = wx.MessageDialog(
                self,
                'You have made changes. Do you want to save file?',
                'Confirmation',
                wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION
            )
            result = dlg.ShowModal()
            dlg.Destroy()
            return result
        else:
            return 0

    def is_opened_json(self) -> bool:
        """Checks if we have loaded JSON file."""
        if self.json_filepath is None:
            return False
        return True

    def reset_state(self) -> None:
        self.json_filepath = None
        self.mb_file_save.Enable(False)
        if self.json_data:
            self.json_data = None
            self.tctl_events.DeleteAllItems()

    def load_json(self, filepath: str) -> None:
        """Loads JSON file with map events."""

        # Clear old data/state if have
        if self.json_data:
            self.reset_state()

        try:
            # Load input file
            with open(filepath, 'r') as fp:
                json_data = json.load(fp)

            # Validate JSON data
            assert 'events' in json_data, 'Does not have "events" key in JSON'
            for event in json_data['events']:
                assert 'id' in event, 'Does not have "id" key in JSON'
                assert 'name' in event, 'Does not have "name" key in JSON'
                assert 'x' in event, 'Does not have "x" key in JSON'
                assert 'y' in event, 'Does not have "y" key in JSON'
                assert 'pages' in event, 'Does not have "pages" key in JSON'
        except Exception as exc:
            # Print traceback
            traceback.print_exc()
            # Show error message box
            wx.MessageBox(
                f'{exc}\n\nPlease, load exactly "event_mapID.json"',
                'Error while loading JSON',
                wx.ICON_ERROR
            )
        else:
            if self.is_opened_json():
                self.json_filepath = None
                self.tctl_events.DeleteAllItems()

            self.json_data = json_data
            self.json_filepath = filepath
            self.need_save = False

            if not self.json_data['events']:
                self.json_filepath = None
                self.reset_state()
                wx.MessageBox(
                    'No map events in this file',
                    'Map events information',
                    wx.ICON_INFORMATION
                )
            else:
                # Make tree list
                self.tctl_events_root = self.tctl_events.AddRoot('Map events', image=0, data=-1)
                evcount = 0
                for event in self.json_data['events']:
                    self.tctl_events.AppendItem(
                        self.tctl_events_root,
                        f'{event["name"]} (ID: {event["id"]})',
                        image=(2 if event['name'] == '!collectible' else 1), data=evcount
                    )
                    evcount += 1
                self.tctl_events.ExpandAll()

                # Enable save menu item
                self.mb_file_save.Enable(True)

    def save_json(self) -> bool:
        """Saves current JSON data to current file."""

        if not self.need_save or not self.json_filepath or not self.json_data:
            return False

        try:
            # Open and write JSON
            with open(self.json_filepath, 'w') as fp:
                fp.write(json.dumps(self.json_data, separators=(',', ':')))
        except Exception as exc:
            # Show error message box
            wx.MessageBox(
                f'Failed to save {self.json_filepath}\n\n{exc.__class__.__name__}: {exc}',
                'Error while writing JSON file',
                wx.ICON_ERROR
            )
            return False
        else:
            self.need_save = False
            return True
