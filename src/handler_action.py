from gi.repository import Gtk, Gio, Adw

def create_action(application, name, callback, shortcuts=None):
    """Adds an application action.
    Args:
        name: the name of the action
        callback: the function to be called when the action is
        activated
        shortcuts: an optional list of accelerators
    """
    action = Gio.SimpleAction.new(name, None)
    action.connect("activate", callback)
    application.add_action(action)
    if shortcuts:
        application.set_accels_for_action(f"app.{name}", shortcuts)
