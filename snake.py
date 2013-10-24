from gi.repository import Gtk
#test
#wejqifjiojfsidojiosjifojiowejrweirjfewmojfijdisjfiojsoidfoiwer
Gtk.init(None)

win = Gtk.Window(Gtk.WindowType.TOPLEVEL)
win.connect("destroy", Gtk.main_quit)
win.show()

Gtk.main()
