from ezgraphics import GraphicsWindow

win = GraphicsWindow()

canvas = win.canvas()

canvas.drawRect(40, 40, 200, 150)

win.wait()
