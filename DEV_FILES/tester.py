import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
 
btn = Gtk.Button("test")
 
#make a gdk.color for red
map = btn.get_colormap() 
color = map.alloc_color("red")
 
#copy the current style and replace the background
style = btn.get_style().copy()
style.bg[gtk.STATE_NORMAL] = color
 
#set the button's style to the one you created
btn.set_style(style)
 
win.add(btn)
win.show_all()
 
Gtk.main()