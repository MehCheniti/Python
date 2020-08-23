from ezgraphics import GraphicsWindow
win = GraphicsWindow()
can = win.canvas()

can.drawOval(20, 20, 50, 50)

can.drawOval(120, 20, 50, 50)

can.drawOval(220, 40, 50, 50)

can.drawOval(320, 60, 50, 70)
win.wait()
