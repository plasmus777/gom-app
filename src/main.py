# main.py
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

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from .window import *
from .handler_action import *
from .config import *

class GomAppApplication(Adw.Application):
    """The main application singleton class."""

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='Gpu Offloading Manager',
                                application_icon='plasmus777.gnome.GpuOffloadingManager',
                                developer_name='Fernando Lopes',
                                copyright='© 2022 Fernando B. F. Lopes',
                                website='https://github.com/plasmus777/gom-app',
                                issue_url='https://github.com/plasmus777/gom-app/issues',
                                license_type=Gtk.License.GPL_3_0,
                                version='0.1.0',
                                developers=['Fernando Lopes'])
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def __init__(self):
        super().__init__(application_id='plasmus777.gnome.GpuOffloadingManager',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        create_action(self, 'quit', self.quit, ['<primary>q'])
        create_action(self, 'about', self.on_about_action)
        create_action(self, 'preferences', self.on_preferences_action)

        c = Config()
        c.initialize()

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = GomAppWindow(application=self)
        win.present()

def main(version):
    """The application's entry point."""
    app = GomAppApplication()
    return app.run(sys.argv)
