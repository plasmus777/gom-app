from gi.repository import Gio

class Notify:
    def send_notification(text):
        gom = Gio.Application.get_default()

        ntf = Gio.Notification.new('GPU Offloading Manager')
        ntf.set_body(text)
        
        gom.send_notification(None, ntf)
        print('GPU Offloading Manager: ' + text)
