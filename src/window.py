# window.py
#
# Copyright 2022 Fernando Lopes
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, Gio

from .handler_action import *

@Gtk.Template(resource_path='/plasmus777/gnome/GpuOffloadingManager/ui/gom-app-window.ui')
class GomAppWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'GomAppWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        menu_toggle = Gtk.Template.Child('menu_toggle')
        menu_revealer = Gtk.Template.Child('menu_revealer')

        create_action(self, 'toggled', self.toggle_menu)

    def toggle_menu(self):
        if menu_revealer.reveal_child:
            menu_revealer.reveal_child = false
            print('The menu was hidden.')
        else:
            menu_revealer.reveal_child = true
            print('The menu was shown.')
