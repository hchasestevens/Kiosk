#!/usr/bin/python
from Xlib import X, display
d = display.Display()
s = d.screen()
root = s.root()
root.warp_pointer(10000,10000)
d.sync()
