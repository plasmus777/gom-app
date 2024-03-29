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

from .config import *

@Gtk.Template(resource_path='/com/github/plasmus777/GpuOffloadingManager/ui/gom-app-window.ui')
class GomAppWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'GomAppWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        display_protocol_label = Gtk.Template.Child('display_protocol_label')
        display_protocol_icon = Gtk.Template.Child('display_protocol_icon')

    #@Gtk.Template.Callback()
    #def onButtonPressed(self, button):
    #    print("Hello World!")
