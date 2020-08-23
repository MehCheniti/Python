#Dette programmet åpner opp et vindu med en rød sirkel.

from ezgraphics import GraphicsWindow
win = GraphicsWindow()
win.setTitle("En Rod Sirkel") #Her setter jeg på tittelen.
canvas = win.canvas()
canvas.setColor("red") #Her setter jeg på fargen.
canvas.drawOval(60, 10, 100, 100)
win.wait()
