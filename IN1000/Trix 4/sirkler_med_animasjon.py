import time
from ezgraphics import GraphicsWindow
win = GraphicsWindow()
can = win.canvas()

teller = 0
x_pos = 10

stoerrelse = 50
while teller < 9:
    time.sleep(0.5)
    can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    stoerrelse += 50
    x_pos += 10
    stoerrelse -= 50
    teller += 1

win.wait()
